---
layout: archive
title: "Index of notebooks"
permalink: /notebooks/
author_profile: true
redirect_from:
  - /notebooks
---

{% include base_path %}

Sample of different notebooks in different programming languages in order to show certain public (and publishable) tasks.


{% for post in site.notebooks reversed %}
  {% include archive-single.html %}
{% endfor %}
