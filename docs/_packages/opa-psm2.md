---
name: "opa-psm2"
layout: package
next_package: opencv
previous_package: onednn
languages: ['c']
---
## 11.2.68
2 / 181 files match, 2 filtered matches.

 - [psm.c](#psmc)
 - [ptl_ips/ips_opp_path_rec.c](#ptl_ipsips_opp_path_recc)

### psm.c

```c

{% raw %}
140 | 	PSM2_LOG_MSG("entering");
141 | 	_HFI_VDBG("Loading CUDA library.\n");
142 | 
143 | 	psmi_cuda_lib = dlopen("libcuda.so", RTLD_LAZY);
144 | 	if (!psmi_cuda_lib) {
145 | 		dlerr = dlerror();
195 | 	PSMI_CUDA_DLSYM(psmi_cuda_lib, cuDevicePrimaryCtxRelease);
196 | 	PSMI_CUDA_DLSYM(psmi_cuda_lib, cuCtxGetDevice);
197 | 
198 | 	psmi_nvml_lib = dlopen("libnvidia-ml.so", RTLD_LAZY);
199 | 	if (!psmi_nvml_lib) {
200 | 		dlerr = dlerror();
{% endraw %}

```
### ptl_ips/ips_opp_path_rec.c

```c

{% raw %}
521 | 	psm2_error_t err = PSM2_OK;
522 | 	char hfiName[32];
523 | 
524 | 	proto->opp_lib = dlopen(DF_OPP_LIBRARY, RTLD_NOW);
525 | 	if (!proto->opp_lib) {
526 | 		char *err = dlerror();
{% endraw %}

```