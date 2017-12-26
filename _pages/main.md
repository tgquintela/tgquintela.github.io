---
permalink: /
title: "Main"
excerpt: "Main"
author_profile: true
---

<style>
#roundedbox {
  border-radius: 25px;
  background: LightGray;
  padding: 5px 5px 20px 20px;
  width: 100%;
}
</style>

v3

{% include base_path %}

## Projects
<div id="roundedbox">
{% assign projectslist = site.projects | reversed %}
{% for post in projectslist limit:2 %}
  {% include archive-single.html %}
{% endfor %}

<a href="{{ base_path }}/projects" rel="permalink">... see more</a>
</div>


## Software
<div id="roundedbox">
{% for post in site.software | reversed limit:3 %}
  {% include archive-single.html %}
{% endfor %}

<a href="{{ base_path }}/software" rel="permalink">... see more</a>
</div>


## Blog entries
<div id="roundedbox">
{% capture written_year %}'None'{% endcapture %}
{% for post in paginator.posts %}
  {% capture year %}{{ post.date | date: '%Y' }}{% endcapture %}
  {% if year != written_year %}
   <!-- <h2 id="{{ year | slugify }}" class="archive__subtitle">{{ year }}</h2> -->
    {% capture written_year %}{{ year }}{% endcapture %}
  {% endif %}
  {% include archive-single.html %}
{% endfor %}

{% include paginator.html %}

<a href="{{ base_path }}/blog" rel="permalink">... see more</a>
</div>
