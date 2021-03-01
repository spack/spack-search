---
name: "talloc"
layout: package
next_package: tau
previous_package: swipl
library_name: dlopen
matches: ['dlsym', 'dlopen']
languages: ['python', 'c']
---
## 2.1.9
6 / 246 files match, 4 filtered matches.

 - [third_party/waf/wafadmin/Tools/libtool.py](#third_partywafwafadmintoolslibtoolpy)
 - [lib/replace/replace.h](#libreplacereplaceh)
 - [lib/replace/dlfcn.c](#libreplacedlfcnc)
 - [lib/replace/test/testsuite.c](#libreplacetesttestsuitec)

### third_party/waf/wafadmin/Tools/libtool.py

```python

{% raw %}
43 | 	fu("dependency_libs='%s'\n" % vars)
44 | 	fu("current=0\n")
45 | 	fu("age=0\nrevision=0\ninstalled=yes\nshouldnotlink=no\n")
46 | 	fu("dlopen=''\ndlpreopen=''\n")
47 | 	fu("libdir='%s/lib'\n" % env['PREFIX'])
48 | 	dest.close()
137 | 		# Should we warn about portability when linking against -modules?
138 | 		self.shouldnotlink = None
139 | 		# Files to dlopen/dlpreopen
140 | 		self.dlopen = None
141 | 		self.dlpreopen = None
142 | 		# Directory that this library needs to be installed in:
185 | version = %(current)s.%(age)s.%(revision)s
186 | installed = "%(installed)s"
187 | shouldnotlink = "%(shouldnotlink)s"
188 | dlopen = "%(dlopen)s"
189 | dlpreopen = "%(dlpreopen)s"
190 | libdir = "%(libdir)s"''' % self.__dict__
{% endraw %}

```
### lib/replace/replace.h

```c

{% raw %}
412 | #ifndef HAVE_DLOPEN
413 | #define dlopen rep_dlopen
414 | #ifdef DLOPEN_TAKES_UNSIGNED_FLAGS
415 | void *rep_dlopen(const char *name, unsigned int flags);
416 | #else
417 | void *rep_dlopen(const char *name, int flags);
418 | #endif
419 | #endif
{% endraw %}

```
### lib/replace/dlfcn.c

```c

{% raw %}
29 | 
30 | #ifndef HAVE_DLOPEN
31 | #ifdef DLOPEN_TAKES_UNSIGNED_FLAGS
32 | void *rep_dlopen(const char *name, unsigned int flags)
33 | #else
34 | void *rep_dlopen(const char *name, int flags)
35 | #endif
36 | {
{% endraw %}

```
### lib/replace/test/testsuite.c

```c

{% raw %}
405 | 	return true;
406 | }
407 | 
408 | static int test_dlopen(void)
409 | {
410 | 	/* FIXME: test dlopen, dlsym, dlclose, dlerror */
1122 | 	ret &= test_readdir();
1123 | 	ret &= test_telldir();
1124 | 	ret &= test_seekdir();
1125 | 	ret &= test_dlopen();
1126 | 	ret &= test_chroot();
1127 | 	ret &= test_bzero();
{% endraw %}

```