---
title: "Mixing Audio in / out"
tags: sound mixing audio win mac
---

If you need to record something that's being playing on the same computer, keep on reading.

## macOs

The was once a tool called Soundflower, now it became Loopback of Rogue Amoeba, which is $125.
It is not installable on m1 and does not compile either.

But there is a better choice – [BlackHole](https://existential.audio/blackhole/), that is gem
(check their [sponsors like on gh](https://github.com/sponsors/ExistentialAudio/).

And don't forget: use *Audio MIDI Setup* app to switch and configre audio devices.

## Windows

### *Stereo mix* device (doesn't work on Shadow PC)

You'll need to enable a *Stereo mix* device in *Sound* control panel applet
(Start > Run > `mmsys.cpl`) in Recording tab.
Then right-click and enable the *Stereo mix* device. If you can't find it there, check this [post](https://www.wintips.org/how-to-enable-stereo-mix-if-not-showing-as-recording-device-in-windows-11-10/) but be aware that downloading driver
from Realtek site is f'n slow (2h on a gigabit!).

### VoicMeeter (works on Shadow PC)

1. Install (VoiceMeeter](https://vb-audio.com/Voicemeeter/index.htm), reboot.
2. Run VoiceMeeter, select your normal output in HARDWARE OUT (BladeShadow for Shadow PC).
3. Open Sound settins, check that output device is *VoiceMeeter Input* and input device is *VoiceMeeter Output*.

Then, for ex. in Discord app choose *VoiceMeeter Output* as input devince in Voice & Video and enjoy.
