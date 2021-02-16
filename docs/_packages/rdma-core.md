---
name: "rdma-core"
layout: package
next_package: opa-psm2
previous_package: imlib2
languages: ['c']
---
## 33.1
6 / 1036 files match, 2 filtered matches.

 - [libibverbs/dynamic_driver.c](#libibverbsdynamic_driverc)
 - [ibacm/src/acm.c](#ibacmsrcacmc)

### libibverbs/dynamic_driver.c

```c

{% raw %}
172 | 		dlhandle = dlopen(so_name, RTLD_NOW);
174 | 			goto out_dlopen;
185 | 		dlhandle = dlopen(so_name, RTLD_NOW);
196 | 	dlhandle = dlopen(so_name, RTLD_NOW);
198 | 		goto out_dlopen;
205 | out_dlopen:
{% endraw %}

```
### ibacm/src/acm.c

```c

{% raw %}
2885 | 		if (!(handle = dlopen(file_name, RTLD_LAZY))) {
{% endraw %}

```