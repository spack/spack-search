---
name: "catalyst"
layout: package
next_package: py-shapely
previous_package: coreutils
languages: ['cmake', 'cpp', 'python']
---
## 4.4.0
23 / 25420 files match

 - [VTK/Rendering/OpenGL/vtkOpenGLExtensionManager.cxx](#vtkrenderingopenglvtkopenglextensionmanagercxx)
 - [VTK/Wrapping/Python/vtk/__init__.py.in](#vtkwrappingpythonvtk__init__pyin)
 - [VTK/CMake/VTKValgrindSuppressions.supp](#vtkcmakevtkvalgrindsuppressionssupp)
 - [VTK/Utilities/KWSys/vtksys/DynamicLoader.cxx](#vtkutilitieskwsysvtksysdynamicloadercxx)
 - [VTK/Utilities/KWSys/vtksys/DynamicLoader.hxx.in](#vtkutilitieskwsysvtksysdynamicloaderhxxin)
 - [VTK/Utilities/KWSys/vtksys/testDynamicLoader.cxx](#vtkutilitieskwsysvtksystestdynamicloadercxx)
 - [VTK/ThirdParty/mpi4py/vtkmpi4py/HISTORY.txt](#vtkthirdpartympi4pyvtkmpi4pyhistorytxt)
 - [VTK/ThirdParty/mpi4py/vtkmpi4py/src/dynload.c](#vtkthirdpartympi4pyvtkmpi4pysrcdynloadc)
 - [VTK/ThirdParty/mpi4py/vtkmpi4py/src/rc.py](#vtkthirdpartympi4pyvtkmpi4pysrcrcpy)
 - [VTK/ThirdParty/mpi4py/vtkmpi4py/src/dynload.h](#vtkthirdpartympi4pyvtkmpi4pysrcdynloadh)
 - [VTK/ThirdParty/mpi4py/vtkmpi4py/src/compat/sicortex.h](#vtkthirdpartympi4pyvtkmpi4pysrccompatsicortexh)
 - [VTK/ThirdParty/mpi4py/vtkmpi4py/src/compat/hpmpi.h](#vtkthirdpartympi4pyvtkmpi4pysrccompathpmpih)
 - [VTK/ThirdParty/mpi4py/vtkmpi4py/src/compat/openmpi.h](#vtkthirdpartympi4pyvtkmpi4pysrccompatopenmpih)
 - [VTK/ThirdParty/glew/vtkglew/src/glew.c](#vtkthirdpartyglewvtkglewsrcglewc)
 - [VTK/ThirdParty/libxml2/vtklibxml2/config_cmake.h.in](#vtkthirdpartylibxml2vtklibxml2config_cmakehin)
 - [VTK/ThirdParty/libxml2/vtklibxml2/xmlmodule.c](#vtkthirdpartylibxml2vtklibxml2xmlmodulec)
 - [VTK/ThirdParty/libxml2/vtklibxml2/CMakeLists.txt](#vtkthirdpartylibxml2vtklibxml2cmakeliststxt)
 - [VTK/ThirdParty/sqlite/vtksqlite/vtk_sqlite3.c](#vtkthirdpartysqlitevtksqlitevtk_sqlite3c)
 - [VTK/ThirdParty/hdf5/vtkhdf5/config/cmake/ConfigureChecks.cmake](#vtkthirdpartyhdf5vtkhdf5configcmakeconfigurecheckscmake)
 - [VTK/ThirdParty/hdf5/vtkhdf5/src/H5PL.c](#vtkthirdpartyhdf5vtkhdf5srch5plc)
 - [CMake/ParaViewValgrindSuppressions.supp](#cmakeparaviewvalgrindsuppressionssupp)
 - [Utilities/VisItBridge/Library/VisItLib/common/plugin/PluginManager.C](#utilitiesvisitbridgelibraryvisitlibcommonpluginpluginmanagerc)
 - [ThirdParty/protobuf/vtkprotobuf/src/solaris/libstdc++.la](#thirdpartyprotobufvtkprotobufsrcsolarislibstdc++la)

### VTK/Rendering/OpenGL/vtkOpenGLExtensionManager.cxx

```

{% raw %}
636 |   void* globalsymbolobject = dlopen(NULL, RTLD_GLOBAL);
{% endraw %}

```
### VTK/Wrapping/Python/vtk/__init__.py.in

```

{% raw %}
26 | # set the dlopen flags so that VTK does not run into problems with
30 |     orig_dlopen_flags = sys.getdlopenflags()
32 |     orig_dlopen_flags = None
35 |     sys.setdlopenflags(dl.RTLD_NOW|dl.RTLD_GLOBAL)
69 | # reset the dlopen flags to the original state if possible.
70 | if dl and (os.name == 'posix') and orig_dlopen_flags:
71 |     sys.setdlopenflags(orig_dlopen_flags)
74 | del orig_dlopen_flags
{% endraw %}

```
### VTK/CMake/VTKValgrindSuppressions.supp

```

{% raw %}
257 |    fun:dlopen
289 |    fun:dlopen
323 |    fun:dlopen
342 |    fun:dlopen
361 |    fun:dlopen
382 |    fun:dlopen
409 |    fun:dlopen
460 |    fun:dlopen
488 |    fun:dlopen
516 |    fun:dlopen
546 |    fun:dlopen
588 |    fun:dlopen
662 |    fun:dlopen
858 |    fun:dlopen
{% endraw %}

```
### VTK/Utilities/KWSys/vtksys/DynamicLoader.cxx

```

{% raw %}
27 | // 4. Most unix systems (including Mac OS X 10.3 and later) which use dlopen
493 |   return dlopen(libname.c_str(), RTLD_LAZY);
{% endraw %}

```
### VTK/Utilities/KWSys/vtksys/DynamicLoader.hxx.in

```

{% raw %}
41 |  * \warning dlopen on *nix system works the following way:
{% endraw %}

```
### VTK/Utilities/KWSys/vtksys/testDynamicLoader.cxx

```

{% raw %}
104 | // dlopen() on Syllable before 11/22/2007 doesn't return 0 on error
113 |   // This one is actually fun to test, since dlopen is by default loaded...wonder why :)
114 |   res += TestDynamicLoader("foobar.lib", "dlopen",0,1,0);
115 |   res += TestDynamicLoader("libdl.so", "dlopen",1,1,1);
{% endraw %}

```
### VTK/ThirdParty/mpi4py/vtkmpi4py/HISTORY.txt

```

{% raw %}
47 | * HP-MPI: fix for missing Fortran datatypes, use dlopen() to load the
97 |   MPI calls is supported in POSIX platforms implementing ``dlopen()``.
104 |   loading of extension modules in platforms supporting ``dlopen()``.
{% endraw %}

```
### VTK/ThirdParty/mpi4py/vtkmpi4py/src/dynload.c

```cpp

{% raw %}
8 | dl_dlopen(PyObject *self, PyObject *args)
13 |   if (!PyArg_ParseTuple(args, (char *)"zi:dlopen",
15 |   handle = dlopen(filename, mode);
63 |   { (char *)"dlopen",  dl_dlopen,  METH_VARARGS, NULL },
{% endraw %}

```
### VTK/ThirdParty/mpi4py/vtkmpi4py/src/rc.py

```python

{% raw %}
53 |         from mpi4py.dl import dlopen, RTLD_NOW, RTLD_GLOBAL
56 |         from ctypes import CDLL as dlopen, RTLD_GLOBAL
95 |     handle = dlopen(filename, RTLD_NOW|RTLD_GLOBAL)
{% endraw %}

```
### VTK/ThirdParty/mpi4py/vtkmpi4py/src/dynload.h

```cpp

{% raw %}
43 |   extern void *dlopen(const char *, int);
{% endraw %}

```
### VTK/ThirdParty/mpi4py/vtkmpi4py/src/compat/sicortex.h

```cpp

{% raw %}
5 | static void PyMPI_SCMPI_dlopen_libslurm(void)
7 |   (void)dlopen("libslurm.so", RTLD_NOW|RTLD_GLOBAL|RTLD_NOLOAD);
13 |   PyMPI_SCMPI_dlopen_libslurm();
22 |   PyMPI_SCMPI_dlopen_libslurm();
{% endraw %}

```
### VTK/ThirdParty/mpi4py/vtkmpi4py/src/compat/hpmpi.h

```cpp

{% raw %}
23 | #ifndef HPMPI_DLOPEN_LIBMPI
24 | #define HPMPI_DLOPEN_LIBMPI 1
27 | #if HPMPI_DLOPEN_LIBMPI
28 | #if HAVE_DLOPEN
32 | static void HPMPI_dlopen_libmpi(void)
41 |   if (!handle) handle = dlopen("libhpmpi.3.dylib", mode);
42 |   if (!handle) handle = dlopen("libhpmpi.2.dylib", mode);
43 |   if (!handle) handle = dlopen("libhpmpi.1.dylib", mode);
44 |   if (!handle) handle = dlopen("libhpmpi.0.dylib", mode);
45 |   if (!handle) handle = dlopen("libhpmpi.dylib",   mode);
48 |   if (!handle) handle = dlopen("libhpmpi.so.3", mode);
49 |   if (!handle) handle = dlopen("libhpmpi.so.2", mode);
50 |   if (!handle) handle = dlopen("libhpmpi.so.1", mode);
51 |   if (!handle) handle = dlopen("libhpmpi.so.0", mode);
52 |   if (!handle) handle = dlopen("libhpmpi.so",   mode);
58 |   HPMPI_dlopen_libmpi();
67 |   HPMPI_dlopen_libmpi();
73 | #endif /* !HAVE_DLOPEN */
74 | #endif /* !HPMPI_DLOPEN_LIBMPI */
{% endraw %}

```
### VTK/ThirdParty/mpi4py/vtkmpi4py/src/compat/openmpi.h

```cpp

{% raw %}
9 |  * library with appropriate flags to 'dlopen()' ensuring global
13 | #ifndef OPENMPI_DLOPEN_LIBMPI
14 | #define OPENMPI_DLOPEN_LIBMPI 1
17 | #if OPENMPI_DLOPEN_LIBMPI
18 | #if HAVE_DLOPEN
23 | static void * my_dlopen(const char *name, int mode) {
43 |   handle = dlopen(name, mode);
44 |   printf("dlopen(\"%s\",0x%X) -> %p\n", name, mode, handle);
48 | #define dlopen my_dlopen
51 | static void OPENMPI_dlopen_libmpi(void)
59 |   if (!handle) handle = dlopen("cygmpi.dll", mode);
60 |   if (!handle) handle = dlopen("mpi.dll",    mode);
63 |   if (!handle) handle = dlopen("libmpi.3.dylib", mode);
64 |   if (!handle) handle = dlopen("libmpi.2.dylib", mode);
65 |   if (!handle) handle = dlopen("libmpi.1.dylib", mode);
66 |   if (!handle) handle = dlopen("libmpi.0.dylib", mode);
67 |   if (!handle) handle = dlopen("libmpi.dylib",   mode);
70 |   if (!handle) handle = dlopen("libmpi.so.3", mode);
71 |   if (!handle) handle = dlopen("libmpi.so.2", mode);
72 |   if (!handle) handle = dlopen("libmpi.so.1", mode);
73 |   if (!handle) handle = dlopen("libmpi.so.0", mode);
74 |   if (!handle) handle = dlopen("libmpi.so",   mode);
80 |   OPENMPI_dlopen_libmpi();
89 |   OPENMPI_dlopen_libmpi();
95 | #endif /* !HAVE_DLOPEN */
96 | #endif /* !OPENMPI_DLOPEN_LIBMPI */
{% endraw %}

```
### VTK/ThirdParty/glew/vtkglew/src/glew.c

```cpp

{% raw %}
99 |     if ((h = dlopen(NULL, RTLD_LAZY | RTLD_LOCAL)) == NULL) return NULL;
122 |     if ((h = dlopen(NULL, RTLD_LAZY | RTLD_LOCAL)) == NULL)
149 |     image = dlopen("/System/Library/Frameworks/OpenGL.framework/Versions/Current/OpenGL", RTLD_LAZY);
{% endraw %}

```
### VTK/ThirdParty/libxml2/vtklibxml2/config_cmake.h.in

```

{% raw %}
27 | /* Have dlopen based dso */
28 | #cmakedefine HAVE_DLOPEN
{% endraw %}

```
### VTK/ThirdParty/libxml2/vtklibxml2/xmlmodule.c

```cpp

{% raw %}
192 | #ifdef HAVE_DLOPEN
211 |     return dlopen(name, RTLD_GLOBAL | RTLD_NOW);
243 | #else /* ! HAVE_DLOPEN */
288 | #endif /* ! HAVE_DLOPEN */
290 | #if defined(_WIN32) && !defined(HAVE_DLOPEN)
{% endraw %}

```
### VTK/ThirdParty/libxml2/vtklibxml2/CMakeLists.txt

```

{% raw %}
38 | CHECK_LIBRARY_EXISTS_CONCAT("dl"       dlopen         HAVE_LIBDL)
57 | # Check for symbol dlopen separately from the dl library.
58 | CHECK_LIBRARY_EXISTS("${LIBXML2_LIBS}" dlopen "" HAVE_DLOPEN)
{% endraw %}

```
### VTK/ThirdParty/sqlite/vtksqlite/vtk_sqlite3.c

```cpp

{% raw %}
1355 |   void *(*xDlOpen)(vtk_sqlite3_vfs*, const char *zFilename);
8070 | VTK_SQLITE_PRIVATE void *vtk_sqlite3OsDlOpen(vtk_sqlite3_vfs *, const char *);
12191 | VTK_SQLITE_PRIVATE void *vtk_sqlite3OsDlOpen(vtk_sqlite3_vfs *pVfs, const char *zPath){
12192 |   return pVfs->xDlOpen(pVfs, zPath);
21079 | static void *os2DlOpen(vtk_sqlite3_vfs *pVfs, const char *zFilename){
21090 | ** os2Dlopen returns zero if DosLoadModule is not successful.
21113 |   #define os2DlOpen 0
21263 |     os2DlOpen,         /* xDlOpen */
25672 | static void *unixDlOpen(vtk_sqlite3_vfs *NotUsed, const char *zFilename){
25674 |   return dlopen(zFilename, RTLD_NOW | RTLD_GLOBAL);
25679 | ** unixDlOpen() fails (returns a null pointer). If a more detailed error
25722 |   #define unixDlOpen  0
26844 |     unixDlOpen,           /* xDlOpen */                     \
28827 | static void *winDlOpen(vtk_sqlite3_vfs *pVfs, const char *zFilename){
28868 |   #define winDlOpen  0
29032 |     winDlOpen,         /* xDlOpen */
76471 |   handle = vtk_sqlite3OsDlOpen(pVfs, zFile);
{% endraw %}

```
### VTK/ThirdParty/hdf5/vtkhdf5/config/cmake/ConfigureChecks.cmake

```cmake

{% raw %}
217 |   CHECK_LIBRARY_EXISTS_CONCAT ("dl" dlopen     H5_HAVE_LIBDL)
{% endraw %}

```
### VTK/ThirdParty/hdf5/vtkhdf5/src/H5PL.c

```cpp

{% raw %}
73 | #define H5PL_OPEN_DLIB(S) dlopen(S, RTLD_NOW)
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
1562 |     // dlopen the plugin
1563 |     handle = dlopen(pluginFile.c_str(), RTLD_LAZY);
{% endraw %}

```
### ThirdParty/protobuf/vtkprotobuf/src/solaris/libstdc++.la

```

{% raw %}
22 | # The name that we can dlopen(3).
45 | # Files to dlopen/dlpreopen
46 | dlopen=''
{% endraw %}

```