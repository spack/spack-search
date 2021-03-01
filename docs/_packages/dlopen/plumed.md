---
name: "plumed"
layout: package
next_package: pmdk
previous_package: php
library_name: dlopen
matches: ['dlsym', 'dlopen']
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
109 |   As of PLUMED 2.5, you can also initialize a plumed object using the following functions,
110 |   that load a specific kernel:
111 | \verbatim
112 |   (C)        plumed_create_dlopen
113 |   (C++)      PLMD::Plumed::dlopen
114 |   (FORTRAN)  PLUMED_F_CREATE_DLOPEN
115 | \endverbatim
338 | // now plumed has been really finalized
339 | \endverbatim
340 | 
341 |   In other words, every \ref plumed_create, \ref plumed_create_dlopen, \ref plumed_create_reference,
342 |   \ref plumed_create_reference_f, and \ref plumed_create_reference_v call must be matched by a \ref plumed_finalize.
343 |   Notice that in C++ whenever an object goes out of scope the reference counter
359 | 
360 |   Another difference is that the value of the variable `PLUMED_KERNEL` is read every time a new
361 |   plumed object is instantiated. So, you might even use it to load different plumed versions
362 |   simultaneously, although the preferred way to do this is using the function \ref plumed_create_dlopen.
363 |   Notice that if you want to load multiple versions simultaneously you should load them in a local namespace.
364 |   \ref plumed_create_dlopen does it automatically, whereas loading through env var `PLUMED_KERNEL` only does it if
365 |   you also set env var `PLUMED_NAMESPACE=LOCAL`.
366 | 
368 |   - Functions to find if a plumed object is valid
369 |     (\ref plumed_valid(), \ref plumed_gvalid(), \ref PLMD::Plumed::valid(), and \ref PLMD::Plumed::gvalid()).
370 |   - Functions to create a plumed object based on the path of a specific kernel
371 |     (\ref plumed_create_dlopen() and \ref PLMD::Plumed::dlopen()).
372 |   - Functions to create a plumed object referencing to another one, implementing a reference counter
373 |     (\ref plumed_create_reference(), \ref plumed_create_reference_v(), \ref plumed_create_reference_f().
642 |     \return The constructed plumed object
643 | */
644 | __PLUMED_WRAPPER_C_BEGIN
645 | plumed plumed_create_dlopen(const char*path);
646 | __PLUMED_WRAPPER_C_END
647 | 
649 | /**
650 |   \brief Constructor from path. Available as of PLUMED 2.5
651 | 
652 |   Same as \ref plumed_create_dlopen, but also allows to specify the mode for dlopen.
653 | 
654 |   \warning
655 |   Use with care, since not all the possible modes work correctly with PLUMED.
656 | */
657 | __PLUMED_WRAPPER_C_BEGIN
658 | plumed plumed_create_dlopen2(const char*path,int mode);
659 | __PLUMED_WRAPPER_C_END
660 | 
711 |     \brief Constructor as invalid. Available as of PLUMED 2.5
712 | 
713 |    Can be used to create an object in the same state as if it was returned by
714 |    plumed_create_dlopen with an incorrect path (or plumed_create using runtime binding
715 |    and an incorrect PLUMED_KERNEL).
716 | 
1553 |   /**
1554 |     Create a PLUMED object loading a specific kernel. Available as of PLUMED 2.5.
1555 | 
1556 |     It returns an object created with \ref plumed_create_dlopen. The object is owned and
1557 |     is then finalized in the destructor. It can be used as follows:
1558 |   \verbatim
1559 |     PLMD::Plumed p = PLMD::Plumed::dlopen("/path/to/libplumedKernel.so");
1560 |   // or, equivalenty:
1561 |   //    PLMD::Plumed p(PLMD::Plumed::dlopen("/path/to/libplumedKernel.so"));
1563 |   \endverbatim
1564 |     or, equivalently, as
1565 |   \verbatim
1566 |     auto p = PLMD::Plumed::dlopen("/path/to/libplumedKernel.so");
1567 |     p.cmd("init");
1568 |   \endverbatim
1569 |   */
1570 |   static Plumed dlopen(const char* path)__PLUMED_WRAPPER_CXX_NOEXCEPT  {
1571 | // use decref to remove the extra reference
1572 |     return Plumed(plumed_create_dlopen(path)).decref();
1573 |   }
1574 | 
1575 |   /**
1576 |     Create a PLUMED object loading a specific kernel. Available as of PLUMED 2.5.
1577 | 
1578 |     Same as \ref dlopen(const char* path), but allows a dlopen mode to be chosen explicitly.
1579 |   */
1580 |   static Plumed dlopen(const char* path,int mode)__PLUMED_WRAPPER_CXX_NOEXCEPT  {
1581 | // use decref to remove the extra reference
1582 |     return Plumed(plumed_create_dlopen2(path,mode)).decref();
1583 |   }
1584 |   /** Invalid constructor. Available as of PLUMED 2.5.
1675 |     A possible usage is to transfer the ownership of a temporary
1676 |     object when it is converted
1677 |   \verbatim
1678 |   plumed p=Plumed::dlopen(path).incref()
1679 |   // without incref(), the just constructed object will be destroyed
1680 |   // when the temporary object is deleted.
2017 | 
2018 | #if defined( __PLUMED_HAS_DLOPEN) /*{*/
2019 | /**
2020 | Try to dlopen a path with a given mode.
2021 | If the dlopen command fails, it tries to strip the `Kernel` part of the name.
2022 | 
2023 | This function is declared static (internal linkage) so that it is not visible from outside.
2025 | */
2026 | 
2027 | __PLUMED_WRAPPER_INTERNALS_BEGIN
2028 | void* plumed_attempt_dlopen(const char*path,int mode) {
2029 |   char* pathcopy;
2030 |   void* p;
2042 |   }
2043 |   __PLUMED_WRAPPER_STD fclose(fp);
2044 |   dlerror();
2045 |   p=dlopen(path,mode);
2046 |   if(!p) {
2047 |     /*
2051 |       not visible. All the other cases (either PLUMED>=2.5 or symbols in the main executable visible)
2052 |       should work correctly without entering here.
2053 |     */
2054 |     __PLUMED_FPRINTF(stderr,"+++ An error occurred. Message from dlopen(): %s +++\n",dlerror());
2055 |     strlenpath=__PLUMED_WRAPPER_STD strlen(path);
2056 |     pathcopy=(char*) __PLUMED_MALLOC(strlenpath+1);
2069 |       }
2070 |       __PLUMED_WRAPPER_STD fclose(fp);
2071 |       dlerror();
2072 |       p=dlopen(pathcopy,mode);
2073 |       if(!p) __PLUMED_FPRINTF(stderr,"+++ An error occurred. Message from dlopen(): %s +++\n",dlerror());
2074 |     }
2075 |     __PLUMED_FREE(pathcopy);
2093 |   }
2094 | 
2095 | /**
2096 | Search symbols in a dlopened library.
2097 | 
2098 | This function is declared static (internal linkage) so that it is not visible from outside.
2208 |   (if available).
2209 |   Notice that problems can be detected checking if the functions have a NULL ptr.
2210 |   On the other hand, the symbol table pointer might be NULL just because the plumed version is <=2.4.
2211 |   If handle is not NULL, it is used to return a dlopen handle that could be subsequently dlclosed.
2212 | */
2213 | __PLUMED_WRAPPER_INTERNALS_BEGIN
2223 |   if(functions) *functions=ptr->functions;
2224 | #elif ! defined(__PLUMED_HAS_DLOPEN)
2225 |   /*
2226 |     When dlopen is not available, we hard code them to NULL
2227 |   */
2228 |   fprintf(stderr,"+++ PLUMED has been compiled without dlopen and without a static kernel +++\n");
2229 |   plumed_plumedmain_function_holder g= {NULL,NULL,NULL};
2230 |   if(plumed_symbol_table_ptr) *plumed_symbol_table_ptr=NULL;
2239 |   const char* path;
2240 |   void* p;
2241 |   char* debug;
2242 |   int dlopenmode;
2243 |   g.create=NULL;
2244 |   g.cmd=NULL;
2246 |   path=__PLUMED_GETENV("PLUMED_KERNEL");
2247 |   p=NULL;
2248 |   debug=__PLUMED_GETENV("PLUMED_LOAD_DEBUG");
2249 |   dlopenmode=0;
2250 |   if(plumed_symbol_table_ptr) *plumed_symbol_table_ptr=NULL;
2251 |   if(handle) *handle=NULL;
2266 |     fprintf(stderr,"+++ Loading the PLUMED kernel runtime +++\n");
2267 |     fprintf(stderr,"+++ PLUMED_KERNEL=\"%s\" +++\n",path);
2268 |     if(debug) __PLUMED_FPRINTF(stderr,"+++ Loading with mode RTLD_NOW");
2269 |     dlopenmode=RTLD_NOW;
2270 |     if(__PLUMED_GETENV("PLUMED_LOAD_NAMESPACE") && !__PLUMED_WRAPPER_STD strcmp(__PLUMED_GETENV("PLUMED_LOAD_NAMESPACE"),"LOCAL")) {
2271 |       dlopenmode=dlopenmode|RTLD_LOCAL;
2272 |       if(debug) __PLUMED_FPRINTF(stderr,"|RTLD_LOCAL");
2273 |     } else {
2274 |       dlopenmode=dlopenmode|RTLD_GLOBAL;
2275 |       if(debug) __PLUMED_FPRINTF(stderr,"|RTLD_GLOBAL");
2276 |     }
2277 | #ifdef RTLD_DEEPBIND
2278 |     if(!__PLUMED_GETENV("PLUMED_LOAD_NODEEPBIND")) {
2279 |       dlopenmode=dlopenmode|RTLD_DEEPBIND;
2280 |       if(debug) __PLUMED_FPRINTF(stderr,"|RTLD_DEEPBIND");
2281 |     }
2282 | #endif
2283 |     if(debug) __PLUMED_FPRINTF(stderr," +++\n");
2284 |     p=plumed_attempt_dlopen(path,dlopenmode);
2285 |     if(p) plumed_search_symbols(p,&g,plumed_symbol_table_ptr);
2286 |   }
2391 | __PLUMED_WRAPPER_C_END
2392 | 
2393 | __PLUMED_WRAPPER_C_BEGIN
2394 | plumed plumed_create_dlopen(const char*path) {
2395 |   int dlopenmode;
2396 |   /* plumed_create_dlopen always uses RTLD_LOCAL and, when possible, RTLD_DEEPBIND to allow multiple versions */
2397 | #ifdef __PLUMED_HAS_DLOPEN
2398 |   dlopenmode=RTLD_NOW|RTLD_LOCAL;
2399 | #ifdef RTLD_DEEPBIND
2400 |   dlopenmode=dlopenmode|RTLD_DEEPBIND;
2401 | #endif
2402 | #else
2403 |   dlopenmode=0;
2404 | #endif
2405 |   return plumed_create_dlopen2(path,dlopenmode);
2406 | }
2407 | __PLUMED_WRAPPER_C_END
2408 | 
2409 | __PLUMED_WRAPPER_C_BEGIN
2410 | plumed plumed_create_dlopen2(const char*path,int mode) {
2411 |   /* returned object */
2412 |   plumed p;
2415 |   /* allocate space for implementation object. this is free-ed in plumed_finalize(). */
2416 |   pimpl=plumed_malloc_pimpl();
2417 | #ifdef __PLUMED_HAS_DLOPEN
2418 |   if(path) pimpl->dlhandle=plumed_attempt_dlopen(path,mode);
2419 |   /* mark this library to be dlclosed when the object is finalized */
2420 |   pimpl->dlclose=1;
2732 |   plumed_c2f(plumed_create(),c);
2733 | }
2734 | 
2735 | __PLUMED_IMPLEMENT_FORTRAN(plumed_f_create_dlopen,PLUMED_F_CREATE_DLOPEN,(char*path,char*c),(path,c)) {
2736 |   plumed_c2f(plumed_create_dlopen(path),c);
2737 | }
2738 | 
{% endraw %}

```
### src/core/PlumedMainInitializer.h

```c

{% raw %}
79 | /**
80 |   Static symbol table that is accessed by the plumed loader.
81 |   Notice that this table is initialized with a static object construction.
82 |   In principle, it should be accessed by other programs dlopening the plumed kernel.
83 |   In that case, it is guaranteed to be already initialized.
84 |   However, when accessed directly it might be safer to first call \ref plumed_symbol_table_init.
{% endraw %}

```
### src/tools/PlumedHandle.h

```c

{% raw %}
57 | 
58 | The following syntax instead creates a handle referring to a loaded kernel
59 | \verbatim
60 | PlumedHandle p(PlumedHandle::dlopen("/path/to/libplumedkernel.so");
61 | // Alternatively:
62 | // auto p=PlumedHandle::dlopen("/path/to/libplumedkernel.so");
117 |   PlumedHandle();
118 | /// Construct a PlumedHandle given the path to a kernel.
119 | /// It just uses the private constructor PlumedHandle(const char* path).
120 |   static PlumedHandle dlopen(const char* path);
121 | /// Destructor.
122 | /// In case a kernel was dlopened, it dlcloses it.
{% endraw %}

```