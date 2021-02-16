---
name: "dotconf"
layout: package
next_package: py-ipython
previous_package: rrdtool
languages: ['c']
---
## 1.3
3 / 42 files match

 - [examples/duplicates/duplicate.c](#examplesduplicatesduplicatec)
 - [examples/modules/module.c](#examplesmodulesmodulec)

### examples/duplicates/duplicate.c

```c

{% raw %}
217 | 				    dlopen(filename, RTLD_LAZY);
{% endraw %}

```
### examples/modules/module.c

```c

{% raw %}
108 | 		handles[i] = dlopen(filename, RTLD_LAZY);
{% endraw %}

```