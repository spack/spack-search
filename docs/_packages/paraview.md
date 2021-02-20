---
name: "paraview"
layout: package
next_package: parsec
previous_package: papi
languages: ['c']
---
## 5.8.0
21 / 28269 files match, 12 filtered matches.

 - [VTK/ThirdParty/mpi4py/vtkmpi4py/src/dynload.h](#vtkthirdpartympi4pyvtkmpi4pysrcdynloadh)
 - [VTK/ThirdParty/mpi4py/vtkmpi4py/src/lib-mpi/compat/sicortex.h](#vtkthirdpartympi4pyvtkmpi4pysrclib-mpicompatsicortexh)
 - [VTK/ThirdParty/mpi4py/vtkmpi4py/src/lib-mpi/compat/pcmpi.h](#vtkthirdpartympi4pyvtkmpi4pysrclib-mpicompatpcmpih)
 - [VTK/ThirdParty/mpi4py/vtkmpi4py/src/lib-mpi/compat/openmpi.h](#vtkthirdpartympi4pyvtkmpi4pysrclib-mpicompatopenmpih)
 - [VTK/ThirdParty/glew/vtkglew/src/glew.c](#vtkthirdpartyglewvtkglewsrcglewc)
 - [VTK/ThirdParty/libxml2/vtklibxml2/xmlmodule.c](#vtkthirdpartylibxml2vtklibxml2xmlmodulec)
 - [VTK/ThirdParty/sqlite/vtksqlite/sqlite3.c](#vtkthirdpartysqlitevtksqlitesqlite3c)
 - [Utilities/VisItBridge/Library/VisItLib/common/plugin/PluginManager.C](#utilitiesvisitbridgelibraryvisitlibcommonpluginpluginmanagerc)
 - [ThirdParty/NvPipe/vtknvpipe/winposix.c](#thirdpartynvpipevtknvpipewinposixc)
 - [ThirdParty/NvPipe/vtknvpipe/decode.c](#thirdpartynvpipevtknvpipedecodec)
 - [ThirdParty/NvPipe/vtknvpipe/winposix.h](#thirdpartynvpipevtknvpipewinposixh)
 - [ThirdParty/NvPipe/vtknvpipe/encode.c](#thirdpartynvpipevtknvpipeencodec)

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
### VTK/ThirdParty/mpi4py/vtkmpi4py/src/lib-mpi/compat/sicortex.h

```c

{% raw %}
2 | 
3 | #include "../../dynload.h"
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
### VTK/ThirdParty/mpi4py/vtkmpi4py/src/lib-mpi/compat/pcmpi.h

```c

{% raw %}
42 | 
43 | #include "../../dynload.h"
44 | 
45 | static void PyMPI_PCMPI_dlopen_libmpi(void)
46 | {
47 |   void *handle1 = (void *)0;
51 |   mode |= RTLD_NOLOAD;
52 |   #endif
53 | #if defined(__APPLE__)
54 |   if (!handle1) handle1 = dlopen("libmpi.2.dylib", mode);
55 |   if (!handle1) handle1 = dlopen("libmpi.1.dylib", mode);
56 |   if (!handle1) handle1 = dlopen("libmpi.dylib", mode);
57 |   if (!handle2) handle2 = dlopen("libmpio.2.dylib", mode);
58 |   if (!handle2) handle2 = dlopen("libmpio.1.dylib", mode);
59 |   if (!handle2) handle2 = dlopen("libmpio.dylib", mode);
60 | #else
61 |   if (!handle1) handle1 = dlopen("libmpi.so.2", mode);
62 |   if (!handle1) handle1 = dlopen("libmpi.so.1", mode);
63 |   if (!handle1) handle1 = dlopen("libmpi.so", mode);
64 |   if (!handle2) handle2 = dlopen("libmpio.so.2", mode);
65 |   if (!handle2) handle2 = dlopen("libmpio.so.1", mode);
66 |   if (!handle2) handle2 = dlopen("libmpio.so", mode);
67 | #endif
68 | }
69 | 
70 | static int PyMPI_PCMPI_MPI_Init(int *argc, char ***argv)
71 | {
72 |   PyMPI_PCMPI_dlopen_libmpi();
73 |   return MPI_Init(argc, argv);
74 | }
78 | static int PyMPI_PCMPI_MPI_Init_thread(int *argc, char ***argv,
79 |                                        int required, int *provided)
80 | {
81 |   PyMPI_PCMPI_dlopen_libmpi();
82 |   return MPI_Init_thread(argc, argv, required, provided);
83 | }
{% endraw %}

```
### VTK/ThirdParty/mpi4py/vtkmpi4py/src/lib-mpi/compat/openmpi.h

```c

{% raw %}
26 | #include "../../dynload.h"
27 | 
28 | /*
29 | static void * my_dlopen(const char *name, int mode) {
30 |   void *handle;
31 |   static int called = 0;
46 |     #endif
47 |     printf("\n");
48 |   }
49 |   handle = dlopen(name, mode);
50 |   printf("dlopen(\"%s\",0x%X) -> %p\n", name, mode, handle);
51 |   printf("dlerror() -> %s\n\n", dlerror());
52 |   return handle;
54 | #define dlopen my_dlopen
55 | */
56 | 
57 | static void PyMPI_OPENMPI_dlopen_libmpi(void)
58 | {
59 |   void *handle = 0;
65 |   #endif
66 |   #if defined(OMPI_MAJOR_VERSION)
67 |   #if OMPI_MAJOR_VERSION == 3
68 |   if (!handle) handle = dlopen("libmpi.40.dylib", mode);
69 |   #elif OMPI_MAJOR_VERSION == 2
70 |   if (!handle) handle = dlopen("libmpi.20.dylib", mode);
71 |   #elif OMPI_MAJOR_VERSION == 1 && OMPI_MINOR_VERSION >= 10
72 |   if (!handle) handle = dlopen("libmpi.12.dylib", mode);
73 |   #elif OMPI_MAJOR_VERSION == 1 && OMPI_MINOR_VERSION >= 6
74 |   if (!handle) handle = dlopen("libmpi.1.dylib", mode);
75 |   #elif OMPI_MAJOR_VERSION == 1
76 |   if (!handle) handle = dlopen("libmpi.0.dylib", mode);
77 |   #endif
78 |   #endif
79 |   if (!handle) handle = dlopen("libmpi.dylib", mode);
80 | #else
81 |   /* GNU/Linux and others */
84 |   #endif
85 |   #if defined(OMPI_MAJOR_VERSION)
86 |   #if OMPI_MAJOR_VERSION >= 10 /* IBM Spectrum MPI */
87 |   if (!handle) handle = dlopen("libmpi_ibm.so.2", mode);
88 |   if (!handle) handle = dlopen("libmpi_ibm.so.1", mode);
89 |   if (!handle) handle = dlopen("libmpi_ibm.so", mode);
90 |   #elif OMPI_MAJOR_VERSION == 3
91 |   if (!handle) handle = dlopen("libmpi.so.40", mode);
92 |   #elif OMPI_MAJOR_VERSION == 2
93 |   if (!handle) handle = dlopen("libmpi.so.20", mode);
94 |   #elif OMPI_MAJOR_VERSION == 1 && OMPI_MINOR_VERSION >= 10
95 |   if (!handle) handle = dlopen("libmpi.so.12", mode);
96 |   #elif OMPI_MAJOR_VERSION == 1 && OMPI_MINOR_VERSION >= 6
97 |   if (!handle) handle = dlopen("libmpi.so.1", mode);
98 |   #elif OMPI_MAJOR_VERSION == 1
99 |   if (!handle) handle = dlopen("libmpi.so.0", mode);
100 |   #endif
101 |   #endif
102 |   if (!handle) handle = dlopen("libmpi.so", mode);
103 | #endif
104 | }
105 | 
106 | static int PyMPI_OPENMPI_MPI_Init(int *argc, char ***argv)
107 | {
108 |   PyMPI_OPENMPI_dlopen_libmpi();
109 |   return MPI_Init(argc, argv);
110 | }
114 | static int PyMPI_OPENMPI_MPI_Init_thread(int *argc, char ***argv,
115 |                                          int required, int *provided)
116 | {
117 |   PyMPI_OPENMPI_dlopen_libmpi();
118 |   return MPI_Init_thread(argc, argv, required, provided);
119 | }
{% endraw %}

```
### VTK/ThirdParty/glew/vtkglew/src/glew.c

```c

{% raw %}
85 | 
86 |   if (h == NULL)
87 |   {
88 |     if ((h = dlopen(NULL, RTLD_LAZY | RTLD_LOCAL)) == NULL) return NULL;
89 |     gpa = dlsym(h, "glXGetProcAddress");
90 |   }
111 |   void* addr;
112 |   if (NULL == image)
113 |   {
114 |     image = dlopen("/System/Library/Frameworks/OpenGL.framework/Versions/Current/OpenGL", RTLD_LAZY);
115 |   }
116 |   if( !image ) return NULL;
{% endraw %}

```
### VTK/ThirdParty/libxml2/vtklibxml2/xmlmodule.c

```c

{% raw %}
221 | static void *
222 | xmlModulePlatformOpen(const char *name)
223 | {
224 |     return dlopen(name, RTLD_GLOBAL | RTLD_NOW);
225 | }
226 | 
{% endraw %}

```
### VTK/ThirdParty/sqlite/vtksqlite/sqlite3.c

```c

{% raw %}
39082 | #include <dlfcn.h>
39083 | static void *unixDlOpen(sqlite3_vfs *NotUsed, const char *zFilename){
39084 |   UNUSED_PARAMETER(NotUsed);
39085 |   return dlopen(zFilename, RTLD_NOW | RTLD_GLOBAL);
39086 | }
39087 | 
{% endraw %}

```
### Utilities/VisItBridge/Library/VisItLib/common/plugin/PluginManager.C

```c

{% raw %}
1586 |     handle = (void *)lib;
1587 | #else
1588 |     // dlopen the plugin
1589 |     handle = dlopen(pluginFile.c_str(), RTLD_LAZY);
1590 |     if (!handle)
1591 |     {
{% endraw %}

```
### ThirdParty/NvPipe/vtknvpipe/winposix.c

```c

{% raw %}
34 | #endif
35 | 
36 | void*
37 | dlopen(const char* nm, int flags) {
38 |     (void)flags;
39 |     HINSTANCE lib = LoadLibrary(nm);
{% endraw %}

```
### ThirdParty/NvPipe/vtknvpipe/decode.c

```c

{% raw %}
134 | 
135 |     if (*pInstance == NULL)
136 |     {
137 |         printf("dlopen \"%s\" failed!\n", __DriverLibName);
138 |         return CUDA_ERROR_UNKNOWN;
139 |     }
{% endraw %}

```
### ThirdParty/NvPipe/vtknvpipe/winposix.h

```c

{% raw %}
36 |     RTLD_LAZY, RTLD_NOW, RTLD_GLOBAL, RTLD_LOCAL
37 | };
38 | 
39 | void* dlopen(const char* handle, int flags);
40 | int dlclose(void* handle);
41 | void* dlsym(void* __restrict handle, const char* __restrict symbol);
{% endraw %}

```
### ThirdParty/NvPipe/vtknvpipe/encode.c

```c

{% raw %}
59 |     nvp_impl_t impl;
60 |     uint64_t bitrate;
61 |     NV_ENCODE_API_FUNCTION_LIST f;
62 |     void* lib; /**< dlopen'd library handle for nvenc */
63 |     CUcontext ctx;
64 |     void* encoder; /**< the nvEnc opaque object */
843 |     nvp->bitrate = bitrate;
844 | 
845 |     CLEAR_DL_ERRORS();
846 |     nvp->lib = dlopen(NVENC_LIB, RTLD_LAZY|RTLD_LOCAL);
847 |     if(nvp->lib == NULL) {
848 |         ERR(enc, "error loading %s: %s", NVENC_LIB, dlerror());
{% endraw %}

```