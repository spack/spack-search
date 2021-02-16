---
name: "qnnpack"
layout: package
next_package: g2o
previous_package: libtiff
languages: ['c']
---
## master
4 / 1357 files match, 3 filtered matches.

 - [deps/cpuinfo/src/arm/linux/hwcap.c](#depscpuinfosrcarmlinuxhwcapc)
 - [deps/cpuinfo/tools/auxv-dump.c](#depscpuinfotoolsauxv-dumpc)
 - [deps/cpuinfo/tools/gpu-dump.c](#depscpuinfotoolsgpu-dumpc)

### deps/cpuinfo/src/arm/linux/hwcap.c

```c

{% raw %}
55 | 			libc = dlopen("libc.so", RTLD_LAZY);
{% endraw %}

```
### deps/cpuinfo/tools/auxv-dump.c

```c

{% raw %}
13 | 	void* libc = dlopen("libc.so", RTLD_NOW);
{% endraw %}

```
### deps/cpuinfo/tools/gpu-dump.c

```c

{% raw %}
294 | 	libEGL = dlopen("libEGL.so", RTLD_LAZY | RTLD_LOCAL);
{% endraw %}

```