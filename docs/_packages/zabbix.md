---
name: "zabbix"
layout: package
next_package: vgm
previous_package: activeharmony
languages: ['cpp']
---
## 5.0.3
2 / 3540 files match

 - [configure.ac](#configureac)
 - [src/libs/zbxmodules/modules.c](#srclibszbxmodulesmodulesc)

### configure.ac

```

{% raw %}
148 | AC_SEARCH_LIBS(dlopen, dl)
{% endraw %}

```
### src/libs/zbxmodules/modules.c

```cpp

{% raw %}
244 | 	if (NULL == (lib = dlopen(full_name, RTLD_NOW)))
{% endraw %}

```