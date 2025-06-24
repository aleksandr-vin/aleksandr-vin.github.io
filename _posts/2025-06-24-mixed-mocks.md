---
title: "Mixed mocks"
tags: python, testing, mocks, async
---

Just an example on how to construct mocks with mixed sync and async methods:

```python
from typing import Protocol
from mock import AsyncMock, MagicMock
import pytest
from hypothesis import given, strategies as st


class Sample(Protocol):
    def sync_meth(p):
        """This method you call"""
        ...

    async def async_meth(p):
        """This method you await"""
        ...


class Worker:
    def __init__(self, c: Sample):
        self.c = c

    async def run(self, p):
        r1 = self.c.sync_meth(p)
        return await self.c.async_meth(r1)


@given(
    m=st.sampled_from(
        [
            AsyncMock(the_sync=MagicMock()),
            MagicMock(the_async=AsyncMock()),
        ]
    )
)
@pytest.mark.asyncio
async def test_it(m):
    """Should work for both ways of constructing a mock with mixed sync/async methods"""
    m.the_sync.return_value = "s"
    m.the_async.return_value = "a"
    w = Worker(c=m)
    r = await w.run("p")
    m.the_sync.assert_called_once_with("p")
    m.the_async.assert_awaited_once_with("s")
    assert r == "a"
```
