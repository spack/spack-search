---
name: "cpuinfo"
layout: package
next_package: iproute2
previous_package: php
library_name: dlopen
matches: ['dlsym', 'dlopen']
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
52 | 			getauxval_function_t getauxval = NULL;
53 | 
54 | 			dlerror();
55 | 			libc = dlopen("libc.so", RTLD_LAZY);
56 | 			if (libc == NULL) {
57 | 				cpuinfo_log_warning("failed to load libc.so: %s", dlerror());
{% endraw %}

```
### tools/auxv-dump.c

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
### tools/gpu-dump.c

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