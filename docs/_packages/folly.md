---
name: "folly"
layout: package
next_package: turbine
previous_package: libxext
languages: ['cpp']
---
## 2016.10.24.00
7 / 906 files match

 - [folly/VersionCheck.h](#follyversioncheckh)
 - [folly/configure.ac](#follyconfigureac)
 - [folly/ClockGettimeWrappers.cpp](#follyclockgettimewrapperscpp)
 - [folly/Malloc.h](#follymalloch)
 - [folly/detail/CacheLocality.cpp](#follydetailcachelocalitycpp)
 - [folly/test/ThreadLocalTest.cpp](#follytestthreadlocaltestcpp)
 - [folly/docs/Overview.md](#follydocsoverviewmd)

### folly/VersionCheck.h

```cpp

{% raw %}
41 |  * dlopen calls with RTLD_DEEPBIND), any symbols from libfoo1.so that are
{% endraw %}

```
### folly/configure.ac

```

{% raw %}
312 |         void *h = dlopen("linux-vdso.so.1", RTLD_LAZY | RTLD_LOCAL | RTLD_NOLOAD);
{% endraw %}

```
### folly/ClockGettimeWrappers.cpp

```

{% raw %}
56 |     m_handle = dlopen("linux-vdso.so.1", RTLD_LAZY | RTLD_LOCAL | RTLD_NOLOAD);
{% endraw %}

```
### folly/Malloc.h

```cpp

{% raw %}
143 |   // Checking for rallocx != NULL is not sufficient; we may be in a dlopen()ed
{% endraw %}

```
### folly/detail/CacheLocality.cpp

```

{% raw %}
213 |   void* h = dlopen("linux-vdso.so.1", RTLD_LAZY | RTLD_LOCAL | RTLD_NOLOAD);
{% endraw %}

```
### folly/test/ThreadLocalTest.cpp

```

{% raw %}
578 | // Elide this test when using any sanitizer. Otherwise, the dlopen'ed code
587 |   auto handle = dlopen(lib.string().c_str(), RTLD_LAZY);
{% endraw %}

```
### folly/docs/Overview.md

```

{% raw %}
193 | correctly upon program creation, program end and sometimes `dlopen` and `fork`.
{% endraw %}

```