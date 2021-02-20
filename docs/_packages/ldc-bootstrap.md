---
name: "ldc-bootstrap"
layout: package
next_package: legion
previous_package: ldc
languages: ['c']
---
## 0.17.4
8 / 2988 files match, 2 filtered matches.

 - [runtime/druntime/test/shared/src/loadDR.c](#runtimedruntimetestsharedsrcloaddrc)
 - [runtime/druntime/test/shared/src/host.c](#runtimedruntimetestsharedsrchostc)

### runtime/druntime/test/shared/src/loadDR.c

```c

{% raw %}
6 | {
7 |     if (argc != 2)
8 |         return EXIT_FAILURE;
9 |     void *h = dlopen(argv[1], RTLD_LAZY); // load druntime
10 |     assert(h != NULL);
11 | 
{% endraw %}

```
### runtime/druntime/test/shared/src/host.c

```c

{% raw %}
9 |     memcpy(name, argv[0], pathlen);
10 |     memcpy(name+pathlen, "plugin1.so", sizeof("plugin1.so"));
11 | 
12 |     void* plugin1 = dlopen(name, RTLD_LAZY);
13 |     name[pathlen + sizeof("plugin1.so") - 5] = '2';
14 |     void* plugin2 = dlopen(name, RTLD_LAZY);
15 | 
16 |     int (*plugin1_init)() = dlsym(plugin1, "plugin_init");
29 |     assert(runTests2());
30 | 
31 |     name[pathlen + sizeof("plugin1.so") - 5] = '1';
32 |     plugin1 = dlopen(name, RTLD_LAZY);
33 |     plugin1_init = dlsym(plugin1, "plugin_init");
34 |     plugin1_term = dlsym(plugin1, "plugin_term");
{% endraw %}

```