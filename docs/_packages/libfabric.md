---
name: "libfabric"
layout: package
next_package: libfastcommon
previous_package: libevpath
languages: ['c']
---
## 1.6.1
5 / 638 files match, 1 filtered matches.

 - [src/fabric.c](#srcfabricc)

### src/fabric.c

```c

{% raw %}
406 | 		dlhandle = dlopen(lib, RTLD_NOW);
410 | 			       "dlopen(%s): %s\n", lib, dlerror());
470 | 	dlhandle = dlopen(NULL, RTLD_NOW);
{% endraw %}

```