---
title: "VR Workspace"
tags: vr, workspace, work, setup, future, performance
---

Random thoughts on the workspace (for future me).

Tasks that I perform most of the time are:
1. Researching the Internet
2. Programming a thing

Let's have a deeper dive.

# The process

## Researching the Internet

That includes:
- Searching answers to a question
- Searching for examples
- Searching for a better description of the problem
- Searching for records (wikipedia) about something or somebody
- Searching for tutorials
- Searching for documentation

Then it becomes:
- Reading the articles
- Following the links
- Making notes (!) **(that proved to be a big problem as you need to get back to your notes and work with them later)**
- Correcting the docs (best through Github PRs)

## Programming a thing

It is hard to separate it from the previous process, as it vastly intersects, but still, let's enumerate:
- Playing with examples (in playgrounds)
- Applying what you've learned (can be in a new Github repo or new PR to existing one, or an issue if you've found smth.
  isn't right)
- Experimenting with specific tools (for example, try in Logic Pro something you learned about audio processing, or try
  something in Unity)

# Execution

So we've defined the steps of the process, let's think on how to execute them. Currently I see these setups:

1. At the desk: macbook on a stand, external keyboard, touchpad, sometimes mouse, midi keyboard, audio interface, monitors,
   studio microphone, wall desk from IKEA.
2. At the couch: macbook on your knees.
3. In VR at the desk: Oculus Quest 2, external keyboard and touchpad, immersedVR app to cast (virtual) screens from macbook into VR.

I don't want to explain first 2, but the one in VR has some thoughts.

## VR

I'm standing in VR, as I don't have any process that involves movement, so stand (maybe seated) doesn't add to nausea.
I use pass-through to "stay" in the real environment. That increases the speed of getting to the keyboard. I tried displaying
virtual keyboard at the place where real keyboard is but small discrepancies breaks the whole thing. That's why having a
old-style keyboard wins vs thin one on the macbook: there is a difference between blind typing and not seeing you keyboard
(with peripherial view) at all. Same for touchpad: it is way better to have a real self-standing object that you can locate
with non-precise gesture and then when you located it do the fine moves to operate it.

In VR the space around you is the advantage. So it is handy to have a big screen, where you can place different things in
different corners. But if it could be no screen at all -- that would be even better: you can seamingly arrange "windows"
around you and even place some closer to you and some further.

Then typing: it could be beneficial not to have real keyboard and touchpad in VR at all. But then how to input? Controllers
or hands (that are tracked). Controllers can be better to fine-interact with VR environment, maybe because they have joysticks
and buttons that allow discrete states so that you don't accidently stop interaction session with an object. That can happen
with tracked hands, as tracking can temporarily decide that you moved your finger a bit wider and then you drop an object or
untap the button. Also typing on a virtual keyboard is not that fast as on real one, that can be because the skill was not
trained that long and maybe it can be improved with time. Alternatives: voice input. Maybe dictating text can be the key,
especially when you use hands (or tracked eye direction) to assist, like: "Replace this *pointing with your finger* phrase with ...".

### Resources

Quick notes on what looks promising to help working in VR:

1. Gitpod [gitpod.io](https://www.gitpod.io) -- vscode in browser with compilation and running
2. WebXR [immersiveweb.dev](https://immersiveweb.dev) -- interfacing sites with/from VR
3. Shadow [shadow.tech](https://shadow.tech/) -- virtual computer with desktop that can be streamed into headset
