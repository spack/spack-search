---
name: "qemu"
layout: package
next_package: qnnpack
previous_package: q-e-sirius
languages: ['c']
---
## 1.4.0
4 / 5228 files match, 3 filtered matches.

 - [roms/seabios/tools/kconfig/kconfig_load.c](#romsseabiostoolskconfigkconfig_loadc)
 - [roms/openbios/arch/unix/plugins.c](#romsopenbiosarchunixpluginsc)
 - [roms/openbios/arch/unix/plugins/loader.c](#romsopenbiosarchunixpluginsloaderc)

### roms/seabios/tools/kconfig/kconfig_load.c

```c

{% raw %}
12 | 	void *handle;
13 | 	char *error;
14 | 
15 | 	handle = dlopen("./libkconfig.so", RTLD_LAZY);
16 | 	if (!handle) {
17 | 		handle = dlopen("./tools/kconfig/libkconfig.so", RTLD_LAZY);
18 | 		if (!handle) {
19 | 			fprintf(stderr, "%s\n", dlerror());
{% endraw %}

```
### roms/openbios/arch/unix/plugins.c

```c

{% raw %}
123 | 	printf("Opening plugin %s\n", path);
124 | #endif
125 | 
126 | 	handle = dlopen(path, RTLD_LAZY | RTLD_GLOBAL);
127 | 	if (!handle) {
128 | 		error = dlerror();
{% endraw %}

```
### roms/openbios/arch/unix/plugins/loader.c

```c

{% raw %}
116 | 	printf("Opening plugin %s\n", path);
117 | #endif
118 | 
119 | 	handle = dlopen(path, RTLD_LAZY | RTLD_GLOBAL);
120 | 	if (!handle) {
121 | 		error = dlerror();
{% endraw %}

```