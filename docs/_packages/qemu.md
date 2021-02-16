---
name: "qemu"
layout: package
next_package: qt
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
15 | 	handle = dlopen("./libkconfig.so", RTLD_LAZY);
17 | 		handle = dlopen("./tools/kconfig/libkconfig.so", RTLD_LAZY);
{% endraw %}

```
### roms/openbios/arch/unix/plugins.c

```c

{% raw %}
126 | 	handle = dlopen(path, RTLD_LAZY | RTLD_GLOBAL);
{% endraw %}

```
### roms/openbios/arch/unix/plugins/loader.c

```c

{% raw %}
119 | 	handle = dlopen(path, RTLD_LAZY | RTLD_GLOBAL);
{% endraw %}

```