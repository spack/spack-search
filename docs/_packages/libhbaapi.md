---
name: "libhbaapi"
layout: package
next_package: pinentry
previous_package: vt
languages: ['c']
---
## 3.10
1 / 13 files match

 - [hbaapilib.c](#hbaapilibc)

### hbaapilib.c

```c

{% raw %}
544 | 	if((lib_infop->hLibrary = dlopen(librarypath,RTLD_LAZY)) == NULL) {
1013 |     if((handle = dlopen("libHBAAPI.so", RTLD_NOW)) != NULL) {
{% endraw %}

```