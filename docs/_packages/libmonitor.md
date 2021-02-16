---
name: "libmonitor"
layout: package
next_package: vpic
previous_package: libfs
languages: ['c']
---
## 2013.02.18
11 / 63 files match

 - [src/monitor.h](#srcmonitorh)
 - [src/callback.c](#srccallbackc)
 - [src/main.c](#srcmainc)
 - [src/dlopen.c](#srcdlopenc)
 - [tests/early.c](#testsearlyc)

### src/monitor.h

```c

{% raw %}
66 | extern void monitor_pre_dlopen(const char *path, int flags);
67 | extern void monitor_dlopen(const char *path, int flags, void *handle);
84 | extern void *monitor_real_dlopen(const char *path, int flags);
{% endraw %}

```
### src/callback.c

```c

{% raw %}
113 | monitor_pre_dlopen(const char *path, int flags)
119 | monitor_dlopen(const char *path, int flags, void *handle)
{% endraw %}

```
### src/main.c

```c

{% raw %}
658 | monitor_real_dlopen(const char *path, int flags)
{% endraw %}

```
### src/dlopen.c

```c

{% raw %}
61 | typedef void *dlopen_fcn_t(const char *, int);
65 | extern dlopen_fcn_t   __real_dlopen;
69 | static dlopen_fcn_t   *real_dlopen = NULL;
79 | monitor_dlopen_init(void)
86 |     MONITOR_GET_REAL_NAME_WRAP(real_dlopen, dlopen);
101 | monitor_real_dlopen(const char *path, int flags)
103 |     monitor_dlopen_init();
104 |     return (*real_dlopen)(path, flags);
110 |     monitor_dlopen_init();
118 | MONITOR_WRAP_NAME(dlopen)(const char *path, int flags)
122 |     monitor_dlopen_init();
124 |     monitor_pre_dlopen(path, flags);
125 |     handle = (*real_dlopen)(path, flags);
126 |     monitor_dlopen(path, flags, handle);
137 |     monitor_dlopen_init();
{% endraw %}

```
### tests/early.c

```c

{% raw %}
38 | do_dlopen(void)
40 |     TITLE("dlopen");
41 |     handle = dlopen("/lib64/libm.so.6", RTLD_LAZY);
42 |     printf("dlopen: handle = %p\n", handle);
130 | 	    do_dlopen();
{% endraw %}

```