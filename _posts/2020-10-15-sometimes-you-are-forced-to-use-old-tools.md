---
layout: post
title:  "Sometimes you're forced to use old tools"
tags:   security, linux, exp
---

Somebody's playing in security. You need to use **docker-machine**
because you can't run native **docker** on localhost *(last [commit](https://github.com/docker/machine/commit/b170508bf44c3405e079e26d5fdffe35a64c6972) to
docker-machine repo on github was made more than a year ago)*. And
it doesn't work from the box.  So you're tuning it up *(like almost
everything on Linux)*.

This time the problem was in names' differences of default shared
folder (host `/home` was mounted as `/hosthome` in guest vm, where
actual docker engine runs), and rather loosy behaviour of `-v`,
`--volume` option of `docker run` in comparison to more explicit
`--mount`. See question answer on [superuser.com](https://superuser.com/a/1594651/1230369).
