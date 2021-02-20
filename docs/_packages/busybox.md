---
name: "busybox"
layout: package
next_package: cairo
previous_package: brltty
languages: ['c']
---
## 1.30.0
1 / 2335 files match, 1 filtered matches.

 - [scripts/kconfig/kconfig_load.c](#scriptskconfigkconfig_loadc)

### scripts/kconfig/kconfig_load.c

```c

{% raw %}
12 | 	void *handle;
13 | 	char *error;
14 | 
15 | 	handle = dlopen("./libkconfig.so", RTLD_LAZY);
16 | 	if (!handle) {
17 | 		handle = dlopen("./scripts/kconfig/libkconfig.so", RTLD_LAZY);
18 | 		if (!handle) {
19 | 			fprintf(stderr, "%s\n", dlerror());
{% endraw %}

```