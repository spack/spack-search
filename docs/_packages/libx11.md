---
name: "libx11"
layout: package
next_package: cctools
previous_package: py-or-tools
languages: ['c']
---
## 1.6.5
9 / 1605 files match, 4 filtered matches.

 - [src/locking.c](#srclockingc)
 - [src/CrGlCur.c](#srccrglcurc)
 - [src/xlibi18n/XlcDL.c](#srcxlibi18nxlcdlc)
 - [src/xlibi18n/lcDynamic.c](#srcxlibi18nlcdynamicc)

### src/locking.c

```c

{% raw %}
577 |        void *dl_handle = dlopen(NULL, RTLD_LAZY);
{% endraw %}

```
### src/CrGlCur.c

```c

{% raw %}
73 | 	module =  dlopen(library, RTLD_LAZY);
{% endraw %}

```
### src/xlibi18n/XlcDL.c

```c

{% raw %}
306 |       object->dl_module = dlopen(path, RTLD_LAZY);
{% endraw %}

```
### src/xlibi18n/lcDynamic.c

```c

{% raw %}
69 |     nlshandler = dlopen(libpath,LAZY);
{% endraw %}

```