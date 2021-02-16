---
name: "papi"
layout: package
next_package: cvs
previous_package: tinker
languages: ['c']
---
## 5.4.3
11 / 1681 files match, 9 filtered matches.

 - [src/threads.c](#srcthreadsc)
 - [src/ctests/shlib.c](#srcctestsshlibc)
 - [src/components/vmware/vmware.c](#srccomponentsvmwarevmwarec)
 - [src/components/nvml/linux-nvml.c](#srccomponentsnvmllinux-nvmlc)
 - [src/components/libmsr/linux-libmsr.c](#srccomponentslibmsrlinux-libmsrc)
 - [src/components/host_micpower/linux-host_micpower.c](#srccomponentshost_micpowerlinux-host_micpowerc)
 - [src/components/cuda/linux-cuda.c](#srccomponentscudalinux-cudac)
 - [src/components/cuda/tests/cuda_ld_preload_example.c](#srccomponentscudatestscuda_ld_preload_examplec)
 - [src/components/infiniband_umad/linux-infiniband_umad.c](#srccomponentsinfiniband_umadlinux-infiniband_umadc)

### src/threads.c

```c

{% raw %}
61 | 	handle = dlopen( NULL, RTLD_LAZY );
63 | 		PAPIERROR( "Error from dlopen(NULL, RTLD_LAZY): %d %s", errno,
{% endraw %}

```
### src/ctests/shlib.c

```c

{% raw %}
97 | 		handle = dlopen( _libname, RTLD_NOW );
99 | 			printf( "dlopen: %s\n", dlerror(  ) );
102 | 			test_fail( __FILE__, __LINE__, "dlopen", 1 );
{% endraw %}

```
### src/components/vmware/vmware.c

```c

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

```c

{% raw %}
1006 | 	dl1 = dlopen("libcuda.so", RTLD_NOW | RTLD_GLOBAL);
1019 | 	dl2 = dlopen("libcudart.so", RTLD_NOW | RTLD_GLOBAL);
1044 | 	dl3 = dlopen("libnvidia-ml.so", RTLD_NOW | RTLD_GLOBAL);
{% endraw %}

```
### src/components/libmsr/linux-libmsr.c

```c

{% raw %}
141 |     dllib1 = dlopen("libmsr.so", RTLD_NOW | RTLD_GLOBAL);
{% endraw %}

```
### src/components/host_micpower/linux-host_micpower.c

```c

{% raw %}
124 | 	scif_access = dlopen("libscif.so", RTLD_NOW | RTLD_GLOBAL);
132 |     mic_access = dlopen("libMicAccessSDK.so", RTLD_NOW | RTLD_GLOBAL);
{% endraw %}

```
### src/components/cuda/linux-cuda.c

```c

{% raw %}
193 |     dl1 = dlopen( "libcuda.so", RTLD_NOW | RTLD_GLOBAL );
210 |     dl2 = dlopen( "libcudart.so", RTLD_NOW | RTLD_GLOBAL );
219 |     dl3 = dlopen( "libcupti.so", RTLD_NOW | RTLD_GLOBAL );
{% endraw %}

```
### src/components/cuda/tests/cuda_ld_preload_example.c

```c

{% raw %}
45 |         dl1 = dlopen( "libpapi.so", RTLD_NOW | RTLD_GLOBAL );
{% endraw %}

```
### src/components/infiniband_umad/linux-infiniband_umad.c

```c

{% raw %}
614 | 	dl1 = dlopen("libibumad.so", RTLD_NOW | RTLD_GLOBAL);
640 | 	dl2 = dlopen("libibmad.so", RTLD_NOW | RTLD_GLOBAL);
{% endraw %}

```