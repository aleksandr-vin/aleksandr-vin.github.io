---
title:  "VSCode Again"
tags:   vscode dev bloop metals java hints vr oculus
---

It's funny but I did try swapping IDEA with VSCode two or three times already. For Scala projects. And everytime something was not compiling
or not running or not debugging. I think, that time back, debugging was not supported in Metals.

Recently I've appeared to be coding more often in VSCode: some React apps, some Unity scripts... So I decided to give it a try one more time
for Scala. And saved a [post (with a wrong
title)](https://www.iteratorshq.com/blog/migrating-from-intellij-idea-to-vscode-and-metals-staying-productive-at-writing-scala/) to follow
it up. So the post appeared to be of no help in setting up a Scala project or fixing potential issues, it only listed some good
extensions. But the project I'm working now *did not compile in VSCode*, again! Actually it was failing on macro expansion of some quill
code with have. And it was blaiming of missed `--add-opens` option for `java.base/java.util`, while nothing is said of that by sbt in
termnal or by IDEA. We build and run in Java 11. I'm using `jenv` for management. I was laughing (or gigling, or swearing) at night and
tried to configure that everywhere I could find: `.sbtopts`, `.jvmopts`, `settings.json`, `build.sbt`, `.bsp/sbt.json`, `.bloop/*`... no
diff. And I gave up at night.

Don't know why, I decided to `ps aux | grep -i java` while VSCode was compiling and I saw Java 17 running `bloop.Server`!!!

It appeared that change of `"metals.javaHome"` in `settings.json` does not restart that bloop. Actually it survives even VSCode restarts.

Kill it and start VSCode again (with proper `"metals.javaHome"`) and errors are gone.

Phew!


### Some notes

1. [Gitpod](https://www.gitpod.io/) looks like a nice idea to try in Oculus Browser

2. [Code server](https://github.com/coder/code-server) and [deploys](https://github.com/coder/deploy-code-server#deploy-code-server-)

3. [Settings Sync](https://code.visualstudio.com/docs/editor/settings-sync)
