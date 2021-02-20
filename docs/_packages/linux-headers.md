---
name: "linux-headers"
layout: package
next_package: linux-pam
previous_package: likwid
languages: ['c']
---
## 4.9.10
5 / 50920 files match, 2 filtered matches.

 - [tools/lib/traceevent/event-plugin.c](#toolslibtraceeventevent-pluginc)
 - [tools/perf/ui/setup.c](#toolsperfuisetupc)

### tools/lib/traceevent/event-plugin.c

```c

{% raw %}
300 | 	strcat(plugin, "/");
301 | 	strcat(plugin, file);
302 | 
303 | 	handle = dlopen(plugin, RTLD_NOW | RTLD_GLOBAL);
304 | 	if (!handle) {
305 | 		warning("could not load plugin '%s'\n%s\n",
{% endraw %}

```
### tools/perf/ui/setup.c

```c

{% raw %}
15 | 	if (perf_gtk_handle)
16 | 		return 0;
17 | 
18 | 	perf_gtk_handle = dlopen(PERF_GTK_DSO, RTLD_LAZY);
19 | 	if (perf_gtk_handle == NULL) {
20 | 		char buf[PATH_MAX];
21 | 		scnprintf(buf, sizeof(buf), "%s/%s", LIBDIR, PERF_GTK_DSO);
22 | 		perf_gtk_handle = dlopen(buf, RTLD_LAZY);
23 | 	}
24 | 	if (perf_gtk_handle == NULL)
{% endraw %}

```