---
name: "guacamole-server"
layout: package
next_package: guile
previous_package: gromacs
languages: ['c']
---
## 1.1.0
3 / 490 files match, 1 filtered matches.

 - [src/libguac/client.c](#srclibguacclientc)

### src/libguac/client.c

```c

{% raw %}
450 |     }
451 | 
452 |     /* Load client plugin */
453 |     client_plugin_handle = dlopen(protocol_lib, RTLD_LAZY);
454 |     if (!client_plugin_handle) {
455 |         guac_error = GUAC_STATUS_NOT_FOUND;
{% endraw %}

```