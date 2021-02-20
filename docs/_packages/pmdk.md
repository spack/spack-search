---
name: "pmdk"
layout: package
next_package: pmix
previous_package: plumed
languages: ['python', 'c']
---
## 1.7
12 / 4145 files match, 4 filtered matches.

 - [src/common/dlsym.h](#srccommondlsymh)
 - [src/common/set.c](#srccommonsetc)
 - [src/test/vmmalloc_init/vmmalloc_init.c](#srctestvmmalloc_initvmmalloc_initc)
 - [src/test/unittest/valgrind.py](#srctestunittestvalgrindpy)

### src/common/dlsym.h

```c

{% raw %}
46 |  * util_dlopen -- calls real dlopen()
47 |  */
48 | static inline void *
49 | util_dlopen(const char *filename)
50 | {
51 | 	LOG(3, "filename %s", filename);
52 | 
53 | 	return dlopen(filename, RTLD_NOW);
54 | }
55 | 
90 |  * util_dlopen -- empty function
91 |  */
92 | static inline void *
93 | util_dlopen(const char *filename)
94 | {
95 | 	errno = ENOSYS;
{% endraw %}

```
### src/common/set.c

```c

{% raw %}
228 | 	if (Rpmem_handle_remote)
229 | 		goto end;
230 | 
231 | 	Rpmem_handle_remote = util_dlopen(LIBRARY_REMOTE);
232 | 	if (util_dl_check_error(Rpmem_handle_remote, "dlopen")) {
233 | 		ERR("the pool set requires a remote replica, "
234 | 		    "but the '%s' library cannot be loaded",
{% endraw %}

```
### src/test/vmmalloc_init/vmmalloc_init.c

```c

{% raw %}
56 | 		switch (argv[1][0]) {
57 | 		case 'd':
58 | 			UT_OUT("deep binding");
59 | 			handle = dlopen("./libtest.so",
60 | 				RTLD_NOW | RTLD_LOCAL | RTLD_DEEPBIND);
61 | 			break;
62 | 		case 'l':
63 | 			UT_OUT("lazy binding");
64 | 			handle = dlopen("./libtest.so", RTLD_LAZY);
65 | 			break;
66 | 		default:
68 | 		}
69 | 
70 | 		if (handle == NULL)
71 | 			UT_OUT("dlopen: %s", dlerror());
72 | 		UT_ASSERTne(handle, NULL);
73 | 
{% endraw %}

```
### src/test/unittest/valgrind.py

```python

{% raw %}
128 |         if tool == MEMCHECK:
129 |             self.add_suppression('memcheck-libunwind.supp')
130 |             self.add_suppression('memcheck-ndctl.supp')
131 |             self.add_suppression('memcheck-dlopen.supp')
132 |             if memcheck_check_leaks:
133 |                 self.add_opt('--leak-check=full')
{% endraw %}

```