---
layout: post
title:  "Keeping docs on GitHub"
tags:   docs, github, encryption, security, idea
---

Having a scanned version of your passport or other legal paper at hand
when you're travelling can be handy. Sometimes it helps even when you're at home...


## Requirements

1. Docs are encrypted

2. If key is compromised, there should be a procedure to keep docs safe

3. Access/decryption should be available by Yubikey


## Concept

1. Scan can a doc in PDF

2. Encrypt it

3. Store it in git

4. Push to github

5. Go to github pages

6. Authenticate with Yubikey

7. See the decrypted PDF


## Procedure when key is compromised

1. Key is compromised

2. [TBD] see _perfect forward secrecy_
