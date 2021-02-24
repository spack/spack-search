---
name: "p11-kit"
layout: package
next_package: apex
previous_package: lighttpd
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 0.23.20
2 / 446 files match, 2 filtered matches.

 - [common/compat.h](#commoncompath)
 - [trust/frob-multi-init.c](#trustfrob-multi-initc)

### common/compat.h

```c

{% raw %}
235 | #define p11_dl_open(f) \
236 | 	(dlopen ((f), RTLD_LOCAL | RTLD_NOW))
237 | #define p11_dl_symbol(d, s) \
238 | 	(dlsym ((d), (s)))
239 | 
240 | char * p11_dl_error (void);
{% endraw %}

```
### trust/frob-multi-init.c

```c

{% raw %}
28 | 		fprintf (stderr, "%s\n", dlerror());
29 | 	assert (dl != NULL);
30 | 
31 | 	C_GetFunctionList = dlsym (dl, "C_GetFunctionList");
32 | 	assert (C_GetFunctionList != NULL);
33 | 
{% endraw %}

```