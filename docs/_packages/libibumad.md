---
name: "libibumad"
layout: package
next_package: emboss
previous_package: libvips
languages: ['c']
---
## 25.0
5 / 960 files match

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
2791 | 		if (!(handle = dlopen(file_name, RTLD_LAZY))) {
{% endraw %}

```