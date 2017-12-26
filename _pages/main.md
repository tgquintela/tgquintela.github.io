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

v4

{% include base_path %}

## Projects
<div id="roundedbox">
{% assign items = site.projects | sort: 'date' | reverse %}
{% for post in items limit:2 %}
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
{% for post in site.blog | reversed limit:3 %}
  {% include archive-single.html %}
{% endfor %}

{% include paginator.html %}

<a href="{{ base_path }}/blog" rel="permalink">... see more</a>
</div>
