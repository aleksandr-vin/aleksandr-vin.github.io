---
title:  "IDEA Intentions"
tags:   idea dev programming style refactoring hints
---

Reading a comment on your PR, which you normally write youreslf, raises the bar.

That happened today with me. I asked for a code review and got response that everything was good,
except the small comment:

> maybe not for this PR, because it is also in other places, but named parameters would make this
> easier to review with all the None's

That's for the 10 arguments' call with 5 None's in a row. I normally fix such things when I touch them,
as it is really hard to understand what is what there. But that day I was fixing compilation errors after
adding new parameter (to a parameter of that call) and was doing that in bulk (_open error place, add
new default value for the test, next..._) and didn't pay attention to the outlining call with anonymous
args.

So it raised the bar for me: to go and fix it in that PR. But I didn't want to do that by hand. So after
googling for some 10 minutes, I've learned about existance of _Intentions_ in IDEA and one of them is
really the one I need: _Use named parameters for current and subsequent arguments_. To open _Intentions_
for the code, type Opt + Enter and select it from there.

Cool!
