---
name: "dpdk"
layout: package
next_package: perl-alien-build
previous_package: rempi
languages: ['cpp']
---
## 20.02
9 / 3923 files match

 - [meson_options.txt](#meson_optionstxt)
 - [lib/librte_eal/common/eal_common_options.c](#liblibrte_ealcommoneal_common_optionsc)
 - [drivers/common/mlx5/meson.build](#driverscommonmlx5mesonbuild)
 - [drivers/common/mlx5/mlx5_common.c](#driverscommonmlx5mlx5_commonc)
 - [drivers/net/mlx4/meson.build](#driversnetmlx4mesonbuild)
 - [drivers/net/mlx4/mlx4.c](#driversnetmlx4mlx4c)
 - [drivers/net/ark/ark_ethdev.c](#driversnetarkark_ethdevc)
 - [doc/guides/nics/mlx4.rst](#docguidesnicsmlx4rst)
 - [doc/guides/nics/mlx5.rst](#docguidesnicsmlx5rst)

### meson_options.txt

```

{% raw %}
16 | option('ibverbs_link', type: 'combo', choices : ['static', 'shared', 'dlopen'], value: 'shared',
17 | 	description: 'Linkage method (static/shared/dlopen) for Mellanox PMDs with ibverbs dependencies.')
{% endraw %}

```
### lib/librte_eal/common/eal_common_options.c

```cpp

{% raw %}
306 | 			solib->lib_handle = dlopen(solib->name, RTLD_NOW);
{% endraw %}

```
### drivers/common/mlx5/meson.build

```

{% raw %}
10 | dlopen_ibverbs = (get_option('ibverbs_link') == 'dlopen')
14 | if dlopen_ibverbs
15 | 	dpdk_conf.set('RTE_IBVERBS_LINK_DLOPEN', 1)
31 | 		if not static_ibverbs and not dlopen_ibverbs
40 | if static_ibverbs or dlopen_ibverbs
58 | if not dlopen_ibverbs
197 | if dlopen_ibverbs
198 | 	dlopen_name = 'mlx5_glue'
199 | 	dlopen_lib_name = 'rte_pmd_@0@'.format(dlopen_name)
200 | 	dlopen_so_version = LIB_GLUE_VERSION
201 | 	dlopen_sources = files('mlx5_glue.c')
202 | 	dlopen_install_dir = [ eal_pmd_path + '-glue' ]
203 | 	dlopen_includes = [global_inc]
204 | 	dlopen_includes += include_directories(
208 | 		dlopen_lib_name,
209 | 		dlopen_sources,
210 | 		include_directories: dlopen_includes,
217 | 		soversion: dlopen_so_version,
219 | 		install_dir: dlopen_install_dir,
{% endraw %}

```
### drivers/common/mlx5/mlx5_common.c

```cpp

{% raw %}
162 | #ifdef RTE_IBVERBS_LINK_DLOPEN
233 | #ifdef RTE_IBVERBS_LINK_DLOPEN
244 | 		 * variant, otherwise let dlopen() look up libraries on its
280 | 			handle = dlopen(name, RTLD_LAZY);
303 | #endif /* RTE_IBVERBS_LINK_DLOPEN */
{% endraw %}

```
### drivers/net/mlx4/meson.build

```

{% raw %}
11 | dlopen_ibverbs = (get_option('ibverbs_link') == 'dlopen')
15 | if dlopen_ibverbs
16 | 	dpdk_conf.set('RTE_IBVERBS_LINK_DLOPEN', 1)
32 | 		if not static_ibverbs and not dlopen_ibverbs
41 | if static_ibverbs or dlopen_ibverbs
65 | if not dlopen_ibverbs
117 | if dlopen_ibverbs
118 | 	dlopen_name = 'mlx4_glue'
119 | 	dlopen_lib_name = driver_name_fmt.format(dlopen_name)
120 | 	dlopen_so_version = LIB_GLUE_VERSION
121 | 	dlopen_sources = files('mlx4_glue.c')
122 | 	dlopen_install_dir = [ eal_pmd_path + '-glue' ]
124 | 		dlopen_lib_name,
125 | 		dlopen_sources,
133 | 		soversion: dlopen_so_version,
135 | 		install_dir: dlopen_install_dir,
{% endraw %}

```
### drivers/net/mlx4/mlx4.c

```cpp

{% raw %}
1147 | #ifdef RTE_IBVERBS_LINK_DLOPEN
1206 | 		 * variant, otherwise let dlopen() look up libraries on its
1242 | 			handle = dlopen(name, RTLD_LAZY);
1300 | #ifdef RTE_IBVERBS_LINK_DLOPEN
{% endraw %}

```
### drivers/net/ark/ark_ethdev.c

```cpp

{% raw %}
174 | 	ark->d_handle = dlopen(dllpath, RTLD_LOCAL | RTLD_LAZY);
{% endraw %}

```
### doc/guides/nics/mlx4.rst

```

{% raw %}
64 | - ``CONFIG_RTE_IBVERBS_LINK_DLOPEN`` (default **n**)
96 | - ``ibverbs_link`` can be ``static``, ``shared``, or ``dlopen``.
106 |   Only matters when compiled with ``CONFIG_RTE_IBVERBS_LINK_DLOPEN``
{% endraw %}

```
### doc/guides/nics/mlx5.rst

```

{% raw %}
282 | - ``CONFIG_RTE_IBVERBS_LINK_DLOPEN`` (default **n**)
321 | - ``ibverbs_link`` can be ``static``, ``shared``, or ``dlopen``.
331 |   Only matters when compiled with ``CONFIG_RTE_IBVERBS_LINK_DLOPEN``
{% endraw %}

```