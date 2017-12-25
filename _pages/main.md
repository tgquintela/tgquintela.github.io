---
permalink: /
title: "Main"
excerpt: "Main"
author_profile: true
---

<style>
div {
}
</style>


{% include base_path %}

## Projects
<div>
{% for post in site.projects | reversed | list[0:4] %}
  {% include archive-single.html %}
{% endfor %}
</div>

## Software
<div>
{% for post in site.software | reversed | list[0:4] %}
  {% include archive-single.html %}
{% endfor %}
</div>


## Blog entries
<div>
{% for post in site.blog | reversed | list[0:4] %}
  {% include archive-single.html %}
{% endfor %}
</div>
