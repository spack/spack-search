---
name: "zabbix"
layout: package
next_package: vgm
previous_package: activeharmony
languages: ['c']
---
## 5.0.3
2 / 3540 files match

 - [src/libs/zbxmodules/modules.c](#srclibszbxmodulesmodulesc)

### src/libs/zbxmodules/modules.c

```c

{% raw %}
244 | 	if (NULL == (lib = dlopen(full_name, RTLD_NOW)))
{% endraw %}

```