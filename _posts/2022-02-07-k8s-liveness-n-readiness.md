---
title:  "readiness and liveness probe of k8s"
tags:   reliability service k8s probe sre
---

Read and noted: https://blog.colinbreck.com/kubernetes-liveness-and-readiness-probes-how-to-avoid-shooting-yourself-in-the-foot/

> If the readiness probe is verifying a dependency that is exclusive to the container—a private cache or database—then you can be more aggressive in failing the readiness probe, with the assumption that container dependencies are independent. However, if the readiness probe is verifying a shared dependency—like a common service used for authentication, authorization, metrics, logging, or metadata—you should be very conservative in failing the readiness probe.

> Unlike a readiness probe, it is not idiomatic to check dependencies in a liveness probe. A liveness probe should be used to check if the container itself has become unresponsive.

> To avoid surprises from these dynamics changing over time, it is advantageous to have pods restart on a somewhat regular basis—it should not necessarily be a goal to have individual pods backing a service run for weeks or months at a time. It is important to regularly exercise and evaluate deployments, restarts, and failures as part of running a reliable service.

To read: https://blog.colinbreck.com/kubernetes-liveness-and-readiness-probes-revisited-how-to-avoid-shooting-yourself-in-the-other-foot/
