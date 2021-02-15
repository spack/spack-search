---
name: "activeharmony"
layout: package
next_package: zabbix
previous_package: draco
languages: ['cpp']
---
## 4.6.0
5 / 312 files match

 - [example/code_generation/gemm.c](#examplecode_generationgemmc)
 - [src/hinfo.c](#srchinfoc)
 - [src/hplugin.c](#srchpluginc)
 - [code-server/gemm/code.properties](#code-servergemmcodeproperties)
 - [code-server/generic/code.properties](#code-servergenericcodeproperties)

### example/code_generation/gemm.c

```cpp

{% raw %}
396 |     flib_eval = dlopen(filename, RTLD_LAZY);
{% endraw %}

```
### src/hinfo.c

```cpp

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

```cpp

{% raw %}
24 | #include <dlfcn.h>  // For dlopen(), dlsym(), dlerror(), and dlclose().
46 |     plugin->handle = dlopen(filename, RTLD_LAZY | RTLD_LOCAL);
{% endraw %}

```
### code-server/gemm/code.properties

```

{% raw %}
62 | #  the new code using dlopen/dlsym, we should compile the code to .so. If
{% endraw %}

```
### code-server/generic/code.properties

```

{% raw %}
52 | #  the new code using dlopen/dlsym, we should compile the code to .so. If
{% endraw %}

```