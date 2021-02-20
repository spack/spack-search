---
name: "meme"
layout: package
next_package: memkind
previous_package: mc
languages: ['c']
---
## 4.11.4
5 / 1804 files match, 1 filtered matches.

 - [src/libxml2/xmlmodule.c](#srclibxml2xmlmodulec)

### src/libxml2/xmlmodule.c

```c

{% raw %}
208 | static void *
209 | xmlModulePlatformOpen(const char *name)
210 | {
211 |     return dlopen(name, RTLD_GLOBAL | RTLD_NOW);
212 | }
213 | 
{% endraw %}

```