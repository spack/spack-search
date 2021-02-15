---
name: "papi"
layout: package
next_package: cvs
previous_package: tinker
languages: ['cpp']
---
## 5.4.3
11 / 1681 files match

 - [ChangeLogP520.txt](#changelogp520txt)
 - [src/threads.c](#srcthreadsc)
 - [src/configure.in](#srcconfigurein)
 - [src/ctests/shlib.c](#srcctestsshlibc)
 - [src/components/vmware/vmware.c](#srccomponentsvmwarevmwarec)
 - [src/components/nvml/linux-nvml.c](#srccomponentsnvmllinux-nvmlc)
 - [src/components/libmsr/linux-libmsr.c](#srccomponentslibmsrlinux-libmsrc)
 - [src/components/host_micpower/linux-host_micpower.c](#srccomponentshost_micpowerlinux-host_micpowerc)
 - [src/components/cuda/linux-cuda.c](#srccomponentscudalinux-cudac)
 - [src/components/cuda/tests/cuda_ld_preload_example.c](#srccomponentscudatestscuda_ld_preload_examplec)
 - [src/components/infiniband_umad/linux-infiniband_umad.c](#srccomponentsinfiniband_umadlinux-infiniband_umadc)

### ChangeLogP520.txt

```

{% raw %}
44 |   src/components/nvml/linux-nvml.c...: Components: Use the cuda dlopen fix all
45 |   cases.  See 4cb76a9b for details, the short version is if you call dlopen
331 |   the dlopen. The test ctests/shlib fails as a reult of this. > > -Will >
570 |   this patch file to remove an unneeded variable in the dlopen code to resolve
630 |   src/components/nvml/configure.in...: nvml: Apply Gary Mohr's dlopen patch. 
631 |   Move the nvml component over to using the dlopen and weak linking
890 |   dlopen/dlsym for symbols  Apply Gary Mohr's patch to switch the infiniband
{% endraw %}

```
### src/threads.c

```cpp

{% raw %}
61 | 	handle = dlopen( NULL, RTLD_LAZY );
63 | 		PAPIERROR( "Error from dlopen(NULL, RTLD_LAZY): %d %s", errno,
{% endraw %}

```
### src/configure.in

```

{% raw %}
155 | AC_MSG_CHECKING([for dlopen and dlerror symbols in base system])
157 | 	[void *p = dlopen ("", 0); char *c = dlerror();],
164 | 	AC_MSG_CHECKING([for dlopen and dlerror symbols in -ldl])
168 | 		[void *p = dlopen ("", 0); char *c = dlerror();],
175 | 		AC_MSG_ERROR([cannot find dlopen and dlerror symbols neither in the base system libraries nor in -ldl])
{% endraw %}

```
### src/ctests/shlib.c

```cpp

{% raw %}
97 | 		handle = dlopen( _libname, RTLD_NOW );
99 | 			printf( "dlopen: %s\n", dlerror(  ) );
102 | 			test_fail( __FILE__, __LINE__, "dlopen", 1 );
{% endraw %}

```
### src/components/vmware/vmware.c

```cpp

{% raw %}
220 | 	dlHandle = dlopen(filename, RTLD_NOW);
223 | 	   fprintf(stderr, "dlopen of %s failed: \'%s\'\n", filename, 
227 | 	   dlHandle = dlopen(filename, RTLD_NOW);
230 | 	      fprintf(stderr, "dlopen of %s failed: \'%s\'\n", filename, 
234 | 	      dlHandle = dlopen(filename, RTLD_NOW);
237 | 	         fprintf(stderr, "dlopen of %s failed: \'%s\'\n", filename, 
{% endraw %}

```
### src/components/nvml/linux-nvml.c

```cpp

{% raw %}
51 |  *  These function pointers will be resolved with dlopen/dlsym calls at         *
112 | // file handles used to access cuda libraries with dlopen
1006 | 	dl1 = dlopen("libcuda.so", RTLD_NOW | RTLD_GLOBAL);
1019 | 	dl2 = dlopen("libcudart.so", RTLD_NOW | RTLD_GLOBAL);
1044 | 	dl3 = dlopen("libnvidia-ml.so", RTLD_NOW | RTLD_GLOBAL);
{% endraw %}

```
### src/components/libmsr/linux-libmsr.c

```cpp

{% raw %}
141 |     dllib1 = dlopen("libmsr.so", RTLD_NOW | RTLD_GLOBAL);
{% endraw %}

```
### src/components/host_micpower/linux-host_micpower.c

```cpp

{% raw %}
124 | 	scif_access = dlopen("libscif.so", RTLD_NOW | RTLD_GLOBAL);
132 |     mic_access = dlopen("libMicAccessSDK.so", RTLD_NOW | RTLD_GLOBAL);
{% endraw %}

```
### src/components/cuda/linux-cuda.c

```cpp

{% raw %}
72 | // file handles used to access cuda libraries with dlopen
107 |  *  These function pointers will be resolved with dlopen/dlsym calls at        *
193 |     dl1 = dlopen( "libcuda.so", RTLD_NOW | RTLD_GLOBAL );
210 |     dl2 = dlopen( "libcudart.so", RTLD_NOW | RTLD_GLOBAL );
219 |     dl3 = dlopen( "libcupti.so", RTLD_NOW | RTLD_GLOBAL );
{% endraw %}

```
### src/components/cuda/tests/cuda_ld_preload_example.c

```cpp

{% raw %}
45 |         dl1 = dlopen( "libpapi.so", RTLD_NOW | RTLD_GLOBAL );
{% endraw %}

```
### src/components/infiniband_umad/linux-infiniband_umad.c

```cpp

{% raw %}
44 |  *  These function pointers will be resolved with dlopen/dlsym calls at component    *
66 | // file handles used to access Infiniband libraries with dlopen
614 | 	dl1 = dlopen("libibumad.so", RTLD_NOW | RTLD_GLOBAL);
640 | 	dl2 = dlopen("libibmad.so", RTLD_NOW | RTLD_GLOBAL);
{% endraw %}

```