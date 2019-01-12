---
title: Aurii Game Master Blog
permalink: /aurii_blog/
---

{% for post in site.tags.aurii-blog %}
* [{{ post.title }}]({{site.baseurl}}{{ post.url }}) *{{ post.date | date_to_string }}*
> {{ post.excerpt }}
{% endfor %}