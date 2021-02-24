---
name: "vim"
layout: package
next_package: guile
previous_package: autogen
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 7.4.2367
10 / 2670 files match, 1 filtered matches.

 - [src/os_unix.c](#srcos_unixc)

### src/os_unix.c

```c

{% raw %}
6830 | 	    if (argstring != NULL)
6831 | 	    {
6832 | # if defined(USE_DLOPEN)
6833 | 		ProcAdd = (STRPROCSTR)dlsym(hinstLib, (const char *)funcname);
6834 | 		dlerr = (char *)dlerror();
6835 | # else
6852 | 	    else
6853 | 	    {
6854 | # if defined(USE_DLOPEN)
6855 | 		ProcAddI = (INTPROCSTR)dlsym(hinstLib, (const char *)funcname);
6856 | 		dlerr = (char *)dlerror();
6857 | # else
{% endraw %}

```