---
name: "libmonitor"
layout: package
next_package: libnl
previous_package: libmicrohttpd
languages: ['c']
---
## 2013.02.18
11 / 63 files match, 5 filtered matches.

 - [src/monitor.h](#srcmonitorh)
 - [src/callback.c](#srccallbackc)
 - [src/main.c](#srcmainc)
 - [src/dlopen.c](#srcdlopenc)
 - [tests/early.c](#testsearlyc)

### src/monitor.h

```c

{% raw %}
63 | extern void *monitor_init_thread(int tid, void *data);
64 | extern void monitor_fini_thread(void *data);
65 | extern size_t monitor_reset_stacksize(size_t old_size);
66 | extern void monitor_pre_dlopen(const char *path, int flags);
67 | extern void monitor_dlopen(const char *path, int flags, void *handle);
68 | extern void monitor_dlclose(void *handle);
69 | extern void monitor_post_dlclose(void *handle, int ret);
81 | extern int monitor_real_execve(const char *path, char *const argv[],
82 | 			       char *const envp[]);
83 | extern int monitor_real_system(const char *command);
84 | extern void *monitor_real_dlopen(const char *path, int flags);
85 | extern int monitor_real_dlclose(void *handle);
86 | extern int monitor_real_sigprocmask(int how, const sigset_t *set,
{% endraw %}

```
### src/callback.c

```c

{% raw %}
110 | }
111 | 
112 | void __attribute__ ((weak))
113 | monitor_pre_dlopen(const char *path, int flags)
114 | {
115 |     MONITOR_DEBUG1("(default callback)\n");
116 | }
117 | 
118 | void __attribute__ ((weak))
119 | monitor_dlopen(const char *path, int flags, void *handle)
120 | {
121 |     MONITOR_DEBUG("(default callback) path = %s, flags = %d, handle = %p\n",
{% endraw %}

```
### src/main.c

```c

{% raw %}
655 | }
656 | 
657 | void * __attribute__ ((weak))
658 | monitor_real_dlopen(const char *path, int flags)
659 | {
660 |     MONITOR_DEBUG1("(weak)\n");
{% endraw %}

```
### src/dlopen.c

```c

{% raw %}
58 |  *----------------------------------------------------------------------
59 |  */
60 | 
61 | typedef void *dlopen_fcn_t(const char *, int);
62 | typedef int dlclose_fcn_t(void *);
63 | 
64 | #ifdef MONITOR_STATIC
65 | extern dlopen_fcn_t   __real_dlopen;
66 | extern dlclose_fcn_t  __real_dlclose;
67 | #endif
68 | 
69 | static dlopen_fcn_t   *real_dlopen = NULL;
70 | static dlclose_fcn_t  *real_dlclose = NULL;
71 | 
76 |  */
77 | 
78 | static void
79 | monitor_dlopen_init(void)
80 | {
81 |     static int init_done = 0;
83 |     if (init_done)
84 | 	return;
85 | 
86 |     MONITOR_GET_REAL_NAME_WRAP(real_dlopen, dlopen);
87 |     MONITOR_GET_REAL_NAME_WRAP(real_dlclose, dlclose);
88 |     init_done = 1;
98 |  *  Client access to the real dlopen() and dlclose().
99 |  */
100 | void *
101 | monitor_real_dlopen(const char *path, int flags)
102 | {
103 |     monitor_dlopen_init();
104 |     return (*real_dlopen)(path, flags);
105 | }
106 | 
107 | int
108 | monitor_real_dlclose(void *handle)
109 | {
110 |     monitor_dlopen_init();
111 |     return (*real_dlclose)(handle);
112 | }
115 |  *  Override dlopen() and dlclose().
116 |  */
117 | void *
118 | MONITOR_WRAP_NAME(dlopen)(const char *path, int flags)
119 | {
120 |     void *handle;
121 | 
122 |     monitor_dlopen_init();
123 |     MONITOR_DEBUG("(pre) path: %s, flags: %d\n", path, flags);
124 |     monitor_pre_dlopen(path, flags);
125 |     handle = (*real_dlopen)(path, flags);
126 |     monitor_dlopen(path, flags, handle);
127 |     MONITOR_DEBUG("(post) path: %s, handle: %p\n", path, handle);
128 | 
134 | {
135 |     int ret;
136 | 
137 |     monitor_dlopen_init();
138 |     MONITOR_DEBUG("(pre) handle: %p\n", handle);
139 |     monitor_dlclose(handle);
{% endraw %}

```
### tests/early.c

```c

{% raw %}
35 | }
36 | 
37 | void
38 | do_dlopen(void)
39 | {
40 |     TITLE("dlopen");
41 |     handle = dlopen("/lib64/libm.so.6", RTLD_LAZY);
42 |     printf("dlopen: handle = %p\n", handle);
43 | }
44 | 
127 | 	    break;
128 | 
129 | 	case 'O': case 'o':
130 | 	    do_dlopen();
131 | 	    break;
132 | 
{% endraw %}

```