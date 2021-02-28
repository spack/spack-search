---
name: "collectd"
layout: package
next_package: gawk
previous_package: gdb
library_name: dlopen
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 5.10.0
2 / 489 files match, 1 filtered matches.

 - [src/daemon/plugin.c](#srcdaemonpluginc)

### src/daemon/plugin.c

```c

{% raw %}
412 |   if (global)
413 |     flags |= RTLD_GLOBAL;
414 | 
415 |   void *dlh = dlopen(file, flags);
416 |   if (dlh == NULL) {
417 |     char errbuf[1024] = "";
418 | 
419 |     snprintf(errbuf, sizeof(errbuf),
420 |              "dlopen(\"%s\") failed: %s. "
421 |              "The most common cause for this problem is missing dependencies. "
422 |              "Use ldd(1) to check the dependencies of the plugin / shared "
{% endraw %}

```