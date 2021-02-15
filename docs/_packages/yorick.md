---
name: "yorick"
layout: package
next_package: fox
previous_package: r-rcmdcheck
languages: ['cpp']
---
## 2.2.04
9 / 571 files match

 - [yorick/dlsym.c](#yorickdlsymc)
 - [yorick/NOTES-1.6](#yoricknotes-16)
 - [yorick/task.c](#yoricktaskc)
 - [play/pstdlib.h](#playpstdlibh)
 - [play/win/wdl.c](#playwinwdlc)
 - [play/unix/PLUGIN.txt](#playunixplugintxt)
 - [play/unix/config.c](#playunixconfigc)
 - [play/unix/udltest.c](#playunixudltestc)
 - [play/unix/udl.c](#playunixudlc)

### yorick/dlsym.c

```cpp

{% raw %}
14 | void *dlopen()
{% endraw %}

```
### yorick/NOTES-1.6

```

{% raw %}
33 | you call a system function to "dlopen" a shared object file, whose
35 | requires just two functions: "dlopen" to open the shared object file
42 | be connected using explicit "dlopen" and "dlsym" calls, there is no
89 | time yorick was built.  Thus, not only must you "dlopen" the shared
101 | required dlopen of the plug-in shared binary, say, mylib.so (or
{% endraw %}

```
### yorick/task.c

```cpp

{% raw %}
1441 |   plug = p_dlopen(pkgname);
1447 |       plug = p_dlopen(tmp);
{% endraw %}

```
### play/pstdlib.h

```cpp

{% raw %}
71 | PLUG_API void *p_dlopen(const char *dlname);
{% endraw %}

```
### play/win/wdl.c

```cpp

{% raw %}
27 | p_dlopen(const char *dlname)
52 | p_dlopen(const char *dlname)
{% endraw %}

```
### play/unix/PLUGIN.txt

```

{% raw %}
2 | (1) Compiling the udl.c p_dlopen/p_dlsym dynamic linking functions:
6 | (2) Linking the main program which calls p_dlopen/p_dlsym:
29 |   -DPLUG_LIBDL   dlopen/dlsym in most UNIX systems
96 | the yorick executable (or whatever program calls p_dlopen).  This is
{% endraw %}

```
### play/unix/config.c

```cpp

{% raw %}
99 |   void *h = test_dlopen();
{% endraw %}

```
### play/unix/udltest.c

```cpp

{% raw %}
12 | /* main() that dlopens this is TEST_DL branch of config.c */
46 | extern void *test_dlopen(void);
50 | test_dlopen(void)
52 |   return dlopen("./udltest" PLUG_SUFFIX, PLUG_FLAGS);
77 | extern void *test_dlopen(void);
81 | test_dlopen(void)
105 | test_dlopen(void)
143 | extern void *test_dlopen(void);
147 | test_dlopen(void)
{% endraw %}

```
### play/unix/udl.c

```cpp

{% raw %}
35 | p_dlopen(const char *dlname)
40 |     handle = dlopen(name, PLUG_FLAGS);
74 | p_dlopen(const char *dlname)
108 | p_dlopen(const char *dlname)
165 | p_dlopen(const char *dlname)
200 | p_dlopen(const char *dlname)
{% endraw %}

```