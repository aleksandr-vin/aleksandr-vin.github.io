---
layout: post
title:  "PIP of Azure"
tags:   azure devops pip
---

Some notes on installation of a Python package from Azure feed.

Let's say you have a feed *Boogaga*, and the *Connect to feed* tell you to add this to your _pip.conf_:

    [global]
    index-url=https://pkgs.dev.azure.com/Foo/Bar/_packaging/Boogaga%40Local/pypi/simple/

One thing to change first: `index-url` to `extra-index-url` -- that will allow checking default index (https://pypi.org/simple) too.

Then, you can also keep your _pip.conf_ unmodified and install with the option:

    pip install <fancy-package> --extra-index-url https://pkgs.dev.azure.com/Foo/Bar/_packaging/Boogaga%40Local/pypi/simple/

But that thing still doesn't work, as `pip install ...` asks you to authenticate on _pkgs.dev.azure.com_.


So locally you can use these options to authenticate (ignoring obvious interactive one):

1. Add authentication info to _~/.netrc_ (provided you have personal access token, see https://dev.azure.com/Foo/_usersSettings/tokens):

       echo machine pkgs.dev.azure.com login $USER password $PRIVATE_ACCESS_TOKEN >> ~/.netrc

2. Install [artifacts-keyring](https://pypi.org/project/artifacts-keyring/), which should authenticate you via browser. I didn't check that way, as it required dotnet:

       WARNING: Keyring is skipped due to an exception: Unable to find dependency dotnet, please manually install the .NET Core runtime and ensure 'dotnet' is in your PATH. Error: [Errno 2] No such file or directory: 'dotnet'

    And I fell back to variant 1.

Then you go to the pipeline and here is only one option, to use [*PipAuthenticate*](https://docs.microsoft.com/en-us/azure/devops/pipelines/tasks/package/pip-authenticate?view=azure-devops) task.

Note, that you need to provide project and scope (like *@Local* in my case) in the _artifactFeeds_ input, and use _onlyAddExtraIndex_ like this:

     - task: PipAuthenticate@1
       inputs:
         artifactFeeds: 'Bar/Boogaga@Local'
         onlyAddExtraIndex: true

You can even keep the same command in the pipeline:

    pip install <fancy-package> --extra-index-url https://pkgs.dev.azure.com/Foo/Bar/_packaging/Boogaga%40Local/pypi/simple/

as *PipAuthenticate* will add one more _extra-index-url_ to the list.
