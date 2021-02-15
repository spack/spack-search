---
name: "meson"
layout: package
next_package: plumed
previous_package: aomp
languages: ['cpp', 'python']
---
## 0.56.0
11 / 3471 files match

 - [mesonbuild/build.py](#mesonbuildbuildpy)
 - [test cases/common/152 shared module resolving symbol in executable/prog.c](#test casescommon152 shared module resolving symbol in executableprogc)
 - [test cases/common/121 shared module/prog.c](#test casescommon121 shared moduleprogc)
 - [test cases/common/121 shared module/module.c](#test casescommon121 shared modulemodulec)
 - [test cases/common/121 shared module/meson.build](#test casescommon121 shared modulemesonbuild)
 - [test cases/cmake/21 shared module/prog.c](#test casescmake21 shared moduleprogc)
 - [test cases/cmake/21 shared module/subprojects/cmMod/module/module.c](#test casescmake21 shared modulesubprojectscmmodmodulemodulec)
 - [tools/ac_converter.py](#toolsac_converterpy)
 - [docs/markdown/Reference-manual.md](#docsmarkdownreference-manualmd)
 - [docs/markdown/IDE-integration.md](#docsmarkdownide-integrationmd)
 - [docs/markdown/Release-notes-for-0.37.0.md](#docsmarkdownrelease-notes-for-0370md)

### mesonbuild/build.py

```python

{% raw %}
2018 | # A shared library that is meant to be used with dlopen rather than linking
{% endraw %}

```
### test cases/common/152 shared module resolving symbol in executable/prog.c

```cpp

{% raw %}
37 |   void *h = dlopen(argv[1], RTLD_NOW);
{% endraw %}

```
### test cases/common/121 shared module/prog.c

```cpp

{% raw %}
73 |     dl = dlopen(argv[1], RTLD_LAZY);
{% endraw %}

```
### test cases/common/121 shared module/module.c

```cpp

{% raw %}
87 |  * dlopens it. We need to make sure that this works, i.e. that we do
{% endraw %}

```
### test cases/common/121 shared module/meson.build

```

{% raw %}
24 | # with dlopen. Any symbols are resolved dynamically
{% endraw %}

```
### test cases/cmake/21 shared module/prog.c

```cpp

{% raw %}
78 |     dl = dlopen(argv[1], RTLD_LAZY);
{% endraw %}

```
### test cases/cmake/21 shared module/subprojects/cmMod/module/module.c

```cpp

{% raw %}
87 |  * dlopens it. We need to make sure that this works, i.e. that we do
{% endraw %}

```
### tools/ac_converter.py

```python

{% raw %}
203 |      'HAVE_DLOPEN': ('dlopen', 'dlfcn.h'),
{% endraw %}

```
### docs/markdown/Reference-manual.md

```

{% raw %}
1539 | This is useful for building modules that will be `dlopen()`ed and
1558 | `dlopen()` and link with a library.
{% endraw %}

```
### docs/markdown/IDE-integration.md

```

{% raw %}
111 | | `shared module`  | A shared library that is meant to be used with dlopen rather than linking into something else |
{% endraw %}

```
### docs/markdown/Release-notes-for-0.37.0.md

```

{% raw %}
31 | The new `shared_module` function allows the creation of shared modules, that is, extension modules such as plugins that are meant to be used solely with `dlopen` rather than linking them to targets.
{% endraw %}

```