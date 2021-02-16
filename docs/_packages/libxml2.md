---
name: "libxml2"
layout: package
next_package: libxslt
previous_package: libx11
languages: ['c']
---
## 2.7.8
6 / 6220 files match, 1 filtered matches.

 - [xmlmodule.c](#xmlmodulec)

### xmlmodule.c

```c

{% raw %}
211 |     return dlopen(name, RTLD_GLOBAL | RTLD_NOW);
{% endraw %}

```