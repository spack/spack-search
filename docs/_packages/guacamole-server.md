---
name: "guacamole-server"
layout: package
next_package: acct
previous_package: rsyslog
languages: ['c']
---
## 1.1.0
3 / 490 files match, 1 filtered matches.

 - [src/libguac/client.c](#srclibguacclientc)

### src/libguac/client.c

```c

{% raw %}
453 |     client_plugin_handle = dlopen(protocol_lib, RTLD_LAZY);
{% endraw %}

```