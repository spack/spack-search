---
name: "libgssglue"
layout: package
next_package: openwsman
previous_package: z-checker
languages: ['c']
---
## 0.3
3 / 60 files match

 - [src/g_initialize.c](#srcg_initializec)

### src/g_initialize.c

```c

{% raw %}
231 | 	if ((dl = dlopen(buffer, RTLD_NOW)) == NULL) {
308 | 	if ((dl = dlopen(buffer, RTLD_NOW | RTLD_LOCAL)) == NULL) {
{% endraw %}

```