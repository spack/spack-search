---
name: "zabbix"
layout: package
next_package: zfs
previous_package: yorick
languages: ['c']
---
## 5.0.3
2 / 3540 files match, 1 filtered matches.

 - [src/libs/zbxmodules/modules.c](#srclibszbxmodulesmodulesc)

### src/libs/zbxmodules/modules.c

```c

{% raw %}
241 | 
242 | 	zabbix_log(LOG_LEVEL_DEBUG, "loading module \"%s\"", full_name);
243 | 
244 | 	if (NULL == (lib = dlopen(full_name, RTLD_NOW)))
245 | 	{
246 | 		zabbix_log(LOG_LEVEL_CRIT, "cannot load module \"%s\": %s", name, dlerror());
{% endraw %}

```