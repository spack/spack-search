---
name: "meson"
layout: package
next_package: mivisionx
previous_package: mesa-glu
languages: ['python', 'c']
---
## 0.56.0
11 / 3471 files match, 4 filtered matches.

 - [test cases/common/152 shared module resolving symbol in executable/prog.c](#test casescommon152 shared module resolving symbol in executableprogc)
 - [test cases/common/121 shared module/prog.c](#test casescommon121 shared moduleprogc)
 - [test cases/cmake/21 shared module/prog.c](#test casescmake21 shared moduleprogc)
 - [tools/ac_converter.py](#toolsac_converterpy)

### test cases/common/152 shared module resolving symbol in executable/prog.c

```c

{% raw %}
34 | #ifdef _WIN32
35 |   HMODULE h = LoadLibraryA(argv[1]);
36 | #else
37 |   void *h = dlopen(argv[1], RTLD_NOW);
38 | #endif
39 |   assert(h != NULL);
{% endraw %}

```
### test cases/common/121 shared module/prog.c

```c

{% raw %}
70 |     if(argc==0) {};
71 | 
72 |     dlerror();
73 |     dl = dlopen(argv[1], RTLD_LAZY);
74 |     error = dlerror();
75 |     if(error) {
{% endraw %}

```
### test cases/cmake/21 shared module/prog.c

```c

{% raw %}
75 |     if(argc==0) {};
76 | 
77 |     dlerror();
78 |     dl = dlopen(argv[1], RTLD_LAZY);
79 |     error = dlerror();
80 |     if(error) {
{% endraw %}

```
### tools/ac_converter.py

```python

{% raw %}
200 |      'HAVE_CONFSTR': ('confstr', 'time.h'),
201 |      'HAVE_CTERMID': ('ctermid', 'stdio.h'),
202 |      'HAVE_DIRFD': ('dirfd', 'dirent.h'),
203 |      'HAVE_DLOPEN': ('dlopen', 'dlfcn.h'),
204 |      'HAVE_DUP2': ('dup2', 'unistd.h'),
205 |      'HAVE_DUP3': ('dup3', 'unistd.h'),
{% endraw %}

```