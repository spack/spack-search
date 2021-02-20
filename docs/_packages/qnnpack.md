---
name: "qnnpack"
layout: package
next_package: qt
previous_package: qemu
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
52 | 			getauxval_function_t getauxval = NULL;
53 | 
54 | 			dlerror();
55 | 			libc = dlopen("libc.so", RTLD_LAZY);
56 | 			if (libc == NULL) {
57 | 				cpuinfo_log_warning("failed to load libc.so: %s", dlerror());
{% endraw %}

```
### deps/cpuinfo/tools/auxv-dump.c

```c

{% raw %}
10 | typedef unsigned long (*getauxval_function_t)(unsigned long);
11 | 
12 | int main(int argc, char** argv) {
13 | 	void* libc = dlopen("libc.so", RTLD_NOW);
14 | 	if (libc == NULL) {
15 | 		fprintf(stderr, "Error: failed to load libc.so: %s\n", dlerror());
{% endraw %}

```
### deps/cpuinfo/tools/gpu-dump.c

```c

{% raw %}
291 | 	EGLBoolean egl_make_current_status = EGL_FALSE;
292 | 	EGLBoolean egl_status;
293 | 
294 | 	libEGL = dlopen("libEGL.so", RTLD_LAZY | RTLD_LOCAL);
295 | 
296 | 	display = eglGetDisplay(EGL_DEFAULT_DISPLAY);
{% endraw %}

```