---
name: "krb5"
layout: package
next_package: py-mypy
previous_package: geopm
languages: ['cpp']
---
## 1.16.2
7 / 4638 files match

 - [src/aclocal.m4](#srcaclocalm4)
 - [src/lib/gssapi/mechglue/g_initialize.c](#srclibgssapimechglueg_initializec)
 - [src/include/autoconf.h.in](#srcincludeautoconfhin)
 - [src/tests/shlib/t_loader.c](#srctestsshlibt_loaderc)
 - [src/plugins/preauth/pkinit/pkinit_crypto_openssl.c](#srcpluginspreauthpkinitpkinit_crypto_opensslc)
 - [src/util/support/plugins.c](#srcutilsupportpluginsc)
 - [doc/thread-safe.txt](#docthread-safetxt)

### src/aclocal.m4

```

{% raw %}
94 | KRB5_AC_FIND_DLOPEN
147 | dnl find dlopen
148 | AC_DEFUN([KRB5_AC_FIND_DLOPEN],[
151 | AC_SEARCH_LIBS(dlopen, dl, [
152 | if test "$ac_cv_search_dlopen" != "none required"; then
153 |   DL_LIB=$ac_cv_search_dlopen
156 | AC_DEFINE(USE_DLOPEN,1,[Define if dlopen should be used])])
899 | AC_REQUIRE([KRB5_AC_FIND_DLOPEN])
{% endraw %}

```
### src/lib/gssapi/mechglue/g_initialize.c

```cpp

{% raw %}
919 | 		(void) syslog(LOG_INFO, "libgss dlopen(%s): %s\n",
1164 | 		(void) syslog(LOG_INFO, "libgss dlopen(%s): %s\n",
{% endraw %}

```
### src/include/autoconf.h.in

```

{% raw %}
693 | /* Define if dlopen should be used */
694 | #undef USE_DLOPEN
{% endraw %}

```
### src/tests/shlib/t_loader.c

```cpp

{% raw %}
29 | #define HAVE_DLOPEN 1
62 | #ifdef HAVE_DLOPEN
95 |     p = dlopen(namebuf, (lazy ? RTLD_LAZY : RTLD_NOW) | RTLD_MEMBER);
97 |         fprintf(stderr, "dlopen of %s failed: %s\n", namebuf, dlerror());
{% endraw %}

```
### src/plugins/preauth/pkinit/pkinit_crypto_openssl.c

```cpp

{% raw %}
3675 |     handle = dlopen(modname, RTLD_NOW);
{% endraw %}

```
### src/util/support/plugins.c

```cpp

{% raw %}
28 | #if USE_DLOPEN
42 | #if USE_DLOPEN
53 | #define PLUGIN_DLOPEN_FLAGS (RTLD_NOW | RTLD_LOCAL | GROUP | NODELETE)
56 | #if USE_DLOPEN && USE_CFBUNDLE
78 | #if USE_DLOPEN
84 | #if !defined (USE_DLOPEN) && !defined (_WIN32)
195 | #if USE_DLOPEN
269 |             handle = dlopen(filepath, PLUGIN_DLOPEN_FLAGS);
274 |                 Tprintf ("dlopen(%s): %s\n", filepath, e);
289 | #endif /* USE_DLOPEN */
336 | #if USE_DLOPEN
414 | #if USE_DLOPEN
{% endraw %}

```
### doc/thread-safe.txt

```

{% raw %}
5 | library in question in use.  (If dlopen or dlsym in one thread starts
6 | running the initializer, and then dlopen/dlsym in another thread
9 | dlopen/dlsym bug.)
{% endraw %}

```