---
name: "procps"
layout: package
next_package: libdrm
previous_package: mlocate
languages: ['cpp']
---
## 3.3.15
5 / 173 files match

 - [configure.ac](#configureac)
 - [ps/output.c](#psoutputc)
 - [proc/numa.c](#procnumac)
 - [proc/sysinfo.c](#procsysinfoc)
 - [top/top.c](#toptopc)

### configure.ac

```

{% raw %}
260 |   AC_SEARCH_LIBS([dlopen], [dl], [],
262 |   if test "x$ac_cv_search_dlopen" != "xnone required"; then
263 |     DL_LIB="$ac_cv_search_dlopen"
{% endraw %}

```
### ps/output.c

```cpp

{% raw %}
1320 |     void *handle = dlopen("libselinux.so.1", RTLD_NOW);
{% endraw %}

```
### proc/numa.c

```cpp

{% raw %}
31 |  * option might be required when libdl.so (necessary for dlopen) is missing. |
70 |     if ((libnuma_handle = dlopen("libnuma.so", RTLD_LAZY))
71 |     || (libnuma_handle = dlopen("libnuma.so.1", RTLD_LAZY))) {
{% endraw %}

```
### proc/sysinfo.c

```cpp

{% raw %}
285 |                // ... functions with dlopen -> FIXME :(
{% endraw %}

```
### top/top.c

```cpp

{% raw %}
4496 |       ld route to symbol resolution (we use that dlopen() guy instead)! */
{% endraw %}

```