---
name: "timemory"
layout: package
next_package: fermisciencetools
previous_package: binutils
languages: ['c']
---
## master
29 / 2657 files match

 - [external/gotcha/src/gotcha_dl.h](#externalgotchasrcgotcha_dlh)
 - [external/gotcha/src/gotcha_dl.c](#externalgotchasrcgotcha_dlc)
 - [external/gotcha/src/gotcha.c](#externalgotchasrcgotchac)
 - [external/gotcha/test/dlopen/test_dlopen.c](#externalgotchatestdlopentest_dlopenc)
 - [external/gotcha/test/multi_agent_dlopen/dlsym.c](#externalgotchatestmulti_agent_dlopendlsymc)
 - [external/gotcha/test/multi_agent_dlopen/monitor.c](#externalgotchatestmulti_agent_dlopenmonitorc)
 - [external/gotcha/test/multi_agent_dlopen/main.c](#externalgotchatestmulti_agent_dlopenmainc)
 - [external/caliper/ext/gotcha/src/gotcha_dl.h](#externalcaliperextgotchasrcgotcha_dlh)
 - [external/caliper/ext/gotcha/src/gotcha_dl.c](#externalcaliperextgotchasrcgotcha_dlc)
 - [external/caliper/ext/gotcha/src/gotcha.c](#externalcaliperextgotchasrcgotchac)

### external/gotcha/src/gotcha_dl.h

```c

{% raw %}
10 | extern gotcha_wrappee_handle_t orig_dlopen_handle;
{% endraw %}

```
### external/gotcha/src/gotcha_dl.c

```c

{% raw %}
9 | gotcha_wrappee_handle_t orig_dlopen_handle;
17 |    debug_printf(3, "Trying to re-bind %s from tool %s after dlopen\n",
28 |       debug_printf(3, "Still could not prepare binding %s after dlopen\n", binding->user_binding->name);
36 | static void* dlopen_wrapper(const char* filename, int flags) {
37 |    typeof(&dlopen_wrapper) orig_dlopen = gotcha_get_wrappee(orig_dlopen_handle);
39 |    debug_printf(1, "User called dlopen(%s, 0x%x)\n", filename, (unsigned int) flags);
40 |    handle = orig_dlopen(filename,flags);
42 |    debug_printf(2, "Searching new dlopened libraries for previously-not-found exports\n");
45 |    debug_printf(2, "Updating GOT entries for new dlopened libraries\n");
72 |   {"dlopen", dlopen_wrapper, &orig_dlopen_handle},
{% endraw %}

```
### external/gotcha/src/gotcha.c

```c

{% raw %}
317 |            debug_printf(2, "Stashing %s in notfound_binding table to re-lookup on dlopens\n",
{% endraw %}

```
### external/gotcha/test/dlopen/test_dlopen.c

```c

{% raw %}
59 |    result = gotcha_wrap(funcs, 2, "dlopen_test");
65 |    libnum = dlopen(LIB_NAME, RTLD_NOW);
67 |       fprintf(stderr, "ERROR: Test failed to dlopen libnum.so\n");
{% endraw %}

```
### external/gotcha/test/multi_agent_dlopen/dlsym.c

```c

{% raw %}
16 | typedef void * dlopen_mode_fcn_t(const char *, int);
19 | dlopen_mode_fcn_t __libc_dlopen_mode;
26 |     void * dl_handle = __libc_dlopen_mode("libdl.so", RTLD_LAZY);
29 | 	err(1, "__libc_dlopen_mode failed");
{% endraw %}

```
### external/gotcha/test/multi_agent_dlopen/monitor.c

```c

{% raw %}
16 | typedef void *dlopen_fcn_t(const char *, int);
18 | gotcha_wrappee_handle_t reel_dlopen_handle;
21 | wrap_dlopen(const char *file, int flag)
23 |     typeof(&wrap_dlopen) reel_dlopen = gotcha_get_wrappee(reel_dlopen_handle);
24 |     fprintf(stderr, "ENTER WRAP: %p\n", reel_dlopen);
25 |     fprintf(stderr, "%s:  enter dlopen:  file = %s\n", MYNAME, file);
27 |     void *ans = reel_dlopen ? (reel_dlopen)(file, flag) : NULL;
29 |       fprintf(stderr, "Real dlopen not found\n");
31 |     fprintf(stderr, "%s:  exit  dlopen:  handle = %p\n", MYNAME, ans);
37 |   { "dlopen", wrap_dlopen, &reel_dlopen_handle}
40 |   reel_dlopen_handle = NULL;
42 |   typeof(&wrap_dlopen) reel_dlopen = gotcha_get_wrappee(reel_dlopen_handle);
43 |   fprintf(stderr, "IMMEDIATE WRITE: %p\n", reel_dlopen);
{% endraw %}

```
### external/gotcha/test/multi_agent_dlopen/main.c

```c

{% raw %}
23 |     void *handle = dlopen("libm.so", RTLD_NOW);
25 | 	err(1, "dlopen failed");
{% endraw %}

```
### external/caliper/ext/gotcha/src/gotcha_dl.h

```c

{% raw %}
10 | extern gotcha_wrappee_handle_t orig_dlopen_handle;
{% endraw %}

```
### external/caliper/ext/gotcha/src/gotcha_dl.c

```c

{% raw %}
9 | gotcha_wrappee_handle_t orig_dlopen_handle;
17 |    debug_printf(3, "Trying to re-bind %s from tool %s after dlopen\n",
28 |       debug_printf(3, "Still could not prepare binding %s after dlopen\n", binding->user_binding->name);
36 | static void* dlopen_wrapper(const char* filename, int flags) {
37 |    typeof(&dlopen_wrapper) orig_dlopen = gotcha_get_wrappee(orig_dlopen_handle);
39 |    debug_printf(1, "User called dlopen(%s, 0x%x)\n", filename, (unsigned int) flags);
40 |    handle = orig_dlopen(filename,flags);
42 |    debug_printf(2, "Searching new dlopened libraries for previously-not-found exports\n");
45 |    debug_printf(2, "Updating GOT entries for new dlopened libraries\n");
68 |   {"dlopen", dlopen_wrapper, &orig_dlopen_handle},
{% endraw %}

```
### external/caliper/ext/gotcha/src/gotcha.c

```c

{% raw %}
317 |            debug_printf(2, "Stashing %s in notfound_binding table to re-lookup on dlopens\n",
{% endraw %}

```