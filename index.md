
# Table of Contents

1.  [So many things to learn <span class="timestamp-wrapper"><span class="timestamp">[2020-12-04 Fri]</span></span>](#orgb88f753)
    1.  [Progress on VideoParking](#orgeecccc7)
    2.  [And now, all the things to learn:](#orga7dd20c)
    3.  [Vendée Globe, RYA courses](#org21fbe39)
2.  [Sometimes you're forced to use old tools <span class="timestamp-wrapper"><span class="timestamp">[2020-10-15 Thu]</span></span>](#orgd82c7a4)
3.  [Something to start with <span class="timestamp-wrapper"><span class="timestamp">[2020-10-15 Thu]</span></span>](#org6d11186)
    1.  [I made it. Again. After, maybe, 10 years.](#orgba83127)
    2.  [Here is a link to a note I made last evening about](#org9aadc36)
    3.  [Thoughts about VR (home) office](#org20b1712)



<a id="orgb88f753"></a>

# So many things to learn <span class="timestamp-wrapper"><span class="timestamp">[2020-12-04 Fri]</span></span>

I was not making any records for almost 2 months. Will do that now.


<a id="orgeecccc7"></a>

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


<a id="orga7dd20c"></a>

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


<a id="org21fbe39"></a>

## Vendée Globe, RYA courses

Yeah, the race started at the first part of November. And I
attended RYA skipper theory courses. Big plans.

And yesterday made an account in Virtual Regatta, now I'm also
doing round the globe.

> You can. You should. And if you're brave enough to start, you
> will. &#x2014;Stephen King

And **T &#x2013;(+W)&#x2013;> C**.


<a id="orgd82c7a4"></a>

# Sometimes you're forced to use old tools <span class="timestamp-wrapper"><span class="timestamp">[2020-10-15 Thu]</span></span>

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


<a id="org6d11186"></a>

# Something to start with <span class="timestamp-wrapper"><span class="timestamp">[2020-10-15 Thu]</span></span>

> Everything should be made as simple as possible,
> but not any simpler &#x2014;Albert Einstein


<a id="orgba83127"></a>

## I made it. Again. After, maybe, 10 years.

And again I have the same mood here, I think. I'm home alone, listening to
blues.


<a id="org9aadc36"></a>

## Here is a link to a note I made last evening about

[resizing ext4 partition of a guest Ubuntu on vmdk on ESXi 6.0](https://superuser.com/a/1594385/1230369).

I spent some time finding out how to atually resize the disk and wrote down
the steps to remember, and now I have mine **aleksandr.vin**
domain name and a site running on github pages.


<a id="org20b1712"></a>

## Thoughts about VR (home) office

Last Friday my colleague told me about Oculus Quest 2. Checking the specs,
I had the same feeling when was reading about DJI Mavic Air 2&#x2026; after not
following any updates on DJI for a 2 years. As the VR headset become much
more powerful and much less heavy, I returned to old idea of using VR headset
as a replacement for home office monitor(s) for coding. It should be ok to
have 2K per eye on resolution, but the questions are:

-   Will it be warm to work?

-   Will it be ok to work for 1 hour before the break (also maintaining
    regular breaks should become a habbit)?

-   Eyes strain and degradation?

So I'm thiking about giving it a try in upcoming months.

