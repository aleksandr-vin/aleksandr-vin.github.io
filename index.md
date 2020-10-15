
# Table of Contents

1.  [Sometime you're forced to use old tools <span class="timestamp-wrapper"><span class="timestamp">[2020-10-15 Thu]</span></span>](#org78c077b)
2.  [Something to start with <span class="timestamp-wrapper"><span class="timestamp">[2020-10-15 Thu]</span></span>](#orgd005cb2)
    1.  [I made it. Again. After, maybe, 10 years.](#orgc51fe1b)
    2.  [Here is a link to a note I made last evening about](#org94e52de)
    3.  [Thoughts about VR (home) office](#org7ce7c46)



<a id="org78c077b"></a>

# Sometime you're forced to use old tools <span class="timestamp-wrapper"><span class="timestamp">[2020-10-15 Thu]</span></span>

Somebody's playing in security. You need to use **docker-machine** because you
can't run native **docker** on localhost *(last [commit](https://github.com/docker/machine/commit/b170508bf44c3405e079e26d5fdffe35a64c6972) to docker-machine repo
on github was made more than a year ago)*. And it doesn't work from the box.
So you're tuning it up *(like almost everything on Linux)*.

This time the problem was in the difference of names of the default shared
folder (host `/home` was mounted as `/hosthome` in guest vm, where actual
docker engine runs). And rather loosy behaviour of `-v`, `--volume` option
of `docker run` in comparison to more explicit `--mount`. See question answer
on [superuser.com](https://superuser.com/a/1594651/1230369).


<a id="orgd005cb2"></a>

# Something to start with <span class="timestamp-wrapper"><span class="timestamp">[2020-10-15 Thu]</span></span>

> Everything should be made as simple as possible,
> but not any simpler &#x2014;Albert Einstein


<a id="orgc51fe1b"></a>

## I made it. Again. After, maybe, 10 years.

And again I have the same mood here, I think. I'm home alone, listening to
blues.


<a id="org94e52de"></a>

## Here is a link to a note I made last evening about

[resizing ext4 partition of a guest Ubuntu on vmdk on ESXi 6.0](https://superuser.com/a/1594385/1230369).

I spent some time finding out how to atually resize the disk and wrote down
the steps to remember, and now I have mine **aleksandr.vin**
domain name and a site running on github pages.


<a id="org7ce7c46"></a>

## Thoughts about VR (home) office

Last Friday my colleague told me about Oculus Quest 2. Checking the specs,
I had the same feeling when was reading about DJI Mavic Air 2&#x2026; after not
following any updates on DJI for a 2 years. As the VR headset become much
more powerful and much less heavy, I returned to old idea of using VR headset
as a replacement for home office monitor(s) for coding. It should be ok to
have 2K per eye on resolution, but the questions are:

-   Will it be warm to work?

-   Will it be ok to work for 1 hour before the break (also maintaining
    regular breaks should become a habbit)?

-   Eyes strain and degradation?

So I'm thiking about giving it a try in upcoming months.

