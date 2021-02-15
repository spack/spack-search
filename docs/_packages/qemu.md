---
name: "qemu"
layout: package
next_package: swig
previous_package: openssl
languages: ['cpp']
---
## 1.4.0
4 / 5228 files match

 - [roms/seabios/tools/kconfig/kconfig_load.c](#romsseabiostoolskconfigkconfig_loadc)
 - [roms/openbios/arch/unix/plugins.c](#romsopenbiosarchunixpluginsc)
 - [roms/openbios/arch/unix/plugins/loader.c](#romsopenbiosarchunixpluginsloaderc)
 - [roms/openbios/Documentation/kernel/Changelog.stepan](#romsopenbiosdocumentationkernelchangelogstepan)

### roms/seabios/tools/kconfig/kconfig_load.c

```cpp

{% raw %}
15 | 	handle = dlopen("./libkconfig.so", RTLD_LAZY);
17 | 		handle = dlopen("./tools/kconfig/libkconfig.so", RTLD_LAZY);
{% endraw %}

```
### roms/openbios/arch/unix/plugins.c

```cpp

{% raw %}
126 | 	handle = dlopen(path, RTLD_LAZY | RTLD_GLOBAL);
{% endraw %}

```
### roms/openbios/arch/unix/plugins/loader.c

```cpp

{% raw %}
119 | 	handle = dlopen(path, RTLD_LAZY | RTLD_GLOBAL);
{% endraw %}

```
### roms/openbios/Documentation/kernel/Changelog.stepan

```

{% raw %}
240 |  - check whether dlopen() needs libdl.
{% endraw %}

```