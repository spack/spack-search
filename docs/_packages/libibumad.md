---
name: "libibumad"
layout: package
next_package: emboss
previous_package: libvips
languages: ['cmake', 'cpp']
---
## 25.0
5 / 960 files match

 - [libibverbs/dynamic_driver.c](#libibverbsdynamic_driverc)
 - [libibverbs/driver.h](#libibverbsdriverh)
 - [ibacm/src/acm.c](#ibacmsrcacmc)
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
394 |  * ibv_static_providers() machinery, and a global constructor for the dlopen
{% endraw %}

```
### ibacm/src/acm.c

```cpp

{% raw %}
2791 | 		if (!(handle = dlopen(file_name, RTLD_LAZY))) {
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