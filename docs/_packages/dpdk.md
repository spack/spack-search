---
name: "dpdk"
layout: package
next_package: draco
previous_package: dmtcp
languages: ['c']
---
## 20.02
9 / 3923 files match, 4 filtered matches.

 - [lib/librte_eal/common/eal_common_options.c](#liblibrte_ealcommoneal_common_optionsc)
 - [drivers/common/mlx5/mlx5_common.c](#driverscommonmlx5mlx5_commonc)
 - [drivers/net/mlx4/mlx4.c](#driversnetmlx4mlx4c)
 - [drivers/net/ark/ark_ethdev.c](#driversnetarkark_ethdevc)

### lib/librte_eal/common/eal_common_options.c

```c

{% raw %}
306 | 			solib->lib_handle = dlopen(solib->name, RTLD_NOW);
{% endraw %}

```
### drivers/common/mlx5/mlx5_common.c

```c

{% raw %}
280 | 			handle = dlopen(name, RTLD_LAZY);
{% endraw %}

```
### drivers/net/mlx4/mlx4.c

```c

{% raw %}
1242 | 			handle = dlopen(name, RTLD_LAZY);
{% endraw %}

```
### drivers/net/ark/ark_ethdev.c

```c

{% raw %}
174 | 	ark->d_handle = dlopen(dllpath, RTLD_LOCAL | RTLD_LAZY);
{% endraw %}

```