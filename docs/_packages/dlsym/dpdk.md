---
name: "dpdk"
layout: package
next_package: p11-kit
previous_package: curl
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 20.02
5 / 3923 files match, 4 filtered matches.

 - [drivers/common/mlx5/mlx5_common.c](#driverscommonmlx5mlx5_commonc)
 - [drivers/net/mlx4/mlx4.c](#driversnetmlx4mlx4c)
 - [drivers/net/ark/ark_ethdev.c](#driversnetarkark_ethdevc)
 - [examples/performance-thread/pthread_shim/pthread_shim.c](#examplesperformance-threadpthread_shimpthread_shimc)

### drivers/common/mlx5/mlx5_common.c

```c

{% raw %}
291 | 			DRV_LOG(WARNING, "Cannot load glue library: %s", dlmsg);
292 | 		goto glue_error;
293 | 	}
294 | 	sym = dlsym(handle, "mlx5_glue");
295 | 	if (!sym || !*sym) {
296 | 		rte_errno = EINVAL;
{% endraw %}

```
### drivers/net/mlx4/mlx4.c

```c

{% raw %}
1253 | 			WARN("cannot load glue library: %s", dlmsg);
1254 | 		goto glue_error;
1255 | 	}
1256 | 	sym = dlsym(handle, "mlx4_glue");
1257 | 	if (!sym || !*sym) {
1258 | 		rte_errno = EINVAL;
{% endraw %}

```
### drivers/net/ark/ark_ethdev.c

```c

{% raw %}
183 | 	/* Get the entry points */
184 | 	ark->user_ext.dev_init =
185 | 		(void *(*)(struct rte_eth_dev *, void *, int))
186 | 		dlsym(ark->d_handle, "dev_init");
187 | 	PMD_DEBUG_LOG(DEBUG, "device ext init pointer = %p\n",
188 | 		      ark->user_ext.dev_init);
189 | 	ark->user_ext.dev_get_port_count =
190 | 		(int (*)(struct rte_eth_dev *, void *))
191 | 		dlsym(ark->d_handle, "dev_get_port_count");
192 | 	ark->user_ext.dev_uninit =
193 | 		(void (*)(struct rte_eth_dev *, void *))
194 | 		dlsym(ark->d_handle, "dev_uninit");
195 | 	ark->user_ext.dev_configure =
196 | 		(int (*)(struct rte_eth_dev *, void *))
197 | 		dlsym(ark->d_handle, "dev_configure");
198 | 	ark->user_ext.dev_start =
199 | 		(int (*)(struct rte_eth_dev *, void *))
200 | 		dlsym(ark->d_handle, "dev_start");
201 | 	ark->user_ext.dev_stop =
202 | 		(void (*)(struct rte_eth_dev *, void *))
203 | 		dlsym(ark->d_handle, "dev_stop");
204 | 	ark->user_ext.dev_close =
205 | 		(void (*)(struct rte_eth_dev *, void *))
206 | 		dlsym(ark->d_handle, "dev_close");
207 | 	ark->user_ext.link_update =
208 | 		(int (*)(struct rte_eth_dev *, int, void *))
209 | 		dlsym(ark->d_handle, "link_update");
210 | 	ark->user_ext.dev_set_link_up =
211 | 		(int (*)(struct rte_eth_dev *, void *))
212 | 		dlsym(ark->d_handle, "dev_set_link_up");
213 | 	ark->user_ext.dev_set_link_down =
214 | 		(int (*)(struct rte_eth_dev *, void *))
215 | 		dlsym(ark->d_handle, "dev_set_link_down");
216 | 	ark->user_ext.stats_get =
217 | 		(int (*)(struct rte_eth_dev *, struct rte_eth_stats *,
218 | 			  void *))
219 | 		dlsym(ark->d_handle, "stats_get");
220 | 	ark->user_ext.stats_reset =
221 | 		(void (*)(struct rte_eth_dev *, void *))
222 | 		dlsym(ark->d_handle, "stats_reset");
223 | 	ark->user_ext.mac_addr_add =
224 | 		(void (*)(struct rte_eth_dev *, struct rte_ether_addr *,
225 | 			uint32_t, uint32_t, void *))
226 | 		dlsym(ark->d_handle, "mac_addr_add");
227 | 	ark->user_ext.mac_addr_remove =
228 | 		(void (*)(struct rte_eth_dev *, uint32_t, void *))
229 | 		dlsym(ark->d_handle, "mac_addr_remove");
230 | 	ark->user_ext.mac_addr_set =
231 | 		(void (*)(struct rte_eth_dev *, struct rte_ether_addr *,
232 | 			  void *))
233 | 		dlsym(ark->d_handle, "mac_addr_set");
234 | 	ark->user_ext.set_mtu =
235 | 		(int (*)(struct rte_eth_dev *, uint16_t,
236 | 			  void *))
237 | 		dlsym(ark->d_handle, "set_mtu");
238 | 
239 | 	return found;
{% endraw %}

```
### examples/performance-thread/pthread_shim/pthread_shim.c

```c

{% raw %}
159 | 
160 | #define get_addr_of_loaded_symbol(name) do {				\
161 | 	char *error_str;						\
162 | 	_sys_pthread_funcs.f_##name = dlsym(__libc_dl_handle, (#name));	\
163 | 	error_str = dlerror();						\
164 | 	if (error_str != NULL) {					\
{% endraw %}

```