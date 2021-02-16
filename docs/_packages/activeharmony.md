---
name: "activeharmony"
layout: package
next_package: zabbix
previous_package: draco
languages: ['c']
---
## 4.6.0
5 / 312 files match

 - [example/code_generation/gemm.c](#examplecode_generationgemmc)
 - [src/hinfo.c](#srchinfoc)
 - [src/hplugin.c](#srchpluginc)

### example/code_generation/gemm.c

```c

{% raw %}
396 |     flib_eval = dlopen(filename, RTLD_LAZY);
{% endraw %}

```
### src/hinfo.c

```c

{% raw %}
239 |             handle = dlopen(cmd_arg, RTLD_LAZY | RTLD_LOCAL);
241 |                 fprintf(stderr, "Could not dlopen %s: %s\n",
431 |         handle = dlopen(fname, RTLD_LAZY | RTLD_LOCAL);
504 |                 handle = dlopen(fname, RTLD_LAZY | RTLD_LOCAL);
506 |                     fprintf(stderr, "Could not dlopen %s: %s\n",
513 |             handle = dlopen(fname, RTLD_LAZY | RTLD_LOCAL);
{% endraw %}

```
### src/hplugin.c

```c

{% raw %}
46 |     plugin->handle = dlopen(filename, RTLD_LAZY | RTLD_LOCAL);
{% endraw %}

```