---
title: "Video Production Workflow"
tags: video-production workflow automation macos fcp video-editing tips getting-started site-dev
---

I'm busy with creating a Get Started page for [negotiate.ninja](https://negotiate.ninja/), where there is a How It Works section.
This is a series of steps with media, which I decided to make as GIFs. I've captured raw video from the screen, where I performed the
necessary steps, which I need to cut into parts, add some transformations (like zooming in and out effects) and make final GIF files
per part.

Editiing video in FCP and then, sharing it to Compressor app, to export it in the desired format. I've found that Apple 
Compressor app does a poor-to-average job with GIF exports, due to lack of control over the palette it creates, which is deemed to be
limited to 256 colors.

That lead me to searching on how to do that with ffmpeg. And I've found a good explanation of it,
[here](http://blog.pkh.me/p/21-high-quality-gif-with-ffmpeg.html).

![compressed gif with global palette](/img/compressor-result-with-global-palette.gif){: width="30%" }
![compressed gif with local palette](/img/compressor-result-with-local-palette.gif){: width="30%" }
![ffmpeg'd gif with created palette](/img/ffmpeg-result-with-created-palette.gif){: width="30%" }

Then I've made a custom preset in Compressor from "Prepare for HTTP Live Streaming / Broadband High", only to make it fitting the video
dimensions, which I decided to stay in.

In FCP I've added it as a new share destination, menu File > Share > Add Destination...

Then, using Automator app, I've created a Folder Automation for Movies folder, where I export from FCP (using my custom destination).

![Folder automation script](/img/Screenshot 2024-01-11 at 21.21.42.png){: width="50%" }

It converts mp4 file from ~/Movies into a gif file in the assets folder of the site, that I'm developing.

This way I am editiing the video in FCP, sharing it to a custom destination, switching to browser and refreshing the page (I am running
`ng serve`, which serves the files from local folder).

This is the code for the script:

```
#!/bin/sh
#
# Credits to http://blog.pkh.me/p/21-high-quality-gif-with-ffmpeg.html

if [[ "$1" != *.mp4 ]]
then
  echo File type not supported
  exit 11
fi

palette="/tmp/create-gif-automator-palette.png"
filters="fps=15,scale=-1:-1:flags=lanczos"

output_dir="/Users/aleksandrvin/Developer/marktplaats-gpt-site/src/assets/get-started"
output_filename="$(basename "${1%%.mp4}.gif")"

/opt/homebrew/bin/ffmpeg -i "$1" -vf "$filters,palettegen" -y "$palette"
logger -t gif-creator-script "Palette stored in \"$palette\""

/opt/homebrew/bin/ffmpeg -i "$1" -i "$palette" -lavfi "$filters [x]; [x][1:v] paletteuse" -y "$output_dir/$output_filename"
logger -t gif-creator-script "Creating GIF \"$output_filename\" from \"$1\""

rm "$1"
logger -t gif-creator-script "Original file \"$1\" removed"
```

PS. Do not transfort your video on keyframes until you move the transform anchor to a point of interest of the clip,
[help from ChatGPT](https://chat.openai.com/share/6aad8103-b56b-4031-9cea-75d769c503cf)!