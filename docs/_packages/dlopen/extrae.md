---
name: "extrae"
layout: package
next_package: lvm2
previous_package: nix
library_name: dlopen
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 3.4.1
7 / 975 files match, 2 filtered matches.

 - [src/loader/extrae-loader.c](#srcloaderextrae-loaderc)
 - [src/tracer/wrappers/OPENCL/opencl_wrapper.c](#srctracerwrappersopenclopencl_wrapperc)

### src/loader/extrae-loader.c

```c

{% raw %}
202 |   }
203 | 
204 |   fprintf(stderr, "extrae-loader: Opening application binary '%s'... ", app);
205 |   handle = dlopen(app, RTLD_LAZY);
206 |   if (!handle)
207 |   {
{% endraw %}

```
### src/tracer/wrappers/OPENCL/opencl_wrapper.c

```c

{% raw %}
112 | #if defined(PIC)
113 | 
114 | #if defined(__APPLE__)
115 | 	void *lib = dlopen("/System/Libraries/Frameworks/OpenCL.framework/OpenCL", RTLD_NOW);
116 | #else
117 | 	void *lib = RTLD_NEXT;
{% endraw %}

```