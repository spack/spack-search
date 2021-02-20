---
name: "libx11"
layout: package
next_package: libxml2
previous_package: libwebsockets
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
574 | 	return 1;
575 | #ifdef __UNIXWARE__
576 |     else {
577 |        void *dl_handle = dlopen(NULL, RTLD_LAZY);
578 |        if (!dl_handle ||
579 |          ((_x11_thr_self = (xthread_t(*)())dlsym(dl_handle,"thr_self")) == 0)) {
{% endraw %}

```
### src/CrGlCur.c

```c

{% raw %}
70 | #if defined(hpux)
71 | 	module = shl_load(library, BIND_DEFERRED, 0L);
72 | #else
73 | 	module =  dlopen(library, RTLD_LAZY);
74 | #endif
75 | 	if (module)
{% endraw %}

```
### src/xlibi18n/XlcDL.c

```c

{% raw %}
303 | #if defined(hpux)
304 |       object->dl_module = shl_load(path, BIND_DEFERRED, 0L);
305 | #else
306 |       object->dl_module = dlopen(path, RTLD_LAZY);
307 | #endif
308 |       Xfree(path);
{% endraw %}

```
### src/xlibi18n/lcDynamic.c

```c

{% raw %}
66 | 
67 |     snprintf(libpath, sizeof(libpath), "%s/%s/%s",
68 | 	     XLOCALEDIR, name, LCLIBNAME);
69 |     nlshandler = dlopen(libpath,LAZY);
70 |     _XlcGenericMethods = (XLCdMethods)dlsym(nlshandler,"genericMethods");
71 |     lcd = _XlcCreateLC(name,_XlcGenericMethods);
{% endraw %}

```