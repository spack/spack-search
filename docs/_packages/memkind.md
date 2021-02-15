---
name: "memkind"
layout: package
next_package: mount-point-attributes
previous_package: gosam-contrib
languages: ['cpp']
---
## 1.9.0
7 / 482 files match

 - [src/tbb_wrapper.c](#srctbb_wrapperc)
 - [copying_headers/MANIFEST.freeBSD](#copying_headersmanifestfreebsd)
 - [test/dlopen_test.cpp](#testdlopen_testcpp)
 - [test/load_tbbmalloc_symbols.c](#testload_tbbmalloc_symbolsc)
 - [test/Makefile.mk](#testmakefilemk)
 - [jemalloc/INSTALL.md](#jemallocinstallmd)
 - [jemalloc/src/jemalloc.c](#jemallocsrcjemallocc)

### src/tbb_wrapper.c

```cpp

{% raw %}
54 |     tbb_handle = dlopen(so_name, RTLD_LAZY);
{% endraw %}

```
### copying_headers/MANIFEST.freeBSD

```

{% raw %}
116 | test/dlopen_test.cpp
{% endraw %}

```
### test/dlopen_test.cpp

```

{% raw %}
29 | class DlopenTest: public :: testing::Test
32 |     DlopenTest()
39 |         handle = dlopen(path, RTLD_LAZY);
47 |     ~DlopenTest()
83 | TEST_F(DlopenTest, test_TC_MEMKIND_DEFAULT_4194305_bytes)
88 | TEST_F(DlopenTest, test_TC_MEMKIND_HBW_4194305_bytes)
93 | TEST_F(DlopenTest, test_TC_MEMKIND_HBW_HUGETLB_4194305_bytes)
99 | TEST_F(DlopenTest, test_TC_MEMKIND_HBW_PREFERRED_4194305_bytes)
104 | TEST_F(DlopenTest, test_TC_MEMKIND_HBW_INTERLEAVE_4194305_bytes)
{% endraw %}

```
### test/load_tbbmalloc_symbols.c

```cpp

{% raw %}
29 |     void *tbb_handle = dlopen(so_name, RTLD_LAZY);
{% endraw %}

```
### test/Makefile.mk

```

{% raw %}
79 |                          test/dlopen_test.cpp \
{% endraw %}

```
### jemalloc/INSTALL.md

```

{% raw %}
271 |     jemalloc to be dynamically loaded after program startup (e.g. using dlopen).
{% endraw %}

```
### jemalloc/src/jemalloc.c

```cpp

{% raw %}
2367 |  * glibc provides the RTLD_DEEPBIND flag for dlopen which can make it possible
{% endraw %}

```