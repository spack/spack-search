---
name: "emacs"
layout: package
next_package: kylin
previous_package: ermod
languages: ['cpp']
---
## 25.2
4 / 5054 files match

 - [ChangeLog.2](#changelog2)
 - [configure.ac](#configureac)
 - [src/ChangeLog.5](#srcchangelog5)
 - [src/dynlib.c](#srcdynlibc)

### ChangeLog.2

```

{% raw %}
15953 | 	'dlopen' does.  Record the error, if any, for use by dynlib_error.
{% endraw %}

```
### configure.ac

```

{% raw %}
3367 |       # BSD systems have dlopen in libc.
3368 |       AC_CHECK_FUNC([dlopen],
{% endraw %}

```
### src/ChangeLog.5

```

{% raw %}
5328 | 	* sysdep.c [USE_DL_STUBS] (dlopen, dlsym, dlclose): New functions.
{% endraw %}

```
### src/dynlib.c

```cpp

{% raw %}
275 |   return dlopen (path, RTLD_LAZY);
{% endraw %}

```