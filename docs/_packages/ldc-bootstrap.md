---
name: "ldc-bootstrap"
layout: package
next_package: sshpass
previous_package: lvm2
languages: ['cpp']
---
## 0.17.4
8 / 2988 files match

 - [runtime/phobos/std/net/curl.d](#runtimephobosstdnetcurld)
 - [runtime/druntime/src/rt/sections_elf_shared.d](#runtimedruntimesrcrtsections_elf_sharedd)
 - [runtime/druntime/src/core/sys/posix/dlfcn.d](#runtimedruntimesrccoresysposixdlfcnd)
 - [runtime/druntime/src/core/sys/linux/dlfcn.d](#runtimedruntimesrccoresyslinuxdlfcnd)
 - [runtime/druntime/src/core/sys/freebsd/dlfcn.d](#runtimedruntimesrccoresysfreebsddlfcnd)
 - [runtime/druntime/test/shared/src/loadDR.c](#runtimedruntimetestsharedsrcloaddrc)
 - [runtime/druntime/test/shared/src/host.c](#runtimedruntimetestsharedsrchostc)
 - [runtime/druntime/test/shared/src/load.d](#runtimedruntimetestsharedsrcloadd)

### runtime/phobos/std/net/curl.d

```

{% raw %}
3629 |             handle = dlopen(null, RTLD_LAZY);
3650 |                     handle = dlopen(name.ptr, RTLD_LAZY);
{% endraw %}

```
### runtime/druntime/src/rt/sections_elf_shared.d

```

{% raw %}
170 |                 // Increment the dlopen ref for explicitly loaded libraries to pin them.
171 |                 .dlopen(linkMapForHandle(tdso._pdso._handle).l_name, RTLD_LAZY) !is null || assert(0);
204 |     // Called after all TLS dtors ran, decrements all remaining dlopen refs.
373 |                  * the first dlopen call from a C program.
401 |             // rt_loadLibrary will run tls ctors, so do this only for dlopen
514 |         auto handle = .dlopen(name, RTLD_LAZY);
676 |         auto handle = .dlopen(name, RTLD_NOLOAD | RTLD_LAZY);
883 |  *      the dlopen handle for that DSO or null if addr is not within a loaded DSO
{% endraw %}

```
### runtime/druntime/src/core/sys/posix/dlfcn.d

```

{% raw %}
34 | void* dlopen(in char*, int);
108 |     void* dlopen(in char*, int);
134 |     void* dlopen(in char*, int);
155 |     void* dlopen(in char*, int);
176 |     void* dlopen(in char*, int);
201 |     void*        dlopen(in char*, int);
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
### runtime/druntime/test/shared/src/loadDR.c

```cpp

{% raw %}
9 |     void *h = dlopen(argv[1], RTLD_LAZY); // load druntime
{% endraw %}

```
### runtime/druntime/test/shared/src/host.c

```cpp

{% raw %}
12 |     void* plugin1 = dlopen(name, RTLD_LAZY);
14 |     void* plugin2 = dlopen(name, RTLD_LAZY);
32 |     plugin1 = dlopen(name, RTLD_LAZY);
{% endraw %}

```
### runtime/druntime/test/shared/src/load.d

```

{% raw %}
136 |     assert(.dlopen(name.ptr, RTLD_LAZY | RTLD_NOLOAD) is null);
{% endraw %}

```