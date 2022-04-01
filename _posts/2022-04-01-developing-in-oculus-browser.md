---
title: "Developing in Oculus Browser"
tags: dev oculus browser workstation
---

So couple of days ago I've stepped into the [gitpod.io](https://gitpod.io/) -- a service that runs VSCode in your browser window and
loads folder from a link.

You put together `gitpod.io/#` and `https://github.com/foo/bar` and the magic happens.

I've got the idea of doing that in Oculus. In browser. Having only the headset, bluetooth keyboard and a mouse tracking device (Apple trackpad).

And now I'm there! Writing this post in my Oculus in gitpod.io workspace with a terminal with bash with VSCode extensions and git integration,
so I can commit and push it to github.com!

Still blind typing without even seeing where the keyboard is is having some complexions (ImmersedVR recently supports passthrough, so
it's much better there, but you need a computer for that).

Plus it appeared that Oculus browser has a shortcut (or at least it feels like this is a shortcut) for Left Shift key to act as an Enter key.
This way it messes up text editing and it took some time to figure that out, while I was trying to make that magit link for gitpod with `#` :-D

Also trackpad support looks basic (or broken): you can't select range of text with the pointer -- it looks like trackpad is simulating the
Oculus controller, which does not know double tap or triple tap and no point-click and drag...

Also there are no settings for the keyboard so far: repeat rate is out of setting in Oculus (at least for now).

But even though, this is already a freaking big step towards the computer-less work life. Or step back to terminal clients for mainframes :)

PS. will commit it like this and add video after.

PPS. You can compile/test/debug and even share running services in gitpod.io, I forgot to mention. YOU NEED TO TRY IT!!!

PPPS. Here is the video (captured on Oculus, uploaded to Vimeo from oculus via browser):

{% include vimeoPlayer.html id="694840441" %}
