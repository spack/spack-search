---
name: "ruby"
layout: package
next_package: rust
previous_package: rsyslog
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 2.7.1
17 / 9819 files match, 6 filtered matches.

 - [mjit.c](#mjitc)
 - [addr2line.c](#addr2linec)
 - [mjit_worker.c](#mjit_workerc)
 - [dln.c](#dlnc)
 - [ext/-test-/popen_deadlock/infinite_loop_dlsym.c](#ext-test-popen_deadlockinfinite_loop_dlsymc)
 - [ext/fiddle/handle.c](#extfiddlehandlec)

### mjit.c

```c

{% raw %}
510 |         // `make install`. Don't use $MJIT_SEARCH_BUILD_DIR except for test-all.
511 | 
512 |         struct stat st;
513 |         const char *hdr = dlsym(RTLD_DEFAULT, "MJIT_HEADER");
514 |         if (!hdr) {
515 |             verbose(1, "No MJIT_HEADER");
{% endraw %}

```
### addr2line.c

```c

{% raw %}
1737 |                     Dl_info info;
1738 |                     void *s;
1739 |                     if (ELF_ST_TYPE(sym->st_info) != STT_FUNC || sym->st_size == 0) continue;
1740 |                     s = dlsym(handle, strtab + sym->st_name);
1741 |                     if (s && dladdr(s, &info)) {
1742 |                         obj->base_addr = dladdr_fbase;
{% endraw %}

```
### mjit_worker.c

```c

{% raw %}
893 |             char funcname[35]; // TODO: reconsider `35`
894 |             sprintf(funcname, "_mjit%d", cur->id);
895 | 
896 |             if ((func = dlsym(handle, funcname)) == NULL) {
897 |                 mjit_warning("skipping to reload '%s' from '%s': %s", funcname, so_file, dlerror());
898 |                 continue;
926 |         return (void *)NOT_ADDED_JIT_ISEQ_FUNC;
927 |     }
928 | 
929 |     func = dlsym(handle, funcname);
930 |     unit->handle = handle;
931 |     return func;
{% endraw %}

```
### dln.c

```c

{% raw %}
1250 | static bool
1251 | dln_incompatible_library_p(void *handle)
1252 | {
1253 |     void *ex = dlsym(handle, EXTERNAL_PREFIX"ruby_xmalloc");
1254 |     return ex && ex != ruby_xmalloc;
1255 | }
1359 | 	}
1360 | # endif
1361 | 
1362 | 	init_fct = (void(*)())(VALUE)dlsym(handle, buf);
1363 | 	if (init_fct == NULL) {
1364 | 	    const size_t errlen = strlen(error = dln_strerror()) + 1;
{% endraw %}

```
### ext/-test-/popen_deadlock/infinite_loop_dlsym.c

```c

{% raw %}
1 | #include "ruby/thread.h"
2 | #include <dlfcn.h>
3 | 
4 | struct data_for_loop_dlsym {
5 |     const char *name;
6 |     volatile int stop;
7 | };
8 | 
9 | static void*
10 | native_loop_dlsym(void *data)
11 | {
12 |     struct data_for_loop_dlsym *s = data;
13 | 
14 |     while (!(s->stop)) {
15 |         dlsym(RTLD_DEFAULT, s->name);
16 |     }
17 | 
19 | }
20 | 
21 | static void
22 | ubf_for_loop_dlsym(void *data)
23 | {
24 |     struct data_for_loop_dlsym *s = data;
25 | 
26 |     s->stop = 1;
29 | }
30 | 
31 | static VALUE
32 | loop_dlsym(VALUE self, VALUE name)
33 | {
34 |     struct data_for_loop_dlsym d;
35 | 
36 |     d.stop = 0;
37 |     d.name = StringValuePtr(name);
38 | 
39 |     rb_thread_call_without_gvl(native_loop_dlsym, &d,
40 |                                ubf_for_loop_dlsym, &d);
41 | 
42 |     return self;
43 | }
44 | 
45 | void
46 | Init_infinite_loop_dlsym(void)
47 | {
48 |     rb_define_method(rb_cThread, "__infinite_loop_dlsym__", loop_dlsym, 1);
49 | }
50 | 
{% endraw %}

```
### ext/fiddle/handle.c

```c

{% raw %}
321 | #ifdef HAVE_DLERROR
322 |     dlerror();
323 | #endif
324 |     func = (void (*)())(VALUE)dlsym(handle, name);
325 |     CHECK_DLERROR;
326 | #if defined(FUNC_STDCALL)
335 | 	    name_n = name_a;
336 | 	    name_a[len]   = 'A';
337 | 	    name_a[len+1] = '\0';
338 | 	    func = dlsym(handle, name_a);
339 | 	    CHECK_DLERROR;
340 | 	    if( func ) goto found;
347 | 	name_n[len++] = '@';
348 | 	for( i = 0; i < 256; i += 4 ){
349 | 	    sprintf(name_n + len, "%d", i);
350 | 	    func = dlsym(handle, name_n);
351 | 	    CHECK_DLERROR;
352 | 	    if( func ) break;
356 | 	name_n[len++] = '@';
357 | 	for( i = 0; i < 256; i += 4 ){
358 | 	    sprintf(name_n + len, "%d", i);
359 | 	    func = dlsym(handle, name_n);
360 | 	    CHECK_DLERROR;
361 | 	    if( func ) break;
{% endraw %}

```