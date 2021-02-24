---
name: "nbdkit"
layout: package
next_package: ncl
previous_package: darshan-util
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 1.23.7
6 / 763 files match, 2 filtered matches.

 - [server/debug-flags.c](#serverdebug-flagsc)
 - [plugins/vddk/vddk.c](#pluginsvddkvddkc)

### server/debug-flags.c

```c

{% raw %}
134 |       int *sym;
135 | 
136 |       /* Find the symbol. */
137 |       sym = dlsym (dl, flag->symbol);
138 |       if (sym) {
139 |         /* Set the flag. */
{% endraw %}

```
### plugins/vddk/vddk.c

```c

{% raw %}
347 |   /* Load symbols. */
348 | #define STUB(fn,ret,args)                                         \
349 |   do {                                                            \
350 |     fn = dlsym (dl, #fn);                                         \
351 |     if (fn == NULL) {                                             \
352 |       nbdkit_error ("required VDDK symbol \"%s\" is missing: %s", \
{% endraw %}

```