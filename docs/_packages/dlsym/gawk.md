---
name: "gawk"
layout: package
next_package: gcc
previous_package: flexiblas
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 5.1.0
12 / 1886 files match, 3 filtered matches.

 - [ext.c](#extc)
 - [nonposix.h](#nonposixh)
 - [pc/dlfcn.h](#pcdlfcnh)

### ext.c

```c

{% raw %}
60 | 		      dlerror());
61 | 
62 | 	/* Per the GNU Coding standards */
63 | 	gpl_compat = (int *) dlsym(dl, "plugin_is_GPL_compatible");
64 | 	if (gpl_compat == NULL)
65 | 		fatal(_("load_ext: library `%s': does not define `plugin_is_GPL_compatible': %s"),
66 | 				lib_name, dlerror());
67 | 
68 | 	install_func = (int (*)(const gawk_api_t *const, awk_ext_id_t))
69 | 				dlsym(dl, INIT_FUNC);
70 | 	if (install_func == NULL)
71 | 		fatal(_("load_ext: library `%s': cannot call function `%s': %s"),
{% endraw %}

```
### nonposix.h

```c

{% raw %}
93 | void *os2_dlopen(const char *file, int mode);
94 | 
95 | #define dlsym(h, n) os2_dlsym(h, n)
96 | void *os2_dlsym(void *handle, const char *name);
97 | #endif /* __KLIBC__ */
98 | 
{% endraw %}

```
### pc/dlfcn.h

```c

{% raw %}
5 | 
6 | extern void *dlopen (const char *, int);
7 | extern int   dlclose (void *);
8 | extern void *dlsym (void *, const char *);
9 | extern char *dlerror (void);
10 | 
{% endraw %}

```