---
name: "rt-tests"
layout: package
next_package: rtags
previous_package: rsyslog
languages: ['c']
---
## 1.2
1 / 46 files match, 1 filtered matches.

 - [src/lib/rt-get_cpu.c](#srclibrt-get_cpuc)

### src/lib/rt-get_cpu.c

```c

{% raw %}
10 | 
11 | int get_cpu_setup(void)
12 | {
13 | 	void *handle = dlopen("linux-vdso.so.1", RTLD_LAZY);
14 | 	get_cpu_vdsop = NULL;
15 | 	if (handle) {
{% endraw %}

```