---
name: "rdma-core"
layout: package
next_package: opa-psm2
previous_package: imlib2
languages: ['cmake', 'cpp']
---
## 33.1
6 / 1036 files match

 - [libibverbs/dynamic_driver.c](#libibverbsdynamic_driverc)
 - [libibverbs/driver.h](#libibverbsdriverh)
 - [ibacm/src/acm.c](#ibacmsrcacmc)
 - [ABI/ibverbs.dump](#abiibverbsdump)
 - [buildlib/rdma_functions.cmake](#buildlibrdma_functionscmake)
 - [buildlib/provider.map](#buildlibprovidermap)

### libibverbs/dynamic_driver.c

```cpp

{% raw %}
172 | 		dlhandle = dlopen(so_name, RTLD_NOW);
174 | 			goto out_dlopen;
185 | 		dlhandle = dlopen(so_name, RTLD_NOW);
196 | 	dlhandle = dlopen(so_name, RTLD_NOW);
198 | 		goto out_dlopen;
205 | out_dlopen:
{% endraw %}

```
### libibverbs/driver.h

```cpp

{% raw %}
407 |  * ibv_static_providers() machinery, and a global constructor for the dlopen
{% endraw %}

```
### ibacm/src/acm.c

```cpp

{% raw %}
2885 | 		if (!(handle = dlopen(file_name, RTLD_LAZY))) {
{% endraw %}

```
### ABI/ibverbs.dump

```

{% raw %}
18159 |                                                                  'dlopen@GLIBC_2.2.5' => 0,
{% endraw %}

```
### buildlib/rdma_functions.cmake

```cmake

{% raw %}
125 | # VERBS_PROVIDER_DIR so it can be dlopened as a provider as well.
{% endraw %}

```
### buildlib/provider.map

```

{% raw %}
1 |    attribute(constructor) to cause their init function to run at dlopen
{% endraw %}

```