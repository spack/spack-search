---
name: "pmdk"
layout: package
next_package: sst-macro
previous_package: texstudio
languages: ['python', 'cpp', 'bash']
---
## 1.7
12 / 4145 files match

 - [src/common/dlsym.h](#srccommondlsymh)
 - [src/common/set.c](#srccommonsetc)
 - [src/common/os.h](#srccommonosh)
 - [src/libvmmalloc/libvmmalloc.c](#srclibvmmalloclibvmmallocc)
 - [src/test/ld.supp](#srctestldsupp)
 - [src/test/memcheck-dlopen.supp](#srctestmemcheck-dlopensupp)
 - [src/test/vmmalloc_init/vmmalloc_init.c](#srctestvmmalloc_initvmmalloc_initc)
 - [src/test/unittest/unittest.sh](#srctestunittestunittestsh)
 - [src/test/unittest/valgrind.py](#srctestunittestvalgrindpy)
 - [src/jemalloc/src/jemalloc.c](#srcjemallocsrcjemallocc)
 - [doc/librpmem/librpmem.7.md](#doclibrpmemlibrpmem7md)
 - [doc/generated/librpmem.7](#docgeneratedlibrpmem7)

### src/common/dlsym.h

```cpp

{% raw %}
46 |  * util_dlopen -- calls real dlopen()
49 | util_dlopen(const char *filename)
53 | 	return dlopen(filename, RTLD_NOW);
90 |  * util_dlopen -- empty function
93 | util_dlopen(const char *filename)
{% endraw %}

```
### src/common/set.c

```cpp

{% raw %}
231 | 	Rpmem_handle_remote = util_dlopen(LIBRARY_REMOTE);
232 | 	if (util_dl_check_error(Rpmem_handle_remote, "dlopen")) {
{% endraw %}

```
### src/common/os.h

```cpp

{% raw %}
67 | /* dlopen() */
{% endraw %}

```
### src/libvmmalloc/libvmmalloc.c

```cpp

{% raw %}
51 |  *    malloc(3) functions in case the application uses dlopen with
354 |  * Interpose malloc hooks in glibc.  Even if the application uses dlopen
{% endraw %}

```
### src/test/ld.supp

```

{% raw %}
33 |    <Leak in dlopen, pmem/issues#858>
{% endraw %}

```
### src/test/memcheck-dlopen.supp

```

{% raw %}
1 |    dlopen suppression
14 |    <dlopen suppression, pmem/issues#1098>
18 |    fun:dlopen@@GLIBC*
{% endraw %}

```
### src/test/vmmalloc_init/vmmalloc_init.c

```cpp

{% raw %}
59 | 			handle = dlopen("./libtest.so",
64 | 			handle = dlopen("./libtest.so", RTLD_LAZY);
71 | 			UT_OUT("dlopen: %s", dlerror());
{% endraw %}

```
### src/test/unittest/unittest.sh

```bash

{% raw %}
835 | 		export VALGRIND_OPTS="$VALGRIND_OPTS --suppressions=../memcheck-dlopen.supp"
{% endraw %}

```
### src/test/unittest/valgrind.py

```python

{% raw %}
131 |             self.add_suppression('memcheck-dlopen.supp')
{% endraw %}

```
### src/jemalloc/src/jemalloc.c

```cpp

{% raw %}
1432 |  * glibc provides the RTLD_DEEPBIND flag for dlopen which can make it possible
{% endraw %}

```
### doc/librpmem/librpmem.7.md

```

{% raw %}
278 | prior to **dlopen**(3) if **librpmem** is being dynamically loaded).
486 | **rpmemd**(1), **ssh**(1), **fork**(2), **dlclose**(3), **dlopen**(3),
{% endraw %}

```
### doc/generated/librpmem.7

```

{% raw %}
274 | \f[B]dlopen\f[](3) if \f[B]librpmem\f[] is being dynamically loaded).
500 | \f[B]dlclose\f[](3), \f[B]dlopen\f[](3), \f[B]ibv_fork_init\f[](3),
{% endraw %}

```