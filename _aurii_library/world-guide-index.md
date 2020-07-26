---
title: New World Guide Collection
excerpt: Campaign Setting 
---

**History**
* 1.1 The History of Aurii
* 1.2 Timeline of Events
* 1.3 Seven Things to Know

**Aurii**
* 2.1 Races on Aurii
* 2.2 Languages, Calendar, Holidays, Currency, Names, Titles, Technology and Terminology
* 2.3 Creatures of Aurii
* 2.4 Magic on Aurii
* 2.5 Religions on Aurii

**Nations**
* 3.1 Wynne
* 3.2 Callora
* 3.3 Dwyr
* 3.4 Torshan
* 3.5 Theanovene
* 3.6 Eraia
* 3.7 Ferre
* 3.8 The Kissaelain Territories
* 3.9 Dreca

**City of Theanovene**
* 4.1 City of Theanovene

**Adventure Threads**
* ?.0 Themes for the Realm
* ?.1 The Drecian Invasion
* ?.2 The Return of Lyarlel
* ?.3 FFXV basically

---

--- 

{% for item in site.aurii_world_guide %}
# [{{ item.title }}]({{site.baseurl}}{{item.url}})
> {{ item.excerpt }}
{% endfor %}