---
name: "ldc"
layout: package
next_package: cquery
previous_package: enca
languages: ['c']
---
## 1.3.0
9 / 3909 files match, 2 filtered matches.

 - [runtime/druntime/test/shared/src/loadDR.c](#runtimedruntimetestsharedsrcloaddrc)
 - [runtime/druntime/test/shared/src/host.c](#runtimedruntimetestsharedsrchostc)

### runtime/druntime/test/shared/src/loadDR.c

```c

{% raw %}
9 |     void *h = dlopen(argv[1], RTLD_LAZY); // load druntime
{% endraw %}

```
### runtime/druntime/test/shared/src/host.c

```c

{% raw %}
9 |     void *druntime = dlopen(argv[1], RTLD_LAZY); // load druntime
18 |     void* plugin1 = dlopen(name, RTLD_LAZY);
20 |     void* plugin2 = dlopen(name, RTLD_LAZY);
38 |     plugin1 = dlopen(name, RTLD_LAZY);
{% endraw %}

```