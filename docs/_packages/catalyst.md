---
name: "catalyst"
layout: package
next_package: cbtf-krell
previous_package: casacore
languages: ['python', 'c']
---
## 4.4.0
23 / 25420 files match, 10 filtered matches.

 - [VTK/ThirdParty/mpi4py/vtkmpi4py/src/dynload.c](#vtkthirdpartympi4pyvtkmpi4pysrcdynloadc)
 - [VTK/ThirdParty/mpi4py/vtkmpi4py/src/rc.py](#vtkthirdpartympi4pyvtkmpi4pysrcrcpy)
 - [VTK/ThirdParty/mpi4py/vtkmpi4py/src/dynload.h](#vtkthirdpartympi4pyvtkmpi4pysrcdynloadh)
 - [VTK/ThirdParty/mpi4py/vtkmpi4py/src/compat/sicortex.h](#vtkthirdpartympi4pyvtkmpi4pysrccompatsicortexh)
 - [VTK/ThirdParty/mpi4py/vtkmpi4py/src/compat/hpmpi.h](#vtkthirdpartympi4pyvtkmpi4pysrccompathpmpih)
 - [VTK/ThirdParty/mpi4py/vtkmpi4py/src/compat/openmpi.h](#vtkthirdpartympi4pyvtkmpi4pysrccompatopenmpih)
 - [VTK/ThirdParty/glew/vtkglew/src/glew.c](#vtkthirdpartyglewvtkglewsrcglewc)
 - [VTK/ThirdParty/libxml2/vtklibxml2/xmlmodule.c](#vtkthirdpartylibxml2vtklibxml2xmlmodulec)
 - [VTK/ThirdParty/sqlite/vtksqlite/vtk_sqlite3.c](#vtkthirdpartysqlitevtksqlitevtk_sqlite3c)
 - [Utilities/VisItBridge/Library/VisItLib/common/plugin/PluginManager.C](#utilitiesvisitbridgelibraryvisitlibcommonpluginpluginmanagerc)

### VTK/ThirdParty/mpi4py/vtkmpi4py/src/dynload.c

```c

{% raw %}
5 | #include "dynload.h"
6 | 
7 | static PyObject *
8 | dl_dlopen(PyObject *self, PyObject *args)
9 | {
10 |   void *handle = NULL;
11 |   char *filename = NULL;
12 |   int mode = 0;
13 |   if (!PyArg_ParseTuple(args, (char *)"zi:dlopen",
14 |                         &filename, &mode)) return NULL;
15 |   handle = dlopen(filename, mode);
16 |   return PyLong_FromVoidPtr(handle);
17 | }
60 | }
61 | 
62 | static PyMethodDef dl_methods[] = {
63 |   { (char *)"dlopen",  dl_dlopen,  METH_VARARGS, NULL },
64 |   { (char *)"dlsym",   dl_dlsym,   METH_VARARGS, NULL },
65 |   { (char *)"dlclose", dl_dlclose, METH_O,       NULL },
{% endraw %}

```
### VTK/ThirdParty/mpi4py/vtkmpi4py/src/rc.py

```python

{% raw %}
50 |     import sys, os, imp
51 |     #
52 |     try:
53 |         from mpi4py.dl import dlopen, RTLD_NOW, RTLD_GLOBAL
54 |         from mpi4py.dl import dlerror
55 |     except ImportError:
56 |         from ctypes import CDLL as dlopen, RTLD_GLOBAL
57 |         try:
58 |             from DLFCN import RTLD_NOW
92 |             "profiler '%s' not found in '%s'" % (name, relpath))
93 |     #
94 |     global _pmpi_
95 |     handle = dlopen(filename, RTLD_NOW|RTLD_GLOBAL)
96 |     if handle:
97 |         _pmpi_.append( (name, (handle, filename)) )
{% endraw %}

```
### VTK/ThirdParty/mpi4py/vtkmpi4py/src/dynload.h

```c

{% raw %}
40 |   #if defined(__cplusplus)
41 |   extern "C" {
42 |   #endif
43 |   extern void *dlopen(const char *, int);
44 |   extern void *dlsym(void *, const char *);
45 |   extern int   dlclose(void *);
{% endraw %}

```
### VTK/ThirdParty/mpi4py/vtkmpi4py/src/compat/sicortex.h

```c

{% raw %}
2 | 
3 | #include "../dynload.h"
4 | 
5 | static void PyMPI_SCMPI_dlopen_libslurm(void)
6 | {
7 |   (void)dlopen("libslurm.so", RTLD_NOW|RTLD_GLOBAL|RTLD_NOLOAD);
8 |   (void)dlerror();
9 | }
10 | 
11 | static int PyMPI_SCMPI_MPI_Init(int *argc, char ***argv)
12 | {
13 |   PyMPI_SCMPI_dlopen_libslurm();
14 |   return MPI_Init(argc, argv);
15 | }
19 | static int PyMPI_SCMPI_MPI_Init_thread(int *argc, char ***argv,
20 |                                        int required, int *provided)
21 | {
22 |   PyMPI_SCMPI_dlopen_libslurm();
23 |   return MPI_Init_thread(argc, argv, required, provided);
24 | }
{% endraw %}

```
### VTK/ThirdParty/mpi4py/vtkmpi4py/src/compat/hpmpi.h

```c

{% raw %}
29 | 
30 | #include "../dynload.h"
31 | 
32 | static void HPMPI_dlopen_libmpi(void)
33 | {
34 |   void *handle = 0;
38 |   #endif
39 | #if defined(__APPLE__)
40 |   /* Mac OS X */
41 |   if (!handle) handle = dlopen("libhpmpi.3.dylib", mode);
42 |   if (!handle) handle = dlopen("libhpmpi.2.dylib", mode);
43 |   if (!handle) handle = dlopen("libhpmpi.1.dylib", mode);
44 |   if (!handle) handle = dlopen("libhpmpi.0.dylib", mode);
45 |   if (!handle) handle = dlopen("libhpmpi.dylib",   mode);
46 | #else
47 |   /* GNU/Linux and others*/
48 |   if (!handle) handle = dlopen("libhpmpi.so.3", mode);
49 |   if (!handle) handle = dlopen("libhpmpi.so.2", mode);
50 |   if (!handle) handle = dlopen("libhpmpi.so.1", mode);
51 |   if (!handle) handle = dlopen("libhpmpi.so.0", mode);
52 |   if (!handle) handle = dlopen("libhpmpi.so",   mode);
53 | #endif
54 | }
55 | 
56 | static int PyMPI_HPMPI_MPI_Init(int *argc, char ***argv)
57 | {
58 |   HPMPI_dlopen_libmpi();
59 |   return MPI_Init(argc, argv);
60 | }
64 | static int PyMPI_HPMPI_MPI_Init_thread(int *argc, char ***argv,
65 |                                          int required, int *provided)
66 | {
67 |   HPMPI_dlopen_libmpi();
68 |   return MPI_Init_thread(argc, argv, required, provided);
69 | }
{% endraw %}

```
### VTK/ThirdParty/mpi4py/vtkmpi4py/src/compat/openmpi.h

```c

{% raw %}
20 | #include "../dynload.h"
21 | 
22 | /*
23 | static void * my_dlopen(const char *name, int mode) {
24 |   void *handle;
25 |   static int called = 0;
40 |     #endif
41 |     printf("\n");
42 |   }
43 |   handle = dlopen(name, mode);
44 |   printf("dlopen(\"%s\",0x%X) -> %p\n", name, mode, handle);
45 |   printf("dlerror() -> %s\n\n", dlerror());
46 |   return handle;
48 | #define dlopen my_dlopen
49 | */
50 | 
51 | static void OPENMPI_dlopen_libmpi(void)
52 | {
53 |   void *handle = 0;
56 |   mode |= RTLD_NOLOAD;
57 |   #endif
58 | #if defined(__CYGWIN__)
59 |   if (!handle) handle = dlopen("cygmpi.dll", mode);
60 |   if (!handle) handle = dlopen("mpi.dll",    mode);
61 | #elif defined(__APPLE__)
62 |   /* Mac OS X */
63 |   if (!handle) handle = dlopen("libmpi.3.dylib", mode);
64 |   if (!handle) handle = dlopen("libmpi.2.dylib", mode);
65 |   if (!handle) handle = dlopen("libmpi.1.dylib", mode);
66 |   if (!handle) handle = dlopen("libmpi.0.dylib", mode);
67 |   if (!handle) handle = dlopen("libmpi.dylib",   mode);
68 | #else
69 |   /* GNU/Linux and others*/
70 |   if (!handle) handle = dlopen("libmpi.so.3", mode);
71 |   if (!handle) handle = dlopen("libmpi.so.2", mode);
72 |   if (!handle) handle = dlopen("libmpi.so.1", mode);
73 |   if (!handle) handle = dlopen("libmpi.so.0", mode);
74 |   if (!handle) handle = dlopen("libmpi.so",   mode);
75 | #endif
76 | }
77 | 
78 | static int PyMPI_OPENMPI_MPI_Init(int *argc, char ***argv)
79 | {
80 |   OPENMPI_dlopen_libmpi();
81 |   return MPI_Init(argc, argv);
82 | }
86 | static int PyMPI_OPENMPI_MPI_Init_thread(int *argc, char ***argv,
87 |                                          int required, int *provided)
88 | {
89 |   OPENMPI_dlopen_libmpi();
90 |   return MPI_Init_thread(argc, argv, required, provided);
91 | }
{% endraw %}

```
### VTK/ThirdParty/glew/vtkglew/src/glew.c

```c

{% raw %}
96 | 
97 |   if (h == NULL)
98 |   {
99 |     if ((h = dlopen(NULL, RTLD_LAZY | RTLD_LOCAL)) == NULL) return NULL;
100 |     gpa = dlsym(h, "glXGetProcAddress");
101 |   }
119 | 
120 |   if (h == NULL)
121 |   {
122 |     if ((h = dlopen(NULL, RTLD_LAZY | RTLD_LOCAL)) == NULL)
123 |       return NULL;
124 |     gpa = dlsym(h, "OSMesaGetProcAddress");
146 |   void* addr;
147 |   if (NULL == image)
148 |   {
149 |     image = dlopen("/System/Library/Frameworks/OpenGL.framework/Versions/Current/OpenGL", RTLD_LAZY);
150 |   }
151 |   if( !image ) return NULL;
{% endraw %}

```
### VTK/ThirdParty/libxml2/vtklibxml2/xmlmodule.c

```c

{% raw %}
208 | static void *
209 | xmlModulePlatformOpen(const char *name)
210 | {
211 |     return dlopen(name, RTLD_GLOBAL | RTLD_NOW);
212 | }
213 | 
{% endraw %}

```
### VTK/ThirdParty/sqlite/vtksqlite/vtk_sqlite3.c

```c

{% raw %}
25671 | #include <dlfcn.h>
25672 | static void *unixDlOpen(vtk_sqlite3_vfs *NotUsed, const char *zFilename){
25673 |   UNUSED_PARAMETER(NotUsed);
25674 |   return dlopen(zFilename, RTLD_NOW | RTLD_GLOBAL);
25675 | }
25676 | 
{% endraw %}

```
### Utilities/VisItBridge/Library/VisItLib/common/plugin/PluginManager.C

```c

{% raw %}
1560 |     debug1 << "Not opening " << pluginFile << " because this is a static build." << endl;
1561 | #else
1562 |     // dlopen the plugin
1563 |     handle = dlopen(pluginFile.c_str(), RTLD_LAZY);
1564 |     if (!handle)
1565 |     {
{% endraw %}

```