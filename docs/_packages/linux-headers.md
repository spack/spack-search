---
name: "linux-headers"
layout: package
next_package: dateutils
previous_package: wonton
languages: ['c']
---
## 4.9.10
5 / 50920 files match, 2 filtered matches.

 - [tools/lib/traceevent/event-plugin.c](#toolslibtraceeventevent-pluginc)
 - [tools/perf/ui/setup.c](#toolsperfuisetupc)

### tools/lib/traceevent/event-plugin.c

```c

{% raw %}
303 | 	handle = dlopen(plugin, RTLD_NOW | RTLD_GLOBAL);
{% endraw %}

```
### tools/perf/ui/setup.c

```c

{% raw %}
18 | 	perf_gtk_handle = dlopen(PERF_GTK_DSO, RTLD_LAZY);
22 | 		perf_gtk_handle = dlopen(buf, RTLD_LAZY);
{% endraw %}

```