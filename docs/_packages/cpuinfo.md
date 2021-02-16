---
name: "cpuinfo"
layout: package
next_package: util-linux-uuid
previous_package: pkg-config
languages: ['c']
---
## master
4 / 547 files match, 3 filtered matches.

 - [src/arm/linux/hwcap.c](#srcarmlinuxhwcapc)
 - [tools/auxv-dump.c](#toolsauxv-dumpc)
 - [tools/gpu-dump.c](#toolsgpu-dumpc)

### src/arm/linux/hwcap.c

```c

{% raw %}
55 | 			libc = dlopen("libc.so", RTLD_LAZY);
{% endraw %}

```
### tools/auxv-dump.c

```c

{% raw %}
13 | 	void* libc = dlopen("libc.so", RTLD_NOW);
{% endraw %}

```
### tools/gpu-dump.c

```c

{% raw %}
294 | 	libEGL = dlopen("libEGL.so", RTLD_LAZY | RTLD_LOCAL);
{% endraw %}

```