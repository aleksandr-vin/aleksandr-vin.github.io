---
title: "ChatGPT companion for Marktplaats conversations"
tags: chatgpt marktplaats bot telegram conversations service idea
---

Did you ever sell something on [marktplaats.nl](https://marktplaats.nl)? So many people ask for 50% discount from first message!

So one Friday morning I thought: what if I make ChatGPT keep such conversations, convincing these people to buy at the listed
price. And by the end of that day I had a command-line tool that was listing my marktplaats' conversations and was able
to answer to potential buyers with a ChatGPT-suggested answer.

After playing around with that, I decided to not allow it to answer automatically and wrapped it in a Telegram Bot. So it
become a selling representative, who can list user's conversations, fetch messages of the selected conversation and product
description from marktplaats.nl, and ask ChatGPT (`gpt-4` model worked better than `gpt-3.5-turbo`) for a suggested answer.
You can regenerate the suggestion if you don't like it.

Even in this inital version it helped me to make a deal with one guy. ChatGPT made elaborative answers pointing out why
the item worth the price that I've set. It described good sides of the deal and made it way better than I would have done it
myself.

Since than I've added some features to that bot, mostly because I wanted to make it a paid service eventually, and needed
to bring friends to test it. Making the list of features as this:

1. Change of context, which is used to configure ChatGPT
2. Save cookie -- this is the main mean of authentication on marktplaats.nl for now
3. Activate/deactivate user
4. Set user's quota on OpenAI usage -- I don't want one user to completely drain my OpenAI account :)

If you're willing to try it yourself, here it is: [@mpSalesRepBot](https://t.me/mpSalesRepBot) -- start with `/help` command,
or `/start`.

BTW, the default context looks like this:

> You are selling your item on marktplaats.nl.
> A potential buyer is asking questions.
> Answer questions and do not lower the price.
> Convince the buyer to buy it for defined price.
> All messages from 'user' are proxied buyers messages.

PS. Meanwhile, I've tried to reach Marktplaats guys to register me as a partner and give me a normal authentication via API,
but still waiting for their response.
