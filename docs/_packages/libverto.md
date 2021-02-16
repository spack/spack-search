---
name: "libverto"
layout: package
next_package: amgx
previous_package: libgd
languages: ['c']
---
## 0.3.1
2 / 45 files match

 - [src/module.c](#srcmodulec)

### src/module.c

```c

{% raw %}
105 |     mod = dlopen(NULL, RTLD_LAZY | RTLD_LOCAL);
181 |     intdll = dlopen(filename, RTLD_LAZY | RTLD_LOCAL);
204 |     intdll = dlopen(filename, RTLD_NOW | RTLD_LOCAL);
{% endraw %}

```