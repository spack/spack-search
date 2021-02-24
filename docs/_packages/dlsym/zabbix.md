---
name: "zabbix"
layout: package
next_package: gdb
previous_package: pnmpi
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 5.0.3
2 / 3540 files match, 1 filtered matches.

 - [src/libs/zbxmodules/modules.c](#srclibszbxmodulesmodulesc)

### src/libs/zbxmodules/modules.c

```c

{% raw %}
254 | 		return SUCCEED;
255 | 	}
256 | 
257 | 	if (NULL == (func_version = (int (*)(void))dlsym(lib, ZBX_MODULE_FUNC_API_VERSION)))
258 | 	{
259 | 		zabbix_log(LOG_LEVEL_CRIT, "cannot find \"" ZBX_MODULE_FUNC_API_VERSION "()\""
267 | 		goto fail;
268 | 	}
269 | 
270 | 	if (NULL == (func_init = (int (*)(void))dlsym(lib, ZBX_MODULE_FUNC_INIT)))
271 | 	{
272 | 		zabbix_log(LOG_LEVEL_DEBUG, "cannot find \"" ZBX_MODULE_FUNC_INIT "()\""
278 | 		goto fail;
279 | 	}
280 | 
281 | 	if (NULL == (func_list = (ZBX_METRIC *(*)(void))dlsym(lib, ZBX_MODULE_FUNC_ITEM_LIST)))
282 | 	{
283 | 		zabbix_log(LOG_LEVEL_DEBUG, "cannot find \"" ZBX_MODULE_FUNC_ITEM_LIST "()\""
291 | 			goto fail;
292 | 		}
293 | 
294 | 		if (NULL == (func_timeout = (void (*)(int))dlsym(lib, ZBX_MODULE_FUNC_ITEM_TIMEOUT)))
295 | 		{
296 | 			zabbix_log(LOG_LEVEL_DEBUG, "cannot find \"" ZBX_MODULE_FUNC_ITEM_TIMEOUT "()\""
303 | 	/* module passed validation and can now be registered */
304 | 	module = zbx_register_module(lib, name);
305 | 
306 | 	if (NULL == (func_history_write_cbs = (ZBX_HISTORY_WRITE_CBS (*)(void))dlsym(lib,
307 | 			ZBX_MODULE_FUNC_HISTORY_WRITE_CBS)))
308 | 	{
387 | 	zbx_module_t	*module = (zbx_module_t *)data;
388 | 	int		(*func_uninit)(void);
389 | 
390 | 	if (NULL == (func_uninit = (int (*)(void))dlsym(module->lib, ZBX_MODULE_FUNC_UNINIT)))
391 | 	{
392 | 		zabbix_log(LOG_LEVEL_DEBUG, "cannot find \"" ZBX_MODULE_FUNC_UNINIT "()\""
{% endraw %}

```