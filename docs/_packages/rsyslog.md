---
name: "rsyslog"
layout: package
next_package: guacamole-server
previous_package: gettext
languages: ['cpp']
---
## 8.2006.0
5 / 1621 files match

 - [configure.ac](#configureac)
 - [tests/known_issues.supp](#testsknown_issuessupp)
 - [runtime/modules.c](#runtimemodulesc)
 - [runtime/modules.h](#runtimemodulesh)
 - [runtime/rsyslog.h](#runtimersyslogh)

### configure.ac

```

{% raw %}
46 | # AIXPORT START: enable dlopen
48 | 	AC_LIBTOOL_DLOPEN
159 | AC_SEARCH_LIBS(dlopen, dl)
{% endraw %}

```
### tests/known_issues.supp

```

{% raw %}
4 |    fun:dlopen*
{% endraw %}

```
### runtime/modules.c

```cpp

{% raw %}
71 | /* already dlopen()-ed libs */
1236 | 			pModHdlr = dlopen((char *) pPathBuf, RTLD_NOW);
1260 | 		LogError(0, RS_RET_MODULE_LOAD_ERR_DLOPEN, "could not load module '%s', errors: %s", pModName,
1262 | 		ABORT_FINALIZE(RS_RET_MODULE_LOAD_ERR_DLOPEN);
{% endraw %}

```
### runtime/modules.h

```cpp

{% raw %}
82 | /* remember which shared libs we dlopen()-ed */
{% endraw %}

```
### runtime/rsyslog.h

```cpp

{% raw %}
364 | 	RS_RET_MODULE_LOAD_ERR_DLOPEN = -2066, /**< module could not be loaded - problem in dlopen() */
{% endraw %}

```