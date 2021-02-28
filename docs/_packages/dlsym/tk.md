---
name: "tk"
layout: package
next_package: mvapich2
previous_package: glfw
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 8.5.19
1 / 856 files match, 1 filtered matches.

 - [macosx/tkMacOSXInit.c](#macosxtkmacosxinitc)

### macosx/tkMacOSXInit.c

```c

{% raw %}
545 |     const char* module,
546 |     const char* symbol)
547 | {
548 |     void *addr = dlsym(RTLD_NEXT, symbol);
549 |     if (!addr) {
550 | 	(void) dlerror(); /* Clear dlfcn error state */
{% endraw %}

```