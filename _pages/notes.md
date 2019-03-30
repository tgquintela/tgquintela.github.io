---
layout: archive
title: "Index of notes"
permalink: /notes/
author_profile: true
redirect_from:
  - /notes
---

{% include base_path %}

That is my personal collection of notes that I decided to make it public.
Most of the notes only have value as aggregators of bibliography material or ideas for projects.

In that index of notes it is showed the title and the last modification date of each note.


{% assign sortednotes = site.notes | sort: 'order_item' | reverse %}
<ul>
{% for post in sortednotes %}
    <li><a href="{{ base_path }}{{ post.url }}"><strong>{{ post.title }}</strong></a> {{ post.date | date: '%Y-%m-%d' }}</li>
{% endfor %}
</ul>


<script type="text/javascript">
  var GOOG_FIXURL_LANG = 'en',
      GOOG_FIXURL_SITE = '{{ site.url }}'.concat('/notes/');
//          GOOG_FIXURL_SITE = 'https://tgquintela.github.io/notes/';
//      domain = '{{ site.url }}',
//      domain = domain.concat('/notes/');
</script>
<script type="text/javascript"
  src="//linkhelp.clients.google.com/tbproxy/lh/wm/fixurl.js">
</script>

