---
name: "sollya"
layout: package
next_package: sox
previous_package: slurm
library_name: dlopen
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 7.0
9 / 1132 files match, 2 filtered matches.

 - [library.c](#libraryc)
 - [external.c](#externalc)

### library.c

```c

{% raw %}
521 | 
522 |   if (!foundElsewhere) {
523 |     dlerror();
524 |     dlfcnHandle = dlopen(libraryName, RTLD_LOCAL | RTLD_NOW);
525 |     if (dlfcnHandle == NULL)
526 |       return NULL;
{% endraw %}

```
### external.c

```c

{% raw %}
310 |     return;
311 |   }
312 | 
313 |   descr = dlopen(library, RTLD_NOW);
314 |   if (descr==NULL) {
315 |     printMessage(1,SOLLYA_MSG_EXTERNALPLOT_COULD_NOT_OPEN_A_LIBRARY, "Error: the given library (%s) is not available (%s)!\n",library,dlerror());
{% endraw %}

```