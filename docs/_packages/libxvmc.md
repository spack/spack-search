---
name: "libxvmc"
layout: package
next_package: mpfi
previous_package: httpd
languages: ['c']
---
## 1.0.9
4 / 24 files match, 1 filtered matches.

 - [wrapper/XvMCWrapper.c](#wrapperxvmcwrapperc)

### wrapper/XvMCWrapper.c

```c

{% raw %}
206 | static void  *dlopenversion(const char *lib, const char *version, int flag)
224 |   ret = dlopen(curName, flag);
241 |     xvhandle = dlopenversion("libXv.so", XV_SOVERSION, RTLD_LAZY | RTLD_GLOBAL);
247 |     handle2 = dlopenversion("libXvMC.so", XVMC_SOVERSION, RTLD_LAZY | RTLD_GLOBAL);
307 | 	handle = dlopenversion(nameBuffer, XVMC_SOVERSION,RTLD_LAZY);
352 | 	handle = dlopen(nameBuffer,RTLD_LAZY);
{% endraw %}

```