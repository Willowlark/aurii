---
title: Behind the GM Screen
permalink: /gm_screen/
---

*This a secured area. Are you supposed to be here?*

{% for item in site.gm_screen %}
# [{{ item.title }}]({{site.baseurl}}{{item.url}})
> {{ item.excerpt }}
{% endfor %}