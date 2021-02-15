---
name: "vtk"
layout: package
next_package: intel-tbb
previous_package: ffsb
languages: ['cpp']
---
## 9.0.0
14 / 19019 files match

 - [Utilities/KWSys/vtksys/DynamicLoader.cxx](#utilitieskwsysvtksysdynamicloadercxx)
 - [Utilities/KWSys/vtksys/DynamicLoader.hxx.in](#utilitieskwsysvtksysdynamicloaderhxxin)
 - [Utilities/KWSys/vtksys/testDynamicLoader.cxx](#utilitieskwsysvtksystestdynamicloadercxx)
 - [ThirdParty/mpi4py/vtkmpi4py/CHANGES.rst](#thirdpartympi4pyvtkmpi4pychangesrst)
 - [ThirdParty/mpi4py/vtkmpi4py/src/dynload.h](#thirdpartympi4pyvtkmpi4pysrcdynloadh)
 - [ThirdParty/mpi4py/vtkmpi4py/src/lib-mpi/compat/sicortex.h](#thirdpartympi4pyvtkmpi4pysrclib-mpicompatsicortexh)
 - [ThirdParty/mpi4py/vtkmpi4py/src/lib-mpi/compat/pcmpi.h](#thirdpartympi4pyvtkmpi4pysrclib-mpicompatpcmpih)
 - [ThirdParty/mpi4py/vtkmpi4py/src/lib-mpi/compat/openmpi.h](#thirdpartympi4pyvtkmpi4pysrclib-mpicompatopenmpih)
 - [ThirdParty/glew/vtkglew/src/glew.c](#thirdpartyglewvtkglewsrcglewc)
 - [ThirdParty/libxml2/vtklibxml2/config_cmake.h.in](#thirdpartylibxml2vtklibxml2config_cmakehin)
 - [ThirdParty/libxml2/vtklibxml2/xmlmodule.c](#thirdpartylibxml2vtklibxml2xmlmodulec)
 - [ThirdParty/libxml2/vtklibxml2/CMakeLists.txt](#thirdpartylibxml2vtklibxml2cmakeliststxt)
 - [ThirdParty/sqlite/vtksqlite/sqlite3.c](#thirdpartysqlitevtksqlitesqlite3c)
 - [ThirdParty/hdf5/vtkhdf5/src/H5PLpkg.h](#thirdpartyhdf5vtkhdf5srch5plpkgh)

### Utilities/KWSys/vtksys/DynamicLoader.cxx

```

{% raw %}
27 | //   later) which use dlopen
452 | // later) which use dlopen
462 |   return dlopen(libname.c_str(), RTLD_LAZY);
{% endraw %}

```
### Utilities/KWSys/vtksys/DynamicLoader.hxx.in

```

{% raw %}
32 |  * \warning dlopen on *nix system works the following way:
{% endraw %}

```
### Utilities/KWSys/vtksys/testDynamicLoader.cxx

```

{% raw %}
96 | // dlopen() on Syllable before 11/22/2007 doesn't return 0 on error
106 |   // This one is actually fun to test, since dlopen is by default
108 |   res += TestDynamicLoader("foobar.lib", "dlopen", 0, 1, 0);
109 |   res += TestDynamicLoader("libdl.so", "dlopen", 1, 1, 1);
{% endraw %}

```
### ThirdParty/mpi4py/vtkmpi4py/CHANGES.rst

```

{% raw %}
190 | * HP-MPI: fix for missing Fortran datatypes, use dlopen() to load the
240 |   MPI calls is supported in POSIX platforms implementing ``dlopen()``.
247 |   loading of extension modules in platforms supporting ``dlopen()``.
{% endraw %}

```
### ThirdParty/mpi4py/vtkmpi4py/src/dynload.h

```cpp

{% raw %}
43 |   extern void *dlopen(const char *, int);
{% endraw %}

```
### ThirdParty/mpi4py/vtkmpi4py/src/lib-mpi/compat/sicortex.h

```cpp

{% raw %}
5 | static void PyMPI_SCMPI_dlopen_libslurm(void)
7 |   (void)dlopen("libslurm.so", RTLD_NOW|RTLD_GLOBAL|RTLD_NOLOAD);
13 |   PyMPI_SCMPI_dlopen_libslurm();
22 |   PyMPI_SCMPI_dlopen_libslurm();
{% endraw %}

```
### ThirdParty/mpi4py/vtkmpi4py/src/lib-mpi/compat/pcmpi.h

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
### ThirdParty/mpi4py/vtkmpi4py/src/lib-mpi/compat/openmpi.h

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
### ThirdParty/glew/vtkglew/src/glew.c

```cpp

{% raw %}
88 |     if ((h = dlopen(NULL, RTLD_LAZY | RTLD_LOCAL)) == NULL) return NULL;
114 |     image = dlopen("/System/Library/Frameworks/OpenGL.framework/Versions/Current/OpenGL", RTLD_LAZY);
{% endraw %}

```
### ThirdParty/libxml2/vtklibxml2/config_cmake.h.in

```

{% raw %}
12 | /* Have dlopen based dso */
13 | #cmakedefine HAVE_DLOPEN
{% endraw %}

```
### ThirdParty/libxml2/vtklibxml2/xmlmodule.c

```cpp

{% raw %}
205 | #if defined(HAVE_DLOPEN) && !defined(_WIN32)
224 |     return dlopen(name, RTLD_GLOBAL | RTLD_NOW);
256 | #else /* ! HAVE_DLOPEN */
301 | #endif /* ! HAVE_DLOPEN */
{% endraw %}

```
### ThirdParty/libxml2/vtklibxml2/CMakeLists.txt

```

{% raw %}
42 | # Check for symbol dlopen separately from the dl library.
43 | CHECK_LIBRARY_EXISTS("${LIBXML2_LIBS}" dlopen "" HAVE_DLOPEN)
{% endraw %}

```
### ThirdParty/sqlite/vtksqlite/sqlite3.c

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
### ThirdParty/hdf5/vtkhdf5/src/H5PLpkg.h

```cpp

{% raw %}
96 | #   define H5PL_OPEN_DLIB(S) dlopen(S, RTLD_LAZY)
105 | #   define H5PL_CLR_ERROR HERROR(H5E_PLUGIN, H5E_CANTGET, "can't dlopen:%s", dlerror())
{% endraw %}

```