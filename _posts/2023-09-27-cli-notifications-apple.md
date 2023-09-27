---
title: "Once again: notifying of long-running cli commands' completion, in Apple ecosystem"
tags: cli notify apple scripts applescript jobs productivity
---

Once again I'm starting a long task in terminal and I don't want to wait for it infront of the screen. I've already had
two options before: `imessageme` and `facetimeme` -- two aliases for [small cli scripts](https://github.com/aleksandr-vin/macos-scripts)
that sends iMesasge to me and calls me (my iPhone was showing that I'm calling), which I was placing after a long-running task. Somehow 
Facetime trick stopped working and iMessage was not notifying me on messages from myself anymore (probably treating them as readed).
So what I've eneded up now is a new script that creates a reminder in Reminder.app with immediate due date. This way you:

1. Get a notification on all your Apple devices (Mac, iPhone, Apple Watch, AirPods?)
2. Exploit common Reminders' UX, like _Remind Me in an Hour_ or _Mark as Completed_
3. Have a list of such _Reports_

As an extension, I've even made a `remind-job-done` shell function that can remind you when a shell job is finished, adding
the start time of the process, the time you asked to remind about it (_Waited since ..._) and the success/failure designator.

Check the scripts at [aleksandr-vin/macos-scripts](https://github.com/aleksandr-vin/macos-scripts).

## Example

```
brew upgrade & remind-job-done
```

Then `brew upgrade` is made a background job which is immediately put into foreground and waited for completion.

This is how you see notification on iPhone:
![Notification on iPhone](/img/iphone-notification.jpg){: width="50%" }

And on Apple Watch:
![Notification on Apple Watch](/img/apple-watch-notification.png){: width="50%" }

And in Reminders.app:
![List of notifications in Reminders.app](/img/reports-reminders.png){: width="50%" }
