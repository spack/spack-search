---
name: "xdm"
layout: package
next_package: gmt
previous_package: libepoxy
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 1.1.11
3 / 75 files match, 1 filtered matches.

 - [xdm/session.c](#xdmsessionc)

### xdm/session.c

```c

{% raw %}
342 |     Debug ("ManageSession: loading greeter library %s\n", greeterLib);
343 |     greet_lib_handle = dlopen(greeterLib, RTLD_NOW);
344 |     if (greet_lib_handle != NULL)
345 | 	greet_user_proc = (GreetUserProc)dlsym(greet_lib_handle, "GreetUser");
346 |     if (greet_user_proc == NULL) {
347 | 	LogError ("%s while loading %s\n", dlerror(), greeterLib);
{% endraw %}

```