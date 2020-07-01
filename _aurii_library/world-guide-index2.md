---
title: World Guide Collection
excerpt: 
---

The following is the international primer on the Nations and people of Aurii. Additionally covered is a short history of the nations and their interaction, including the First Eraian Crusade and The Drecian Conflict. This document, while large, is well regarded all the greatest introduction to world at large for one of any age.

{% for item in site.aurii_world_guide_old %}
# [{{ item.title }}]({{site.baseurl}}{{item.url}})
> {{ item.excerpt }}
{% endfor %}