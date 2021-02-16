---
name: "dmd"
layout: package
next_package: qt
previous_package: xedit
languages: ['c']
---
## 2.081.1
11 / 4009 files match, 2 filtered matches.

 - [druntime/test/shared/src/loadDR.c](#druntimetestsharedsrcloaddrc)
 - [druntime/test/shared/src/host.c](#druntimetestsharedsrchostc)

### druntime/test/shared/src/loadDR.c

```c

{% raw %}
9 |     void *h = dlopen(argv[1], RTLD_LAZY); // load druntime
{% endraw %}

```
### druntime/test/shared/src/host.c

```c

{% raw %}
9 |     void *druntime = dlopen(argv[1], RTLD_LAZY); // load druntime
14 |     void *druntime = dlopen(argv[1], RTLD_LAZY); // load druntime
23 |     void* plugin1 = dlopen(name, RTLD_LAZY);
25 |     void* plugin2 = dlopen(name, RTLD_LAZY);
43 |     plugin1 = dlopen(name, RTLD_LAZY);
{% endraw %}

```