---
name: "kmod"
layout: package
next_package: krb5
previous_package: kitty
library_name: dlopen
matches: ['dlsym', 'dlopen']
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
36 | #ifdef RTLD_NEXT
37 | 		nextlib = RTLD_NEXT;
38 | #else
39 | 		nextlib = dlopen("libc.so.6", RTLD_LAZY);
40 | #endif
41 | 		nextlib_uname = dlsym(nextlib, "uname");
{% endraw %}

```
### testsuite/path.c

```c

{% raw %}
86 | #ifdef RTLD_NEXT
87 | 		nextlib = RTLD_NEXT;
88 | #else
89 | 		nextlib = dlopen("libc.so.6", RTLD_LAZY);
90 | #endif
91 | 	}
{% endraw %}

```
### testsuite/init_module.c

```c

{% raw %}
362 | #ifdef RTLD_NEXT
363 | 			nextlib = RTLD_NEXT;
364 | #else
365 | 			nextlib = dlopen("libc.so.6", RTLD_LAZY);
366 | #endif
367 | 			nextlib_syscall = dlsym(nextlib, "syscall");
{% endraw %}

```