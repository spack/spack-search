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
244 | 	if (NULL == (lib = dlopen(full_name, RTLD_NOW)))
{% endraw %}

```