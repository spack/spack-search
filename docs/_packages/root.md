---
name: "root"
layout: package
next_package: gobject-introspection
previous_package: hadoop
languages: ['cmake', 'cpp', 'python']
---
## 6.22.06
26 / 18941 files match

 - [interpreter/llvm/src/lib/ExecutionEngine/IntelJITEvents/jitprofiling.c](#interpreterllvmsrclibexecutionengineinteljiteventsjitprofilingc)
 - [interpreter/llvm/src/lib/ExecutionEngine/IntelJITEvents/ittnotify_config.h](#interpreterllvmsrclibexecutionengineinteljiteventsittnotify_configh)
 - [interpreter/llvm/src/lib/Support/Windows/DynamicLibrary.inc](#interpreterllvmsrclibsupportwindowsdynamiclibraryinc)
 - [interpreter/llvm/src/lib/Support/Unix/DynamicLibrary.inc](#interpreterllvmsrclibsupportunixdynamiclibraryinc)
 - [interpreter/llvm/src/include/llvm/Config/config.h.cmake](#interpreterllvmsrcincludellvmconfigconfighcmake)
 - [interpreter/llvm/src/include/llvm/BinaryFormat/ELF.h](#interpreterllvmsrcincludellvmbinaryformatelfh)
 - [interpreter/llvm/src/include/llvm/Support/DynamicLibrary.h](#interpreterllvmsrcincludellvmsupportdynamiclibraryh)
 - [interpreter/llvm/src/include/llvm-c/LinkTimeOptimizer.h](#interpreterllvmsrcincludellvm-clinktimeoptimizerh)
 - [interpreter/llvm/src/cmake/config-ix.cmake](#interpreterllvmsrccmakeconfig-ixcmake)
 - [interpreter/llvm/src/tools/clang/lib/StaticAnalyzer/Checkers/GenericTaintChecker.cpp](#interpreterllvmsrctoolsclanglibstaticanalyzercheckersgenerictaintcheckercpp)
 - [interpreter/llvm/src/tools/clang/docs/ControlFlowIntegrityDesign.rst](#interpreterllvmsrctoolsclangdocscontrolflowintegritydesignrst)
 - [interpreter/cling/lib/Utils/PlatformPosix.cpp](#interpreterclinglibutilsplatformposixcpp)
 - [interpreter/cling/lib/Interpreter/IncrementalParser.cpp](#interpreterclinglibinterpreterincrementalparsercpp)
 - [interpreter/cling/include/cling/Interpreter/DynamicLibraryManager.h](#interpreterclingincludeclinginterpreterdynamiclibrarymanagerh)
 - [bindings/pyroot/pythonizations/python/ROOT/_numbadeclare.py](#bindingspyrootpythonizationspythonroot_numbadeclarepy)
 - [bindings/pyroot/cppyy/cppyy/etc/valgrind-cppyy-cling.supp](#bindingspyrootcppyycppyyetcvalgrind-cppyy-clingsupp)
 - [bindings/pyroot_legacy/cppyy.py](#bindingspyroot_legacycppyypy)
 - [bindings/pyroot_legacy/JupyROOT/helpers/cppcompleter.py](#bindingspyroot_legacyjupyroothelperscppcompleterpy)
 - [bindings/jupyroot/python/JupyROOT/helpers/cppcompleter.py](#bindingsjupyrootpythonjupyroothelperscppcompleterpy)
 - [graf2d/asimage/src/libAfterImage/aclocal.m4](#graf2dasimagesrclibafterimageaclocalm4)
 - [README/README.CXXMODULES.md](#readmereadmecxxmodulesmd)
 - [core/base/src/TROOT.cxx](#corebasesrctrootcxx)
 - [core/metacling/src/TCling.cxx](#coremetaclingsrctclingcxx)
 - [etc/valgrind-root.supp](#etcvalgrind-rootsupp)
 - [net/http/civetweb/civetweb.c](#nethttpcivetwebcivetwebc)
 - [builtins/glew/src/glew.c](#builtinsglewsrcglewc)

### interpreter/llvm/src/lib/ExecutionEngine/IntelJITEvents/jitprofiling.c

```cpp

{% raw %}
349 |         m_libHandle = dlopen(dllName, RTLD_LAZY);
358 |         m_libHandle = dlopen(DEFAULT_DLLNAME, RTLD_LAZY);
{% endraw %}

```
### interpreter/llvm/src/lib/ExecutionEngine/IntelJITEvents/ittnotify_config.h

```cpp

{% raw %}
246 | #define __itt_load_lib(name)      dlopen(name, RTLD_LAZY)
{% endraw %}

```
### interpreter/llvm/src/lib/Support/Windows/DynamicLibrary.inc

```

{% raw %}
34 | void *DynamicLibrary::HandleSet::DLOpen(const char *File, std::string *Err) {
36 |   // simillar to dlopen(NULL, RTLD_LAZY|RTLD_GLOBAL)
130 |   // Try EXE first, mirroring what dlsym(dlopen(NULL)) does.
135 |     // This is different behaviour than what Posix dlsym(dlopen(NULL)) does.
{% endraw %}

```
### interpreter/llvm/src/lib/Support/Unix/DynamicLibrary.inc

```

{% raw %}
13 | #if defined(HAVE_DLFCN_H) && defined(HAVE_DLOPEN)
27 | void *DynamicLibrary::HandleSet::DLOpen(const char *File, std::string *Err) {
28 |   void *Handle = ::dlopen(File, RTLD_LAZY|RTLD_GLOBAL);
36 |   // with the handle of dlopen(NULL, RTLD_GLOBAL).
52 | #else // !HAVE_DLOPEN
56 | void *DynamicLibrary::HandleSet::DLOpen(const char *File, std::string *Err) {
57 |   if (Err) *Err = "dlopen() not supported on this platform";
{% endraw %}

```
### interpreter/llvm/src/include/llvm/Config/config.h.cmake

```cmake

{% raw %}
52 | /* Define if dlopen() is available on this platform. */
53 | #cmakedefine HAVE_DLOPEN ${HAVE_DLOPEN}
{% endraw %}

```
### interpreter/llvm/src/include/llvm/BinaryFormat/ELF.h

```cpp

{% raw %}
1208 |                                      // by rld on dlopen() calls.
{% endraw %}

```
### interpreter/llvm/src/include/llvm/Support/DynamicLibrary.h

```cpp

{% raw %}
91 |       /// SO_Linker - Search as a call to dlsym(dlopen(NULL)) would when
{% endraw %}

```
### interpreter/llvm/src/include/llvm-c/LinkTimeOptimizer.h

```cpp

{% raw %}
50 |   /// linker to use dlopen() interface to dynamically load LinkTimeOptimizer.
51 |   /// extern "C" helps, because dlopen() interface uses name to find the symbol.
{% endraw %}

```
### interpreter/llvm/src/cmake/config-ix.cmake

```cmake

{% raw %}
114 |   check_library_exists(dl dlopen "" HAVE_LIBDL)
242 |   check_symbol_exists(dlopen dlfcn.h HAVE_DLOPEN)
{% endraw %}

```
### interpreter/llvm/src/tools/clang/lib/StaticAnalyzer/Checkers/GenericTaintChecker.cpp

```

{% raw %}
726 |     .Case("dlopen", 0)
{% endraw %}

```
### interpreter/llvm/src/tools/clang/docs/ControlFlowIntegrityDesign.rst

```

{% raw %}
383 | dlopen-ed/dlclose-d periodically, even frequently.
502 | performance in the handling of dlopen(). It is recommended that
{% endraw %}

```
### interpreter/cling/lib/Utils/PlatformPosix.cpp

```

{% raw %}
116 | const void* DLOpen(const std::string& Path, std::string* Err) {
117 |   void* Lib = dlopen(Path.c_str(), RTLD_LAZY|RTLD_GLOBAL);
123 |   if (const void* Self = ::dlopen(nullptr, RTLD_GLOBAL)) {
124 |     // get dlopen error if there is one
129 |     // only get dlclose error if dlopen & dlsym haven't emited one
{% endraw %}

```
### interpreter/cling/lib/Interpreter/IncrementalParser.cpp

```

{% raw %}
193 |   // plugins if cling is in a single shared library which is dlopen-ed with
204 |     // because the dlopen happens after creating the clang::Preprocessor which
{% endraw %}

```
### interpreter/cling/include/cling/Interpreter/DynamicLibraryManager.h

```cpp

{% raw %}
163 |     ///       resolution, e.g. because it was dlopened with RTLD_LOCAL.
{% endraw %}

```
### bindings/pyroot/pythonizations/python/ROOT/_numbadeclare.py

```python

{% raw %}
191 |         C = ffi.dlopen(None)
{% endraw %}

```
### bindings/pyroot/cppyy/cppyy/etc/valgrind-cppyy-cling.supp

```

{% raw %}
475 |    Ignore deficient in dlopen and/or pthread and/or valgrind. See for example https://bugs.kde.org/show_bug.cgi?id=358980.
{% endraw %}

```
### bindings/pyroot_legacy/cppyy.py

```python

{% raw %}
57 |       dlflags = sys.getdlopenflags()
58 |       sys.setdlopenflags( 0x100 | 0x2 )    # RTLD_GLOBAL | RTLD_NOW
64 |       sys.setdlopenflags( dlflags )
{% endraw %}

```
### bindings/pyroot_legacy/JupyROOT/helpers/cppcompleter.py

```python

{% raw %}
111 |             dlOpenRint = 'dlopen("libRint.so",RTLD_NOW);'
112 |             utils.processCppCode(dlOpenRint)
{% endraw %}

```
### bindings/jupyroot/python/JupyROOT/helpers/cppcompleter.py

```python

{% raw %}
111 |             dlOpenRint = 'dlopen("libRint.so",RTLD_NOW);'
112 |             utils.processCppCode(dlOpenRint)
{% endraw %}

```
### graf2d/asimage/src/libAfterImage/aclocal.m4

```

{% raw %}
545 |               dnl age, revision, installed, dlopen, dlpreopen, libdir.
{% endraw %}

```
### README/README.CXXMODULES.md

```

{% raw %}
230 | fails. The implementation knows that `foo::bar` is in *libFoo*. It `dlopen`s
{% endraw %}

```
### core/base/src/TROOT.cxx

```

{% raw %}
82 | #define dlopen(library_name, flags) ::LoadLibrary(library_name)
302 |       // loaded via dlopen by libCore, the destruction of its global
1995 |       void *libRIOHandle = dlopen(libRIO, RTLD_NOW|RTLD_GLOBAL);
2004 |       gInterpreterLib = dlopen(libcling, RTLD_LAZY|RTLD_LOCAL);
{% endraw %}

```
### core/metacling/src/TCling.cxx

```

{% raw %}
200 | #define dlopen(library_name, flags) ::LoadLibraryA(library_name)
2036 |    bool wasDlopened = false;
2038 |    // If this call happens after dlopen has finished (i.e. late registration)
2039 |    // there is no need to dlopen the library recursively. See ROOT-8437 where
2045 |          // requested by the JIT from it: as the library is currently being dlopen'ed,
2047 |          // Recursive dlopen seems to work just fine.
2048 |          void* dyLibHandle = dlopen(dyLibName.c_str(), RTLD_LAZY | RTLD_GLOBAL);
2051 |             wasDlopened = true;
2287 |    if (wasDlopened) {
3018 |    // We will only load the modulemap for libEvent.so after we dlopen libEvent
{% endraw %}

```
### etc/valgrind-root.supp

```

{% raw %}
1300 |    Ignore deficient in dlopen and/or pthread and/or valgrind. See for example https://bugs.kde.org/show_bug.cgi?id=358980.
{% endraw %}

```
### net/http/civetweb/civetweb.c

```cpp

{% raw %}
5521 | /* If SSL is loaded dynamically, dlopen/dlclose is required. */
5533 | dlopen(const char *dll_name, int flags)
15280 | 	if ((dll_handle = dlopen(dll_name, RTLD_LAZY)) == NULL) {
{% endraw %}

```
### builtins/glew/src/glew.c

```cpp

{% raw %}
88 |     if ((h = dlopen(NULL, RTLD_LAZY | RTLD_LOCAL)) == NULL) return NULL;
114 |     image = dlopen("/System/Library/Frameworks/OpenGL.framework/Versions/Current/OpenGL", RTLD_LAZY);
{% endraw %}

```