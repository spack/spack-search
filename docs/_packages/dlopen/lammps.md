---
name: "lammps"
layout: package
next_package: laszip
previous_package: krb5
library_name: dlopen
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 20200303
7 / 10633 files match, 1 filtered matches.

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