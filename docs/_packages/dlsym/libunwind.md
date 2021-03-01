---
name: "libunwind"
layout: package
next_package: libuv
previous_package: libtool
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 1.5.0
4 / 773 files match, 2 filtered matches.

 - [tests/Ltest-nocalloc.c](#testsltest-nocallocc)
 - [tests/Gtest-nomalloc.c](#testsgtest-nomallocc)

### tests/Ltest-nocalloc.c

```c

{% raw %}
50 |     func = &__libc_calloc;
51 | #else
52 |   if(!func)
53 |     func = dlsym(RTLD_NEXT, "calloc");
54 | #endif
55 | 
67 |   static void * (*func)(size_t);
68 | 
69 |   if(!func)
70 |     func = dlsym(RTLD_NEXT, "malloc");
71 | 
72 |   if (in_unwind) {
{% endraw %}

```
### tests/Gtest-nomalloc.c

```c

{% raw %}
39 |   static void * (*func)();
40 | 
41 |   if(!func)
42 |     func = (void *(*)()) dlsym(RTLD_NEXT, "malloc");
43 | 
44 |   if (in_unwind) {
{% endraw %}

```