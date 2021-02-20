---
name: "dmd"
layout: package
next_package: dmtcp
previous_package: dimemas
languages: ['c']
---
## 2.081.1
11 / 4009 files match, 2 filtered matches.

 - [druntime/test/shared/src/loadDR.c](#druntimetestsharedsrcloaddrc)
 - [druntime/test/shared/src/host.c](#druntimetestsharedsrchostc)

### druntime/test/shared/src/loadDR.c

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
### druntime/test/shared/src/host.c

```c

{% raw %}
6 | {
7 | #if defined(__FreeBSD__)
8 |     // workaround for Bugzilla 14824
9 |     void *druntime = dlopen(argv[1], RTLD_LAZY); // load druntime
10 |     assert(druntime);
11 | #endif
12 | #if defined(__DragonFly__)
13 |     // workaround for Bugzilla 14824
14 |     void *druntime = dlopen(argv[1], RTLD_LAZY); // load druntime
15 |     assert(druntime);
16 | #endif
20 |     memcpy(name, argv[0], pathlen);
21 |     memcpy(name+pathlen, "plugin1.so", sizeof("plugin1.so"));
22 | 
23 |     void* plugin1 = dlopen(name, RTLD_LAZY);
24 |     name[pathlen + sizeof("plugin1.so") - 5] = '2';
25 |     void* plugin2 = dlopen(name, RTLD_LAZY);
26 | 
27 |     int (*plugin1_init)() = dlsym(plugin1, "plugin_init");
40 |     assert(runTests2());
41 | 
42 |     name[pathlen + sizeof("plugin1.so") - 5] = '1';
43 |     plugin1 = dlopen(name, RTLD_LAZY);
44 |     plugin1_init = dlsym(plugin1, "plugin_init");
45 |     plugin1_term = dlsym(plugin1, "plugin_term");
{% endraw %}

```