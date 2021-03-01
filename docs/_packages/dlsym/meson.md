---
name: "meson"
layout: package
next_package: None
previous_package: None
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 0.56.0
5 / 3471 files match, 5 filtered matches.

 - [test cases/common/152 shared module resolving symbol in executable/prog.c](#test casescommon152 shared module resolving symbol in executableprogc)
 - [test cases/common/121 shared module/prog.c](#test casescommon121 shared moduleprogc)
 - [test cases/common/121 shared module/module.c](#test casescommon121 shared modulemodulec)
 - [test cases/cmake/21 shared module/prog.c](#test casescmake21 shared moduleprogc)
 - [test cases/cmake/21 shared module/subprojects/cmMod/module/module.c](#test casescmake21 shared modulesubprojectscmmodmodulemodulec)

### test cases/common/152 shared module resolving symbol in executable/prog.c

```c

{% raw %}
41 | #ifdef _WIN32
42 |   importedfunc = (fptr) GetProcAddress (h, "func");
43 | #else
44 |   importedfunc = (fptr) dlsym(h, "func");
45 | #endif
46 |   assert(importedfunc != NULL);
{% endraw %}

```
### test cases/common/121 shared module/prog.c

```c

{% raw %}
77 |         goto nodl;
78 |     }
79 | 
80 |     importedfunc = (fptr) dlsym(dl, "func");
81 |     if (importedfunc == NULL) {
82 |         printf ("Could not find 'func'\n");
{% endraw %}

```
### test cases/common/121 shared module/module.c

```c

{% raw %}
19 | #include <dlfcn.h>
20 | 
21 | fptr find_any_f (const char *name) {
22 |     return (fptr) dlsym(RTLD_DEFAULT, name);
23 | }
24 | #else /* _WIN32 */
{% endraw %}

```
### test cases/cmake/21 shared module/prog.c

```c

{% raw %}
82 |         goto nodl;
83 |     }
84 | 
85 |     importedfunc = (fptr) dlsym(dl, "func");
86 |     if (importedfunc == NULL) {
87 |         printf ("Could not find 'func'\n");
{% endraw %}

```
### test cases/cmake/21 shared module/subprojects/cmMod/module/module.c

```c

{% raw %}
19 | #include <dlfcn.h>
20 | 
21 | fptr find_any_f (const char *name) {
22 |     return (fptr) dlsym(RTLD_DEFAULT, name);
23 | }
24 | #else /* _WIN32 */
{% endraw %}

```