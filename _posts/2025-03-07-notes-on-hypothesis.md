---
title: Notes on coding with hypothesis
tags: dev python testing hypothesis
---

Having done a big project recently which required a lot of tests, I've collected quite a bunch
of notes on testing with [Hypothesis](https://hypothesis.works), a Python library for creating
unit tests.

Here they are, in no particular order:


## Examples

It's handy to be able to run all your tests on explicit examples only:

```shell
pytest --hypothesis-profile examples
```

If you have a profile (in *conftest.py*):

```python
settings.register_profile(
    "examples",
    verbosity=Verbosity.verbose,
    phases=[Phase.explicit],
)
```

That's why,..

#### Start with *@example*
When only starting to write a test, it often breaks a lot, with strategies already in *@given*, you'll waste a lot of time on running *shrink* and *explain* phases only to find out that the test is unconditionally failing, for ex. because of undefined variable. If you start with *@example*, or provide it even when test already has *@given* strategies, the explicit example fail will not be shrunk and explained, giving you the fastest time-to-fail.
## Slow tests
Some tests are not like others, maybe you exploit `asyncio.sleep` a lot there and even follow a strategy to generate timeouts. So in any case, I've found it useful to use a *reduced_max_examples* settings def:
```python
def reduced_max_examples():
	"""Reducing max_examples to 20%, up to minimum 1"""
    return settings(
        max_examples=max(
            1, int(settings().max_examples / 5)
        ),
    )
```
That will be used like:
```python
@given(
	time_to_stop=st.timedeltas(
		min_value=timedelta(seconds=0.1),
		max_value=timedelta(seconds=0.5),
	)
)
@example(
	time_to_stop=timedelta(seconds=0.1),
)
@settings(
	reduced_max_examples(),
	deadline=timedelta(seconds=5),
)
@pytest.mark.asyncio
@pytest.mark.with_sleep
async def test_something(time_to_stop: AwareDatetime):
    ...
```
Also note using **with_sleep** pytest mark to run specifically slow tests, if needed:
```
pytest -m "with_sleep" --hypothesis-profile ci
```
## Free strategies
Sometimes you need a little bit simpler range, than possible. Here are some *free lunch*:
```python
from string import printable
from hypothesis import strategies as st


ids = st.text(printable)

error_text = st.text(printable)

timestamps = st.datetimes(
    min_value=datetime(year=2020, month=1, day=1),
    max_value=datetime(year=2030, month=1, day=1),
    timezones=st.timezones(),
)
```
### Quick checks for *pre-commit-hooks*
Register profile in *conftest.py*:
```python
settings.register_profile(
    "quick-check",
    max_examples=5,
    phases=(
        Phase.explicit,
        Phase.reuse,
        Phase.generate,
        Phase.target,
        # Phase.shrink, # Saving time on quick check
        # Phase.explain, # Saving time on quick check
    ),
)
```
And use it in *.pre-commit-config.yaml*:
```yaml
  ...
  - id: pytest
    name: Pytest
    description: Quick-check pytest
    entry: poetry run pytest --hypothesis-profile quick-check
    pass_filenames: false
    language: system
    always_run: true
  ...
```
