---
name: "dmd"
layout: package
next_package: qt
previous_package: xedit
languages: ['cpp']
---
## 2.081.1
11 / 4009 files match

 - [src/dmd/link.d](#srcdmdlinkd)
 - [phobos/std/net/curl.d](#phobosstdnetcurld)
 - [druntime/src/rt/sections_elf_shared.d](#druntimesrcrtsections_elf_sharedd)
 - [druntime/src/core/sys/posix/dlfcn.d](#druntimesrccoresysposixdlfcnd)
 - [druntime/src/core/sys/linux/dlfcn.d](#druntimesrccoresyslinuxdlfcnd)
 - [druntime/src/core/sys/dragonflybsd/dlfcn.d](#druntimesrccoresysdragonflybsddlfcnd)
 - [druntime/src/core/sys/freebsd/dlfcn.d](#druntimesrccoresysfreebsddlfcnd)
 - [druntime/src/core/sys/netbsd/dlfcn.d](#druntimesrccoresysnetbsddlfcnd)
 - [druntime/test/shared/src/loadDR.c](#druntimetestsharedsrcloaddrc)
 - [druntime/test/shared/src/host.c](#druntimetestsharedsrchostc)
 - [druntime/test/shared/src/load.d](#druntimetestsharedsrcloadd)

### src/dmd/link.d

```

{% raw %}
657 |             // Link against libdl for phobos usage of dlopen
{% endraw %}

```
### phobos/std/net/curl.d

```

{% raw %}
4123 |             import core.sys.posix.dlfcn : dlsym, dlopen, dlclose, RTLD_LAZY;
4137 |             handle = dlopen(null, RTLD_LAZY);
4162 |                     handle = dlopen(name.ptr, RTLD_LAZY);
{% endraw %}

```
### druntime/src/rt/sections_elf_shared.d

```

{% raw %}
193 |                 // Increment the dlopen ref for explicitly loaded libraries to pin them.
194 |                 .dlopen(linkMapForHandle(tdso._pdso._handle).l_name, RTLD_LAZY) !is null || assert(0);
232 |     // Called after all TLS dtors ran, decrements all remaining dlopen refs.
401 |                  * the first dlopen call from a C program.
421 |             // rt_loadLibrary will run tls ctors, so do this only for dlopen
539 |         auto handle = .dlopen(name, RTLD_LAZY);
720 |         auto handle = .dlopen(name, RTLD_NOLOAD | RTLD_LAZY);
873 |  *      the dlopen handle for that DSO or null if addr is not within a loaded DSO
{% endraw %}

```
### druntime/src/core/sys/posix/dlfcn.d

```

{% raw %}
43 | void* dlopen(in char*, int);
124 |     void* dlopen(in char*, int);
150 |     void* dlopen(in char*, int);
171 |     void* dlopen(in char*, int);
194 |     void* dlopen(in char*, int);
215 |     void* dlopen(in char*, int);
236 |     void* dlopen(in char*, int);
257 |     void* dlopen(in char*, int);
282 |     void*        dlopen(in char*, int);
305 |     void*        dlopen(in char*, int);
345 |     void* dlopen(in char*, int);
{% endraw %}

```
### druntime/src/core/sys/linux/dlfcn.d

```

{% raw %}
270 | // void* dlopen(in char* __file, int __mode); // POSIX
{% endraw %}

```
### druntime/src/core/sys/dragonflybsd/dlfcn.d

```

{% raw %}
17 |  * Modes and flags for dlopen().
92 | static assert(is(typeof(&dlopen)  == __externC!(void*, const char*, int)));
95 | void*    fdlopen(int, int);
{% endraw %}

```
### druntime/src/core/sys/freebsd/dlfcn.d

```

{% raw %}
19 |  * Modes and flags for dlopen().
96 | static assert(is(typeof(&dlopen)  == __externC!(void*, const char*, int)));
101 |     void*    fdlopen(int, int);
{% endraw %}

```
### druntime/src/core/sys/netbsd/dlfcn.d

```

{% raw %}
21 |  * Modes and flags for dlopen().
97 | static assert(is(typeof(&dlopen)  == __externC!(void*, const char*, int)));
102 |     //void*    fdlopen(int, int);
{% endraw %}

```
### druntime/test/shared/src/loadDR.c

```cpp

{% raw %}
9 |     void *h = dlopen(argv[1], RTLD_LAZY); // load druntime
{% endraw %}

```
### druntime/test/shared/src/host.c

```cpp

{% raw %}
9 |     void *druntime = dlopen(argv[1], RTLD_LAZY); // load druntime
14 |     void *druntime = dlopen(argv[1], RTLD_LAZY); // load druntime
23 |     void* plugin1 = dlopen(name, RTLD_LAZY);
25 |     void* plugin2 = dlopen(name, RTLD_LAZY);
43 |     plugin1 = dlopen(name, RTLD_LAZY);
{% endraw %}

```
### druntime/test/shared/src/load.d

```

{% raw %}
141 |     assert(.dlopen(name.ptr, RTLD_LAZY | RTLD_NOLOAD) is null);
{% endraw %}

```