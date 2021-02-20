---
name: "sblim-sfcc"
layout: package
next_package: scalpel
previous_package: saws
languages: ['c']
---
## 2_2_6
1 / 167 files match, 1 filtered matches.

 - [cimc/cimcclient.c](#cimccimcclientc)

### cimc/cimcclient.c

```c

{% raw %}
41 |    options - options passed to the given backend (ops in cimc.h)
42 | 
43 |    todo: for the next interface revamp, passing in a version number 
44 |          would be a good idea, so we could allow for dlopening different
45 |          versions of .so libs
46 | 
68 |         } else {
69 |             snprintf(libName, LIBLEN, "libcimcClient%s.so.0",id);
70 |         }
71 |         library = dlopen(libName, RTLD_NOW);
72 |         if (library==NULL) {
73 |             *msg=calloc(1,ERRLEN+1);
{% endraw %}

```