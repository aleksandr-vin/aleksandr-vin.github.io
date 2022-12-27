---
title: "Last Week of the Year"
tags: tinkering raspberry pi 
---

Having last week as obligatory vacation I'm finishing some chores at home.

## Shadow on Raspberry Pi

Yep, somehow my pi was running a 32 bit OS. Attempt to install Shadow uncovered
that problem. And now it sounds like a good moment to refresh what I'm running
there:

- [x] avahi — mDNS for service discovery
- [x] netatalk — an AFP fileserver
- [x] minidlna — to stream videos gin LAN
- [x] transmission — a daemon with web UI
- [ ] prometheus
- [ ] node_exporter
- [ ] [mijn-simpel-exporter](https://github.com/aleksandr-vin/mijn-simpel-exporter)
- [ ] grafana
- [ ] homebridge

And actually install Shadow client there at the end.

Put configs to a [repo](https://github.com/xvygyjau/capibara).

## Apple TV

While playing around with Raspberry Pi and walking through settings on ONKYO and Apple TV, I've stepped
into HDR resolution and *Match frame rate* + *Match color range* settings there, which have pros and cons:

### Pros

- Colors range is nice
- It's nice to know that for that movie on Netflix your eyes are less annoyed by default 50Hz
  that beamer refreshes the picture but that it actually runs smothly at 24Hz of that content

### Cons

- It takes 3-5 seconds for my beamer, Optoma, to switch modes. The most jerking happens in Youtube: when
  the mode is switched for the ads which are kindly stitched into the video.

## Back to Shadow on Raspberry Pi

Okay, Shadow client installed following [this blog post](https://shadow.tech/blog/teamshadow/shadow-raspberry-pi).
Some things still not working:

- [ ] Audio is not working on Raspberry Pi
- [ ] Nimbus+ game pad connected by bluetooth, but on shadow Windows it's vertical axis is reversed
- [ ] And mouse over bluetooth is lagging a bit. That *Delux m618 mini* mouse has a radio USB dongle, but looks like
  [drivers](https://www.deluxworld.com/en-service.html?stoken=4e642cda56a52c5f42a222bac9db468e&title=618) are only for Windows.

## Steam Remote Play and Family Sharing

Late night, I'm sitting at the table with my daughter, both at macbooks, both running Steam. She's through Shadow
client and she's in her personal Steam account. I'm sharing my games lib with her and she's starting Untitled
Goose Game and inviting me for remote play. It took us something around 30 min to figure out how to start it
and that we need at least one game controller! And Steam's chat system really sucks!

We need to find out how to connect Switch Joy controllers to macbook tomorrow...

And we gonna stream games via Discord to our family.