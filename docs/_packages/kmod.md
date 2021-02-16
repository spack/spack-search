---
name: "kmod"
layout: package
next_package: krb5
previous_package: kitty
languages: ['c']
---
## 25
3 / 367 files match, 3 filtered matches.

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