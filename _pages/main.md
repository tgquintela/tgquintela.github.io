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
{% for post in site.projects %}
<li>Iteration</li>
<li>post.url</li>
{{% assign countsi = countsi + 1 %}}
{% endfor %}
</ul>

... see more
</div>


<div id="roundedbox">
{% for i in [1] %}
  {% assign post = site.projects[i] %}
  {% include archive-single.html %}
{% endfor %}

... see more
</div>

## Software
<div id="roundedbox">
{% for recent in site.software limit:3 %}
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
