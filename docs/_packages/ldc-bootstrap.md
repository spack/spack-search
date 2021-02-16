---
name: "ldc-bootstrap"
layout: package
next_package: sshpass
previous_package: lvm2
languages: ['c']
---
## 0.17.4
8 / 2988 files match, 2 filtered matches.

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
12 |     void* plugin1 = dlopen(name, RTLD_LAZY);
14 |     void* plugin2 = dlopen(name, RTLD_LAZY);
32 |     plugin1 = dlopen(name, RTLD_LAZY);
{% endraw %}

```