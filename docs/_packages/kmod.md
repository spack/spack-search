---
name: "kmod"
layout: package
next_package: guile
previous_package: libxkbfile
languages: ['cpp']
---
## 25
3 / 367 files match

 - [testsuite/uname.c](#testsuiteunamec)
 - [testsuite/path.c](#testsuitepathc)
 - [testsuite/init_module.c](#testsuiteinit_modulec)

### testsuite/uname.c

```cpp

{% raw %}
39 | 		nextlib = dlopen("libc.so.6", RTLD_LAZY);
{% endraw %}

```
### testsuite/path.c

```cpp

{% raw %}
89 | 		nextlib = dlopen("libc.so.6", RTLD_LAZY);
{% endraw %}

```
### testsuite/init_module.c

```cpp

{% raw %}
365 | 			nextlib = dlopen("libc.so.6", RTLD_LAZY);
{% endraw %}

```