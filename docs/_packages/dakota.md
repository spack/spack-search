---
name: "dakota"
layout: package
next_package: p3dfft3
previous_package: netdata
languages: ['cmake', 'cpp']
---
## 6.12
28 / 13171 files match

 - [src/GridApplicInterface.hpp](#srcgridapplicinterfacehpp)
 - [src/GridApplicInterface.cpp](#srcgridapplicinterfacecpp)
 - [src/NIDRProblemDescDB.cpp](#srcnidrproblemdescdbcpp)
 - [src/DLSolver.cpp](#srcdlsolvercpp)
 - [src/DLSolverLoadLibManager.cpp](#srcdlsolverloadlibmanagercpp)
 - [packages/external/acro/CMakeLists.txt](#packagesexternalacrocmakeliststxt)
 - [packages/external/acro/config/acx_func_dlopen.m4](#packagesexternalacroconfigacx_func_dlopenm4)
 - [packages/external/acro/config/FindDL.cmake](#packagesexternalacroconfigfinddlcmake)
 - [packages/external/acro/bootstrap/root/CMakeLists.txt](#packagesexternalacrobootstraprootcmakeliststxt)
 - [packages/external/acro/tpl/ampl/funcadd1.c](#packagesexternalacrotplamplfuncadd1c)
 - [packages/external/acro/tpl/ampl/FindDL.cmake](#packagesexternalacrotplamplfinddlcmake)
 - [packages/external/acro/tpl/ampl/CMakeLists.txt](#packagesexternalacrotplamplcmakeliststxt)
 - [packages/external/acro/packages/colin/src/libs/LibLoader.cpp](#packagesexternalacropackagescolinsrclibslibloadercpp)
 - [packages/external/acro/packages/colin/test/unit/CMakeLists.txt](#packagesexternalacropackagescolintestunitcmakeliststxt)
 - [packages/external/acro/mvs/v8/colin/acro_config.h](#packagesexternalacromvsv8colinacro_configh)
 - [packages/external/acro/mvs/v8/coliny/acro_config.h](#packagesexternalacromvsv8colinyacro_configh)
 - [packages/external/acro/mvs/v8/pico/acro_config.h](#packagesexternalacromvsv8picoacro_configh)
 - [packages/external/acro/mvs/v8/pebbl/acro_config.h](#packagesexternalacromvsv8pebblacro_configh)
 - [packages/external/acro/cmake/FindDL.cmake](#packagesexternalacrocmakefinddlcmake)
 - [packages/external/ampl/funcadd1.c](#packagesexternalamplfuncadd1c)
 - [packages/external/ampl/FindDL.cmake](#packagesexternalamplfinddlcmake)
 - [packages/external/ampl/CMakeLists.txt](#packagesexternalamplcmakeliststxt)
 - [packages/external/hopspack/doc/userman_cmake.tex](#packagesexternalhopspackdocuserman_cmaketex)
 - [packages/external/nidr/configure.ac](#packagesexternalnidrconfigureac)
 - [packages/external/nidr/nidrgen.c](#packagesexternalnidrnidrgenc)
 - [packages/external/nidr/nidr.c](#packagesexternalnidrnidrc)
 - [packages/external/nidr/nidrgen.l](#packagesexternalnidrnidrgenl)
 - [packages/external/nidr/cmake/FindDL.cmake](#packagesexternalnidrcmakefinddlcmake)

### src/GridApplicInterface.hpp

```

{% raw %}
40 |     dynamically linked using dlopen() services. */
{% endraw %}

```
### src/GridApplicInterface.cpp

```

{% raw %}
53 |   void* handle = dlopen("foo.so", RTLD_NOW);
{% endraw %}

```
### src/NIDRProblemDescDB.cpp

```

{% raw %}
51 | #define dlopen(x,y) LoadLibrary(x)
184 | 	if (!(Dr->dlLib = dlopen(s0, RTLD_NOW))) {
{% endraw %}

```
### src/DLSolver.cpp

```

{% raw %}
10 | #define dlopen(x,y) LoadLibrary(x)
283 | 			h = dlopen(s0, RTLD_NOW/*RTLD_LAZY*/);
286 | 			botch("dlopen(\"%s\") failure", s0);
288 | 			botch("dlopen(\"%s\") failure:\n%s", s0, dlerror());
{% endraw %}

```
### src/DLSolverLoadLibManager.cpp

```

{% raw %}
74 | extern "C" void *nidr_dlopen(const char*);
82 |   void* h = nidr_dlopen(lname = L->libname);
{% endraw %}

```
### packages/external/acro/CMakeLists.txt

```

{% raw %}
20 | option(ACRO_HAVE_DLOPEN "Enable dlopen in Acro" ON)
21 | if (ACRO_HAVE_DLOPEN)
25 |     add_definitions("-DHAVE_DLOPEN")
28 |     message(WARNING "dlopen requested, but not found")
{% endraw %}

```
### packages/external/acro/config/acx_func_dlopen.m4

```

{% raw %}
0 | dnl @synopsis ACX_FUNC_DLOPEN([ACTION-IF-FOUND[, ACTION-IF-NOT-FOUND]])
2 | dnl This macro looks for the dlopen function and identifies the library
3 | dnl that is required to use it. On success, it sets the DLOPEN_LIBS output
6 | dnl ACTION-IF-FOUND is a list of shell commands to run if DLOPEN
9 | dnl the default action will define HAVE_DLOPEN.
12 | AC_DEFUN([ACX_FUNC_DLOPEN], [
13 | acx_func_dlopen_ok=no
15 | # DLOPEN linked to by default?
16 | if test $acx_func_dlopen_ok = no; then
18 |         AC_CHECK_FUNC([dlopen], [acx_func_dlopen_ok=yes])
22 | # DLOPEN in Standard DL library? 
23 | if test $acx_func_dlopen_ok = no; then
24 |         AC_CHECK_LIB(dl, [dlopen], [acx_func_dlopen_ok=yes; DLOPEN_LIBS="-ldl"])
27 | AC_SUBST(DLOPEN_LIBS)
30 | if test x"$acx_func_dlopen_ok" = xyes; then
31 |         ifelse([$1],,AC_DEFINE(HAVE_DLOPEN,1,[Define if you have the dlopen function.]),[$1])
34 |         acx_func_dlopen_ok=no
38 | ])dnl ACX_FUNC_DLOPEN
{% endraw %}

```
### packages/external/acro/config/FindDL.cmake

```cmake

{% raw %}
25 |     # if dlopen can be found without linking in dl then,
26 |     # dlopen is part of libc, so don't need to link extra libs.
27 |     check_function_exists(dlopen DL_FOUND)
{% endraw %}

```
### packages/external/acro/bootstrap/root/CMakeLists.txt

```

{% raw %}
20 | option(ACRO_HAVE_DLOPEN "Enable dlopen in Acro" ON)
21 | if (ACRO_HAVE_DLOPEN)
25 |     add_definitions("-DHAVE_DLOPEN")
28 |     message(WARNING "dlopen requested, but not found")
{% endraw %}

```
### packages/external/acro/tpl/ampl/funcadd1.c

```cpp

{% raw %}
103 | #define dlopen(x,y) LoadLibrary(x)
151 | #define dlopen(x,y) shl_load(x, BIND_IMMEDIATE, 0)
210 | #if defined(WIN32) || defined(AMPL_HAVE_DLOPEN)
241 | 	h = dlopen(name, RTLD_NOW);
257 | #else /* !( #if defined(WIN32) || defined(HAVE_DLOPEN) ) */
273 | #if defined(WIN32) || defined(AMPL_HAVE_DLOPEN)
286 | #if defined(WIN32) || defined(AMPL_HAVE_DLOPEN)
353 | #else /* !( #if defined(WIN32) || defined(HAVE_DLOPEN) ) */
{% endraw %}

```
### packages/external/acro/tpl/ampl/FindDL.cmake

```cmake

{% raw %}
25 |     # if dlopen can be found without linking in dl then,
26 |     # dlopen is part of libc, so don't need to link extra libs.
27 |     check_function_exists(dlopen DL_FOUND)
{% endraw %}

```
### packages/external/acro/tpl/ampl/CMakeLists.txt

```

{% raw %}
137 | option(AMPL_HAVE_DLOPEN "Toggle support for dlopen in AMPL" OFF)
138 | if (AMPL_HAVE_DLOPEN)
141 |     add_definitions("-DAMPL_HAVE_DLOPEN")
143 |     message(WARNING "dlopen requested, but not found")
{% endraw %}

```
### packages/external/acro/packages/colin/src/libs/LibLoader.cpp

```

{% raw %}
16 | #if defined(_WIN32) || defined(HAVE_DLOPEN)
73 |    lib_handle = dlopen(name.c_str(), RTLD_LAZY);
146 | #else  // defined(_WIN32) || defined(HAVE_DLOPEN)
154 | #endif  // defined(_WIN32) || defined(HAVE_DLOPEN)
{% endraw %}

```
### packages/external/acro/packages/colin/test/unit/CMakeLists.txt

```

{% raw %}
38 |   set(runner_link_libraries colin utilib)    # Need m dlopen?
{% endraw %}

```
### packages/external/acro/mvs/v8/colin/acro_config.h

```cpp

{% raw %}
53 | /* Define if you have the dlopen function. */
54 | #ifndef ACRO_HAVE_DLOPEN 
55 | #define ACRO_HAVE_DLOPEN  1 
{% endraw %}

```
### packages/external/acro/mvs/v8/coliny/acro_config.h

```cpp

{% raw %}
53 | /* Define if you have the dlopen function. */
54 | #ifndef ACRO_HAVE_DLOPEN 
55 | #define ACRO_HAVE_DLOPEN  1 
{% endraw %}

```
### packages/external/acro/mvs/v8/pico/acro_config.h

```cpp

{% raw %}
53 | /* Define if you have the dlopen function. */
54 | #ifndef ACRO_HAVE_DLOPEN 
55 | #define ACRO_HAVE_DLOPEN  1 
{% endraw %}

```
### packages/external/acro/mvs/v8/pebbl/acro_config.h

```cpp

{% raw %}
53 | /* Define if you have the dlopen function. */
54 | #ifndef ACRO_HAVE_DLOPEN 
55 | #define ACRO_HAVE_DLOPEN  1 
{% endraw %}

```
### packages/external/acro/cmake/FindDL.cmake

```cmake

{% raw %}
25 |     # if dlopen can be found without linking in dl then,
26 |     # dlopen is part of libc, so don't need to link extra libs.
27 |     check_function_exists(dlopen DL_FOUND)
{% endraw %}

```
### packages/external/ampl/funcadd1.c

```cpp

{% raw %}
103 | #define dlopen(x,y) LoadLibrary(x)
151 | #define dlopen(x,y) shl_load(x, BIND_IMMEDIATE, 0)
210 | #if defined(WIN32) || defined(AMPL_HAVE_DLOPEN)
241 | 	h = dlopen(name, RTLD_NOW);
257 | #else /* !( #if defined(WIN32) || defined(HAVE_DLOPEN) ) */
273 | #if defined(WIN32) || defined(AMPL_HAVE_DLOPEN)
286 | #if defined(WIN32) || defined(AMPL_HAVE_DLOPEN)
353 | #else /* !( #if defined(WIN32) || defined(HAVE_DLOPEN) ) */
{% endraw %}

```
### packages/external/ampl/FindDL.cmake

```cmake

{% raw %}
25 |     # if dlopen can be found without linking in dl then,
26 |     # dlopen is part of libc, so don't need to link extra libs.
27 |     check_function_exists(dlopen DL_FOUND)
{% endraw %}

```
### packages/external/ampl/CMakeLists.txt

```

{% raw %}
137 | option(AMPL_HAVE_DLOPEN "Toggle support for dlopen in AMPL" OFF)
138 | if (AMPL_HAVE_DLOPEN)
141 |     add_definitions("-DAMPL_HAVE_DLOPEN")
143 |     message(WARNING "dlopen requested, but not found")
{% endraw %}

```
### packages/external/hopspack/doc/userman_cmake.tex

```

{% raw %}
121 | system library (perhaps the function {\tt dlopen()} was called in a custom
{% endraw %}

```
### packages/external/nidr/configure.ac

```

{% raw %}
4 | # * Manage optional libraries for dlopen
{% endraw %}

```
### packages/external/nidr/nidrgen.c

```cpp

{% raw %}
542 | #define dlopen(x,y) LoadLibrary(x)
1442 | 	h = dlopen(lname, RTLD_NOW);
5795 | 		fprintf(stderr, "\ndlopen for \"%s\" is NOT SUPPORTED\n", libname);
{% endraw %}

```
### packages/external/nidr/nidr.c

```cpp

{% raw %}
64 | #define dlopen(x,y) LoadLibrary(x)
559 | nidr_dlopen(const char *libname)
562 | 	botch("dlopen for \"%s\" is NOT SUPPORTED", libname);
572 | 		return dlopen(libname, RTLD_NOW);
579 | 			buf = (char*)Alloc("nidr_dlopen", L1);
584 | 		if ((h = dlopen(buf, RTLD_NOW)))
587 | 	if (!(h = dlopen(libname, RTLD_NOW))) {
590 | 			buf = (char*)Alloc("nidr_dlopen", L1);
596 | 		if (!(h = dlopen(buf, RTLD_NOW)))
597 | 			h = dlopen(libname, RTLD_NOW); 	/* for dlerror */
1093 | 	h = nidr_dlopen(lname = (const char*)kw->f.vf);
1537 | 	h = nidr_dlopen(libname);
{% endraw %}

```
### packages/external/nidr/nidrgen.l

```

{% raw %}
46 | #define dlopen(x,y) LoadLibrary(x)
946 | 	h = dlopen(lname, RTLD_NOW);
4017 | 		fprintf(stderr, "\ndlopen for \"%s\" is NOT SUPPORTED\n", libname);
{% endraw %}

```
### packages/external/nidr/cmake/FindDL.cmake

```cmake

{% raw %}
25 |     # if dlopen can be found without linking in dl then,
26 |     # dlopen is part of libc, so don't need to link extra libs.
27 |     check_function_exists(dlopen DL_FOUND)
{% endraw %}

```