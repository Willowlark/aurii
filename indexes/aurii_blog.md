---
title: Aurii Game Master Blog
permalink: /aurii_blog/
---

# Season Two

{% for post in site.tags.aurii-blog %}
{% if post.tags contains "season-two" %}
* [{{ post.title }}]({{site.baseurl}}{{ post.url }}) *{{ post.date | date_to_string }}*
> {{ post.excerpt }}
{% endif %}
{% endfor %}

# Season One

{% for post in site.tags.aurii-blog %}
{% if post.tags contains "season-one" %}
* [{{ post.title }}]({{site.baseurl}}{{ post.url }}) *{{ post.date | date_to_string }}*
> {{ post.excerpt }}
{% endif %}
{% endfor %}