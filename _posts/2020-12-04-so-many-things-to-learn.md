---
layout: post
title:  "So many things to learn"
---

I was not making any records for almost 2 months. Will do that now.

## Progress on VideoParking

There was quite some progress on the VideoParking.live project:

-   We have now a Raspberry PIs with cameras, at 2 (almost 3)
    locations, that upload a photo every minute to S3

-   There is a Lambda triggered by such uploads, that produces zones
    picture (initially it was producing a zip file with each zone as
    a separarte jpg file, but it showed that running detection on a
    file has a constant time and it's around 45 seconds on home
    server, so no zones are just masked on one jpg) and uploads it
    to different S3 bucket

-   Then there is a detector processes, running in k8s, sharded,
    which fetches zones file for its locations every minute,
    performs detections and registers results to Timestream

-   On the page, react app is fetching data (location stats per
    zone, raw image, and detections) and drawing everything on a
    canvas.

Plan is to show only stats on a map and add authorization for
billing and operators' features (raw image and all detections data).


## And now, all the things to learn:

-   **react-leaflet**: to display zones and parking status, show
    current location, find locations in the area, cluster zones.

-   **react-leaflet-draw**: to draw zones on the map easily.

-   Prometheus and Grafana for k8s cluster: to collect metrics from
    services.

-   Drawing on canvas in React App: to ease zones
    corrections/creation on raw image.

-   Authentication for React app and Lambda functions.

-   YOLO3 detector: how to train it on for cars only and to detect
    cars from the top view angle.

-   Running detector in EKS and probably on GKS, AKS to compare.

-   Enabling GPU support on local k8s cluster and using image with
    GPU in cloud.


## Vendée Globe, RYA courses

Yeah, the race started at the first part of November. And I
attended RYA skipper theory courses. Big plans.

And yesterday made an account in Virtual Regatta, now I'm also
doing round the globe.

> You can. You should. And if you're brave enough to start, you
> will. &#x2014;Stephen King

And **T &#x2013;(+W)&#x2013;> C**.
