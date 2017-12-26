---
permalink: /
title: ""
excerpt: "Personal Webpage"
author_profile: true
---

<style>
#roundedbox {
  border-radius: 25px;
  background: #9ba1a6;
  padding: 5px 5px 20px 20px;
  width: 100%;
}
</style>


# Personal Webpage

That my digital home. The place in which my all digital "I"s around the web meet.

{% include base_path %}

## Blog entries
<div id="roundedbox">
{% for post in site.posts limit:3 %}
  {% include archive-single.html %}
{% endfor %}

<a href="{{ base_path }}/blog" rel="permalink">... see more</a>
</div>


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
{% assign items = site.projects | sort: 'date' | reverse %}
{% for post in items limit:3 %}
  {% include archive-single.html %}
{% endfor %}

<a href="{{ base_path }}/software" rel="permalink">... see more</a>
</div>
