---
name: "pmdk"
layout: package
next_package: sst-macro
previous_package: texstudio
languages: ['python', 'c']
---
## 1.7
12 / 4145 files match

 - [src/common/dlsym.h](#srccommondlsymh)
 - [src/common/set.c](#srccommonsetc)
 - [src/test/vmmalloc_init/vmmalloc_init.c](#srctestvmmalloc_initvmmalloc_initc)
 - [src/test/unittest/valgrind.py](#srctestunittestvalgrindpy)

### src/common/dlsym.h

```c

{% raw %}
49 | util_dlopen(const char *filename)
53 | 	return dlopen(filename, RTLD_NOW);
93 | util_dlopen(const char *filename)
{% endraw %}

```
### src/common/set.c

```c

{% raw %}
231 | 	Rpmem_handle_remote = util_dlopen(LIBRARY_REMOTE);
232 | 	if (util_dl_check_error(Rpmem_handle_remote, "dlopen")) {
{% endraw %}

```
### src/test/vmmalloc_init/vmmalloc_init.c

```c

{% raw %}
59 | 			handle = dlopen("./libtest.so",
64 | 			handle = dlopen("./libtest.so", RTLD_LAZY);
71 | 			UT_OUT("dlopen: %s", dlerror());
{% endraw %}

```
### src/test/unittest/valgrind.py

```python

{% raw %}
131 |             self.add_suppression('memcheck-dlopen.supp')
{% endraw %}

```