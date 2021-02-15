---
name: "plumed"
layout: package
next_package: openmolcas
previous_package: meson
languages: ['cpp']
---
## 2.5.1
15 / 5058 files match

 - [configure.ac](#configureac)
 - [src/wrapper/Plumed.h](#srcwrapperplumedh)
 - [src/molfile/vmdplugin.h](#srcmolfilevmdpluginh)
 - [src/generic/Plumed.cpp](#srcgenericplumedcpp)
 - [src/core/PlumedMainInitializer.h](#srccoreplumedmaininitializerh)
 - [src/core/CLToolMain.cpp](#srccorecltoolmaincpp)
 - [src/core/PlumedMainInitializer.cpp](#srccoreplumedmaininitializercpp)
 - [src/tools/DLLoader.cpp](#srctoolsdlloadercpp)
 - [src/tools/PlumedHandle.h](#srctoolsplumedhandleh)
 - [src/tools/PlumedHandle.cpp](#srctoolsplumedhandlecpp)
 - [src/tools/DLLoader.h](#srctoolsdlloaderh)
 - [regtest/basic/rt-make-wrappers/main.cpp](#regtestbasicrt-make-wrappersmaincpp)
 - [developer-doc/Doc.txt](#developer-docdoctxt)
 - [python/plumed.pyx](#pythonplumedpyx)
 - [python/cplumed.pxd](#pythoncplumedpxd)

### configure.ac

```

{% raw %}
254 | PLUMED_CONFIG_ENABLE([dlopen],[search for dlopen],[yes])
626 | AC_CHECK_LIB([dl],dlopen, [STATIC_LIBS="-ldl $STATIC_LIBS"] [LIBS="-ldl $LIBS"])
649 | if test $dlopen == true ; then
650 |   PLUMED_CHECK_PACKAGE([dlfcn.h],[dlopen],[__PLUMED_HAS_DLOPEN])
{% endraw %}

```
### src/wrapper/Plumed.h

```cpp

{% raw %}
112 |   (C)        plumed_create_dlopen
113 |   (C++)      PLMD::Plumed::dlopen
114 |   (FORTRAN)  PLUMED_F_CREATE_DLOPEN
211 |     SUBROUTINE PLUMED_F_CREATE_DLOPEN(p,path)
341 |   In other words, every \ref plumed_create, \ref plumed_create_dlopen, \ref plumed_create_reference,
362 |   simultaneously, although the preferred way to do this is using the function \ref plumed_create_dlopen.
364 |   \ref plumed_create_dlopen does it automatically, whereas loading through env var `PLUMED_KERNEL` only does it if
371 |     (\ref plumed_create_dlopen() and \ref PLMD::Plumed::dlopen()).
645 | plumed plumed_create_dlopen(const char*path);
652 |   Same as \ref plumed_create_dlopen, but also allows to specify the mode for dlopen.
658 | plumed plumed_create_dlopen2(const char*path,int mode);
714 |    plumed_create_dlopen with an incorrect path (or plumed_create using runtime binding
1556 |     It returns an object created with \ref plumed_create_dlopen. The object is owned and
1559 |     PLMD::Plumed p = PLMD::Plumed::dlopen("/path/to/libplumedKernel.so");
1561 |   //    PLMD::Plumed p(PLMD::Plumed::dlopen("/path/to/libplumedKernel.so"));
1566 |     auto p = PLMD::Plumed::dlopen("/path/to/libplumedKernel.so");
1570 |   static Plumed dlopen(const char* path)__PLUMED_WRAPPER_CXX_NOEXCEPT  {
1572 |     return Plumed(plumed_create_dlopen(path)).decref();
1578 |     Same as \ref dlopen(const char* path), but allows a dlopen mode to be chosen explicitly.
1580 |   static Plumed dlopen(const char* path,int mode)__PLUMED_WRAPPER_CXX_NOEXCEPT  {
1582 |     return Plumed(plumed_create_dlopen2(path,mode)).decref();
1678 |   plumed p=Plumed::dlopen(path).incref()
1902 | #ifdef __PLUMED_HAS_DLOPEN
1903 | #include <dlfcn.h> /* dlopen dlerror dlsym */
2018 | #if defined( __PLUMED_HAS_DLOPEN) /*{*/
2020 | Try to dlopen a path with a given mode.
2021 | If the dlopen command fails, it tries to strip the `Kernel` part of the name.
2028 | void* plumed_attempt_dlopen(const char*path,int mode) {
2045 |   p=dlopen(path,mode);
2054 |     __PLUMED_FPRINTF(stderr,"+++ An error occurred. Message from dlopen(): %s +++\n",dlerror());
2072 |       p=dlopen(pathcopy,mode);
2073 |       if(!p) __PLUMED_FPRINTF(stderr,"+++ An error occurred. Message from dlopen(): %s +++\n",dlerror());
2096 | Search symbols in a dlopened library.
2211 |   If handle is not NULL, it is used to return a dlopen handle that could be subsequently dlclosed.
2224 | #elif ! defined(__PLUMED_HAS_DLOPEN)
2226 |     When dlopen is not available, we hard code them to NULL
2228 |   fprintf(stderr,"+++ PLUMED has been compiled without dlopen and without a static kernel +++\n");
2242 |   int dlopenmode;
2249 |   dlopenmode=0;
2269 |     dlopenmode=RTLD_NOW;
2271 |       dlopenmode=dlopenmode|RTLD_LOCAL;
2274 |       dlopenmode=dlopenmode|RTLD_GLOBAL;
2279 |       dlopenmode=dlopenmode|RTLD_DEEPBIND;
2284 |     p=plumed_attempt_dlopen(path,dlopenmode);
2304 |   /* handler to dlopened library. NULL if there was no library opened */
2394 | plumed plumed_create_dlopen(const char*path) {
2395 |   int dlopenmode;
2396 |   /* plumed_create_dlopen always uses RTLD_LOCAL and, when possible, RTLD_DEEPBIND to allow multiple versions */
2397 | #ifdef __PLUMED_HAS_DLOPEN
2398 |   dlopenmode=RTLD_NOW|RTLD_LOCAL;
2400 |   dlopenmode=dlopenmode|RTLD_DEEPBIND;
2403 |   dlopenmode=0;
2405 |   return plumed_create_dlopen2(path,dlopenmode);
2410 | plumed plumed_create_dlopen2(const char*path,int mode) {
2417 | #ifdef __PLUMED_HAS_DLOPEN
2418 |   if(path) pimpl->dlhandle=plumed_attempt_dlopen(path,mode);
2541 | #ifdef __PLUMED_HAS_DLOPEN
2735 | __PLUMED_IMPLEMENT_FORTRAN(plumed_f_create_dlopen,PLUMED_F_CREATE_DLOPEN,(char*path,char*c),(path,c)) {
2736 |   plumed_c2f(plumed_create_dlopen(path),c);
{% endraw %}

```
### src/molfile/vmdplugin.h

```cpp

{% raw %}
89 |  *  and fini routines via dlopen() or similar operating system interfaces.
220 |  * This API is optional; if found by dlopen, it will be called after first
{% endraw %}

```
### src/generic/Plumed.cpp

```

{% raw %}
29 | #ifdef __PLUMED_HAS_DLOPEN
209 |     return PlumedHandle::dlopen(kernel.c_str());
{% endraw %}

```
### src/core/PlumedMainInitializer.h

```cpp

{% raw %}
82 |   In principle, it should be accessed by other programs dlopening the plumed kernel.
{% endraw %}

```
### src/core/CLToolMain.cpp

```

{% raw %}
160 |     } else if(a=="--has-dlopen") {
161 |       return (config::hasDlopen()?0:1);
231 |       "  [--has-dlopen]            : fails if plumed is compiled without dlopen\n"
{% endraw %}

```
### src/core/PlumedMainInitializer.cpp

```

{% raw %}
28 | #if defined __PLUMED_HAS_DLOPEN
205 | #if defined(__PLUMED_HAS_DLOPEN)
217 |     handle=dlopen(NULL,RTLD_LOCAL);
218 |     if(debug) fprintf(stderr,"+++ Registering functions. dlopen handle at %p +++\n",handle);
239 | // - on Linux if we don't use RTLD_DEFAULT, since dlopen(NULL,RTLD_LOCAL) returns a null pointer.
{% endraw %}

```
### src/tools/DLLoader.cpp

```

{% raw %}
23 | #ifdef __PLUMED_HAS_DLOPEN
30 | #ifdef __PLUMED_HAS_DLOPEN
39 | #ifdef __PLUMED_HAS_DLOPEN
40 |   void* p=dlopen(s.c_str(),RTLD_NOW|RTLD_LOCAL);
58 | #ifdef __PLUMED_HAS_DLOPEN
{% endraw %}

```
### src/tools/PlumedHandle.h

```cpp

{% raw %}
60 | PlumedHandle p(PlumedHandle::dlopen("/path/to/libplumedkernel.so");
62 | // auto p=PlumedHandle::dlopen("/path/to/libplumedkernel.so");
99 | /// Used when kernel is dlopened.
102 | /// Used when kernel is dlopened.
105 | /// Used when kernel is dlopened.
108 | /// Used when kernel is dlopened.
120 |   static PlumedHandle dlopen(const char* path);
122 | /// In case a kernel was dlopened, it dlcloses it.
{% endraw %}

```
### src/tools/PlumedHandle.cpp

```

{% raw %}
25 | #ifdef __PLUMED_HAS_DLOPEN
33 | #ifdef __PLUMED_HAS_DLOPEN
44 | #ifdef __PLUMED_HAS_DLOPEN
53 |   void* h=::dlopen(kernel,mode);
61 |       h=::dlopen(k.c_str(),mode);
114 |   plumed_error() << "You are trying to dynamically load a kernel, but PLUMED was compiled without dlopen";
119 | #ifdef __PLUMED_HAS_DLOPEN
124 | PlumedHandle PlumedHandle::dlopen(const char* path) {
{% endraw %}

```
### src/tools/DLLoader.h

```cpp

{% raw %}
31 | /// It contains wrappers to the dlopen() routine.
{% endraw %}

```
### regtest/basic/rt-make-wrappers/main.cpp

```

{% raw %}
16 |   void plumed_f_create_dlopen(char*p,char*c);
29 |   void plumed_f_create_dlopen_(char*p,char*c);
42 |   void plumed_f_create_dlopen__(char*p,char*c);
55 |   void PLUMED_F_CREATE_DLOPEN(char*p,char*c);
68 |   void PLUMED_F_CREATE_DLOPEN_(char*p,char*c);
81 |   void PLUMED_F_CREATE_DLOPEN__(char*p,char*c);
205 | // test dlopen
206 |       PLMD::Plumed p(PLMD::Plumed::dlopen(std::getenv("PLUMED_KERNEL")));
297 | // test dlopen
298 |       plumed p=plumed_create_dlopen(std::getenv("PLUMED_KERNEL"));
346 | // test dlopen
348 |       plumed_f_create_dlopen(std::getenv("PLUMED_KERNEL"),p);
395 | // test dlopen
397 |       plumed_f_create_dlopen_(std::getenv("PLUMED_KERNEL"),p);
444 | // test dlopen
446 |       plumed_f_create_dlopen__(std::getenv("PLUMED_KERNEL"),p);
493 | // test dlopen
495 |       PLUMED_F_CREATE_DLOPEN(std::getenv("PLUMED_KERNEL"),p);
542 | // test dlopen
544 |       PLUMED_F_CREATE_DLOPEN_(std::getenv("PLUMED_KERNEL"),p);
591 | // test dlopen
593 |       PLUMED_F_CREATE_DLOPEN__(std::getenv("PLUMED_KERNEL"),p);
{% endraw %}

```
### developer-doc/Doc.txt

```

{% raw %}
76 |   for recompilation. If dlopen() is available on a system, it should be possible
{% endraw %}

```
### python/plumed.pyx

```

{% raw %}
49 |             self.c_plumed=cplumed.Plumed.dlopen(ckernel)
{% endraw %}

```
### python/cplumed.pxd

```

{% raw %}
36 |          Plumed dlopen(const char*path) except +
{% endraw %}

```