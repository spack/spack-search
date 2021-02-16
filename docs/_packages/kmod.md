---
name: "kmod"
layout: package
next_package: guile
previous_package: libxkbfile
languages: ['c']
---
## 25
3 / 367 files match

 - [testsuite/uname.c](#testsuiteunamec)
 - [testsuite/path.c](#testsuitepathc)
 - [testsuite/init_module.c](#testsuiteinit_modulec)

### testsuite/uname.c

```c

{% raw %}
39 | 		nextlib = dlopen("libc.so.6", RTLD_LAZY);
{% endraw %}

```
### testsuite/path.c

```c

{% raw %}
89 | 		nextlib = dlopen("libc.so.6", RTLD_LAZY);
{% endraw %}

```
### testsuite/init_module.c

```c

{% raw %}
365 | 			nextlib = dlopen("libc.so.6", RTLD_LAZY);
{% endraw %}

```