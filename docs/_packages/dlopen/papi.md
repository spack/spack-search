---
name: "papi"
layout: package
next_package: qt
previous_package: parsec
library_name: dlopen
matches: ['dlsym', 'dlopen']
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
58 | 	char *error_ptc = NULL, *error_ptk = NULL;
59 | 	void *symbol_ptc = NULL, *symbol_ptk = NULL, *handle = NULL;
60 | 
61 | 	handle = dlopen( NULL, RTLD_LAZY );
62 | 	if ( handle == NULL ) {
63 | 		PAPIERROR( "Error from dlopen(NULL, RTLD_LAZY): %d %s", errno,
64 | 				   dlerror(  ) );
65 | 		return ( PAPI_ESYS );
{% endraw %}

```
### src/ctests/shlib.c

```c

{% raw %}
94 | 
95 | 		int oldcount;
96 | 
97 | 		handle = dlopen( _libname, RTLD_NOW );
98 | 		if ( !handle ) {
99 | 			printf( "dlopen: %s\n", dlerror(  ) );
100 | 			printf
101 | 				( "Did you forget to set the environmental variable LIBPATH (in AIX) or LD_LIBRARY_PATH (in linux) ?\n" );
102 | 			test_fail( __FILE__, __LINE__, "dlopen", 1 );
103 | 		}
104 | 
{% endraw %}

```
### src/components/vmware/vmware.c

```c

{% raw %}
217 | 	char filename[BUFSIZ];
218 | 
219 | 	sprintf(filename,"%s","libvmGuestLib.so");
220 | 	dlHandle = dlopen(filename, RTLD_NOW);
221 | 	if (!dlHandle) {
222 | 	   dlErrStr = dlerror();
223 | 	   fprintf(stderr, "dlopen of %s failed: \'%s\'\n", filename, 
224 | 		   dlErrStr);
225 | 
226 | 	   sprintf(filename,"%s/lib/lib64/libvmGuestLib.so",VMWARE_INCDIR);
227 | 	   dlHandle = dlopen(filename, RTLD_NOW);
228 | 	   if (!dlHandle) {
229 | 	      dlErrStr = dlerror();
230 | 	      fprintf(stderr, "dlopen of %s failed: \'%s\'\n", filename, 
231 | 		   dlErrStr);
232 | 
233 | 	      sprintf(filename,"%s/lib/lib32/libvmGuestLib.so",VMWARE_INCDIR);
234 | 	      dlHandle = dlopen(filename, RTLD_NOW);
235 | 	      if (!dlHandle) {
236 | 	         dlErrStr = dlerror();
237 | 	         fprintf(stderr, "dlopen of %s failed: \'%s\'\n", filename, 
238 | 		      dlErrStr);
239 | 		 return PAPI_ECMP;
{% endraw %}

```
### src/components/nvml/linux-nvml.c

```c

{% raw %}
1003 | 	}
1004 | 
1005 | 	/* Need to link in the cuda libraries, if not found disable the component */
1006 | 	dl1 = dlopen("libcuda.so", RTLD_NOW | RTLD_GLOBAL);
1007 | 	if (!dl1)
1008 | 	{
1016 | 		return ( PAPI_ENOSUPP );
1017 | 	}
1018 | 
1019 | 	dl2 = dlopen("libcudart.so", RTLD_NOW | RTLD_GLOBAL);
1020 | 	if (!dl2)
1021 | 	{
1041 | 		return ( PAPI_ENOSUPP );
1042 | 	}
1043 | 
1044 | 	dl3 = dlopen("libnvidia-ml.so", RTLD_NOW | RTLD_GLOBAL);
1045 | 	if (!dl3)
1046 | 	{
{% endraw %}

```
### src/components/libmsr/linux-libmsr.c

```c

{% raw %}
138 |         strncpy( _libmsr_vector.cmp_info.disabled_reason, "The libmsr component REQUIRES dynamic linking capabilities.", PAPI_MAX_STR_LEN);
139 |         return PAPI_ENOSUPP;
140 |     }
141 |     dllib1 = dlopen("libmsr.so", RTLD_NOW | RTLD_GLOBAL);
142 |     CHECK_DL_STATUS( !dllib1 , "Component library libmsr.so not found." );
143 |     init_msr_ptr = dlsym( dllib1, "init_msr" );
{% endraw %}

```
### src/components/host_micpower/linux-host_micpower.c

```c

{% raw %}
121 | 	}
122 | 
123 | 	  /* Need to link in the cuda libraries, if not found disable the component */
124 | 	scif_access = dlopen("libscif.so", RTLD_NOW | RTLD_GLOBAL);
125 |     if (NULL == scif_access)
126 |     {
129 |         return ( PAPI_ENOSUPP );
130 |     }
131 | 
132 |     mic_access = dlopen("libMicAccessSDK.so", RTLD_NOW | RTLD_GLOBAL);
133 |     if (NULL == mic_access)
134 |     {
{% endraw %}

```
### src/components/cuda/linux-cuda.c

```c

{% raw %}
190 |         return PAPI_ENOSUPP;
191 |     }
192 |     /* Need to link in the cuda libraries, if not found disable the component */
193 |     dl1 = dlopen( "libcuda.so", RTLD_NOW | RTLD_GLOBAL );
194 |     CHECK_DL_STATUS( !dl1 , "CUDA library libcuda.so not found." );
195 |     cuCtxGetCurrentPtr = dlsym( dl1, "cuCtxGetCurrent" );
207 |     cuCtxPushCurrentPtr = dlsym( dl1, "cuCtxPushCurrent" );
208 |     CHECK_DL_STATUS( dlerror()!=NULL, "CUDA function cuCtxPushCurrent not found." );
209 | 
210 |     dl2 = dlopen( "libcudart.so", RTLD_NOW | RTLD_GLOBAL );
211 |     CHECK_DL_STATUS( !dl2, "CUDA runtime library libcudart.so not found." );
212 |     cudaGetDevicePtr = dlsym( dl2, "cudaGetDevice" );
216 |     cudaFreePtr = dlsym( dl2, "cudaFree" );
217 |     CHECK_DL_STATUS( dlerror()!=NULL, "CUDART function cudaFree not found." );
218 | 
219 |     dl3 = dlopen( "libcupti.so", RTLD_NOW | RTLD_GLOBAL );
220 |     CHECK_DL_STATUS( !dl3, "CUDA runtime library libcupti.so not found." );
221 |     cuptiDeviceEnumEventDomainsPtr = dlsym( dl3, "cuptiDeviceEnumEventDomains" );
{% endraw %}

```
### src/components/cuda/tests/cuda_ld_preload_example.c

```c

{% raw %}
42 |     if ( onetime==0 ) {
43 |         onetime=1;
44 |         // Load the papi library dynamically and read the relevant functions
45 |         dl1 = dlopen( "libpapi.so", RTLD_NOW | RTLD_GLOBAL );
46 |         if ( dl1==NULL ) printf("Intercept cudaSetDevice: Cannot load libpapi.so\n");
47 |         PAPI_library_init_ptr = dlsym( dl1, "PAPI_library_init" );
{% endraw %}

```
### src/components/infiniband_umad/linux-infiniband_umad.c

```c

{% raw %}
611 | 	}
612 | 
613 | 	/* Need to link in the Infiniband libraries, if not found disable the component */
614 | 	dl1 = dlopen("libibumad.so", RTLD_NOW | RTLD_GLOBAL);
615 | 	if (!dl1)
616 | 	{
637 | 	}
638 | 
639 | 	/* Need to link in the Infiniband libraries, if not found disable the component */
640 | 	dl2 = dlopen("libibmad.so", RTLD_NOW | RTLD_GLOBAL);
641 | 	if (!dl2)
642 | 	{
{% endraw %}

```