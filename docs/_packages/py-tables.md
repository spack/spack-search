---
name: "py-tables"
layout: package
next_package: py-uvloop
previous_package: py-soundfile
languages: ['c']
---
## 3.5.2
2 / 788 files match, 1 filtered matches.

 - [src/utils.c](#srcutilsc)

### src/utils.c

```c

{% raw %}
52 |     void *hinstLib;
53 | 
54 |     /* Load the dynamic library */
55 |     hinstLib = dlopen(libname, RTLD_LAZY);
56 | 
57 |     if (hinstLib != NULL) {
{% endraw %}

```