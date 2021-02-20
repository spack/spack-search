---
name: "fakexrandr"
layout: package
next_package: fenics
previous_package: fakechroot
languages: ['c']
---
## master
1 / 16 files match, 1 filtered matches.

 - [libXrandr.c](#libxrandrc)

### libXrandr.c

```c

{% raw %}
428 | 
429 | static void _init() __attribute__((constructor));
430 | static void _init() {
431 | 	void *xrandr_lib = dlopen(REAL_XRANDR_LIB, RTLD_LAZY | RTLD_GLOBAL);
432 | 
433 | 	/*
{% endraw %}

```