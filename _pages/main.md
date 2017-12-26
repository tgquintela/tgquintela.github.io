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


{% include base_path %}

## Projects
<div id="roundedbox">
{% for post in site.projects | reversed | list[0:1] %}
  {% include archive-single.html %}
{% endfor %}
... see more
</div>

## Software
<div id="roundedbox">
{% for post in site.software | reversed | list[0:4] %}
  {% include archive-single.html %}
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
