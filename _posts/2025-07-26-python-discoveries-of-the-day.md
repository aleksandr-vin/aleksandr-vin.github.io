---
title: "Python discoveries of the day"
tags: python, discoveries
---

Python discoveries of the day.

## f-string debug specifier (=)

Check:

```python
>>> f"hey {randint(0,20)=} {foo=}"
'hey randint(0,20)=0 foo=18'
```

Now debug lines can be more expressive, instead of

```python
    f"Processing finished for task {task!r}"
```

One can write:

```python
    f"Processing finished for {task=}"
```

Slightly different output but does the job.

## Asyncio introspection capabilities (>=3.14)

See [What's new in Python 3.14](https://docs.python.org/3.14/whatsnew/3.14.html#asyncio-introspection-capabilities).

    python -m asyncio ps PID

    python -m asyncio pstree PID
