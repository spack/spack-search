---
name: "vampirtrace"
layout: package
next_package: gtkorvo-dill
previous_package: hpctoolkit
languages: ['c']
---
## 5.14.4
10 / 650 files match

 - [vtlib/vt_mallocwrap.c](#vtlibvt_mallocwrapc)
 - [vtlib/vt_libwrap.c](#vtlibvt_libwrapc)
 - [vtlib/vt_iowrap.c](#vtlibvt_iowrapc)
 - [vtlib/vt_plugin_cntr.c](#vtlibvt_plugin_cntrc)

### vtlib/vt_mallocwrap.c

```c

{% raw %}
92 |      dlopen calls malloc which would result in an infinite recursion when
{% endraw %}

```
### vtlib/vt_libwrap.c

```c

{% raw %}
159 |     libc_handle = dlopen(SHLIBC_PATHNAME,
173 |       printf("VampirTrace: FATAL: dlopen(\""SHLIBC_PATHNAME"\") failed: %s\n",
177 |       vt_error_msg("dlopen(\""SHLIBC_PATHNAME"\") failed: %s\n", dlerror());
262 |         (*lw)->handlev[i] = dlopen((*lw)->attr->shlibs[i],
272 |                    "dlopen(\"%s\") failed: %s",
{% endraw %}

```
### vtlib/vt_iowrap.c

```c

{% raw %}
120 |       iolib_handle = dlopen( iolib_pathname,
127 |         printf("VampirTrace: FATAL: dlopen(\"%s\") error: %s\n", iolib_pathname, dlerror());
{% endraw %}

```
### vtlib/vt_plugin_cntr.c

```c

{% raw %}
213 |     handle = dlopen(buffer, RTLD_NOW);
{% endraw %}

```