---
layout: post
title:  "Refactoring hints"
tags:   refactoring, maven, tests, recompile, rebuild
---

Random hints on refactoring.

Refactorings differ, but some hints remain useful. Recently I was busy with a massive change of a common functionality, such
as _logging_ interface across a multi-module project.


## Some project stats:

For _scala_ and _java_ files:
```
sloc . --exclude '\.(html|xml|yaml|py|svg|css|js)'

---------- Result ------------

            Physical :  133286
              Source :  109278
             Comment :  7745
 Single-line comment :  4205
       Block comment :  3540
               Mixed :  1271
 Empty block comment :  6
               Empty :  17540
               To Do :  160

Number of files read :  1238

----------------------------
```

It take *10.5 min* to run `mvn test` on MacBook Pro (16-inch, 2019) with 2,3 GHz 8-Core i9 with 32 GB 2667 MHz DDR4.


## Hints


### Good test coverage

Don't ever start refactoring without having tests at start.


### Test reruns

When your refactored code is already compiling but some tests have now outdated expectations, you find them when doing
_Run > All Tests_ in project. Then, you iterate over failed test cases while fixing them. And then you
_Rerun Failed Tests_ -- it is a good thing to have. If it is broken (aparently in current project _Run > All Tests_ is
broken), then you run all tests with `mvn test -fn` which will not fail and run really *all* tests (later you'll need
to fish for `*** FAILED ***` in the output).


### Separate commits

It's good to commit changes separately. You can work with git history later. Imagine, while you were doing all that
refactoring, how many unrelated (to the story) fixes/ideas you've made. All such unrelated fixes and ideas are better
to discuss and review in a separate PR.

If each such change has its own commit, then:

```
git checkout -b introduce-new-feature origin/master
git cherry-pick -x $COMMIT_WITH_NEW_FEATURE
git push
```

Later, when that separate PR is merged to master, just rebase your big branch, and cherry-picked commits will disappear.
