---
name: "ldc"
layout: package
next_package: cquery
previous_package: enca
languages: ['cpp']
---
## 1.3.0
9 / 3909 files match

 - [runtime/phobos/std/net/curl.d](#runtimephobosstdnetcurld)
 - [runtime/druntime/src/rt/sections_elf_shared.d](#runtimedruntimesrcrtsections_elf_sharedd)
 - [runtime/druntime/src/core/sys/posix/dlfcn.d](#runtimedruntimesrccoresysposixdlfcnd)
 - [runtime/druntime/src/core/sys/linux/dlfcn.d](#runtimedruntimesrccoresyslinuxdlfcnd)
 - [runtime/druntime/src/core/sys/freebsd/dlfcn.d](#runtimedruntimesrccoresysfreebsddlfcnd)
 - [runtime/druntime/src/core/sys/netbsd/dlfcn.d](#runtimedruntimesrccoresysnetbsddlfcnd)
 - [runtime/druntime/test/shared/src/loadDR.c](#runtimedruntimetestsharedsrcloaddrc)
 - [runtime/druntime/test/shared/src/host.c](#runtimedruntimetestsharedsrchostc)
 - [runtime/druntime/test/shared/src/load.d](#runtimedruntimetestsharedsrcloadd)

### runtime/phobos/std/net/curl.d

```

{% raw %}
3898 |             import core.sys.posix.dlfcn : dlsym, dlopen, dlclose, RTLD_LAZY;
3912 |             handle = dlopen(null, RTLD_LAZY);
3936 |                     handle = dlopen(name.ptr, RTLD_LAZY);
{% endraw %}

```
### runtime/druntime/src/rt/sections_elf_shared.d

```

{% raw %}
205 |                 // Increment the dlopen ref for explicitly loaded libraries to pin them.
206 |                 .dlopen(nameForDSO(tdso._pdso), RTLD_LAZY) !is null || assert(0);
244 |     // Called after all TLS dtors ran, decrements all remaining dlopen refs.
352 |      * Hash table to map the native handle (as returned by dlopen)
482 |                  * the first dlopen call from a C program.
513 |             // rt_loadLibrary will run tls ctors, so do this only for dlopen
636 |         auto handle = .dlopen(name, RTLD_LAZY);
818 |         auto handle = .dlopen(name, RTLD_NOLOAD | RTLD_LAZY);
1145 |  *      the dlopen handle for that DSO or null if addr is not within a loaded DSO
{% endraw %}

```
### runtime/druntime/src/core/sys/posix/dlfcn.d

```

{% raw %}
43 | void* dlopen(in char*, int);
117 |     void* dlopen(in char*, int);
143 |     void* dlopen(in char*, int);
168 |     void* dlopen(in char*, int);
191 |     void* dlopen(in char*, int);
212 |     void* dlopen(in char*, int);
233 |     void* dlopen(in char*, int);
258 |     void*        dlopen(in char*, int);
{% endraw %}

```
### runtime/druntime/src/core/sys/linux/dlfcn.d

```

{% raw %}
245 | // void* dlopen(in char* __file, int __mode); // POSIX
{% endraw %}

```
### runtime/druntime/src/core/sys/freebsd/dlfcn.d

```

{% raw %}
18 |  * Modes and flags for dlopen().
95 | static assert(is(typeof(&dlopen)  == __externC!(void*, const char*, int)));
100 |     void*    fdlopen(int, int);
{% endraw %}

```
### runtime/druntime/src/core/sys/netbsd/dlfcn.d

```

{% raw %}
21 |  * Modes and flags for dlopen().
97 | static assert(is(typeof(&dlopen)  == __externC!(void*, const char*, int)));
102 |     //void*    fdlopen(int, int);
{% endraw %}

```
### runtime/druntime/test/shared/src/loadDR.c

```cpp

{% raw %}
9 |     void *h = dlopen(argv[1], RTLD_LAZY); // load druntime
{% endraw %}

```
### runtime/druntime/test/shared/src/host.c

```cpp

{% raw %}
9 |     void *druntime = dlopen(argv[1], RTLD_LAZY); // load druntime
18 |     void* plugin1 = dlopen(name, RTLD_LAZY);
20 |     void* plugin2 = dlopen(name, RTLD_LAZY);
38 |     plugin1 = dlopen(name, RTLD_LAZY);
{% endraw %}

```
### runtime/druntime/test/shared/src/load.d

```

{% raw %}
138 |     assert(.dlopen(name.ptr, RTLD_LAZY | RTLD_NOLOAD) is null);
{% endraw %}

```