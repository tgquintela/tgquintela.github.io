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
  border: 1px solid #bdc1c4;
}
#btn-main {
  background-color: #52adc8;
  border-color: #357ebd;
  border-radius: 4px;
}
</style>


# Personal Webpage

That's my digital home. The place where my all digital "me"s around the web meet each other.
A place where even the social rules of order or aesthetic are subjected to my criteria.
Welcome to my free myself.
Welcome here!

{% include base_path %}

## Blog entries
<div id="roundedbox">
{% for post in site.posts limit:3 %}
  {% include archive-single.html %}
{% endfor %}

<a href="{{ base_path }}/blog" class="btn btn-primary" id="btn-main" rel="permalink" style="margin-top: 1.3em">... see more</a>
</div>


## Projects
<div id="roundedbox">
{% assign items = site.projects | sort: 'date' | reverse %}
{% for post in items limit:2 %}
  {% include archive-single.html %}
{% endfor %}

<a href="{{ base_path }}/projects" class="btn btn-primary" id="btn-main" rel="permalink" style="margin-top: 1.3em">... see more</a>
</div>


## Software
<div id="roundedbox">
{% assign items = site.software | sort: 'date' | reverse %}
{% for post in items limit:3 %}
  {% include archive-single.html %}
{% endfor %}

<a href="{{ base_path }}/software" class="btn btn-primary" id="btn-main" rel="permalink" style="margin-top: 1.3em">... see more</a>
</div>
