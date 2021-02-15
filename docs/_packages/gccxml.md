---
name: "gccxml"
layout: package
next_package: elpa
previous_package: darshan-runtime
languages: ['cpp']
---
## latest
5 / 2115 files match

 - [GCC/gcc/sys-protos.h](#gccgccsys-protosh)
 - [GCC/gcc/config/darwin-crt3.c](#gccgccconfigdarwin-crt3c)
 - [GCC_XML/KWSys/DynamicLoader.cxx](#gcc_xmlkwsysdynamicloadercxx)
 - [GCC_XML/KWSys/DynamicLoader.hxx.in](#gcc_xmlkwsysdynamicloaderhxxin)
 - [GCC_XML/KWSys/testDynamicLoader.cxx](#gcc_xmlkwsystestdynamicloadercxx)

### GCC/gcc/sys-protos.h

```cpp

{% raw %}
236 | extern void *                 dlopen(char *, int);
{% endraw %}

```
### GCC/gcc/config/darwin-crt3.c

```cpp

{% raw %}
279 |       handle = dlopen ("/usr/lib/libSystem.B.dylib", RTLD_NOLOAD);
{% endraw %}

```
### GCC_XML/KWSys/DynamicLoader.cxx

```

{% raw %}
27 | // 4. Most unix systems (including Mac OS X 10.3 and later) which use dlopen
444 |   return dlopen(libname, RTLD_LAZY);
{% endraw %}

```
### GCC_XML/KWSys/DynamicLoader.hxx.in

```

{% raw %}
40 |  * \warning dlopen on *nix system works the following way:
{% endraw %}

```
### GCC_XML/KWSys/testDynamicLoader.cxx

```

{% raw %}
109 | // dlopen() on Syllable before 11/22/2007 doesn't return 0 on error
118 |   // This one is actually fun to test, since dlopen is by default loaded...wonder why :)
119 |   res += TestDynamicLoader("foobar.lib", "dlopen",0,1,0);
120 |   res += TestDynamicLoader("libdl.so", "dlopen",1,1,1);
{% endraw %}

```