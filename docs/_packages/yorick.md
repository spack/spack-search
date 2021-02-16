---
name: "yorick"
layout: package
next_package: fox
previous_package: r-rcmdcheck
languages: ['c']
---
## 2.2.04
9 / 571 files match, 7 filtered matches.

 - [yorick/dlsym.c](#yorickdlsymc)
 - [yorick/task.c](#yoricktaskc)
 - [play/pstdlib.h](#playpstdlibh)
 - [play/win/wdl.c](#playwinwdlc)
 - [play/unix/config.c](#playunixconfigc)
 - [play/unix/udltest.c](#playunixudltestc)
 - [play/unix/udl.c](#playunixudlc)

### yorick/dlsym.c

```c

{% raw %}
14 | void *dlopen()
{% endraw %}

```
### yorick/task.c

```c

{% raw %}
1441 |   plug = p_dlopen(pkgname);
1447 |       plug = p_dlopen(tmp);
{% endraw %}

```
### play/pstdlib.h

```c

{% raw %}
71 | PLUG_API void *p_dlopen(const char *dlname);
{% endraw %}

```
### play/win/wdl.c

```c

{% raw %}
27 | p_dlopen(const char *dlname)
52 | p_dlopen(const char *dlname)
{% endraw %}

```
### play/unix/config.c

```c

{% raw %}
99 |   void *h = test_dlopen();
{% endraw %}

```
### play/unix/udltest.c

```c

{% raw %}
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

```c

{% raw %}
35 | p_dlopen(const char *dlname)
40 |     handle = dlopen(name, PLUG_FLAGS);
74 | p_dlopen(const char *dlname)
108 | p_dlopen(const char *dlname)
165 | p_dlopen(const char *dlname)
200 | p_dlopen(const char *dlname)
{% endraw %}

```