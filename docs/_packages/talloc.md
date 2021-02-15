---
name: "talloc"
layout: package
next_package: libarchive
previous_package: attr
languages: ['cpp', 'python']
---
## 2.1.9
6 / 246 files match

 - [talloc.h](#talloch)
 - [talloc_guide.txt](#talloc_guidetxt)
 - [third_party/waf/wafadmin/Tools/libtool.py](#third_partywafwafadmintoolslibtoolpy)
 - [lib/replace/replace.h](#libreplacereplaceh)
 - [lib/replace/dlfcn.c](#libreplacedlfcnc)
 - [lib/replace/test/testsuite.c](#libreplacetesttestsuitec)

### talloc.h

```cpp

{% raw %}
1038 |  * dlopen and unloaded with dlclose. talloc_autofree_context()
1040 |  * this fine, but for example FreeBSD does not deal well with dlopen()
{% endraw %}

```
### talloc_guide.txt

```

{% raw %}
82 | with dlopen() and unloaded with dlclose(), as talloc_autofree_context()
84 | this fine, but for example FreeBSD does not deal well with dlopen()
{% endraw %}

```
### third_party/waf/wafadmin/Tools/libtool.py

```python

{% raw %}
46 | 	fu("dlopen=''\ndlpreopen=''\n")
123 | 		# The name that we can dlopen(3).
139 | 		# Files to dlopen/dlpreopen
140 | 		self.dlopen = None
188 | dlopen = "%(dlopen)s"
{% endraw %}

```
### lib/replace/replace.h

```cpp

{% raw %}
412 | #ifndef HAVE_DLOPEN
413 | #define dlopen rep_dlopen
414 | #ifdef DLOPEN_TAKES_UNSIGNED_FLAGS
415 | void *rep_dlopen(const char *name, unsigned int flags);
417 | void *rep_dlopen(const char *name, int flags);
{% endraw %}

```
### lib/replace/dlfcn.c

```cpp

{% raw %}
30 | #ifndef HAVE_DLOPEN
31 | #ifdef DLOPEN_TAKES_UNSIGNED_FLAGS
32 | void *rep_dlopen(const char *name, unsigned int flags)
34 | void *rep_dlopen(const char *name, int flags)
{% endraw %}

```
### lib/replace/test/testsuite.c

```cpp

{% raw %}
408 | static int test_dlopen(void)
410 | 	/* FIXME: test dlopen, dlsym, dlclose, dlerror */
1125 | 	ret &= test_dlopen();
{% endraw %}

```