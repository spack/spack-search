---
name: "xdm"
layout: package
next_package: xedit
previous_package: xapian-core
languages: ['c']
---
## 1.1.11
6 / 75 files match, 1 filtered matches.

 - [xdm/session.c](#xdmsessionc)

### xdm/session.c

```c

{% raw %}
340 |     LoadXloginResources (d);
341 | 
342 |     Debug ("ManageSession: loading greeter library %s\n", greeterLib);
343 |     greet_lib_handle = dlopen(greeterLib, RTLD_NOW);
344 |     if (greet_lib_handle != NULL)
345 | 	greet_user_proc = (GreetUserProc)dlsym(greet_lib_handle, "GreetUser");
{% endraw %}

```