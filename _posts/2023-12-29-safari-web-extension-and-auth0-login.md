---
title: "Safari Web Extension and Auth0 Log-in: the Good, the Bad and the Ugly"
tags: safari apple web-extension callbacks auth0 login browser.runtime
---


## The Good

Simply works with Chrome as extension id is a stable identifier there, and you can regitser a callback url in Auth0 as constant string
`chrome-extension://xxxxxxxxxxxxxxxyyyyyyyyyyyyyzzzzzzzzzzzz/options.html`.


## The Bad

Safari makes a new extension id every time you install the extension (via companion app), so every time you build it in xcode and run
--- you get a new url, every user who installs extension --- gets a new unique url. And Auth0 does not allow you to wildcard callback urls.


## And the Ugly

Looking for a solution.


### 1. Add new extension ids to auth0's callback_urls via my backend

Every time you open extension's options page, it triggers a request to your backend and provides it's extension id, and there you add it
to a list of allowed callback_urls via auth0 management api. Bloody straight.


### 2. Redirect to an owned endpoint

So you launch authentication flow with redirect_to: https://my-backend/redirect. Which can then redirect to a specific options url which
is unique safari-web-extension://XXXX-.....-XXXX/options.html. But you need to provide this `XXXX-.....-XXXX` extension id to your backend.
And Auth0 does not allow you to parameterise the redirect_to callbacks either.

Note: there is only one wildcard supported by auth0, which is subdomain, so you can redirect to https://XXXX-.....-XXXX.my-backend/redirect,
but that brings complexity to your backend hosting provider.

I thought that browser would hint the `XXXX-.....-XXXX` somehow (in Referer for example), but hi did not.


### 3. Login on your site and message access token to your extension

There is a way to send message from
[webpage to safari web extension](https://developer.apple.com/documentation/safariservices/safari_web_extensions/messaging_between_a_webpage_and_your_safari_web_extension),
but that technique simply did not work. [My question](https://developer.apple.com/forums/thread/708820?login%253Dtrue%2526page%253D1#775559022)
in apple support forum.

**UPDATE:** it works, but could be silently not working with non-SSL (http) or localhost or not production extension build (?) -- it just appeared
to be working with real domain name...


### 4. Login on your site and then window.open options page + `#access-token=xyz`

That should not expose the secret on the internet as browser should open extension options page netively. But Chrome blocks the page chrome-extension://djjiokkmnhkmccblpacjpegaaiebcmhm/options.html when you try to open it from the site, unless you specify the page in `"web_accessible_resources"`!


### 5. Login on your site, hide a div tag with secret on the page and find it with content script

Playing hide-and-seek, but that can work. Adding `<div id="my-very-secret-message-to-my-extension" value="xyz" hidden="true"></div>` on the site's page
after login, and query for it in content script.
