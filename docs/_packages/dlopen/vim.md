---
name: "vim"
layout: package
next_package: guile
previous_package: autogen
library_name: dlopen
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 8.1.0001
11 / 2766 files match, 1 filtered matches.

 - [src/os_unix.c](#srcos_unixc)

### src/os_unix.c

```c

{% raw %}
7287 |     /* First clear any error, it's not cleared by the dlopen() call. */
7288 |     (void)dlerror();
7289 | 
7290 |     hinstLib = dlopen((char *)libname, RTLD_LAZY
7291 | #  ifdef RTLD_LOCAL
7292 | 	    | RTLD_LOCAL
{% endraw %}

```