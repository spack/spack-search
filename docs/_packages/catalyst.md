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

```c

{% raw %}
43 |   extern void *dlopen(const char *, int);
{% endraw %}

```
### VTK/ThirdParty/mpi4py/vtkmpi4py/src/compat/sicortex.h

```c

{% raw %}
5 | static void PyMPI_SCMPI_dlopen_libslurm(void)
7 |   (void)dlopen("libslurm.so", RTLD_NOW|RTLD_GLOBAL|RTLD_NOLOAD);
13 |   PyMPI_SCMPI_dlopen_libslurm();
22 |   PyMPI_SCMPI_dlopen_libslurm();
{% endraw %}

```
### VTK/ThirdParty/mpi4py/vtkmpi4py/src/compat/hpmpi.h

```c

{% raw %}
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
{% endraw %}

```
### VTK/ThirdParty/mpi4py/vtkmpi4py/src/compat/openmpi.h

```c

{% raw %}
23 | static void * my_dlopen(const char *name, int mode) {
43 |   handle = dlopen(name, mode);
44 |   printf("dlopen(\"%s\",0x%X) -> %p\n", name, mode, handle);
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
{% endraw %}

```
### VTK/ThirdParty/glew/vtkglew/src/glew.c

```c

{% raw %}
99 |     if ((h = dlopen(NULL, RTLD_LAZY | RTLD_LOCAL)) == NULL) return NULL;
122 |     if ((h = dlopen(NULL, RTLD_LAZY | RTLD_LOCAL)) == NULL)
149 |     image = dlopen("/System/Library/Frameworks/OpenGL.framework/Versions/Current/OpenGL", RTLD_LAZY);
{% endraw %}

```
### VTK/ThirdParty/libxml2/vtklibxml2/xmlmodule.c

```c

{% raw %}
211 |     return dlopen(name, RTLD_GLOBAL | RTLD_NOW);
{% endraw %}

```
### VTK/ThirdParty/sqlite/vtksqlite/vtk_sqlite3.c

```c

{% raw %}
25674 |   return dlopen(zFilename, RTLD_NOW | RTLD_GLOBAL);
{% endraw %}

```
### Utilities/VisItBridge/Library/VisItLib/common/plugin/PluginManager.C

```c

{% raw %}
1563 |     handle = dlopen(pluginFile.c_str(), RTLD_LAZY);
{% endraw %}

```