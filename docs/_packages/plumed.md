---
name: "plumed"
layout: package
next_package: pmdk
previous_package: plplot
languages: ['c']
---
## 2.5.1
15 / 5058 files match, 3 filtered matches.

 - [src/wrapper/Plumed.h](#srcwrapperplumedh)
 - [src/core/PlumedMainInitializer.h](#srccoreplumedmaininitializerh)
 - [src/tools/PlumedHandle.h](#srctoolsplumedhandleh)

### src/wrapper/Plumed.h

```c

{% raw %}
112 |   (C)        plumed_create_dlopen
113 |   (C++)      PLMD::Plumed::dlopen
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
1566 |     auto p = PLMD::Plumed::dlopen("/path/to/libplumedKernel.so");
1570 |   static Plumed dlopen(const char* path)__PLUMED_WRAPPER_CXX_NOEXCEPT  {
1572 |     return Plumed(plumed_create_dlopen(path)).decref();
1578 |     Same as \ref dlopen(const char* path), but allows a dlopen mode to be chosen explicitly.
1580 |   static Plumed dlopen(const char* path,int mode)__PLUMED_WRAPPER_CXX_NOEXCEPT  {
1582 |     return Plumed(plumed_create_dlopen2(path,mode)).decref();
1678 |   plumed p=Plumed::dlopen(path).incref()
2020 | Try to dlopen a path with a given mode.
2021 | If the dlopen command fails, it tries to strip the `Kernel` part of the name.
2028 | void* plumed_attempt_dlopen(const char*path,int mode) {
2045 |   p=dlopen(path,mode);
2054 |     __PLUMED_FPRINTF(stderr,"+++ An error occurred. Message from dlopen(): %s +++\n",dlerror());
2072 |       p=dlopen(pathcopy,mode);
2073 |       if(!p) __PLUMED_FPRINTF(stderr,"+++ An error occurred. Message from dlopen(): %s +++\n",dlerror());
2096 | Search symbols in a dlopened library.
2211 |   If handle is not NULL, it is used to return a dlopen handle that could be subsequently dlclosed.
2226 |     When dlopen is not available, we hard code them to NULL
2228 |   fprintf(stderr,"+++ PLUMED has been compiled without dlopen and without a static kernel +++\n");
2242 |   int dlopenmode;
2249 |   dlopenmode=0;
2269 |     dlopenmode=RTLD_NOW;
2271 |       dlopenmode=dlopenmode|RTLD_LOCAL;
2274 |       dlopenmode=dlopenmode|RTLD_GLOBAL;
2279 |       dlopenmode=dlopenmode|RTLD_DEEPBIND;
2284 |     p=plumed_attempt_dlopen(path,dlopenmode);
2394 | plumed plumed_create_dlopen(const char*path) {
2395 |   int dlopenmode;
2398 |   dlopenmode=RTLD_NOW|RTLD_LOCAL;
2400 |   dlopenmode=dlopenmode|RTLD_DEEPBIND;
2403 |   dlopenmode=0;
2405 |   return plumed_create_dlopen2(path,dlopenmode);
2410 | plumed plumed_create_dlopen2(const char*path,int mode) {
2418 |   if(path) pimpl->dlhandle=plumed_attempt_dlopen(path,mode);
2735 | __PLUMED_IMPLEMENT_FORTRAN(plumed_f_create_dlopen,PLUMED_F_CREATE_DLOPEN,(char*path,char*c),(path,c)) {
2736 |   plumed_c2f(plumed_create_dlopen(path),c);
{% endraw %}

```
### src/core/PlumedMainInitializer.h

```c

{% raw %}
82 |   In principle, it should be accessed by other programs dlopening the plumed kernel.
{% endraw %}

```
### src/tools/PlumedHandle.h

```c

{% raw %}
60 | PlumedHandle p(PlumedHandle::dlopen("/path/to/libplumedkernel.so");
120 |   static PlumedHandle dlopen(const char* path);
{% endraw %}

```