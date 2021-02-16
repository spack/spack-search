---
name: "fakechroot"
layout: package
next_package: faodel
previous_package: extrae
languages: ['c']
---
## 2.20.1
9 / 293 files match, 1 filtered matches.

 - [src/dlopen.c](#srcdlopenc)

### src/dlopen.c

```c

{% raw %}
27 | wrapper(dlopen, void *, (const char * filename, int flag))
31 |     debug("dlopen(\"%s\", %d)", filename, flag);
34 |         debug("dlopen(\"%s\", %d)", filename, flag);
36 |     return nextcall(dlopen)(filename, flag);
{% endraw %}

```