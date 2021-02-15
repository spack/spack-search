---
name: "ferret"
layout: package
next_package: libtheora
previous_package: elmerfem
languages: ['cpp']
---
## 7.6.0
2 / 5578 files match

 - [fer/AIX_MODIFICATIONS.LOG](#feraix_modificationslog)
 - [fer/ccr/EF_InternalUtil.c](#ferccref_internalutilc)

### fer/AIX_MODIFICATIONS.LOG

```

{% raw %}
39 |    added -ldl to SYSLIB  (for dynamic loading functions dlopen, etc)
{% endraw %}

```
### fer/ccr/EF_InternalUtil.c

```cpp

{% raw %}
173 | /* handle returned from dlopen of $FER_LIBS/libpyefcn.so */
1664 |         pyefcn_handle = dlopen(libname, RTLD_LAZY);
1812 |       if ( (ef_ptr->handle = dlopen(tempText, RTLD_LAZY)) == NULL ) {
1814 |                          "  Dynamic linking call dlopen() returns --\n"
{% endraw %}

```