---
name: "papi"
layout: package
next_package: qt
previous_package: parsec
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 5.4.3
12 / 1681 files match, 10 filtered matches.

 - [src/threads.c](#srcthreadsc)
 - [src/ctests/shlib.c](#srcctestsshlibc)
 - [src/components/vmware/vmware.c](#srccomponentsvmwarevmwarec)
 - [src/components/nvml/linux-nvml.c](#srccomponentsnvmllinux-nvmlc)
 - [src/components/appio/appio.c](#srccomponentsappioappioc)
 - [src/components/libmsr/linux-libmsr.c](#srccomponentslibmsrlinux-libmsrc)
 - [src/components/host_micpower/linux-host_micpower.c](#srccomponentshost_micpowerlinux-host_micpowerc)
 - [src/components/cuda/linux-cuda.c](#srccomponentscudalinux-cudac)
 - [src/components/cuda/tests/cuda_ld_preload_example.c](#srccomponentscudatestscuda_ld_preload_examplec)
 - [src/components/infiniband_umad/linux-infiniband_umad.c](#srccomponentsinfiniband_umadlinux-infiniband_umadc)

### src/threads.c

```c

{% raw %}
65 | 		return ( PAPI_ESYS );
66 | 	}
67 | 
68 | 	symbol_ptc = dlsym( handle, "pthread_self" );
69 | 	if ( symbol_ptc == NULL ) {
70 | 		error_ptc = dlerror(  );
71 | 		THRDBG( "dlsym(%p,pthread_self) returned NULL: %s\n",
72 | 				( error_ptc ? error_ptc : "No error, NULL symbol!" ) );
73 | 	}
74 | 
75 | 	symbol_ptk = dlsym( handle, "pthread_kill" );
76 | 	if ( symbol_ptk == NULL ) {
77 | 		error_ptk = dlerror(  );
78 | 		THRDBG( "dlsym(%p,pthread_kill) returned NULL: %s\n",
79 | 				( error_ptk ? error_ptk : "No error, NULL symbol!" ) );
80 | 	}
{% endraw %}

```
### src/ctests/shlib.c

```c

{% raw %}
102 | 			test_fail( __FILE__, __LINE__, "dlopen", 1 );
103 | 		}
104 | 
105 | 		setkey = dlsym( handle, "setkey" );
106 | 		encrypt = dlsym( handle, "encrypt" );
107 | 		if ( setkey == NULL || encrypt == NULL) {
108 | 			printf( "dlsym: %s\n", dlerror(  ) );
109 | 			test_fail( __FILE__, __LINE__, "dlsym", 1 );
110 | 		}
111 | 
{% endraw %}

```
### src/components/vmware/vmware.c

```c

{% raw %}
149 | 
150 | #define LOAD_ONE_FUNC(funcname)                                 \
151 | do {                                                            \
152 | funcname = dlsym(dlHandle, "VM" #funcname);                     \
153 | if ((dlErrStr = dlerror()) != NULL) {                           \
154 | fprintf(stderr, "Failed to load \'%s\': \'%s\'\n",              \
{% endraw %}

```
### src/components/nvml/linux-nvml.c

```c

{% raw %}
1009 | 		strncpy(_nvml_vector.cmp_info.disabled_reason, "CUDA library libcuda.so not found.",PAPI_MAX_STR_LEN);
1010 | 		return ( PAPI_ENOSUPP );
1011 | 	}
1012 | 	cuInitPtr = dlsym(dl1, "cuInit");
1013 | 	if (dlerror() != NULL)
1014 | 	{
1022 | 		strncpy(_nvml_vector.cmp_info.disabled_reason, "CUDA runtime library libcudart.so not found.",PAPI_MAX_STR_LEN);
1023 | 		return ( PAPI_ENOSUPP );
1024 | 	}
1025 | 	cudaGetDevicePtr = dlsym(dl2, "cudaGetDevice");
1026 | 	if (dlerror() != NULL)
1027 | 	{
1028 | 		strncpy(_nvml_vector.cmp_info.disabled_reason, "CUDART function cudaGetDevice not found.",PAPI_MAX_STR_LEN);
1029 | 		return ( PAPI_ENOSUPP );
1030 | 	}
1031 | 	cudaGetDeviceCountPtr = dlsym(dl2, "cudaGetDeviceCount");
1032 | 	if (dlerror() != NULL)
1033 | 	{
1034 | 		strncpy(_nvml_vector.cmp_info.disabled_reason, "CUDART function cudaGetDeviceCount not found.",PAPI_MAX_STR_LEN);
1035 | 		return ( PAPI_ENOSUPP );
1036 | 	}
1037 | 	cudaDeviceGetPCIBusIdPtr = dlsym(dl2, "cudaDeviceGetPCIBusId");
1038 | 	if (dlerror() != NULL)
1039 | 	{
1047 | 		strncpy(_nvml_vector.cmp_info.disabled_reason, "NVML runtime library libnvidia-ml.so not found.",PAPI_MAX_STR_LEN);
1048 | 		return ( PAPI_ENOSUPP );
1049 | 	}
1050 | 	nvmlDeviceGetClockInfoPtr = dlsym(dl3, "nvmlDeviceGetClockInfo");
1051 | 	if (dlerror() != NULL)
1052 | 	{
1053 | 		strncpy(_nvml_vector.cmp_info.disabled_reason, "NVML function nvmlDeviceGetClockInfo not found.",PAPI_MAX_STR_LEN);
1054 | 		return ( PAPI_ENOSUPP );
1055 | 	}
1056 | 	nvmlErrorStringPtr = dlsym(dl3, "nvmlErrorString");
1057 | 	if (dlerror() != NULL)
1058 | 	{
1059 | 		strncpy(_nvml_vector.cmp_info.disabled_reason, "NVML function nvmlErrorString not found.",PAPI_MAX_STR_LEN);
1060 | 		return ( PAPI_ENOSUPP );
1061 | 	}
1062 | 	nvmlDeviceGetDetailedEccErrorsPtr = dlsym(dl3, "nvmlDeviceGetDetailedEccErrors");
1063 | 	if (dlerror() != NULL)
1064 | 	{
1065 | 		strncpy(_nvml_vector.cmp_info.disabled_reason, "NVML function nvmlDeviceGetDetailedEccErrors not found.",PAPI_MAX_STR_LEN);
1066 | 		return ( PAPI_ENOSUPP );
1067 | 	}
1068 | 	nvmlDeviceGetFanSpeedPtr = dlsym(dl3, "nvmlDeviceGetFanSpeed");
1069 | 	if (dlerror() != NULL)
1070 | 	{
1071 | 		strncpy(_nvml_vector.cmp_info.disabled_reason, "NVML function nvmlDeviceGetFanSpeed not found.",PAPI_MAX_STR_LEN);
1072 | 		return ( PAPI_ENOSUPP );
1073 | 	}
1074 | 	nvmlDeviceGetMemoryInfoPtr = dlsym(dl3, "nvmlDeviceGetMemoryInfo");
1075 | 	if (dlerror() != NULL)
1076 | 	{
1077 | 		strncpy(_nvml_vector.cmp_info.disabled_reason, "NVML function nvmlDeviceGetMemoryInfo not found.",PAPI_MAX_STR_LEN);
1078 | 		return ( PAPI_ENOSUPP );
1079 | 	}
1080 | 	nvmlDeviceGetPerformanceStatePtr = dlsym(dl3, "nvmlDeviceGetPerformanceState");
1081 | 	if (dlerror() != NULL)
1082 | 	{
1083 | 		strncpy(_nvml_vector.cmp_info.disabled_reason, "NVML function nvmlDeviceGetPerformanceState not found.",PAPI_MAX_STR_LEN);
1084 | 		return ( PAPI_ENOSUPP );
1085 | 	}
1086 | 	nvmlDeviceGetPowerUsagePtr = dlsym(dl3, "nvmlDeviceGetPowerUsage");
1087 | 	if (dlerror() != NULL)
1088 | 	{
1089 | 		strncpy(_nvml_vector.cmp_info.disabled_reason, "NVML function nvmlDeviceGetPowerUsage not found.",PAPI_MAX_STR_LEN);
1090 | 		return ( PAPI_ENOSUPP );
1091 | 	}
1092 | 	nvmlDeviceGetTemperaturePtr = dlsym(dl3, "nvmlDeviceGetTemperature");
1093 | 	if (dlerror() != NULL)
1094 | 	{
1095 | 		strncpy(_nvml_vector.cmp_info.disabled_reason, "NVML function nvmlDeviceGetTemperature not found.",PAPI_MAX_STR_LEN);
1096 | 		return ( PAPI_ENOSUPP );
1097 | 	}
1098 | 	nvmlDeviceGetTotalEccErrorsPtr = dlsym(dl3, "nvmlDeviceGetTotalEccErrors");
1099 | 	if (dlerror() != NULL)
1100 | 	{
1101 | 		strncpy(_nvml_vector.cmp_info.disabled_reason, "NVML function nvmlDeviceGetTotalEccErrors not found.",PAPI_MAX_STR_LEN);
1102 | 		return ( PAPI_ENOSUPP );
1103 | 	}
1104 | 	nvmlDeviceGetUtilizationRatesPtr = dlsym(dl3, "nvmlDeviceGetUtilizationRates");
1105 | 	if (dlerror() != NULL)
1106 | 	{
1107 | 		strncpy(_nvml_vector.cmp_info.disabled_reason, "NVML function nvmlDeviceGetUtilizationRates not found.",PAPI_MAX_STR_LEN);
1108 | 		return ( PAPI_ENOSUPP );
1109 | 	}
1110 | 	nvmlDeviceGetHandleByIndexPtr = dlsym(dl3, "nvmlDeviceGetHandleByIndex");
1111 | 	if (dlerror() != NULL)
1112 | 	{
1113 | 		strncpy(_nvml_vector.cmp_info.disabled_reason, "NVML function nvmlDeviceGetHandleByIndex not found.",PAPI_MAX_STR_LEN);
1114 | 		return ( PAPI_ENOSUPP );
1115 | 	}
1116 | 	nvmlDeviceGetPciInfoPtr = dlsym(dl3, "nvmlDeviceGetPciInfo");
1117 | 	if (dlerror() != NULL)
1118 | 	{
1119 | 		strncpy(_nvml_vector.cmp_info.disabled_reason, "NVML function nvmlDeviceGetPciInfo not found.",PAPI_MAX_STR_LEN);
1120 | 		return ( PAPI_ENOSUPP );
1121 | 	}
1122 | 	nvmlDeviceGetNamePtr = dlsym(dl3, "nvmlDeviceGetName");
1123 | 	if (dlerror() != NULL)
1124 | 	{
1125 | 		strncpy(_nvml_vector.cmp_info.disabled_reason, "NVML function nvmlDeviceGetName not found.",PAPI_MAX_STR_LEN);
1126 | 		return ( PAPI_ENOSUPP );
1127 | 	}
1128 | 	nvmlDeviceGetInforomVersionPtr = dlsym(dl3, "nvmlDeviceGetInforomVersion");
1129 | 	if (dlerror() != NULL)
1130 | 	{
1131 | 		strncpy(_nvml_vector.cmp_info.disabled_reason, "NVML function nvmlDeviceGetInforomVersion not found.",PAPI_MAX_STR_LEN);
1132 | 		return ( PAPI_ENOSUPP );
1133 | 	}
1134 | 	nvmlDeviceGetEccModePtr = dlsym(dl3, "nvmlDeviceGetEccMode");
1135 | 	if (dlerror() != NULL)
1136 | 	{
1137 | 		strncpy(_nvml_vector.cmp_info.disabled_reason, "NVML function nvmlDeviceGetEccMode not found.",PAPI_MAX_STR_LEN);
1138 | 		return ( PAPI_ENOSUPP );
1139 | 	}
1140 | 	nvmlInitPtr = dlsym(dl3, "nvmlInit");
1141 | 	if (dlerror() != NULL)
1142 | 	{
1143 | 		strncpy(_nvml_vector.cmp_info.disabled_reason, "NVML function nvmlInit not found.",PAPI_MAX_STR_LEN);
1144 | 		return ( PAPI_ENOSUPP );
1145 | 	}
1146 | 	nvmlDeviceGetCountPtr = dlsym(dl3, "nvmlDeviceGetCount");
1147 | 	if (dlerror() != NULL)
1148 | 	{
1149 | 		strncpy(_nvml_vector.cmp_info.disabled_reason, "NVML function nvmlDeviceGetCount not found.",PAPI_MAX_STR_LEN);
1150 | 		return ( PAPI_ENOSUPP );
1151 | 	}
1152 | 	nvmlShutdownPtr = dlsym(dl3, "nvmlShutdown");
1153 | 	if (dlerror() != NULL)
1154 | 	{
{% endraw %}

```
### src/components/appio/appio.c

```c

{% raw %}
49 | 
50 | /*
51 | #pragma weak dlerror
52 | static void *_dlsym_fake(void *handle, const char* symbol) { (void) handle; (void) symbol; return NULL; }
53 | void *dlsym(void *handle, const char* symbol) __attribute__ ((weak, alias ("_dlsym_fake")));
54 | */
55 | 
348 | ssize_t recv(int sockfd, void *buf, size_t len, int flags) {
349 |   int retval;
350 |   SUBDBG("appio: intercepted recv(%d,%p,%lu,%d)\n", sockfd, buf, (unsigned long)len, flags);
351 |   if (!__recv) __recv  = dlsym(RTLD_NEXT, "recv");
352 |   if (!__recv) {
353 |     fprintf(stderr, "appio,c Internal Error: Could not obtain handle for real recv\n");
{% endraw %}

```
### src/components/libmsr/linux-libmsr.c

```c

{% raw %}
140 |     }
141 |     dllib1 = dlopen("libmsr.so", RTLD_NOW | RTLD_GLOBAL);
142 |     CHECK_DL_STATUS( !dllib1 , "Component library libmsr.so not found." );
143 |     init_msr_ptr = dlsym( dllib1, "init_msr" );
144 |     CHECK_DL_STATUS( dlerror()!=NULL , "libmsr function init_msr not found." );
145 |     finalize_msr_ptr = dlsym( dllib1, "finalize_msr" );
146 |     CHECK_DL_STATUS( dlerror()!=NULL, "libmsr function finalize_msr not found." );
147 |     rapl_init_ptr = dlsym( dllib1, "rapl_init" );
148 |     CHECK_DL_STATUS( dlerror()!=NULL, "libmsr function rapl_init not found." );
149 |     poll_rapl_data_ptr = dlsym( dllib1, "poll_rapl_data" );
150 |     CHECK_DL_STATUS( dlerror()!=NULL, "libmsr function poll_rapl_data not found." );
151 |     set_pkg_rapl_limit_ptr = dlsym( dllib1, "set_pkg_rapl_limit" );
152 |     CHECK_DL_STATUS( dlerror()!=NULL, "libmsr function set_pkg_rapl_limit not found." );
153 |     get_pkg_rapl_limit_ptr = dlsym( dllib1, "get_pkg_rapl_limit" );
154 |     CHECK_DL_STATUS( dlerror()!=NULL, "libmsr function get_pkg_rapl_limit not found." );
155 |     core_config_ptr = dlsym( dllib1, "core_config" );
156 |     CHECK_DL_STATUS( dlerror()!=NULL, "libmsr function core_config not found." );
157 |     rapl_storage_ptr = dlsym( dllib1, "rapl_storage" );
158 |     CHECK_DL_STATUS( dlerror()!=NULL, "libmsr function rapl_storage not found." );
159 |     get_rapl_power_info_ptr = dlsym( dllib1, "get_rapl_power_info" );
160 |     CHECK_DL_STATUS( dlerror()!=NULL, "libmsr function get_rapl_power_info not found." );
161 |     return( PAPI_OK);
{% endraw %}

```
### src/components/host_micpower/linux-host_micpower.c

```c

{% raw %}
137 |         return ( PAPI_ENOSUPP );
138 |     }
139 | 
140 | 	MicGetErrorStringPtr = dlsym(mic_access, "MicGetErrorString");
141 | 	if (dlerror() != NULL)
142 | 	{
144 | 			_host_micpower_vector.cmp_info.disabled = 1;
145 | 			return ( PAPI_ENOSUPP );
146 | 	}
147 | 	MicCloseAdapterPtr = dlsym(mic_access, "MicCloseAdapter");
148 | 	if (dlerror() != NULL)
149 | 	{
151 | 			_host_micpower_vector.cmp_info.disabled = 1;
152 | 			return ( PAPI_ENOSUPP );
153 | 	}
154 | 	MicInitAPIPtr = dlsym(mic_access, "MicInitAPI");
155 | 	if (dlerror() != NULL)
156 | 	{
158 | 			_host_micpower_vector.cmp_info.disabled = 1;
159 | 			return ( PAPI_ENOSUPP );
160 | 	}
161 | 	MicCloseAPIPtr = dlsym(mic_access, "MicCloseAPI");
162 | 	if (dlerror() != NULL)
163 | 	{
165 | 			_host_micpower_vector.cmp_info.disabled = 1;
166 | 			return ( PAPI_ENOSUPP );
167 | 	}
168 | 	MicInitAdapterPtr = dlsym(mic_access, "MicInitAdapter");
169 | 	if (dlerror() != NULL)
170 | 	{
173 | 			return ( PAPI_ENOSUPP );
174 | 	}
175 | 
176 | 	MicGetPowerUsagePtr = dlsym(mic_access, "MicGetPowerUsage");
177 | 	if (dlerror() != NULL)
178 | 	{
{% endraw %}

```
### src/components/cuda/linux-cuda.c

```c

{% raw %}
192 |     /* Need to link in the cuda libraries, if not found disable the component */
193 |     dl1 = dlopen( "libcuda.so", RTLD_NOW | RTLD_GLOBAL );
194 |     CHECK_DL_STATUS( !dl1 , "CUDA library libcuda.so not found." );
195 |     cuCtxGetCurrentPtr = dlsym( dl1, "cuCtxGetCurrent" );
196 |     CHECK_DL_STATUS( dlerror()!=NULL , "CUDA function cuCtxGetCurrent not found." );
197 |     cuDeviceGetPtr = dlsym( dl1, "cuDeviceGet" );
198 |     CHECK_DL_STATUS( dlerror()!=NULL, "CUDA function cuDeviceGet not found." );
199 |     cuDeviceGetCountPtr = dlsym( dl1, "cuDeviceGetCount" );
200 |     CHECK_DL_STATUS( dlerror()!=NULL, "CUDA function cuDeviceGetCount not found." );
201 |     cuDeviceGetNamePtr = dlsym( dl1, "cuDeviceGetName" );
202 |     CHECK_DL_STATUS( dlerror()!=NULL, "CUDA function cuDeviceGetName not found." );
203 |     cuInitPtr = dlsym( dl1, "cuInit" );
204 |     CHECK_DL_STATUS( dlerror()!=NULL, "CUDA function cuInit not found." );
205 |     cuCtxPopCurrentPtr = dlsym( dl1, "cuCtxPopCurrent" );
206 |     CHECK_DL_STATUS( dlerror()!=NULL, "CUDA function cuCtxPopCurrent not found." );
207 |     cuCtxPushCurrentPtr = dlsym( dl1, "cuCtxPushCurrent" );
208 |     CHECK_DL_STATUS( dlerror()!=NULL, "CUDA function cuCtxPushCurrent not found." );
209 | 
210 |     dl2 = dlopen( "libcudart.so", RTLD_NOW | RTLD_GLOBAL );
211 |     CHECK_DL_STATUS( !dl2, "CUDA runtime library libcudart.so not found." );
212 |     cudaGetDevicePtr = dlsym( dl2, "cudaGetDevice" );
213 |     CHECK_DL_STATUS( dlerror()!=NULL, "CUDART function cudaGetDevice not found." );
214 |     cudaSetDevicePtr = dlsym( dl2, "cudaSetDevice" );
215 |     CHECK_DL_STATUS( dlerror()!=NULL, "CUDART function cudaSetDevice not found." );
216 |     cudaFreePtr = dlsym( dl2, "cudaFree" );
217 |     CHECK_DL_STATUS( dlerror()!=NULL, "CUDART function cudaFree not found." );
218 | 
219 |     dl3 = dlopen( "libcupti.so", RTLD_NOW | RTLD_GLOBAL );
220 |     CHECK_DL_STATUS( !dl3, "CUDA runtime library libcupti.so not found." );
221 |     cuptiDeviceEnumEventDomainsPtr = dlsym( dl3, "cuptiDeviceEnumEventDomains" );
222 |     CHECK_DL_STATUS( dlerror()!=NULL, "CUPTI function cuptiDeviceEnumEventDomains not found." );
223 |     cuptiDeviceGetNumEventDomainsPtr = dlsym( dl3, "cuptiDeviceGetNumEventDomains" );
224 |     CHECK_DL_STATUS( dlerror()!=NULL, "CUPTI function cuptiDeviceGetNumEventDomains not found." );
225 |     cuptiEventDomainEnumEventsPtr = dlsym( dl3, "cuptiEventDomainEnumEvents" );
226 |     CHECK_DL_STATUS( dlerror()!=NULL, "CUPTI function cuptiEventDomainEnumEvents not found." );
227 |     cuptiEventDomainGetNumEventsPtr = dlsym( dl3, "cuptiEventDomainGetNumEvents" );
228 |     CHECK_DL_STATUS( dlerror()!=NULL, "CUPTI function cuptiEventDomainGetNumEvents not found." );
229 |     cuptiEventGetAttributePtr = dlsym( dl3, "cuptiEventGetAttribute" );
230 |     CHECK_DL_STATUS( dlerror()!=NULL, "CUPTI function cuptiEventGetAttribute not found." );
231 |     cuptiEventGroupAddEventPtr = dlsym( dl3, "cuptiEventGroupAddEvent" );
232 |     CHECK_DL_STATUS( dlerror()!=NULL, "CUPTI function cuptiEventGroupAddEvent not found." );
233 |     cuptiEventGroupCreatePtr = dlsym( dl3, "cuptiEventGroupCreate" );
234 |     CHECK_DL_STATUS( dlerror()!=NULL, "CUPTI function cuptiEventGroupCreate not found." );
235 |     cuptiEventGroupDestroyPtr = dlsym( dl3, "cuptiEventGroupDestroy" );
236 |     CHECK_DL_STATUS( dlerror()!=NULL, "CUPTI function cuptiEventGroupDestroy not found." );
237 |     cuptiEventGroupDisablePtr = dlsym( dl3, "cuptiEventGroupDisable" );
238 |     CHECK_DL_STATUS( dlerror()!=NULL, "CUPTI function cuptiEventGroupDisable not found." );
239 |     cuptiEventGroupEnablePtr = dlsym( dl3, "cuptiEventGroupEnable" );
240 |     CHECK_DL_STATUS( dlerror()!=NULL, "CUPTI function cuptiEventGroupEnable not found." );
241 |     cuptiEventGroupReadAllEventsPtr = dlsym( dl3, "cuptiEventGroupReadAllEvents" );
242 |     CHECK_DL_STATUS( dlerror()!=NULL, "CUPTI function cuptiEventGroupReadAllEvents not found." );
243 |     cuptiEventGroupResetAllEventsPtr = dlsym( dl3, "cuptiEventGroupResetAllEvents" );
244 |     CHECK_DL_STATUS( dlerror()!=NULL, "CUPTI function cuptiEventGroupResetAllEvents not found." );
245 |     return ( PAPI_OK );
{% endraw %}

```
### src/components/cuda/tests/cuda_ld_preload_example.c

```c

{% raw %}
44 |         // Load the papi library dynamically and read the relevant functions
45 |         dl1 = dlopen( "libpapi.so", RTLD_NOW | RTLD_GLOBAL );
46 |         if ( dl1==NULL ) printf("Intercept cudaSetDevice: Cannot load libpapi.so\n");
47 |         PAPI_library_init_ptr = dlsym( dl1, "PAPI_library_init" );
48 |         PAPI_create_eventset_ptr = dlsym( dl1, "PAPI_create_eventset" );
49 |         PAPI_add_named_event_ptr = dlsym( dl1, "PAPI_add_named_event" );
50 |         PAPI_start_ptr = dlsym( dl1, "PAPI_start" );
51 |         PAPI_stop_ptr = dlsym( dl1, "PAPI_stop" );
52 |         // Start using PAPI
53 |         printf("Intercept cudaSetDevice: Initializing PAPI on device %d\n", devnum);
58 |         if( retval != PAPI_OK ) fprintf( stdout, "PAPI_create_eventset failed\n" );
59 |     }
60 |     int (*original_function)(int devnum, int n1, int n2, int n3, void *ptr1);
61 |     original_function = dlsym(RTLD_NEXT, "cudaSetDevice");
62 |     retval_cudaSetDevice = (*original_function)( devnum, n1, n2, n3, ptr1 );
63 |     if ( devseen[devnum]==0 ) {
85 |         if( retval!=PAPI_OK ) fprintf( stdout, "PAPI_start failed\n" );
86 |     }
87 |     int (*original_function)(void *ptr1, void *ptr2);
88 |     original_function = dlsym(RTLD_NEXT, "gettimeofday");
89 |     return (*original_function)(ptr1, ptr2);
90 | }
103 |             printf( "PAPI counterValue: cuda::device:%d:%s: %12lld \n", devnum, "inst_executed", values[devnum] );
104 |     }
105 |     int (*original_function)(void *ptr1, void *ptr2, int n1, int n2, void *ptr3);
106 |     original_function = dlsym(RTLD_NEXT, "cudaFreeHost");
107 |     return (*original_function)(ptr1, ptr2, n1, n2, ptr3);
108 | }
{% endraw %}

```
### src/components/infiniband_umad/linux-infiniband_umad.c

```c

{% raw %}
617 | 		strncpy(_infiniband_vector.cmp_info.disabled_reason, "Infiniband library libibumad.so not found.",PAPI_MAX_STR_LEN);
618 | 		return ( PAPI_ENOSUPP );
619 | 	}
620 | 	umad_initPtr = dlsym(dl1, "umad_init");
621 | 	if (dlerror() != NULL)
622 | 	{
623 | 		strncpy(_infiniband_vector.cmp_info.disabled_reason, "Infiniband function umad_init not found.",PAPI_MAX_STR_LEN);
624 | 		return ( PAPI_ENOSUPP );
625 | 	}
626 | 	umad_get_cas_namesPtr = dlsym(dl1, "umad_get_cas_names");
627 | 	if (dlerror() != NULL)
628 | 	{
629 | 		strncpy(_infiniband_vector.cmp_info.disabled_reason, "Infiniband function umad_get_cas_names not found.",PAPI_MAX_STR_LEN);
630 | 		return ( PAPI_ENOSUPP );
631 | 	}
632 | 	umad_get_caPtr = dlsym(dl1, "umad_get_ca");
633 | 	if (dlerror() != NULL)
634 | 	{
643 | 		strncpy(_infiniband_vector.cmp_info.disabled_reason, "Infiniband library libibmad.so not found.",PAPI_MAX_STR_LEN);
644 | 		return ( PAPI_ENOSUPP );
645 | 	}
646 | 	mad_decode_fieldPtr = dlsym(dl2, "mad_decode_field");
647 | 	if (dlerror() != NULL)
648 | 	{
649 | 		strncpy(_infiniband_vector.cmp_info.disabled_reason, "Infiniband function mad_decode_field not found.",PAPI_MAX_STR_LEN);
650 | 		return ( PAPI_ENOSUPP );
651 | 	}
652 | 	mad_rpc_open_portPtr = dlsym(dl2, "mad_rpc_open_port");
653 | 	if (dlerror() != NULL)
654 | 	{
655 | 		strncpy(_infiniband_vector.cmp_info.disabled_reason, "Infiniband function mad_rpc_open_port not found.",PAPI_MAX_STR_LEN);
656 | 		return ( PAPI_ENOSUPP );
657 | 	}
658 | 	ib_resolve_self_viaPtr = dlsym(dl2, "ib_resolve_self_via");
659 | 	if (dlerror() != NULL)
660 | 	{
661 | 		strncpy(_infiniband_vector.cmp_info.disabled_reason, "Infiniband function ib_resolve_self_via not found.",PAPI_MAX_STR_LEN);
662 | 		return ( PAPI_ENOSUPP );
663 | 	}
664 | 	performance_reset_viaPtr = dlsym(dl2, "performance_reset_via");
665 | 	if (dlerror() != NULL)
666 | 	{
667 | 		strncpy(_infiniband_vector.cmp_info.disabled_reason, "Infiniband function performance_reset_via not found.",PAPI_MAX_STR_LEN);
668 | 		return ( PAPI_ENOSUPP );
669 | 	}
670 | 	pma_query_viaPtr = dlsym(dl2, "pma_query_via");
671 | 	if (dlerror() != NULL)
672 | 	{
{% endraw %}

```