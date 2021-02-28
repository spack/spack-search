---
name: "rsyslog"
layout: package
next_package: petsc
previous_package: rr
library_name: dlopen
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 8.2006.0
5 / 1621 files match, 2 filtered matches.

 - [runtime/modules.c](#runtimemodulesc)
 - [runtime/rsyslog.h](#runtimersyslogh)

### runtime/modules.c

```c

{% raw %}
1233 | 
1234 | 		/* not found, try to dynamically link it */
1235 | 		if (!pModHdlr) {
1236 | 			pModHdlr = dlopen((char *) pPathBuf, RTLD_NOW);
1237 | 		}
1238 | 
{% endraw %}

```
### runtime/rsyslog.h

```c

{% raw %}
361 | 	RS_RET_HOST_NOT_PERMITTED = -2063, /**< a host is not permitted to perform an action it requested */
362 | 	RS_RET_MODULE_LOAD_ERR = -2064, /**< module could not be loaded */
363 | 	RS_RET_MODULE_LOAD_ERR_PATHLEN = -2065, /**< module could not be loaded - path to long */
364 | 	RS_RET_MODULE_LOAD_ERR_DLOPEN = -2066, /**< module could not be loaded - problem in dlopen() */
365 | 	RS_RET_MODULE_LOAD_ERR_NO_INIT = -2067, /**< module could not be loaded - init() missing */
366 | 	RS_RET_MODULE_LOAD_ERR_INIT_FAILED = -2068, /**< module could not be loaded - init() failed */
{% endraw %}

```