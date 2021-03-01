---
name: "gawk"
layout: package
next_package: gcc
previous_package: g2o
library_name: dlopen
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 5.1.0
18 / 1886 files match, 3 filtered matches.

 - [ext.c](#extc)
 - [nonposix.h](#nonposixh)
 - [pc/dlfcn.h](#pcdlfcnh)

### ext.c

```c

{% raw %}
55 | 	if (lib_name == NULL)
56 | 		fatal(_("load_ext: received NULL lib_name"));
57 | 
58 | 	if ((dl = dlopen(lib_name, flags)) == NULL)
59 | 		fatal(_("load_ext: cannot open library `%s': %s"), lib_name,
60 | 		      dlerror());
{% endraw %}

```
### nonposix.h

```c

{% raw %}
90 | #include <dlfcn.h>
91 | 
92 | #define dlopen(f, m) os2_dlopen(f, m)
93 | void *os2_dlopen(const char *file, int mode);
94 | 
95 | #define dlsym(h, n) os2_dlsym(h, n)
{% endraw %}

```
### pc/dlfcn.h

```c

{% raw %}
3 | 
4 | #define RTLD_LAZY 1
5 | 
6 | extern void *dlopen (const char *, int);
7 | extern int   dlclose (void *);
8 | extern void *dlsym (void *, const char *);
{% endraw %}

```