---
name: "talloc"
layout: package
next_package: taskflow
previous_package: systemtap
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
46 | 	fu("dlopen=''\ndlpreopen=''\n")
140 | 		self.dlopen = None
188 | dlopen = "%(dlopen)s"
{% endraw %}

```
### lib/replace/replace.h

```c

{% raw %}
415 | void *rep_dlopen(const char *name, unsigned int flags);
417 | void *rep_dlopen(const char *name, int flags);
{% endraw %}

```
### lib/replace/dlfcn.c

```c

{% raw %}
32 | void *rep_dlopen(const char *name, unsigned int flags)
34 | void *rep_dlopen(const char *name, int flags)
{% endraw %}

```
### lib/replace/test/testsuite.c

```c

{% raw %}
408 | static int test_dlopen(void)
1125 | 	ret &= test_dlopen();
{% endraw %}

```