---
name: "kmod"
layout: package
next_package: krb5
previous_package: kitty
library_name: dlsym
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
38 | #else
39 | 		nextlib = dlopen("libc.so.6", RTLD_LAZY);
40 | #endif
41 | 		nextlib_uname = dlsym(nextlib, "uname");
42 | 	}
43 | 
{% endraw %}

```
### testsuite/path.c

```c

{% raw %}
90 | #endif
91 | 	}
92 | 
93 | 	fp = dlsym(nextlib, f);
94 | 	assert(fp);
95 | 
{% endraw %}

```
### testsuite/init_module.c

```c

{% raw %}
364 | #else
365 | 			nextlib = dlopen("libc.so.6", RTLD_LAZY);
366 | #endif
367 | 			nextlib_syscall = dlsym(nextlib, "syscall");
368 | 			if (nextlib_syscall == NULL) {
369 | 				fprintf(stderr, "FIXME FIXME FIXME: could not load syscall symbol: %s\n",
{% endraw %}

```