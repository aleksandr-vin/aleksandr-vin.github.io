---
layout: default
title: Home Page
---

{% for post in site.posts %}
{% capture day %}{{ post.date | date: '%m%d%Y' }}{% endcapture %}
{% capture nday %}{{ post.next.date | date: '%m%d%Y' }}{% endcapture %}
{% if day != nday %}<h5 class="date">{{ post.date | date: "%A, %B %e, %Y" }}</h5>{% endif %}
  <a href="{{ post.url }}">{{ post.title }}</a>
{{ post.excerpt }}
  <hr>
{% endfor %}
