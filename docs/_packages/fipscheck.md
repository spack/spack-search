---
name: "fipscheck"
layout: package
next_package: flux-core
previous_package: fio
languages: ['c']
---
## 7.0.0.398
2 / 18 files match, 1 filtered matches.

 - [src/library.c](#srclibraryc)

### src/library.c

```c

{% raw %}
74 |         dl = dlopen(libname, RTLD_NODELETE|RTLD_NOLOAD|RTLD_LAZY);
{% endraw %}

```