---
name: "neuron"
layout: package
next_package: cityhash
previous_package: xrootd
languages: ['python', 'cpp', 'bash']
---
## develop
33 / 8194 files match

 - [cmake_nrnconf.h.in](#cmake_nrnconfhin)
 - [configure.ac](#configureac)
 - [bin/nrnmech_makefile.in](#binnrnmech_makefilein)
 - [src/nrnpython/setup.py.in](#srcnrnpythonsetuppyin)
 - [src/nrnjava/njconf.h.in](#srcnrnjavanjconfhin)
 - [src/nrnjava/njvm.cpp](#srcnrnjavanjvmcpp)
 - [src/oc/cygwinprt.cpp](#srcoccygwinprtcpp)
 - [src/oc/hoc_init.cpp](#srcochoc_initcpp)
 - [src/nrnoc/osxdlfcn.h](#srcnrnocosxdlfcnh)
 - [src/nrnoc/init.cpp](#srcnrnocinitcpp)
 - [src/nrnoc/osxdlfcn.cpp](#srcnrnocosxdlfcncpp)
 - [src/nrniv/nrnpy.cpp](#srcnrnivnrnpycpp)
 - [src/nrniv/nrncore_write.cpp](#srcnrnivnrncore_writecpp)
 - [src/nrniv/CMakeLists.txt](#srcnrnivcmakeliststxt)
 - [src/nrniv/nrncore_write/utils/nrncore_utils.cpp](#srcnrnivnrncore_writeutilsnrncore_utilscpp)
 - [src/nrniv/nrncore_write/callbacks/nrncore_callbacks.cpp](#srcnrnivnrncore_writecallbacksnrncore_callbackscpp)
 - [src/ivoc/nrnmain.cpp](#srcivocnrnmaincpp)
 - [src/ivoc/ivocmain.cpp](#srcivocivocmaincpp)
 - [src/nrnmpi/nrnmpi_dynam.cpp](#srcnrnmpinrnmpi_dynamcpp)
 - [packaging/python/fix_demo_libnrnmech.sh](#packagingpythonfix_demo_libnrnmechsh)
 - [m4/nrnbg.m4](#m4nrnbgm4)
 - [m4/nrnjava.m4](#m4nrnjavam4)
 - [share/lib/python/neuron/__init__.py](#sharelibpythonneuron__init__py)
 - [external/coreneuron/coreneuron/mechanism/mech/enginemech.cpp](#externalcoreneuroncoreneuronmechanismmechenginemechcpp)
 - [external/coreneuron/external/nmodl/src/pybind/pyembed.cpp](#externalcoreneuronexternalnmodlsrcpybindpyembedcpp)
 - [external/coreneuron/external/nmodl/ext/pybind11/include/pybind11/detail/internals.h](#externalcoreneuronexternalnmodlextpybind11includepybind11detailinternalsh)
 - [external/coreneuron/external/nmodl/ext/pybind11/docs/faq.rst](#externalcoreneuronexternalnmodlextpybind11docsfaqrst)
 - [external/coreneuron/external/mod2c/src/mod2c_core/nmodlconf.h](#externalcoreneuronexternalmod2csrcmod2c_corenmodlconfh)
 - [external/iv/CMakeLists.txt](#externalivcmakeliststxt)
 - [external/iv/src/lib/x11_dynam/ivx11_dynam.cpp](#externalivsrclibx11_dynamivx11_dynamcpp)
 - [external/iv/src/include/IV-X11/ivx11_dynam.h](#externalivsrcincludeiv-x11ivx11_dynamh)
 - [test/CMakeLists.txt](#testcmakeliststxt)
 - [docs/cmake_doc/options.rst](#docscmake_docoptionsrst)

### cmake_nrnconf.h.in

```

{% raw %}
268 | /* if 1 then dlopen nrnmech instead of special */
{% endraw %}

```
### configure.ac

```

{% raw %}
208 | dnl however we would need to deal with libnrnmech.so and dlopen
237 | AC_LIBTOOL_DLOPEN
325 | 	if test x${java_dlopen} = x ; then
326 | 		java_dlopen="yes"
341 | 	if test x${java_dlopen} = x ; then
342 | 		java_dlopen="yes"
354 | 	AC_DEFINE(NRNMECH_DLL_STYLE, 1,[if 1 then dlopen nrnmech instead of special])
{% endraw %}

```
### bin/nrnmech_makefile.in

```

{% raw %}
2 | # can be dlopen'd from nrniv.
{% endraw %}

```
### src/nrnpython/setup.py.in

```

{% raw %}
134 | # added to rpath to avoid issues with dlopen.
{% endraw %}

```
### src/nrnjava/njconf.h.in

```

{% raw %}
11 | /* if defined then try to dlopen the jvm */
12 | #undef JVM_DLOPEN
{% endraw %}

```
### src/nrnjava/njvm.cpp

```

{% raw %}
30 | #if defined(JVM_DLOPEN)
202 | // allowing Mac classic dlopen and Unix static
270 | // allowing mswin and unix dlopen and unix static
299 | #if defined(_WIN32) || defined(JVM_DLOPEN)
360 | #if defined(JVM_DLOPEN)
379 | 	void* handle = (void *) dlopen(str.string(), RTLD_NOW | RTLD_GLOBAL);
381 | 		fprintf(stderr, "dlopen(\"%s\") failed: %s\n", str.string(), dlerror());
410 | dlopen (const char *name, int)
456 | 	void* handle = dlopen("jvmdll", 0);
{% endraw %}

```
### src/oc/cygwinprt.cpp

```

{% raw %}
22 | void* dlopen(const char *name, int mode) {
33 | void* dlopen_noerr(const char *name, int mode) {return (void*)LoadLibrary(name);}
{% endraw %}

```
### src/oc/hoc_init.cpp

```

{% raw %}
270 | int nrn_noauto_dlopen_nrnmech; /* 0 except when binary special. */
{% endraw %}

```
### src/nrnoc/osxdlfcn.h

```cpp

{% raw %}
53 | extern void * dlopen(const char *path, int mode);
{% endraw %}

```
### src/nrnoc/init.cpp

```

{% raw %}
32 | extern void* dlopen(const char* name, int mode);
44 | extern int nrn_noauto_dlopen_nrnmech; /* default 0 declared in hoc_init.cpp */
202 | void* nrn_realpath_dlopen(const char* relpath, int flags) {
218 |     handle = dlopen(abspath, flags);
222 |     handle = dlopen(relpath, flags);
224 |       Fprintf(stderr, "realpath failed errno=%d (%s) and dlopen failed with %s\n", patherr, strerror(patherr), relpath);
236 | 	handle = nrn_realpath_dlopen(cp1, RTLD_NOW);
238 | 	handle = dlopen(cp1, RTLD_NOW);
251 | 		fprintf(stderr, "dlopen failed - \n%s\n", dlerror());
361 | 	if (!nrn_mech_dll && !nrn_noauto_dlopen_nrnmech) {
{% endraw %}

```
### src/nrnoc/osxdlfcn.cpp

```

{% raw %}
83 | /* dlopen */
84 | extern "C" void *dlopen(const char *path, int mode) {
{% endraw %}

```
### src/nrniv/nrnpy.cpp

```

{% raw %}
42 | extern void* dlopen_noerr(const char* name, int mode);
43 | #define dlopen dlopen_noerr
248 | 		handle = dlopen(nrnpy_pylib, RTLD_NOW|RTLD_GLOBAL);
250 | 			fprintf(stderr, "Could not dlopen NRN_PYLIB: %s\n", nrnpy_pylib);
274 | 	// in these circumstances, it is sufficient to go ahead and dlopen
298 | // important dlopen flags :
313 | 		void* handle = dlopen(name, flag);
363 | 	void* handle = dlopen(name, RTLD_NOW);
{% endraw %}

```
### src/nrniv/nrncore_write.cpp

```

{% raw %}
113 | extern void* dlopen_noerr(const char* name, int mode);
114 | #define dlopen dlopen_noerr
{% endraw %}

```
### src/nrniv/CMakeLists.txt

```

{% raw %}
322 |       # Note that we do not link here to libmpi. That is dlopen first.
{% endraw %}

```
### src/nrniv/nrncore_write/utils/nrncore_utils.cpp

```

{% raw %}
23 | extern void* dlopen_noerr(const char* name, int mode);
24 | #define dlopen dlopen_noerr
35 | // RTLD_NODELETE is used with dlopen
182 |     void * handle = dlopen(NULL, RTLD_NOW | RTLD_GLOBAL);
192 | /** Open library with given path and return dlopen handle **/
194 |     void* handle = dlopen(path, RTLD_NOW|RTLD_GLOBAL|RTLD_NODELETE);
198 |       hoc_execerror("Could not dlopen CoreNEURON mechanism library : ", path);
207 |         return dlopen(NULL, RTLD_NOW|RTLD_GLOBAL);
{% endraw %}

```
### src/nrniv/nrncore_write/callbacks/nrncore_callbacks.cpp

```

{% raw %}
18 | extern void* dlopen_noerr(const char* name, int mode);
19 | #define dlopen dlopen_noerr
{% endraw %}

```
### src/ivoc/nrnmain.cpp

```

{% raw %}
11 | 	extern int nrn_noauto_dlopen_nrnmech;
29 | #if defined(AUTO_DLOPEN_NRNMECH) && AUTO_DLOPEN_NRNMECH == 0
30 | 	nrn_noauto_dlopen_nrnmech = 1;
{% endraw %}

```
### src/ivoc/ivocmain.cpp

```

{% raw %}
215 | linux that dlopen needs a full path to the file. A path to the binary
{% endraw %}

```
### src/nrnmpi/nrnmpi_dynam.cpp

```

{% raw %}
15 | extern void* dlopen_noerr(const char* name, int mode);
16 | #define dlopen dlopen_noerr
43 | 	void* handle = dlopen(name, flag);
55 | 	void* handle = dlopen(name, flag);
91 |      * If libmpi.dylib is not in the standard location and dlopen fails
169 | 		if (!dlopen("libnrniv.so", RTLD_NOW | RTLD_NOLOAD | RTLD_GLOBAL)) {
210 | if (!dlopen("liboc.so", RTLD_NOW | RTLD_NOLOAD | RTLD_GLOBAL)) {
213 | if (!dlopen("libnrniv.so", RTLD_NOW | RTLD_NOLOAD | RTLD_GLOBAL)) {
{% endraw %}

```
### packaging/python/fix_demo_libnrnmech.sh

```bash

{% raw %}
4 | # neurondemo dlopens ..../release/x86_64/.libs/libnrnmech.so
{% endraw %}

```
### m4/nrnbg.m4

```

{% raw %}
10 | 		java_dlopen="no"
69 | 		java_dlopen="no"
145 | 		java_dlopen="no"
212 |                 java_dlopen="no"
{% endraw %}

```
### m4/nrnjava.m4

```

{% raw %}
1 | dnl be built so that neuron can be dlopened by java
259 | if test "$java_dlopen" = "yes" ; then
260 | 	AC_MSG_NOTICE([Use the dlopen technique to load the jvm])
261 | 	NRN_DEFINE(JVM_DLOPEN,1,[if defined then try to dlopen the jvm])
{% endraw %}

```
### share/lib/python/neuron/__init__.py

```python

{% raw %}
81 | ## does a dlopen("libnrnmpi.so", RTLD_NOW | RTLD_GLOBAL) .
82 | ## In this case setting the dlopenflags below fixes the problem. But it
97 | #  sys.setdlopenflags(DLFCN.RTLD_NOW | DLFCN.RTLD_GLOBAL)
118 | # On OSX, dlopen might fail if not using full library path
{% endraw %}

```
### external/coreneuron/coreneuron/mechanism/mech/enginemech.cpp

```

{% raw %}
13 |  * special-core. Also, it is used by NEURON to run CoreNEURON via dlopen to execute
{% endraw %}

```
### external/coreneuron/external/nmodl/src/pybind/pyembed.cpp

```

{% raw %}
34 |     const auto dlopen_opts = RTLD_NOW | RTLD_GLOBAL;
36 |     pylib_handle = dlopen(pylib_env, dlopen_opts);
41 |         throw std::runtime_error("Failed to dlopen");
49 |     pybind_wrapper_handle = dlopen(pybind_wraplib_env, dlopen_opts);
54 |         throw std::runtime_error("Failed to dlopen");
{% endraw %}

```
### external/coreneuron/external/nmodl/ext/pybind11/include/pybind11/detail/internals.h

```cpp

{% raw %}
49 | // Python loads modules by default with dlopen with the RTLD_LOCAL flag; under libc++ and possibly
{% endraw %}

```
### external/coreneuron/external/nmodl/ext/pybind11/docs/faq.rst

```

{% raw %}
166 | typically using ``dlopen`` with the ``RTLD_LOCAL`` flag), this Python default
{% endraw %}

```
### external/coreneuron/external/mod2c/src/mod2c_core/nmodlconf.h

```cpp

{% raw %}
267 | /* if 1 then dlopen nrnmech instead of special */
{% endraw %}

```
### external/iv/CMakeLists.txt

```

{% raw %}
32 | option(IV_ENABLE_X11_DYNAMIC "dlopen X11 after launch" OFF)
{% endraw %}

```
### external/iv/src/lib/x11_dynam/ivx11_dynam.cpp

```

{% raw %}
22 | /** @brief dlopen libivx11dynam.so and call its ivx11_assign.
51 |         // dlopen this with RTLD_GLOBAL to make sure the dlopen of libivx11dynam
53 |         if (!dlopen(name.c_str(), RTLD_NOW | RTLD_NOLOAD | RTLD_GLOBAL)) {
81 |   void* handle = dlopen(name.c_str(), flag);
{% endraw %}

```
### external/iv/src/include/IV-X11/ivx11_dynam.h

```cpp

{% raw %}
10 | /** @brief dlopen libivx11dynam.so and call its ivx11_assign.
{% endraw %}

```
### test/CMakeLists.txt

```

{% raw %}
24 | # Note that DYLD_LIBRARY_PATH is not required and interfere with dlopen
{% endraw %}

```
### docs/cmake_doc/options.rst

```

{% raw %}
142 |   dlopen X11 after launch  
{% endraw %}

```