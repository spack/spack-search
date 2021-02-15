---
name: "rt-tests"
layout: package
next_package: ruby
previous_package: xrx
languages: ['cpp']
---
## 1.2
1 / 46 files match

 - [src/lib/rt-get_cpu.c](#srclibrt-get_cpuc)

### src/lib/rt-get_cpu.c

```cpp

{% raw %}
13 | 	void *handle = dlopen("linux-vdso.so.1", RTLD_LAZY);
{% endraw %}

```