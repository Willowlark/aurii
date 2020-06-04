---
title: Fisher's Field Guide
excerpt: A standard issue Drecian field guide given to all officer's who deploy to the mainland. The Field Guide section itself is only about a fourth of the pages, the rest are blank for the Officer to write their own notes... 

---

{% for post in site.tags.fisher-field-guide %}
* [{{ post.title }}]({{site.baseurl}}{{ post.url }}) *{{ post.date | date_to_string }}*
> {{ post.excerpt }}
{% endfor %}