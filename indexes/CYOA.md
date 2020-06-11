---
title: CYOA
permalink: /CYOA/
---

{% for post in site.tags.CYOA %}
* [{{ post.title }}]({{site.baseurl}}{{ post.url }}) *{{ post.date | date_to_string }}*
> {{ post.excerpt }}
{% endfor %}