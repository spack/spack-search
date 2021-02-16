---
name: "libgssglue"
layout: package
next_package: libhbaapi
previous_package: libgpuarray
languages: ['c']
---
## 0.3
3 / 60 files match, 1 filtered matches.

 - [src/g_initialize.c](#srcg_initializec)

### src/g_initialize.c

```c

{% raw %}
231 | 	if ((dl = dlopen(buffer, RTLD_NOW)) == NULL) {
308 | 	if ((dl = dlopen(buffer, RTLD_NOW | RTLD_LOCAL)) == NULL) {
{% endraw %}

```