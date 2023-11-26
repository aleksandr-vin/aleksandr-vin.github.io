---
title: "Slow Azure Machine Learning"
tags: azure msft ML slow UI DX UX
---

Playing with Azure Machine Learning (AML) and it is really annoying:

1. It's damn slow --- you _submit an experiment_ (at 18:30), and your _compute cluster_ begins to scale only at 18:34 and finishes at 18:37

2. UI is bloated --- same old MSFT, as it was 20 years ago

3. but completely uncaring at some places --- you select to delete the selected _resource group_, and you are the only one who knows what
   you've just asked for: nothing on the screen (f*ng big and overloaded with all the names and colors and icons) resembles any progress or
   name of the operation -- like nothing happened. Until you refresh the screen, then you'll see a light orange toast.

3. UI is inconsistent:

   a. You _deply a model_, then you stare at the _unhealthy_ status on the _endpoint_ details page (and you go-visit other resources/statuses
      and come back and see same result) for 30 minutes, wrapping your head where to find any logs. Then notification appears saying that
      deployment timed out and you can see more on the _details_ page --- but there will be nothing for you, sucker!

   b. You just worship the cult of _Refresh button_ --- be my guest, hit it everywhere you see it, if you're waiting for something from MSFT.
      (There should be a browser plugin with customizable intervals per every _refresh_ button to be pressed on that portal --- just kidding,
      there should be no custom intervals, that extension should just hit-that-button automatically or it would be from MSFT too).

   c. List of notifications is evolving the way they want: one time you see A, B and C messages, then in 3 min event D appears and message C
      is gone, who cares!

4. You're welcomed into the community who puts everything in the name, because UI does not help with knowing what it is, like:
   `name-of-thing-at-location-and-creation-date-and-thing-type-and-probably-better-to-put-the-author-in-the-name-too`
