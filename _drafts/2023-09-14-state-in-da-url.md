---
title: "State in da url"
tags: url http state compression protobuf base64
---

Me was writing a small web site. To make a UI for some optimization algorithm (more on that topic later).
It all started with an idea to assist me with alpha-testing while I'll be extending that algorithm with features.
And I made it in Angular, was not touching it since 2016, so it was a perfect time to check it out. Nevertheless,
the one-pager was ready for spreading into the public (friends and family) and was even capable of reporting a
problem to me by email. The state of what user is seeing on that page and the algorithm (aws lambda) reply were
`JSON.stringify`-ed and attached into the mail body. But that didn't work if the user just wants to share the link.
I wanted that to also encompas the state. And that's serializing it, encoding and putting (as a fragment) into the
URL.

My initial idea was simple: `state | JSON.stringify | compress | base64 | s/[:dangerous_chars:]/../ | append-to-URL`.
But I thought to enhance it with schema, like Protobuf to save on JSON fields duplication in list of objects.
Also I was suggesting it will be compressed by default.

So `npm install -D ts-proto` to compile the `*.proto` file into `*.ts`, then mapping my model to proto-one, then
base64-encoding it and logging it to see the lengths.

It appeared to be huge for the url. I'm talking about around 11_300 chars in JSON string, that became 5_400
elements of Uint8Array after protobuf encoding which goes to 7_200 chars in Base64.

So I decided to just deflate (also compare with gzip) the JSON string of my state and that became 1_400/1_900
compressed/base64'd (almost the same for gzip and deflate-raw, but deflate-raw being the winner by 8 bytes).

So for now I can say that Protobuf encoding is far not a winner in compression here. Maybe I'm missing some settings
for protobuf compiler here, need to check that.

Random links:
- https://github.com/stephenh/ts-proto
- https://protobuf.dev/programming-guides/proto3/#nested
- https://stackoverflow.com/questions/9267899/arraybuffer-to-base64-encoded-string
- https://stackoverflow.com/questions/9267899/arraybuffer-to-base64-encoded-string/38858127#38858127
- https://developer.mozilla.org/en-US/docs/Web/API/Compression_Streams_API
- https://gist.github.com/Explosion-Scratch/357c2eebd8254f8ea5548b0e6ac7a61b
