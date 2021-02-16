---
name: "extrae"
layout: package
next_package: q-e-sirius
previous_package: ffmpeg
languages: ['c']
---
## 3.4.1
7 / 975 files match, 2 filtered matches.

 - [src/loader/extrae-loader.c](#srcloaderextrae-loaderc)
 - [src/tracer/wrappers/OPENCL/opencl_wrapper.c](#srctracerwrappersopenclopencl_wrapperc)

### src/loader/extrae-loader.c

```c

{% raw %}
205 |   handle = dlopen(app, RTLD_LAZY);
{% endraw %}

```
### src/tracer/wrappers/OPENCL/opencl_wrapper.c

```c

{% raw %}
115 | 	void *lib = dlopen("/System/Libraries/Frameworks/OpenCL.framework/OpenCL", RTLD_NOW);
{% endraw %}

```