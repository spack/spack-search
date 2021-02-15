---
name: "paraview"
layout: package
next_package: glew
previous_package: libfuse
languages: ['cpp']
---
## 5.8.0
21 / 28269 files match

 - [Plugins/pvNVIDIAIndeX/src/vtknvindex_instance.cxx](#pluginspvnvidiaindexsrcvtknvindex_instancecxx)
 - [VTK/Utilities/KWSys/vtksys/DynamicLoader.cxx](#vtkutilitieskwsysvtksysdynamicloadercxx)
 - [VTK/Utilities/KWSys/vtksys/DynamicLoader.hxx.in](#vtkutilitieskwsysvtksysdynamicloaderhxxin)
 - [VTK/Utilities/KWSys/vtksys/testDynamicLoader.cxx](#vtkutilitieskwsysvtksystestdynamicloadercxx)
 - [VTK/ThirdParty/mpi4py/vtkmpi4py/CHANGES.rst](#vtkthirdpartympi4pyvtkmpi4pychangesrst)
 - [VTK/ThirdParty/mpi4py/vtkmpi4py/src/dynload.h](#vtkthirdpartympi4pyvtkmpi4pysrcdynloadh)
 - [VTK/ThirdParty/mpi4py/vtkmpi4py/src/lib-mpi/compat/sicortex.h](#vtkthirdpartympi4pyvtkmpi4pysrclib-mpicompatsicortexh)
 - [VTK/ThirdParty/mpi4py/vtkmpi4py/src/lib-mpi/compat/pcmpi.h](#vtkthirdpartympi4pyvtkmpi4pysrclib-mpicompatpcmpih)
 - [VTK/ThirdParty/mpi4py/vtkmpi4py/src/lib-mpi/compat/openmpi.h](#vtkthirdpartympi4pyvtkmpi4pysrclib-mpicompatopenmpih)
 - [VTK/ThirdParty/glew/vtkglew/src/glew.c](#vtkthirdpartyglewvtkglewsrcglewc)
 - [VTK/ThirdParty/libxml2/vtklibxml2/config_cmake.h.in](#vtkthirdpartylibxml2vtklibxml2config_cmakehin)
 - [VTK/ThirdParty/libxml2/vtklibxml2/xmlmodule.c](#vtkthirdpartylibxml2vtklibxml2xmlmodulec)
 - [VTK/ThirdParty/libxml2/vtklibxml2/CMakeLists.txt](#vtkthirdpartylibxml2vtklibxml2cmakeliststxt)
 - [VTK/ThirdParty/sqlite/vtksqlite/sqlite3.c](#vtkthirdpartysqlitevtksqlitesqlite3c)
 - [VTK/ThirdParty/hdf5/vtkhdf5/src/H5PLpkg.h](#vtkthirdpartyhdf5vtkhdf5srch5plpkgh)
 - [CMake/ParaViewValgrindSuppressions.supp](#cmakeparaviewvalgrindsuppressionssupp)
 - [Utilities/VisItBridge/Library/VisItLib/common/plugin/PluginManager.C](#utilitiesvisitbridgelibraryvisitlibcommonpluginpluginmanagerc)
 - [ThirdParty/NvPipe/vtknvpipe/winposix.c](#thirdpartynvpipevtknvpipewinposixc)
 - [ThirdParty/NvPipe/vtknvpipe/decode.c](#thirdpartynvpipevtknvpipedecodec)
 - [ThirdParty/NvPipe/vtknvpipe/winposix.h](#thirdpartynvpipevtknvpipewinposixh)
 - [ThirdParty/NvPipe/vtknvpipe/encode.c](#thirdpartynvpipevtknvpipeencodec)

### Plugins/pvNVIDIAIndeX/src/vtknvindex_instance.cxx

```

{% raw %}
350 |   m_p_handle = dlopen(lib_name.c_str(), RTLD_LAZY);
{% endraw %}

```
### VTK/Utilities/KWSys/vtksys/DynamicLoader.cxx

```

{% raw %}
27 | //   later) which use dlopen
452 | // later) which use dlopen
462 |   return dlopen(libname.c_str(), RTLD_LAZY);
{% endraw %}

```
### VTK/Utilities/KWSys/vtksys/DynamicLoader.hxx.in

```

{% raw %}
32 |  * \warning dlopen on *nix system works the following way:
{% endraw %}

```
### VTK/Utilities/KWSys/vtksys/testDynamicLoader.cxx

```

{% raw %}
96 | // dlopen() on Syllable before 11/22/2007 doesn't return 0 on error
106 |   // This one is actually fun to test, since dlopen is by default
108 |   res += TestDynamicLoader("foobar.lib", "dlopen", 0, 1, 0);
109 |   res += TestDynamicLoader("libdl.so", "dlopen", 1, 1, 1);
{% endraw %}

```
### VTK/ThirdParty/mpi4py/vtkmpi4py/CHANGES.rst

```

{% raw %}
190 | * HP-MPI: fix for missing Fortran datatypes, use dlopen() to load the
240 |   MPI calls is supported in POSIX platforms implementing ``dlopen()``.
247 |   loading of extension modules in platforms supporting ``dlopen()``.
{% endraw %}

```
### VTK/ThirdParty/mpi4py/vtkmpi4py/src/dynload.h

```cpp

{% raw %}
43 |   extern void *dlopen(const char *, int);
{% endraw %}

```
### VTK/ThirdParty/mpi4py/vtkmpi4py/src/lib-mpi/compat/sicortex.h

```cpp

{% raw %}
5 | static void PyMPI_SCMPI_dlopen_libslurm(void)
7 |   (void)dlopen("libslurm.so", RTLD_NOW|RTLD_GLOBAL|RTLD_NOLOAD);
13 |   PyMPI_SCMPI_dlopen_libslurm();
22 |   PyMPI_SCMPI_dlopen_libslurm();
{% endraw %}

```
### VTK/ThirdParty/mpi4py/vtkmpi4py/src/lib-mpi/compat/pcmpi.h

```cpp

{% raw %}
36 | #ifndef PCMPI_DLOPEN_LIBMPI
37 | #define PCMPI_DLOPEN_LIBMPI 1
40 | #if PCMPI_DLOPEN_LIBMPI
41 | #if HAVE_DLOPEN
45 | static void PyMPI_PCMPI_dlopen_libmpi(void)
54 |   if (!handle1) handle1 = dlopen("libmpi.2.dylib", mode);
55 |   if (!handle1) handle1 = dlopen("libmpi.1.dylib", mode);
56 |   if (!handle1) handle1 = dlopen("libmpi.dylib", mode);
57 |   if (!handle2) handle2 = dlopen("libmpio.2.dylib", mode);
58 |   if (!handle2) handle2 = dlopen("libmpio.1.dylib", mode);
59 |   if (!handle2) handle2 = dlopen("libmpio.dylib", mode);
61 |   if (!handle1) handle1 = dlopen("libmpi.so.2", mode);
62 |   if (!handle1) handle1 = dlopen("libmpi.so.1", mode);
63 |   if (!handle1) handle1 = dlopen("libmpi.so", mode);
64 |   if (!handle2) handle2 = dlopen("libmpio.so.2", mode);
65 |   if (!handle2) handle2 = dlopen("libmpio.so.1", mode);
66 |   if (!handle2) handle2 = dlopen("libmpio.so", mode);
72 |   PyMPI_PCMPI_dlopen_libmpi();
81 |   PyMPI_PCMPI_dlopen_libmpi();
87 | #endif /* !HAVE_DLOPEN */
88 | #endif /* !PCMPI_DLOPEN_LIBMPI */
{% endraw %}

```
### VTK/ThirdParty/mpi4py/vtkmpi4py/src/lib-mpi/compat/openmpi.h

```cpp

{% raw %}
9 |  * library with appropriate flags to 'dlopen()' ensuring global
13 | #if !defined(OPENMPI_DLOPEN_LIBMPI) && defined(OMPI_MAJOR_VERSION)
15 | #define OPENMPI_DLOPEN_LIBMPI 0
19 | #ifndef OPENMPI_DLOPEN_LIBMPI
20 | #define OPENMPI_DLOPEN_LIBMPI 1
23 | #if OPENMPI_DLOPEN_LIBMPI
24 | #if HAVE_DLOPEN
29 | static void * my_dlopen(const char *name, int mode) {
49 |   handle = dlopen(name, mode);
50 |   printf("dlopen(\"%s\",0x%X) -> %p\n", name, mode, handle);
54 | #define dlopen my_dlopen
57 | static void PyMPI_OPENMPI_dlopen_libmpi(void)
68 |   if (!handle) handle = dlopen("libmpi.40.dylib", mode);
70 |   if (!handle) handle = dlopen("libmpi.20.dylib", mode);
72 |   if (!handle) handle = dlopen("libmpi.12.dylib", mode);
74 |   if (!handle) handle = dlopen("libmpi.1.dylib", mode);
76 |   if (!handle) handle = dlopen("libmpi.0.dylib", mode);
79 |   if (!handle) handle = dlopen("libmpi.dylib", mode);
87 |   if (!handle) handle = dlopen("libmpi_ibm.so.2", mode);
88 |   if (!handle) handle = dlopen("libmpi_ibm.so.1", mode);
89 |   if (!handle) handle = dlopen("libmpi_ibm.so", mode);
91 |   if (!handle) handle = dlopen("libmpi.so.40", mode);
93 |   if (!handle) handle = dlopen("libmpi.so.20", mode);
95 |   if (!handle) handle = dlopen("libmpi.so.12", mode);
97 |   if (!handle) handle = dlopen("libmpi.so.1", mode);
99 |   if (!handle) handle = dlopen("libmpi.so.0", mode);
102 |   if (!handle) handle = dlopen("libmpi.so", mode);
108 |   PyMPI_OPENMPI_dlopen_libmpi();
117 |   PyMPI_OPENMPI_dlopen_libmpi();
123 | #endif /* !HAVE_DLOPEN */
124 | #endif /* !OPENMPI_DLOPEN_LIBMPI */
{% endraw %}

```
### VTK/ThirdParty/glew/vtkglew/src/glew.c

```cpp

{% raw %}
88 |     if ((h = dlopen(NULL, RTLD_LAZY | RTLD_LOCAL)) == NULL) return NULL;
114 |     image = dlopen("/System/Library/Frameworks/OpenGL.framework/Versions/Current/OpenGL", RTLD_LAZY);
{% endraw %}

```
### VTK/ThirdParty/libxml2/vtklibxml2/config_cmake.h.in

```

{% raw %}
12 | /* Have dlopen based dso */
13 | #cmakedefine HAVE_DLOPEN
{% endraw %}

```
### VTK/ThirdParty/libxml2/vtklibxml2/xmlmodule.c

```cpp

{% raw %}
205 | #if defined(HAVE_DLOPEN) && !defined(_WIN32)
224 |     return dlopen(name, RTLD_GLOBAL | RTLD_NOW);
256 | #else /* ! HAVE_DLOPEN */
301 | #endif /* ! HAVE_DLOPEN */
{% endraw %}

```
### VTK/ThirdParty/libxml2/vtklibxml2/CMakeLists.txt

```

{% raw %}
42 | # Check for symbol dlopen separately from the dl library.
43 | CHECK_LIBRARY_EXISTS("${LIBXML2_LIBS}" dlopen "" HAVE_DLOPEN)
{% endraw %}

```
### VTK/ThirdParty/sqlite/vtksqlite/sqlite3.c

```cpp

{% raw %}
2403 |   void *(*xDlOpen)(sqlite3_vfs*, const char *zFilename);
16086 | SQLITE_PRIVATE void *sqlite3OsDlOpen(sqlite3_vfs *, const char *);
22578 | SQLITE_PRIVATE void *sqlite3OsDlOpen(sqlite3_vfs *pVfs, const char *zPath){
22579 |   return pVfs->xDlOpen(pVfs, zPath);
39083 | static void *unixDlOpen(sqlite3_vfs *NotUsed, const char *zFilename){
39085 |   return dlopen(zFilename, RTLD_NOW | RTLD_GLOBAL);
39090 | ** unixDlOpen() fails (returns a null pointer). If a more detailed error
39133 |   #define unixDlOpen  0
40516 |     unixDlOpen,           /* xDlOpen */                     \
46510 | static void *winDlOpen(sqlite3_vfs *pVfs, const char *zFilename){
46517 |     OSTRACE(("DLOPEN name=%s, handle=%p\n", zFilename, (void*)0));
46522 |     OSTRACE(("DLOPEN name=%s, handle=%p\n", zFilename, (void*)0));
46532 |     OSTRACE(("DLOPEN name=%s, handle=%p\n", zFilename, (void*)0));
46547 |   OSTRACE(("DLOPEN name=%s, handle=%p\n", zFilename, (void*)h));
46569 |   #define winDlOpen  0
46787 |     winDlOpen,             /* xDlOpen */
46812 |     winDlOpen,             /* xDlOpen */
46837 |     winDlOpen,             /* xDlOpen */
46862 |     winDlOpen,             /* xDlOpen */
46997 | static void *memdbDlOpen(sqlite3_vfs*, const char *zFilename);
47018 |   memdbDlOpen,                 /* xDlOpen */
47321 | static void *memdbDlOpen(sqlite3_vfs *pVfs, const char *zPath){
47322 |   return ORIGVFS(pVfs)->xDlOpen(ORIGVFS(pVfs), zPath);
121186 |   handle = sqlite3OsDlOpen(pVfs, zFile);
121191 |     handle = sqlite3OsDlOpen(pVfs, zAltFile);
195756 | static void *rbuVfsDlOpen(sqlite3_vfs *pVfs, const char *zPath){
195758 |   return pRealVfs->xDlOpen(pRealVfs, zPath);
195859 |     rbuVfsDlOpen,                 /* xDlOpen */
{% endraw %}

```
### VTK/ThirdParty/hdf5/vtkhdf5/src/H5PLpkg.h

```cpp

{% raw %}
96 | #   define H5PL_OPEN_DLIB(S) dlopen(S, RTLD_LAZY)
105 | #   define H5PL_CLR_ERROR HERROR(H5E_PLUGIN, H5E_CANTGET, "can't dlopen:%s", dlerror())
{% endraw %}

```
### CMake/ParaViewValgrindSuppressions.supp

```

{% raw %}
2053 |    fun:dlopen
2160 |    fun:dlopen
2366 |    fun:__libc_dlopen_mode
3872 |    fun:dlopen
12638 |    fun:dlopen
14451 |    fun:dlopen
14473 |    fun:dlopen_doit
14476 |    fun:dlopen@@GLIBC_2.2.5
14505 |    fun:dlopen
14535 |    fun:dlopen
24135 |    fun:dlopen@@GLIBC_2.2.5
24588 |    fun:dlopen_doit
24591 |    fun:dlopen@@GLIBC_2.2.5
24616 |    fun:dlopen_doit
24619 |    fun:dlopen@@GLIBC_2.2.5
24636 |    fun:dlopen_doit
24639 |    fun:dlopen@@GLIBC_2.2.5
24664 |    fun:dlopen_doit
24667 |    fun:dlopen@@GLIBC_2.2.5
24749 |    fun:dlopen_doit
24752 |    fun:dlopen@@GLIBC_2.2.5
24777 |    fun:dlopen_doit
24780 |    fun:dlopen@@GLIBC_2.2.5
24805 |    fun:dlopen_doit
24808 |    fun:dlopen@@GLIBC_2.2.5
24821 |    fun:dlopen@@GLIBC_2.2.5
24841 |    fun:dlopen_doit
24844 |    fun:dlopen@@GLIBC_2.2.5
29531 |    fun:dlopen_doit
29534 |    fun:dlopen@@GLIBC_2.2.5
29559 |    fun:dlopen_doit
29562 |    fun:dlopen@@GLIBC_2.2.5
29588 |    fun:dlopen_doit
29591 |    fun:dlopen@@GLIBC_2.2.5
29616 |    fun:dlopen_doit
29619 |    fun:dlopen@@GLIBC_2.2.5
29643 |    fun:dlopen_doit
29646 |    fun:dlopen@@GLIBC_2.2.5
29671 |    fun:dlopen_doit
29674 |    fun:dlopen@@GLIBC_2.2.5
29701 |    fun:dlopen_doit
29704 |    fun:dlopen@@GLIBC_2.2.5
29729 |    fun:dlopen_doit
29732 |    fun:dlopen@@GLIBC_2.2.5
29752 |    fun:dlopen@@GLIBC_2.2.5
29780 |    fun:dlopen@@GLIBC_2.2.5
35962 |    fun:dlopen_doit
35965 |    fun:dlopen@@GLIBC_2.2.5
35990 |    fun:dlopen_doit
35993 |    fun:dlopen@@GLIBC_2.2.5
36018 |    fun:dlopen_doit
36021 |    fun:dlopen@@GLIBC_2.2.5
37834 |    fun:dlopen_doit
37837 |    fun:dlopen@@GLIBC_2.2.5
37856 |    fun:dlopen_doit
37859 |    fun:dlopen@@GLIBC_2.2.5
37886 |    fun:dlopen_doit
37889 |    fun:dlopen@@GLIBC_2.2.5
37914 |    fun:dlopen_doit
37917 |    fun:dlopen@@GLIBC_2.2.5
37945 |    fun:dlopen_doit
37948 |    fun:dlopen@@GLIBC_2.2.5
37968 |    fun:dlopen_doit
37971 |    fun:dlopen@@GLIBC_2.2.5
37995 |    fun:dlopen_doit
37998 |    fun:dlopen@@GLIBC_2.2.5
{% endraw %}

```
### Utilities/VisItBridge/Library/VisItLib/common/plugin/PluginManager.C

```cpp

{% raw %}
1588 |     // dlopen the plugin
1589 |     handle = dlopen(pluginFile.c_str(), RTLD_LAZY);
{% endraw %}

```
### ThirdParty/NvPipe/vtknvpipe/winposix.c

```cpp

{% raw %}
37 | dlopen(const char* nm, int flags) {
{% endraw %}

```
### ThirdParty/NvPipe/vtknvpipe/decode.c

```cpp

{% raw %}
133 |     *pInstance = dlopen(__DriverLibName, RTLD_NOW);
137 |         printf("dlopen \"%s\" failed!\n", __DriverLibName);
{% endraw %}

```
### ThirdParty/NvPipe/vtknvpipe/winposix.h

```cpp

{% raw %}
39 | void* dlopen(const char* handle, int flags);
{% endraw %}

```
### ThirdParty/NvPipe/vtknvpipe/encode.c

```cpp

{% raw %}
62 |     void* lib; /**< dlopen'd library handle for nvenc */
846 |     nvp->lib = dlopen(NVENC_LIB, RTLD_LAZY|RTLD_LOCAL);
{% endraw %}

```