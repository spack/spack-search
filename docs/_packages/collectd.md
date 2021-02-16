---
name: "collectd"
layout: package
next_package: conduit
previous_package: code-server
languages: ['c']
---
## 5.10.0
2 / 489 files match, 1 filtered matches.

 - [src/daemon/plugin.c](#srcdaemonpluginc)

### src/daemon/plugin.c

```c

{% raw %}
415 |   void *dlh = dlopen(file, flags);
420 |              "dlopen(\"%s\") failed: %s. "
{% endraw %}

```