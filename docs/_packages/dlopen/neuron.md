---
name: "neuron"
layout: package
next_package: nfs-ganesha
previous_package: nettle
library_name: dlopen
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## develop
33 / 8194 files match, 1 filtered matches.

 - [src/nrnoc/osxdlfcn.h](#srcnrnocosxdlfcnh)

### src/nrnoc/osxdlfcn.h

```c

{% raw %}
50 |         void            *dli_saddr;     /* Address of nearest symbol */
51 | } Dl_info;
52 | 
53 | extern void * dlopen(const char *path, int mode);
54 | extern void * dlsym(void * dl_restrict handle, const char * dl_restrict symbol);
55 | extern const char * dlerror(void);
{% endraw %}

```