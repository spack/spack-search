---
name: "hashcat"
layout: package
next_package: hdf5
previous_package: guile
library_name: dlopen
matches: ['dlsym', 'dlopen']
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
483 |   memset (ocl, 0, sizeof (OCL_PTR));
484 | 
485 |   #if   defined (_WIN)
486 |   ocl->lib = hc_dlopen ("OpenCL");
487 |   #elif defined (__APPLE__)
488 |   ocl->lib = hc_dlopen ("/System/Library/Frameworks/OpenCL.framework/OpenCL", RTLD_NOW);
489 |   #elif defined (__CYGWIN__)
490 |   ocl->lib = hc_dlopen ("opencl.dll", RTLD_NOW);
491 | 
492 |   if (ocl->lib == NULL) ocl->lib = hc_dlopen ("cygOpenCL-1.dll", RTLD_NOW);
493 |   #else
494 |   ocl->lib = hc_dlopen ("libOpenCL.so", RTLD_NOW);
495 | 
496 |   if (ocl->lib == NULL) ocl->lib = hc_dlopen ("libOpenCL.so.1", RTLD_NOW);
497 |   #endif
498 | 
{% endraw %}

```
### src/dynloader.c

```c

{% raw %}
7 | 
8 | #ifdef _WIN
9 | 
10 | HMODULE hc_dlopen (LPCSTR lpLibFileName)
11 | {
12 |   return LoadLibraryA (lpLibFileName);
24 | 
25 | #else
26 | 
27 | void *hc_dlopen (const char *fileName, int flag)
28 | {
29 |   return dlopen (fileName, flag);
30 | }
31 | 
{% endraw %}

```
### src/hwmon.c

```c

{% raw %}
410 | 
411 |   #if defined (_WIN)
412 | 
413 |   nvml->lib = hc_dlopen ("nvml.dll");
414 | 
415 |   if (!nvml->lib)
448 | 
449 |     strcat (Buffer, "\\nvml.dll");
450 | 
451 |     nvml->lib = hc_dlopen (Buffer);
452 | 
453 |     hcfree (Buffer);
455 | 
456 |   #elif defined (__CYGWIN__)
457 | 
458 |   nvml->lib = hc_dlopen("nvml.dll", RTLD_NOW);
459 | 
460 |   if (!nvml->lib)
495 | 
496 |     strcat (nvml_cygpath, "/nvml.dll");
497 | 
498 |     nvml->lib = hc_dlopen (nvml_cygpath, RTLD_NOW);
499 |   }
500 | 
501 |   #elif defined (_POSIX)
502 | 
503 |   nvml->lib = hc_dlopen ("libnvidia-ml.so", RTLD_NOW);
504 | 
505 |   if (!nvml->lib)
506 |   {
507 |     nvml->lib = hc_dlopen ("libnvidia-ml.so.1", RTLD_NOW);
508 |   }
509 | 
790 |   #if defined (_WIN)
791 | 
792 |   #if defined (_WIN64)
793 |   nvapi->lib = hc_dlopen ("nvapi64.dll");
794 |   #else
795 |   nvapi->lib = hc_dlopen ("nvapi.dll");
796 |   #endif
797 | 
800 |   #if defined (__CYGWIN__)
801 | 
802 |   #if defined (__x86_x64__)
803 |   nvapi->lib = hc_dlopen ("nvapi64.dll", RTLD_NOW);
804 |   #else
805 |   nvapi->lib = hc_dlopen ("nvapi.dll", RTLD_NOW);
806 |   #endif
807 | 
808 |   #else
809 |   nvapi->lib = hc_dlopen ("nvapi.so", RTLD_NOW); // uhm yes, but .. yeah
810 |   #endif
811 | 
1019 |   memset (adl, 0, sizeof (ADL_PTR));
1020 | 
1021 |   #if defined (_WIN)
1022 |   adl->lib = hc_dlopen ("atiadlxx.dll");
1023 | 
1024 |   if (!adl->lib)
1025 |   {
1026 |     adl->lib = hc_dlopen ("atiadlxy.dll");
1027 |   }
1028 |   #elif defined (__CYGWIN__)
1029 |   adl->lib = hc_dlopen ("atiadlxx.dll", RTLD_NOW);
1030 | 
1031 |   if (!adl->lib)
1032 |   {
1033 |     adl->lib = hc_dlopen ("atiadlxy.dll", RTLD_NOW);
1034 |   }
1035 |   #elif defined (_POSIX)
1036 |   adl->lib = hc_dlopen ("libatiadlxx.so", RTLD_NOW);
1037 |   #endif
1038 | 
{% endraw %}

```
### include/dynloader.h

```c

{% raw %}
17 | #endif // _WIN
18 | 
19 | #ifdef _WIN
20 | HMODULE hc_dlopen  (LPCSTR lpLibFileName);
21 | BOOL    hc_dlclose (HMODULE hLibModule);
22 | FARPROC hc_dlsym   (HMODULE hModule, LPCSTR lpProcName);
23 | #else
24 | void *hc_dlopen  (const char *fileName, int flag);
25 | int   hc_dlclose (void *handle);
26 | void *hc_dlsym   (void *module, const char *symbol);
{% endraw %}

```