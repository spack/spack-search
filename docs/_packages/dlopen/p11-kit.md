---
name: "p11-kit"
layout: package
next_package: dbus
previous_package: dpdk
library_name: dlopen
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 0.23.20
9 / 446 files match, 3 filtered matches.

 - [common/compat.h](#commoncompath)
 - [p11-kit/modules.c](#p11-kitmodulesc)
 - [trust/frob-multi-init.c](#trustfrob-multi-initc)

### common/compat.h

```c

{% raw %}
233 | typedef void * dl_module_t;
234 | 
235 | #define p11_dl_open(f) \
236 | 	(dlopen ((f), RTLD_LOCAL | RTLD_NOW))
237 | #define p11_dl_symbol(d, s) \
238 | 	(dlsym ((d), (s)))
{% endraw %}

```
### p11-kit/modules.c

```c

{% raw %}
346 | #endif
347 | 
348 | static CK_RV
349 | dlopen_and_get_function_list (Module *mod,
350 |                               const char *path,
351 |                               CK_FUNCTION_LIST **funcs)
425 | 
426 | 	mod->filename = strdup (path);
427 | 
428 | 	rv = dlopen_and_get_function_list (mod, path, &funcs);
429 | 	free (expand);
430 | 
{% endraw %}

```
### trust/frob-multi-init.c

```c

{% raw %}
23 | 	CK_RV rv;
24 | 	void *dl;
25 | 
26 | 	dl = dlopen (TRUST_SO, RTLD_LOCAL | RTLD_NOW);
27 | 	if (dl == NULL)
28 | 		fprintf (stderr, "%s\n", dlerror());
{% endraw %}

```