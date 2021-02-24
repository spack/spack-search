---
name: "ncl"
layout: package
next_package: spindle
previous_package: nbdkit
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 6.5.0
3 / 8693 files match, 2 filtered matches.

 - [ni/src/ncl/NclDriver.c](#nisrcnclncldriverc)
 - [ni/src/ncl/NclApi.c](#nisrcnclnclapic)

### ni/src/ncl/NclDriver.c

```c

{% raw %}
333 |                         (void) shl_findsym(&so_handle, "Init",
334 |                                 TYPE_UNDEFINED, (void *) &init_function);
335 | #else
336 |                         init_function = dlsym(so_handle, "Init");
337 | #endif /* HPUX */
338 |                         if (init_function != NULL) {
{% endraw %}

```
### ni/src/ncl/NclApi.c

```c

{% raw %}
228 | 						init_function = NULL;
229 | 						(void)shl_findsym(so_handle, "Init",TYPE_UNDEFINED,(void*)&init_function);
230 | #else
231 | 						init_function = dlsym(so_handle, "Init");
232 | #endif
233 | 						if(init_function != NULL) {
{% endraw %}

```