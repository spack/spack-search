---
name: "qnnpack"
layout: package
next_package: g2o
previous_package: libtiff
languages: ['cpp']
---
## master
4 / 1357 files match

 - [deps/cpuinfo/src/arm/linux/init.c](#depscpuinfosrcarmlinuxinitc)
 - [deps/cpuinfo/src/arm/linux/hwcap.c](#depscpuinfosrcarmlinuxhwcapc)
 - [deps/cpuinfo/tools/auxv-dump.c](#depscpuinfotoolsauxv-dumpc)
 - [deps/cpuinfo/tools/gpu-dump.c](#depscpuinfotoolsgpu-dumpc)

### deps/cpuinfo/src/arm/linux/init.c

```cpp

{% raw %}
242 | 			 * 1. dlopen libc.so, and try to find getauxval
{% endraw %}

```
### deps/cpuinfo/src/arm/linux/hwcap.c

```cpp

{% raw %}
55 | 			libc = dlopen("libc.so", RTLD_LAZY);
{% endraw %}

```
### deps/cpuinfo/tools/auxv-dump.c

```cpp

{% raw %}
13 | 	void* libc = dlopen("libc.so", RTLD_NOW);
{% endraw %}

```
### deps/cpuinfo/tools/gpu-dump.c

```cpp

{% raw %}
294 | 	libEGL = dlopen("libEGL.so", RTLD_LAZY | RTLD_LOCAL);
{% endraw %}

```