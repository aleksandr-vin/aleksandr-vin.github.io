---
title: "Workaround for Betaflight, VTX or SmartAudio"
tags: fpv drones hobby workarounds betaflight vtx smartaudio power config setup bug bench rushfpv tinyhawk
---

Since I learned that my Tinyhawk's upgraded [Rushfpv Tank Ultimate mini VTX](https://rushfpv.net/products/tank-ultimate-mini-vtx) supports
different power levels, I started switching it to 800mW most of the flights. But I was doing it with the key, as the button on the pcb was
almost hidden, because of the original orientation of the vtx board. I turned it 90º last time and it became possible to push with the finger.
And last Saturday I saw a [video from Josha Bardwell](https://www.youtube.com/watch?v=a1_U2v0kAjg) on how to setup it on radio.

In short, you supply `vtx 1 6 0 0 2 1100 1300` commands in CLI and that's it. In short.

Parameters are:
1. Line index (from 0), to see all lines there is a `vtx` command
2. Receiver AUX number (from 0)
3. Band to switch to (0 means no change)
4. Channel to switch to (0 means no change)
5. Power value index (from 1) to switch to
6. AUX range min
6. AUX range max

In short all this worked well for Mobula6 (messed up min max ranges at the beginning), where I had this:
![VTX page on Mobula6](/img/Screenshot 2024-09-01 at 13.35.47.png)

And I set 6 position buttons on Boxer like this:

```
vtx 0 6 0 0 1 900 1100
vtx 1 6 0 0 3 1100 1300
vtx 2 6 0 0 4 1300 1500
vtx 3 6 0 0 5 1500 1700
vtx 4 6 0 0 5 1700 1900
vtx 5 6 0 0 5 1900 2100
save
```

Skipping power level labeled `RCE` because it was changing the channel or band so the picture on the screen was partially off.

BTW, power level **values** are mW converted to dBm (at least for SmartAudio 2.1 as I heard [here](https://www.youtube.com/watch?v=thR2XA_0PLM)).

Then in Tinyhawk it did not work for the last power value. I had this for Tinyhawk:
![VTX page on Tinyhawk](/img/Screenshot 2024-09-01 at 13.02.22.png)

That's exactly 4 values that this VTX supports and I applied commands in cli:

```
vtx 0 6 0 0 1 900 1100
vtx 1 6 0 0 2 1100 1300
vtx 2 6 0 0 3 1300 1500
vtx 3 6 0 0 4 1500 1700

###ERROR: PARSE ERROR###

vtx 4 6 0 0 4 1700 1900

###ERROR: PARSE ERROR###

vtx 5 6 0 0 4 1900 2100

###ERROR: PARSE ERROR###

```

And all with power value index 4 were failing!

Trying to search the Internet I didn't find any answer or clue. I tried changing to 0-1-2-3 values as JB mentioned for 2.0 SmartAudio, but that
did not work.

Then I thought if that's a border bug with the array len, when you compare index to array len and miss the start-from-zero. I added one more
power value, dubbed it...

```
vtxtable powerlevels 5
vtxtable powervalues 14 23 27 29 29
vtxtable powerlabels 25 200 500 800 MAX
save
```

and it worked!

```
vtx 0 6 0 0 1 900 1100
vtx 1 6 0 0 2 1100 1300
vtx 2 6 0 0 3 1300 1500
vtx 3 6 0 0 4 1500 1700
vtx 4 6 0 0 4 1700 1900
vtx 5 6 0 0 4 1900 2100
```

Maybe if I upgrade the BF on the FC that issue will be gone, but I'll check it some other day.

Here is the BF logs, just in case:

```
2024-09-02 @09:57:24 -- OS: **macOS**
2024-09-02 @09:57:24 -- Configurator: **10.10.0 (c97deaf)**
2024-09-02 @10:01:26 -- Serial port successfully opened with ID: 1
2024-09-02 @10:01:26 -- MultiWii API version: **1.42.0**
2024-09-02 @10:01:26 -- Flight controller info, identifier: **BTFL**, version: **4.1.0**
2024-09-02 @10:01:26 -- Running firmware released on: **Oct 16 2019 11:57:34**
2024-09-02 @10:01:26 -- Board: **MTKS/MATEKF411RX(STM32F411)**, version: **0**
2024-09-02 @10:01:26 -- Unique device ID: **0x2300444247500f20303634**
2024-09-02 @10:01:26 -- Craft name: **TH**
2024-09-02 @10:01:26 -- **Arming Disabled**
2024-09-02 @10:01:44 -- CLI mode detected
2024-09-02 @10:02:04 -- Serial port successfully closed
2024-09-02 @10:02:19 -- Serial port successfully opened with ID: 2
2024-09-02 @10:02:19 -- MultiWii API version: **1.42.0**
2024-09-02 @10:02:19 -- Flight controller info, identifier: **BTFL**, version: **4.1.0**
2024-09-02 @10:02:19 -- Running firmware released on: **Oct 16 2019 11:57:34**
2024-09-02 @10:02:19 -- Board: **MTKS/MATEKF411RX(STM32F411)**, version: **0**
2024-09-02 @10:02:19 -- Unique device ID: **0x2300444247500f20303634**
2024-09-02 @10:02:19 -- Craft name: **TH**
2024-09-02 @10:02:19 -- **Arming Disabled**
2024-09-02 @10:02:51 -- CLI mode detected
2024-09-02 @10:02:53 -- Device - Rebooting
2024-09-02 @10:02:53 -- Serial port successfully closed
2024-09-02 @10:02:57 -- Serial port successfully opened with ID: 3
2024-09-02 @10:02:57 -- MultiWii API version: **1.42.0**
2024-09-02 @10:02:57 -- Flight controller info, identifier: **BTFL**, version: **4.1.0**
2024-09-02 @10:02:57 -- Running firmware released on: **Oct 16 2019 11:57:34**
2024-09-02 @10:02:57 -- Board: **MTKS/MATEKF411RX(STM32F411)**, version: **0**
2024-09-02 @10:02:57 -- Unique device ID: **0x2300444247500f20303634**
2024-09-02 @10:02:57 -- Craft name: **TH**
2024-09-02 @10:02:57 -- **Arming Disabled**
2024-09-02 @10:02:57 -- Device - Ready
2024-09-02 @10:03:06 -- CLI mode detected
2024-09-02 @10:03:14 -- Serial port successfully closed
2024-09-02 @10:04:08 -- Serial port successfully opened with ID: 4
2024-09-02 @10:04:08 -- MultiWii API version: **1.42.0**
2024-09-02 @10:04:08 -- Flight controller info, identifier: **BTFL**, version: **4.1.0**
2024-09-02 @10:04:08 -- Running firmware released on: **Oct 16 2019 11:57:34**
2024-09-02 @10:04:08 -- Board: **MTKS/MATEKF411RX(STM32F411)**, version: **0**
2024-09-02 @10:04:08 -- Unique device ID: **0x2300444247500f20303634**
2024-09-02 @10:04:08 -- Craft name: **TH**
2024-09-02 @10:04:08 -- **Arming Disabled**
2024-09-02 @10:04:10 -- CLI mode detected
2024-09-02 @10:04:15 -- Serial port successfully closed
2024-09-02 @10:04:26 -- Serial port successfully opened with ID: 5
2024-09-02 @10:04:26 -- MultiWii API version: **1.42.0**
2024-09-02 @10:04:26 -- Flight controller info, identifier: **BTFL**, version: **4.1.0**
2024-09-02 @10:04:26 -- Running firmware released on: **Oct 16 2019 11:57:34**
2024-09-02 @10:04:26 -- Board: **MTKS/MATEKF411RX(STM32F411)**, version: **0**
2024-09-02 @10:04:27 -- Unique device ID: **0x2300444247500f20303634**
2024-09-02 @10:04:27 -- Craft name: **TH**
2024-09-02 @10:04:27 -- **Arming Disabled**
2024-09-02 @10:04:28 -- CLI mode detected
2024-09-02 @10:05:30 -- Serial port successfully closed
2024-09-02 @10:05:37 -- Serial port successfully opened with ID: 6
2024-09-02 @10:05:37 -- MultiWii API version: **1.42.0**
2024-09-02 @10:05:37 -- Flight controller info, identifier: **BTFL**, version: **4.1.0**
2024-09-02 @10:05:37 -- Running firmware released on: **Oct 16 2019 11:57:34**
2024-09-02 @10:05:37 -- Board: **MTKS/MATEKF411RX(STM32F411)**, version: **0**
2024-09-02 @10:05:37 -- Unique device ID: **0x2300444247500f20303634**
2024-09-02 @10:05:37 -- Craft name: **TH**
2024-09-02 @10:05:37 -- **Arming Disabled**
2024-09-02 @10:05:43 -- CLI mode detected
2024-09-02 @10:05:57 -- Serial port successfully closed
2024-09-02 @10:06:04 -- Serial port successfully opened with ID: 7
2024-09-02 @10:06:04 -- MultiWii API version: **1.42.0**
2024-09-02 @10:06:04 -- Flight controller info, identifier: **BTFL**, version: **4.1.0**
2024-09-02 @10:06:04 -- Running firmware released on: **Oct 16 2019 11:57:34**
2024-09-02 @10:06:04 -- Board: **MTKS/MATEKF411RX(STM32F411)**, version: **0**
2024-09-02 @10:06:04 -- Unique device ID: **0x2300444247500f20303634**
2024-09-02 @10:06:04 -- Craft name: **TH**
2024-09-02 @10:06:04 -- **Arming Disabled**
2024-09-02 @10:06:17 -- EEPROM saved
2024-09-02 @10:06:29 -- CLI mode detected
2024-09-02 @10:06:51 -- Serial port successfully closed
2024-09-02 @10:06:51 -- Device - Rebooting
2024-09-02 @10:07:01 -- Failed to open serial port
2024-09-02 @10:14:55 -- Serial port successfully opened with ID: 8
2024-09-02 @10:14:55 -- MultiWii API version: **1.42.0**
2024-09-02 @10:14:55 -- Flight controller info, identifier: **BTFL**, version: **4.1.0**
2024-09-02 @10:14:55 -- Running firmware released on: **Oct 16 2019 11:57:34**
2024-09-02 @10:14:55 -- Board: **MTKS/MATEKF411RX(STM32F411)**, version: **0**
2024-09-02 @10:14:55 -- Unique device ID: **0x2300444247500f20303634**
2024-09-02 @10:14:55 -- Craft name: **TH**
2024-09-02 @10:14:55 -- **Arming Disabled**
2024-09-02 @10:15:00 -- CLI mode detected
2024-09-02 @10:15:12 -- Serial port successfully closed
2024-09-02 @10:15:18 -- Serial port successfully opened with ID: 9
2024-09-02 @10:15:18 -- MultiWii API version: **1.42.0**
2024-09-02 @10:15:18 -- Flight controller info, identifier: **BTFL**, version: **4.1.0**
2024-09-02 @10:15:18 -- Running firmware released on: **Oct 16 2019 11:57:34**
2024-09-02 @10:15:18 -- Board: **MTKS/MATEKF411RX(STM32F411)**, version: **0**
2024-09-02 @10:15:18 -- Unique device ID: **0x2300444247500f20303634**
2024-09-02 @10:15:18 -- Craft name: **TH**
2024-09-02 @10:15:18 -- **Arming Disabled**
2024-09-02 @10:15:33 -- CLI mode detected
2024-09-02 @10:17:15 -- Serial port successfully closed
2024-09-02 @10:17:20 -- Serial port successfully opened with ID: 10
2024-09-02 @10:17:20 -- MultiWii API version: **1.42.0**
2024-09-02 @10:17:20 -- Flight controller info, identifier: **BTFL**, version: **4.1.0**
2024-09-02 @10:17:20 -- Running firmware released on: **Oct 16 2019 11:57:34**
2024-09-02 @10:17:20 -- Board: **MTKS/MATEKF411RX(STM32F411)**, version: **0**
2024-09-02 @10:17:20 -- Unique device ID: **0x2300444247500f20303634**
2024-09-02 @10:17:20 -- Craft name: **TH**
2024-09-02 @10:17:20 -- **Arming Disabled**
2024-09-02 @10:17:36 -- CLI mode detected
2024-09-02 @10:17:50 -- Device - Rebooting
2024-09-02 @10:17:51 -- Serial port successfully closed
2024-09-02 @10:18:01 -- Failed to open serial port
2024-09-02 @10:18:14 -- Serial port successfully opened with ID: 11
2024-09-02 @10:18:14 -- MultiWii API version: **1.42.0**
2024-09-02 @10:18:14 -- Flight controller info, identifier: **BTFL**, version: **4.1.0**
2024-09-02 @10:18:14 -- Running firmware released on: **Oct 16 2019 11:57:34**
2024-09-02 @10:18:14 -- Board: **MTKS/MATEKF411RX(STM32F411)**, version: **0**
2024-09-02 @10:18:14 -- Unique device ID: **0x2300444247500f20303634**
2024-09-02 @10:18:14 -- Craft name: **TH**
2024-09-02 @10:18:14 -- **Arming Disabled**
2024-09-02 @10:18:22 -- EEPROM saved
2024-09-02 @10:18:39 -- EEPROM saved
2024-09-02 @10:18:50 -- **Arming Enabled**
2024-09-02 @10:18:50 -- **Runaway Takeoff Prevention Enabled**
2024-09-02 @10:18:50 -- Serial port successfully closed
2024-09-02 @10:19:38 -- Serial port successfully opened with ID: 12
2024-09-02 @10:19:39 -- MultiWii API version: **1.42.0**
2024-09-02 @10:19:39 -- Flight controller info, identifier: **BTFL**, version: **4.1.0**
2024-09-02 @10:19:39 -- Running firmware released on: **Oct 16 2019 11:57:34**
2024-09-02 @10:19:39 -- Board: **MTKS/MATEKF411RX(STM32F411)**, version: **0**
2024-09-02 @10:19:39 -- Unique device ID: **0x2300444247500f20303634**
2024-09-02 @10:19:39 -- Craft name: **TH**
2024-09-02 @10:19:39 -- **Arming Disabled**
2024-09-02 @10:19:48 -- EEPROM saved
2024-09-02 @10:19:56 -- CLI mode detected
2024-09-02 @10:20:17 -- Serial port successfully closed
2024-09-02 @10:20:17 -- Device - Rebooting
2024-09-02 @10:20:27 -- Failed to open serial port
```
