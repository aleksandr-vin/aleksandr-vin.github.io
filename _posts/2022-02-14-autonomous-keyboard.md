---
title:  "Autonomous keyboard"
tags:   uhk keyboard modding bt batteries wires soldering usb
---

It all started at ING, where I was stuck with ~elite book~ HP waiting for a macbook. I was desparate enough to search and by a UHK (version 1 at that time).

The keyboard is cool but can be cooler. Later that year I'v got Oculus Quest 2 and started using it for everyday work (in ImmersedVR). But the keyboard you don't
see. You need to try it to feel the differences: "you don't look at the keyboard" vs. "you don't see the keyboard". But that's another story. The point with VR
is that you can have you computer somewhere (even in a DC) and HMD on you head and you don't need to sit at your desktop: you can relax in your coach, on a floor
mat, stand somewhere in the room. You just need a good network connection to your computer. And a remotely enabled input devices like touchpad and keyboard.

So I've got a [BT-500](http://handheldsci.com/kb/) adapter that let me working autonomously with the keyboard but with a USB cable hanging from it and plugged
through that doungle into the battery pack.

Now, after almost a year I've checked the internals of the UHK to see that there's no space to wire-up that doungle's chip (with USB sockets taken off) inside the
case. The UHK guys doesn't share the CAD files for the case – that could help 3D printing the modded case with a place to hold the chip. And also, the palm rests
looks like a good place to hide the battery pack.

After thinking about where to hide the chip, I stepped back and decided to do less damage to UHK for now and soldered a short tail of USB mini-b to the BT-500, plugging it into the keyboard the designed way and duck-taped it to the case.

![autonomous-keyboard-1](/img/autonomous-keyboard-1.jpeg){: width="50%" }

The keyboard now is BT-enabled but plugged into socket for elecricity.

Next steps would be:

1. Hide the dongle inside
2. Put battery pack into the palm rests (see [model 1](https://www.prusaprinters.org/prints/29287-palm-rest-for-ultimate-hacking-keyboard) and [model 2](https://www.prusaprinters.org/prints/32425-ultimate-hacking-keyboard-wrist-rests))
3. Potentially making a case, see [DIY cases](https://ultimatehackingkeyboard.com/blog/2019/05/01/diy-uhk-carrying-cases)

TBC

Refs:
1. http://handheldsci.com/wp/wp-content/uploads/Manual_Full_v5.2.10.pdf
