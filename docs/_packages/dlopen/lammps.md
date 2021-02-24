---
name: "lammps"
layout: package
next_package: elfutils
previous_package: folly
library_name: dlopen
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## master
8 / 10134 files match, 1 filtered matches.

 - [examples/COUPLE/plugin/liblammpsplugin.c](#examplescouplepluginliblammpspluginc)

### examples/COUPLE/plugin/liblammpsplugin.c

```c

{% raw %}
28 |   void *handle;
29 | 
30 |   if (lib == NULL) return NULL;
31 |   handle = dlopen(lib,RTLD_NOW|RTLD_GLOBAL);
32 |   if (handle == NULL) return NULL;
33 |   
{% endraw %}

```