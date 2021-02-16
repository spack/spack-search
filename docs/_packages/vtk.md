---
name: "vtk"
layout: package
next_package: intel-tbb
previous_package: ffsb
languages: ['c']
---
## 9.0.0
14 / 19019 files match

 - [ThirdParty/mpi4py/vtkmpi4py/src/dynload.h](#thirdpartympi4pyvtkmpi4pysrcdynloadh)
 - [ThirdParty/mpi4py/vtkmpi4py/src/lib-mpi/compat/sicortex.h](#thirdpartympi4pyvtkmpi4pysrclib-mpicompatsicortexh)
 - [ThirdParty/mpi4py/vtkmpi4py/src/lib-mpi/compat/pcmpi.h](#thirdpartympi4pyvtkmpi4pysrclib-mpicompatpcmpih)
 - [ThirdParty/mpi4py/vtkmpi4py/src/lib-mpi/compat/openmpi.h](#thirdpartympi4pyvtkmpi4pysrclib-mpicompatopenmpih)
 - [ThirdParty/glew/vtkglew/src/glew.c](#thirdpartyglewvtkglewsrcglewc)
 - [ThirdParty/libxml2/vtklibxml2/xmlmodule.c](#thirdpartylibxml2vtklibxml2xmlmodulec)
 - [ThirdParty/sqlite/vtksqlite/sqlite3.c](#thirdpartysqlitevtksqlitesqlite3c)

### ThirdParty/mpi4py/vtkmpi4py/src/dynload.h

```c

{% raw %}
43 |   extern void *dlopen(const char *, int);
{% endraw %}

```
### ThirdParty/mpi4py/vtkmpi4py/src/lib-mpi/compat/sicortex.h

```c

{% raw %}
5 | static void PyMPI_SCMPI_dlopen_libslurm(void)
7 |   (void)dlopen("libslurm.so", RTLD_NOW|RTLD_GLOBAL|RTLD_NOLOAD);
13 |   PyMPI_SCMPI_dlopen_libslurm();
22 |   PyMPI_SCMPI_dlopen_libslurm();
{% endraw %}

```
### ThirdParty/mpi4py/vtkmpi4py/src/lib-mpi/compat/pcmpi.h

```c

{% raw %}
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
{% endraw %}

```
### ThirdParty/mpi4py/vtkmpi4py/src/lib-mpi/compat/openmpi.h

```c

{% raw %}
29 | static void * my_dlopen(const char *name, int mode) {
49 |   handle = dlopen(name, mode);
50 |   printf("dlopen(\"%s\",0x%X) -> %p\n", name, mode, handle);
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
{% endraw %}

```
### ThirdParty/glew/vtkglew/src/glew.c

```c

{% raw %}
88 |     if ((h = dlopen(NULL, RTLD_LAZY | RTLD_LOCAL)) == NULL) return NULL;
114 |     image = dlopen("/System/Library/Frameworks/OpenGL.framework/Versions/Current/OpenGL", RTLD_LAZY);
{% endraw %}

```
### ThirdParty/libxml2/vtklibxml2/xmlmodule.c

```c

{% raw %}
224 |     return dlopen(name, RTLD_GLOBAL | RTLD_NOW);
{% endraw %}

```
### ThirdParty/sqlite/vtksqlite/sqlite3.c

```c

{% raw %}
39085 |   return dlopen(zFilename, RTLD_NOW | RTLD_GLOBAL);
{% endraw %}

```