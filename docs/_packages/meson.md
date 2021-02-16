---
name: "meson"
layout: package
next_package: plumed
previous_package: aomp
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
37 |   void *h = dlopen(argv[1], RTLD_NOW);
{% endraw %}

```
### test cases/common/121 shared module/prog.c

```c

{% raw %}
73 |     dl = dlopen(argv[1], RTLD_LAZY);
{% endraw %}

```
### test cases/cmake/21 shared module/prog.c

```c

{% raw %}
78 |     dl = dlopen(argv[1], RTLD_LAZY);
{% endraw %}

```
### tools/ac_converter.py

```python

{% raw %}
203 |      'HAVE_DLOPEN': ('dlopen', 'dlfcn.h'),
{% endraw %}

```