---
name: "dotconf"
layout: package
next_package: py-ipython
previous_package: rrdtool
languages: ['cpp']
---
## 1.3
3 / 42 files match

 - [configure.ac](#configureac)
 - [examples/duplicates/duplicate.c](#examplesduplicatesduplicatec)
 - [examples/modules/module.c](#examplesmodulesmodulec)

### configure.ac

```

{% raw %}
7 | LT_INIT([dlopen])
{% endraw %}

```
### examples/duplicates/duplicate.c

```cpp

{% raw %}
9 | #include <dlfcn.h>		/* dlopen(), dlerror(), dlclose() */
217 | 				    dlopen(filename, RTLD_LAZY);
{% endraw %}

```
### examples/modules/module.c

```cpp

{% raw %}
7 | #include <dlfcn.h>		/* for dlopen(), dlerror(), dlclose() */
108 | 		handles[i] = dlopen(filename, RTLD_LAZY);
{% endraw %}

```