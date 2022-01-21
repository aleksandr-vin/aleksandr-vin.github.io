---
title:  "Stereoscopic 360 video"
tags:   video 360 3D vr stereo binocular idea
---

Last Tuesday, during proyotyping a demo for our idea at VR hackathon in KLM,
I run into issues. Issues with putting a 360 video into a VR scene.

It all sounded quite easy: there are a lot of 360 videos in youtube, why one
can't just put it on a sphere in VR scene with camera in the center?

Well, you'll find out fast that we have both eyes in need for rendering that
sphere from different points. There is one center of the sphere, but these eyes
are not in it. So there will be two cameras: for left and right eye.

Now if we render same sphere for both eyes, the picture will look flat, not 3D.
To achieve 3D effect, we need to record that video with two cameras, placed at
eyes' distance. Then we create two spheres, each visible only for one eye in VR
scene.

Now there is 3D: you see volumetric objects, but how is 360 doing? It's broken:
if you rotate your head in VR scene, virtual cameras of the eyes will rotate too,
but not the recording cameras, as the imaginary line between them is not rotating
with the VR head! So even if these recording is done with 360 cameras, the stereoscopic
effect will dissapear, at 90° and will be reversed on 180°.

I think that to produce a 360 stereoscopic video we'll need minimum 4 of 360 cameras
placed in the vertices of [tetrahedron](https://en.m.wikipedia.org/wiki/Tetrahedron).
And dynamically choose the two with vector between them being the closest in orientation
to the vector between virtual eyes, so always changing video sources when rotating the
head in VR in 3dof.

Did quick searching for 360 stereoscopic cameras, and did find one interesting sample for
around 5500€ – Insta 360 Pro 2. See specs and pictures. It has 6 lenses on one plane, so
it should loose stereoscopic quality on 2 of 3 DoF.

![Insta360 Pro2 specs](/img/Insta360-Pro2-detailed-specs.jpeg){: width="250" }

![Insta360 Pro2](/img/Insta360-Pro2.jpeg){: width="250" }


## Somethong to read

1. [Multiple View Geometry in Computer Vision](https://books.google.com/books/about/Multiple_View_Geometry_in_Computer_Visio.html?id=e30hAwAAQBAJ)

1. [The Cinematic VR Formula: A Beginner's Guide to Creating Virtual Reality Movies](https://read.amazon.com/kp/embed?asin=B076HZLK55&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_GQ62N25WTWQNKXJFVQ2M)

1. [Flexible Virtual Reality parallax with Blender Tetrahedron Multi Camera VR View Hack](https://blenderartists.org/t/flexible-virtual-reality-parallax-with-blender-tetrahedron-multi-camera-vr-view-hack/682634)
