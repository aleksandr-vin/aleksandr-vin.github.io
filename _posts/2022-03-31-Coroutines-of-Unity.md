---
title: "Coroutines of Unity"
tags: unity programming coroutines dev lerp slerp math
---

Recently I've stumbled onto a [tutorial](https://www.youtube.com/watch?v=IymDGkzwJts) on using Linear intERPolation &
Spherical Linear intERPolation in Unity.

That appeared to be a nice small one tutor, where you pause it many times and open your Unity and try!

{% include youtubePlayer.html id="IymDGkzwJts" %}

## Results

Here is a first result with LERP move: [script](https://gist.github.com/aleksandr-vin/67fc4dfd4263f90e11d336c7814db025)
control LERP move of a GameObject through checkpoints.

{% include vimeoPlayer.html id="694457630/ec5d698c63" %}

## Side steps

### Coroutines

One side step in that tutorial was to use [coroutines (Unity)](https://docs.unity3d.com/Manual/Coroutines.html) to run the transformations.
And that was an interesting side step to see a good case for using them.

Here is a nice reading on Wikipedia about [coroutines](https://en.wikipedia.org/wiki/Coroutine#Comparison_with).

It is interesting also [how example in Wikipedia](https://en.wikipedia.org/wiki/Coroutine#Subroutines) tells it all, I'll put it here:

```
var q := new queue

coroutine produce
    loop
        while q is not full
            create some new items
            add the items to q
        yield to consume

coroutine consume
    loop
        while q is not empty
            remove some items from q
            use the items
        yield to produce

call produce
```

And how [example in Python docs](https://docs.python.org/3/library/asyncio-task.html#coroutine) tells no added value. Check what it shows:

```python
>>> import asyncio

>>> async def main():
...     print('hello')
...     await asyncio.sleep(1)
...     print('world')

>>> asyncio.run(main())
hello
world
```

That boolshit does not make any sense, compare it to straight:

```python
def main():
    print('hello')
    time.sleep(1)
    print('world')

main()
```

If you have no idea why to use coroutines, you'll have hard time finding that out from Python docs!

## Some more refs

1. [PEP 492 – Coroutines with async and await syntax](https://peps.python.org/pep-0492/)
