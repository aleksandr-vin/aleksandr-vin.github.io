---
title: "GoDaddyourself!"
tags: dns customer-rights russian war domain support bullshit
---

One Monday evening, 11 December 2023 to be precise, I've got mail from GoDaddy --- the easy domain registrator company, I've used.
The mail titled _"Important Notice Regarding Your GoDaddy Account"_:

> Important Notice
> Our records indicate you or a contact listed in your account may be located in the Russian Federation. If our records are correct,
> your account(s) and/or affected product(s) will be terminated as of December 31, 2023.
>
> For domain registrations, you have until December 31, 2023 to initiate the transfer of any impacted domain(s) to a registrar of
> your choice, subject to the incoming transfer restrictions of other registrars.  For instructions on transferring domains, see
> https://www.godaddy.com/help/transfer-my-domain-away-from-godaddy-3560
>
> For all other products, your access to all data and content on file with us will be terminated as of December 31, 2023, and we
> will not be able to provide you with backups. Accordingly, we are respectfully asking you to retrieve your data and transfer any
> products you have with us to a new provider prior to that date.
>
> You will not have access to your account(s) and/or affected product(s) once they are terminated.
>
> We appreciate your business and apologize for any inconvenience.

I am living in the Netherlands for more than 7 years now and became an EU citizen. In GoDaddy they never asked to change anything
and were only billing my credit card once a year. I've hopped into their management console and checked where do I have any Russian
traces, I've found my old address in account profile, which I immediately changed.

But, you know what --- I've recently learned
that nowadays **we do not have any customer rights**, at all --- if a company (a worker, their computer or AI, whatever) decides
that you violates something or you act strangely, they apply ban, terminate your account or block you and you have nothing (or
eternity) to do to help yourself. Support lines --- forget it: you can finish a novel while texting their chat bot or explaining
what happenned to mediocre assistant who just reads what on their's screen and types in your answers. Lucky to find a support phone
number --- do not fool yourself: ladies room's waiting line in a theater will look like a race track in comparison.

So I've checked their online chat and skid through their bot to a human assistant. Dropped the first paragraph of their email and
was asked to provide my account number and PIN. Will skip the part where support was sending me a secure form link, which was not
loading due to problems on their site or server configuration (I've checked the network tab and console, which was full of errors).

![Secure support form not working, one](/img/Screenshot 2023-12-11 at 22.44.00.png){:  width="100%" }
![Secure support form not working, two](/img/Screenshot 2023-12-11 at 22.54.13.png){:  width="100%" }

I've finnaly found that PIN and sent it plaintext in the chat after pointing that form links didn't work for couple of times. Next,
to my surprise, I was asked for 6 digit code of my 2FA, which I have on my account. I've raised my concerns that this is new to me:
we all have been learned things like "Our support will never ask your password or PIN numbers". And again, I've been sent a secure
form to provide these 6 digits. Still being unsure, I've asked if I can be directed to a proof link where it is said that support
can ask for 2FA codes. And simultaneously (as it takes minutes for them to type back the reply) searched for a proof myself. I've
found a [community thread](https://community.godaddy.com/s/question/0D58W000070zv7GSAQ/can-godaddy-support-not-actually-access-an-account-if-said-account-has-enabled-two-factor-authentication)
where there was a reply given and I decided that at least it proofs this is a practice in GoDaddy.

![Webarchive screenshot](https://web.archive.org/web/20231212102036/http://web.archive.org/screenshot/https://community.godaddy.com/s/question/0D58W000070zv7GSAQ/can-godaddy-support-not-actually-access-an-account-if-said-account-has-enabled-two-factor-authentication)

When I've returned (after 1-2 minutes)
to the chat, I saw that support personnel dropped that conversation without any reply and I was left to chat bot. Ok, rushed through
it again into the hands of another human and again through process of trying secure forms and finally I'm here: support is checking
my account profile and returning to me saying that there is nothing that will lead to termination of it in the long future.

But, again, should you just put everything you have on that domain name in the hands of somebody on another side of that chat, who
just easily saing to you _"I don't see any problems with your account, you can ignore that email as a bug from us"_ and wait till
1st of January, 2024, when their (buggy?) system will send you another email, saying _"Your account is terminated"_? I would not.

I don't want to, but still will make a note here, that that lightly-minded support assistant was annoying me after that with attempts
to sell their domain protection bullshit. Saying only _"it will protect your domains from unauthorized actions and from accidental
expiring"_, for three or four times in a row, while I was insistingly asking him to explain me **how** exactly this protection plan
is going to do that? He even tried to give me this explanation: _"you buy the protection plan an then it protects your domains"_!
Eventually he put it close enough, I know now that: they will send OTP to my email on every change action to protected domain and
extend expiration window from 30 days to 60. Maybe I'd go for OTP if I was not considering to run away from such service already
at that moment.

Somehow that night I thought I'm fine and went offline.

Next morning something still felt not okay: some light sense of somebody was not doing his job truly --- running a light-minded check
and promising something that he can't guarranty and that can lead to devastating consequencies. My god, how much of such thoughts
do I have in recent months, I wish I can make something with that.

I've decided to check what it takes to transfer a domain name to another registrator. My choice was _namecheap.com_. I've made an
account and ran through their transfer-domain check, it was estimated around 48,- EUR for _aleksandr.vin_ --- looks like a price
for 1 year ownership for *.vin domain name at their shop (even cheaper than it is in GD --- around 70,-).

And you know what? While drilling into the domain settings in GD, I've found that there is a separate address and email and phone
settings per domain and their still sits my former address in Russia. I foresee 1st of January, 2024, some script on GD servers
to terminate the account due to that f***up of a customer support assistent, who for F! could be not even working at GD by that
time, ni-i-ice.

Some notes on the transfer process. Transfer guide from namecheap warns about a possibility to shot-your-leg:

> **Important:** If you make any changes to the **Registrant First and Last name**, **Organization name** or **Email address**,
> GoDaddy will put a **60-day lock** that will prevent outgoing transfers. Updates to any other piece of contact information should
> not trigger this lock.

So I decided to make the transfer ASAP and not draw chances.

In short, GD interface is a bummer: not only it reloads the page almost on every click of their interface, but also,
every time you open your domain from Domain Portfolio, it nags with inconsistent dialogs like:
- "Turn off autorenewal ..." --- you click continue (you already decided to transfer it away, why not), and it says "There was a
  problem ..."
- "Turn off domain privacy ..." --- why you ask me that if I made no attempts to turn it off?

When you initiates transfering of your domain, it makes no visible changes to your domain record in _Domain Portfolio_ and nothing
appears in _Transfers_ section. It took around an hour (during which I finally decided to write down this post) for them to list it
in _Transfers Out_ section.

Again, an example of poor UX design here: you open _Transfers_ section and suddenly you see an empty page with
_Transfers In_ tab selected (nothing listed here as expected), you recognise that now this _Transfers_ page looks different and you
see _Transfers Out_ tab too, where only after you select it, you see your expected domain and the so-much-awaited _Approve Transfer_
button, which you click and after your approval the whole _Transfers_ page mimics to it's original everyday view -- F! the consistency
in our UI!

Page, when you have something:
![Transfers page, when you have something](/img/Screenshot 2023-12-12 at 12.08.22.png)

Same page, when you have nothing:
![Transfers page, when you have nothing](/img/Screenshot 2023-12-12 at 12.24.49.png)

And after you approved the transfer, GD will not render your domain name anywhere on it's pages. Very nice. No statuses in _Domain
Portfolio_, nothing in _Transfers_. Okay --- I've found it only in billing receipts in order history.

Hope everything will be fine, as namecheap is still _awaiting release from previous registrar_:

![Awaiting release from previous registrar](/img/Screenshot%202023-12-12%20at%2012.32.37.png)


## And some more fun/ck from GD

I have some other domains, that I don't care much, but their are still mine for 1/2 year. One has a nice-looking name and GD always
nags me with it's estimated value of $293, which I've baught for £1.69. So, being around the GD interfaces in recent hours,
I've decided to list it for sale with this hustlers. I clicked _List for Sale_ button, set the price and clicked _Publish Listing_.

Then GD brings in some random sheet and informed me that it will make an account in some _Afternic_ (WTF?) for me. Okay, anyway,
clicking further... and bum! An error --- "it didn't make it". Trying again the listing process: setting the price, publishing,
... and now I need to _"sign into Afternic"_. With what password? Checking email...

![Email from Afternic](/img/Screenshot%202023-12-12%20at%2012.48.19.png){: width="50%" }

So with GD account, right...

![There's already an Afternic account associated with your email](/img/Screenshot%202023-12-12%20at%2012.50.47.png){: width="50%" }

So they do create an account on my email and failed to transfer any knowledge about it to me and now I need to link it (do I?) or
just to log-in to a system I learned 2 min ago for what?... I've already forgot what I was aiming for?

So this is all so bulltish to me, that I'm running out of words.

And yes, I thought that was it. Check yourself: I can't reset my password as:

> No accounts exist with that username.

![No accounts exist with that username.](/img/Screenshot%202023-12-12%20at%2012.55.34.png){: width="50%" }

Go F! yourself, GoDaddy!

(Still _awaiting release from previous registrar_, while I' made up to here).

PS. Domain was successfully transferred, and then reconfigured.
PPS. And next morning I've received an email from Richard Kirkendall, CEO of Namecheap Inc --- hope for
     long and good relationship with them.
