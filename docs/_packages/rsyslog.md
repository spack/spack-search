---
name: "rsyslog"
layout: package
next_package: guacamole-server
previous_package: gettext
languages: ['c']
---
## 8.2006.0
5 / 1621 files match

 - [runtime/modules.c](#runtimemodulesc)
 - [runtime/rsyslog.h](#runtimersyslogh)

### runtime/modules.c

```c

{% raw %}
1236 | 			pModHdlr = dlopen((char *) pPathBuf, RTLD_NOW);
{% endraw %}

```
### runtime/rsyslog.h

```c

{% raw %}
364 | 	RS_RET_MODULE_LOAD_ERR_DLOPEN = -2066, /**< module could not be loaded - problem in dlopen() */
{% endraw %}

```