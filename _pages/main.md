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
  padding: 15px 15px 20px 20px;
  width: 100%;
}
</style>

v1

{% include base_path %}

## Projects
<div id="roundedbox">
{% assign countsi = 0 %}
{% for post in site.projects limit:2 %}
  {% include archive-single.html %}
{% endfor %}

[... see more]({{ base_path }}/projects)
</div>


## Software
<div id="roundedbox">
{% for post in site.software limit:3 %}
  {% include archive-single.html %}
{% endfor %}
[... see more]({{ base_path }}/software)
</div>


## Blog entries
<div id="roundedbox">
{% for post in paginator.posts limit:4 %}
  {% include archive-single.html %}
{% endfor %}
[... see more](/blog)
</div>
