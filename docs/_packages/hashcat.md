---
name: "hashcat"
layout: package
next_package: hdf5
previous_package: haproxy
languages: ['c']
---
## 5.0.0
4 / 1181 files match, 4 filtered matches.

 - [src/opencl.c](#srcopenclc)
 - [src/dynloader.c](#srcdynloaderc)
 - [src/hwmon.c](#srchwmonc)
 - [include/dynloader.h](#includedynloaderh)

### src/opencl.c

```c

{% raw %}
486 |   ocl->lib = hc_dlopen ("OpenCL");
488 |   ocl->lib = hc_dlopen ("/System/Library/Frameworks/OpenCL.framework/OpenCL", RTLD_NOW);
490 |   ocl->lib = hc_dlopen ("opencl.dll", RTLD_NOW);
492 |   if (ocl->lib == NULL) ocl->lib = hc_dlopen ("cygOpenCL-1.dll", RTLD_NOW);
494 |   ocl->lib = hc_dlopen ("libOpenCL.so", RTLD_NOW);
496 |   if (ocl->lib == NULL) ocl->lib = hc_dlopen ("libOpenCL.so.1", RTLD_NOW);
{% endraw %}

```
### src/dynloader.c

```c

{% raw %}
10 | HMODULE hc_dlopen (LPCSTR lpLibFileName)
27 | void *hc_dlopen (const char *fileName, int flag)
29 |   return dlopen (fileName, flag);
{% endraw %}

```
### src/hwmon.c

```c

{% raw %}
413 |   nvml->lib = hc_dlopen ("nvml.dll");
451 |     nvml->lib = hc_dlopen (Buffer);
458 |   nvml->lib = hc_dlopen("nvml.dll", RTLD_NOW);
498 |     nvml->lib = hc_dlopen (nvml_cygpath, RTLD_NOW);
503 |   nvml->lib = hc_dlopen ("libnvidia-ml.so", RTLD_NOW);
507 |     nvml->lib = hc_dlopen ("libnvidia-ml.so.1", RTLD_NOW);
793 |   nvapi->lib = hc_dlopen ("nvapi64.dll");
795 |   nvapi->lib = hc_dlopen ("nvapi.dll");
803 |   nvapi->lib = hc_dlopen ("nvapi64.dll", RTLD_NOW);
805 |   nvapi->lib = hc_dlopen ("nvapi.dll", RTLD_NOW);
809 |   nvapi->lib = hc_dlopen ("nvapi.so", RTLD_NOW); // uhm yes, but .. yeah
1022 |   adl->lib = hc_dlopen ("atiadlxx.dll");
1026 |     adl->lib = hc_dlopen ("atiadlxy.dll");
1029 |   adl->lib = hc_dlopen ("atiadlxx.dll", RTLD_NOW);
1033 |     adl->lib = hc_dlopen ("atiadlxy.dll", RTLD_NOW);
1036 |   adl->lib = hc_dlopen ("libatiadlxx.so", RTLD_NOW);
{% endraw %}

```
### include/dynloader.h

```c

{% raw %}
20 | HMODULE hc_dlopen  (LPCSTR lpLibFileName);
24 | void *hc_dlopen  (const char *fileName, int flag);
{% endraw %}

```