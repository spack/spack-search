---
name: "gnupg"
layout: package
next_package: fcgi
previous_package: py-genders
languages: ['cpp']
---
## 2.2.15
9 / 1018 files match

 - [configure.ac](#configureac)
 - [scd/apdu.c](#scdapduc)
 - [common/iobuf.c](#commoniobufc)
 - [common/ChangeLog.jnlib](#commonchangelogjnlib)
 - [common/homedir.c](#commonhomedirc)
 - [common/utf8conv.c](#commonutf8convc)
 - [common/dynload.h](#commondynloadh)
 - [m4/lib-link.m4](#m4lib-linkm4)
 - [build-aux/speedo.mk](#build-auxspeedomk)

### configure.ac

```

{% raw %}
889 | gnupg_dlopen_save_libs="$LIBS"
891 | AC_SEARCH_LIBS(dlopen, c dl,,,)
894 | LIBS="$gnupg_dlopen_save_libs"
{% endraw %}

```
### scd/apdu.c

```cpp

{% raw %}
1954 |       handle = dlopen (opt.pcsc_driver, RTLD_LAZY);
{% endraw %}

```
### common/iobuf.c

```cpp

{% raw %}
2304 | 	handle = dlopen ("kernel32.dll", RTLD_LAZY);
{% endraw %}

```
### common/ChangeLog.jnlib

```

{% raw %}
32 | 	* dynload.h (dlopen, dlsym) [W32CE]: Map to wchar_t.
{% endraw %}

```
### common/homedir.c

```cpp

{% raw %}
138 |           handle = dlopen (dllnames[i], RTLD_LAZY);
{% endraw %}

```
### common/utf8conv.c

```cpp

{% raw %}
693 | /* Wrapper function for iconv_open, required for W32 as we dlopen that
702 | /* Wrapper function for iconv, required for W32 as we dlopen that
713 | /* Wrapper function for iconv_close, required for W32 as we dlopen that
{% endraw %}

```
### common/dynload.h

```cpp

{% raw %}
42 | dlopen (const char *name, int flag)
{% endraw %}

```
### m4/lib-link.m4

```

{% raw %}
459 |               dnl age, revision, installed, dlopen, dlpreopen, libdir.
{% endraw %}

```
### build-aux/speedo.mk

```

{% raw %}
594 | echo "dlopen=''" >> lib/libz.la;			\
{% endraw %}

```