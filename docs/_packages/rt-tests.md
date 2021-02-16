---
name: "rt-tests"
layout: package
next_package: ruby
previous_package: xrx
languages: ['c']
---
## 1.2
1 / 46 files match

 - [src/lib/rt-get_cpu.c](#srclibrt-get_cpuc)

### src/lib/rt-get_cpu.c

```c

{% raw %}
13 | 	void *handle = dlopen("linux-vdso.so.1", RTLD_LAZY);
{% endraw %}

```