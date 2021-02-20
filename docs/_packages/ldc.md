---
name: "ldc"
layout: package
next_package: ldc-bootstrap
previous_package: lammps
languages: ['c']
---
## 1.3.0
9 / 3909 files match, 2 filtered matches.

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
6 | {
7 | #if defined(__FreeBSD__)
8 |     // workaround for Bugzilla 14824
9 |     void *druntime = dlopen(argv[1], RTLD_LAZY); // load druntime
10 |     assert(druntime);
11 | #endif
15 |     memcpy(name, argv[0], pathlen);
16 |     memcpy(name+pathlen, "plugin1.so", sizeof("plugin1.so"));
17 | 
18 |     void* plugin1 = dlopen(name, RTLD_LAZY);
19 |     name[pathlen + sizeof("plugin1.so") - 5] = '2';
20 |     void* plugin2 = dlopen(name, RTLD_LAZY);
21 | 
22 |     int (*plugin1_init)() = dlsym(plugin1, "plugin_init");
35 |     assert(runTests2());
36 | 
37 |     name[pathlen + sizeof("plugin1.so") - 5] = '1';
38 |     plugin1 = dlopen(name, RTLD_LAZY);
39 |     plugin1_init = dlsym(plugin1, "plugin_init");
40 |     plugin1_term = dlsym(plugin1, "plugin_term");
{% endraw %}

```