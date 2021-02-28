---
name: "neuron"
layout: package
next_package: ncl
previous_package: gawk
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## develop
12 / 8236 files match, 1 filtered matches.

 - [src/nrnoc/osxdlfcn.h](#srcnrnocosxdlfcnh)

### src/nrnoc/osxdlfcn.h

```c

{% raw %}
51 | } Dl_info;
52 | 
53 | extern void * dlopen(const char *path, int mode);
54 | extern void * dlsym(void * dl_restrict handle, const char * dl_restrict symbol);
55 | extern const char * dlerror(void);
56 | extern int dlclose(void * handle);
{% endraw %}

```