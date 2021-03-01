---
name: "dpdk"
layout: package
next_package: dyninst
previous_package: dotconf
library_name: dlopen
matches: ['dlsym', 'dlopen']
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
303 | 		} else {
304 | 			RTE_LOG(DEBUG, EAL, "open shared lib %s\n",
305 | 				solib->name);
306 | 			solib->lib_handle = dlopen(solib->name, RTLD_NOW);
307 | 			if (solib->lib_handle == NULL) {
308 | 				RTE_LOG(ERR, EAL, "%s\n", dlerror());
{% endraw %}

```
### drivers/common/mlx5/mlx5_common.c

```c

{% raw %}
277 | 				continue;
278 | 			DRV_LOG(DEBUG, "Looking for rdma-core glue as "
279 | 				"\"%s\"", name);
280 | 			handle = dlopen(name, RTLD_LAZY);
281 | 			break;
282 | 		} while (1);
{% endraw %}

```
### drivers/net/mlx4/mlx4.c

```c

{% raw %}
1239 | 			if (sizeof(name) != (size_t)ret + 1)
1240 | 				continue;
1241 | 			DEBUG("looking for rdma-core glue as \"%s\"", name);
1242 | 			handle = dlopen(name, RTLD_LAZY);
1243 | 			break;
1244 | 		} while (1);
{% endraw %}

```
### drivers/net/ark/ark_ethdev.c

```c

{% raw %}
171 | 	PMD_DRV_LOG(INFO, "ARK EXT found dll path at %s\n", dllpath);
172 | 
173 | 	/* Open and load the .so */
174 | 	ark->d_handle = dlopen(dllpath, RTLD_LOCAL | RTLD_LAZY);
175 | 	if (ark->d_handle == NULL) {
176 | 		PMD_DRV_LOG(ERR, "Could not load user extension %s\n",
{% endraw %}

```