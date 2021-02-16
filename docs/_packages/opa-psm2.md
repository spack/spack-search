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
143 | 	psmi_cuda_lib = dlopen("libcuda.so", RTLD_LAZY);
198 | 	psmi_nvml_lib = dlopen("libnvidia-ml.so", RTLD_LAZY);
{% endraw %}

```
### ptl_ips/ips_opp_path_rec.c

```c

{% raw %}
524 | 	proto->opp_lib = dlopen(DF_OPP_LIBRARY, RTLD_NOW);
{% endraw %}

```