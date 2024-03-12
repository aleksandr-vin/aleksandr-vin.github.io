---
title: "Deepmind.ai and Hugging Face Course"
tags: ai transformers learning huggingface deepmind llm models
---

Started watching a course:
[https://learn.deeplearning.ai/courses/open-source-models-hugging-face](https://learn.deeplearning.ai/courses/open-source-models-hugging-face).

Note: same day a [podcast episode about Hugging Face went online](https://syntax.fm/show/740/local-ai-models-in-javascript-machine-learning-deep-dive-with-xenova) on Syntax :)

## UPDATE

I rewatched DUNE and saw an announcement of Command-R from Cohere,... while *downloading model-00011-of-00015.safetensors* decided to
read what is RAG,... and read on nVidia site [(archive)](https://web.archive.org/web/20240303213825/https%253A//blogs.nvidia.com/blog/what-is-retrieval-augmented-generation/)
that the guy, who coined the term *RAG* -- Lewis, *who now leads a RAG team at AI startup Cohere.* :)

But that thing didn't work, it took around 30 min to download 65GiB:

```shell
% du -h -s /Users/aleksandrvin/.cache/huggingface/hub/*
 65G	/Users/aleksandrvin/.cache/huggingface/hub/models--CohereForAI--c4ai-command-r-v01
```

And then crashed:

```shell
model-00006-of-00015.safetensors: 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 4.93G/4.93G [02:48<00:00, 29.3MB/s]
model-00007-of-00015.safetensors: 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 4.93G/4.93G [02:38<00:00, 31.1MB/s]
model-00008-of-00015.safetensors: 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 4.93G/4.93G [02:35<00:00, 31.8MB/s]
model-00009-of-00015.safetensors: 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 4.93G/4.93G [02:40<00:00, 30.7MB/s]
model-00010-of-00015.safetensors: 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 4.93G/4.93G [02:48<00:00, 29.3MB/s]
model-00011-of-00015.safetensors: 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 4.93G/4.93G [03:18<00:00, 24.8MB/s]
model-00012-of-00015.safetensors: 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 4.93G/4.93G [03:37<00:00, 22.7MB/s]
model-00013-of-00015.safetensors: 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 4.93G/4.93G [03:22<00:00, 24.3MB/s]
model-00014-of-00015.safetensors: 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 4.93G/4.93G [02:24<00:00, 34.2MB/s]
model-00015-of-00015.safetensors: 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 1.11G/1.11G [00:28<00:00, 38.5MB/s]
Downloading shards: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 15/15 [37:37<00:00, 150.50s/it]
Loading checkpoint shards:  33%|███████████████████████████████████████████████████████████▋                                                                                                                       | 5/15 [02:32<05:36, 33.69s/it]zsh: killed     python3 commandR.py
/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/multiprocessing/resource_tracker.py:254: UserWarning: resource_tracker: There appear to be 1 leaked semaphore objects to clean up at shutdown
  warnings.warn('resource_tracker: There appear to be %d '
```
