---
name: "cpuinfo"
layout: package
next_package: util-linux-uuid
previous_package: pkg-config
languages: ['cpp']
---
## master
4 / 547 files match

 - [src/arm/linux/init.c](#srcarmlinuxinitc)
 - [src/arm/linux/hwcap.c](#srcarmlinuxhwcapc)
 - [tools/auxv-dump.c](#toolsauxv-dumpc)
 - [tools/gpu-dump.c](#toolsgpu-dumpc)

### src/arm/linux/init.c

```cpp

{% raw %}
242 | 			 * 1. dlopen libc.so, and try to find getauxval
{% endraw %}

```
### src/arm/linux/hwcap.c

```cpp

{% raw %}
55 | 			libc = dlopen("libc.so", RTLD_LAZY);
{% endraw %}

```
### tools/auxv-dump.c

```cpp

{% raw %}
13 | 	void* libc = dlopen("libc.so", RTLD_NOW);
{% endraw %}

```
### tools/gpu-dump.c

```cpp

{% raw %}
294 | 	libEGL = dlopen("libEGL.so", RTLD_LAZY | RTLD_LOCAL);
{% endraw %}

```