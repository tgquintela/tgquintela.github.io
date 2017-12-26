---
permalink: /
title: ""
excerpt: "Personal Webpage"
author_profile: true
---

<style>
#roundedbox {
  border-radius: 20px;
  background: #f2f3f3;
  padding: 0.5em 0.5em 2em 2em;
  width: 100%;
  margin: 3em;
  color: #f2f3f3;
}
</style>


# Personal Webpage

That's my digital home. The place in which my all digital "me"s around the web meet each other.

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
