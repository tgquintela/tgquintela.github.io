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
  padding: 20px;
  width: 100%;
}
</style>

v2

{% include base_path %}

## Projects
<div id="roundedbox">
{% assign countsi = 0 %}
<ul>
{% for post in site.projects | slice(2) %}
<li>Iteration</li>
<li>""</li>
{% endfor %}
</ul>

... see more
</div>

## Software
<div id="roundedbox">
{% for recent in site.software[:4] %}
  {% for post in recent %}
    {% include archive-single.html %}
  {% endfor %}
{% endfor %}
... see more
</div>


## Blog entries
<div id="roundedbox">
{% for post in paginator.posts | list[0:4] %}
  {% include archive-single.html %}
{% endfor %}
... see more
</div>
