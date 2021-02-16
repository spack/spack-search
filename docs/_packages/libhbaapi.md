---
name: "libhbaapi"
layout: package
next_package: libhio
previous_package: libgssglue
languages: ['c']
---
## 3.10
1 / 13 files match, 1 filtered matches.

 - [hbaapilib.c](#hbaapilibc)

### hbaapilib.c

```c

{% raw %}
544 | 	if((lib_infop->hLibrary = dlopen(librarypath,RTLD_LAZY)) == NULL) {
1013 |     if((handle = dlopen("libHBAAPI.so", RTLD_NOW)) != NULL) {
{% endraw %}

```