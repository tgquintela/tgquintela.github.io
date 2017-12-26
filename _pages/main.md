---
permalink: /
title: "Main"
excerpt: "Main"
author_profile: true
---

<style>
#roundedbox {
  border-radius: 25px;
  background: #73AD21;
}
</style>


{% include base_path %}

## Projects
<div id="roundedbox">
{% for post in site.projects | reversed | list[0:2] %}
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
{% for post in site.blog | reversed | list[0:4] %}
  {% include archive-single.html %}
{% endfor %}
... see more
</div>
