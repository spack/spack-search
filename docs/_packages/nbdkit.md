---
name: "nbdkit"
layout: package
next_package: nccl
previous_package: namd
languages: ['c']
---
## 1.23.7
8 / 763 files match, 3 filtered matches.

 - [server/main.c](#servermainc)
 - [plugins/vddk/vddk.c](#pluginsvddkvddkc)
 - [plugins/cc/cc.c](#pluginsccccc)

### server/main.c

```c

{% raw %}
808 |   dl = dlopen (filename, RTLD_NOW|RTLD_GLOBAL);
861 |   dl = dlopen (filename, RTLD_NOW|RTLD_GLOBAL);
{% endraw %}

```
### plugins/vddk/vddk.c

```c

{% raw %}
76 | static void *dl;                           /* dlopen handle */
321 |     dl = dlopen (path, RTLD_NOW);
{% endraw %}

```
### plugins/cc/cc.c

```c

{% raw %}
234 |   dl = dlopen (tmpfile, RTLD_NOW);
{% endraw %}

```