---
name: "guacamole-server"
layout: package
next_package: acct
previous_package: rsyslog
languages: ['cpp']
---
## 1.1.0
3 / 490 files match

 - [configure.ac](#configureac)
 - [src/libguac/client.c](#srclibguacclientc)
 - [src/libguac/guacamole/client.h](#srclibguacguacamoleclienth)

### configure.ac

```

{% raw %}
26 | LT_INIT([dlopen])
70 | # Include libdl for dlopen() if necessary
71 | AC_CHECK_LIB([dl], [dlopen],
73 |              [AC_CHECK_DECL([dlopen],,
74 |                             AC_MSG_ERROR("libdl is required on systems which do not otherwise provide dlopen()"),
{% endraw %}

```
### src/libguac/client.c

```cpp

{% raw %}
429 |     /* Reference to dlopen()'d plugin */
453 |     client_plugin_handle = dlopen(protocol_lib, RTLD_LAZY);
{% endraw %}

```
### src/libguac/guacamole/client.h

```cpp

{% raw %}
253 |      * Handle to the dlopen()'d plugin, which should be given to dlclose() when
{% endraw %}

```