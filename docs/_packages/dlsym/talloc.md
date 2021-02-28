---
name: "talloc"
layout: package
next_package: gcc
previous_package: nnvm
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 2.1.9
3 / 246 files match, 2 filtered matches.

 - [lib/replace/replace.h](#libreplacereplaceh)
 - [lib/replace/dlfcn.c](#libreplacedlfcnc)

### lib/replace/replace.h

```c

{% raw %}
420 | 
421 | #ifndef HAVE_DLSYM
422 | #define dlsym rep_dlsym
423 | void *rep_dlsym(void *handle, const char *symbol);
424 | #endif
425 | 
{% endraw %}

```
### lib/replace/dlfcn.c

```c

{% raw %}
45 | #endif
46 | 
47 | #ifndef HAVE_DLSYM
48 | void *rep_dlsym(void *handle, const char *symbol)
49 | {
50 | #ifdef HAVE_SHL_FINDSYM
{% endraw %}

```