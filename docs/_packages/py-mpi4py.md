---
name: "py-mpi4py"
layout: package
next_package: py-mx
previous_package: py-jpype1
languages: ['python', 'c']
---
## develop
11 / 393 files match, 10 filtered matches.

 - [setup.py](#setuppy)
 - [demo/wrap-cffi/helloworld.py](#demowrap-cffihelloworldpy)
 - [src/dynload.c](#srcdynloadc)
 - [src/dynload.h](#srcdynloadh)
 - [src/lib-mpi/compat/sicortex.h](#srclib-mpicompatsicortexh)
 - [src/lib-mpi/compat/pcmpi.h](#srclib-mpicompatpcmpih)
 - [src/lib-mpi/compat/openmpi.h](#srclib-mpicompatopenmpih)
 - [src/mpi4py/__init__.py](#srcmpi4py__init__py)
 - [src/mpi4py/dl.pyi](#srcmpi4pydlpyi)
 - [test/test_dl.py](#testtest_dlpy)

### setup.py

```python

{% raw %}
173 | 
174 | def configure_dl(ext, config_cmd):
175 |     from distutils import log
176 |     log.info("checking for dlopen() availability ...")
177 |     ok = config_cmd.check_header('dlfcn.h')
178 |     if ok : ext.define_macros += [('HAVE_DLFCN_H', 1)]
179 |     ok = config_cmd.check_library('dl')
180 |     if ok: ext.libraries += ['dl']
181 |     ok = config_cmd.check_function('dlopen',
182 |                                    libraries=['dl'],
183 |                                    decl=1, call=1)
{% endraw %}

```
### demo/wrap-cffi/helloworld.py

```python

{% raw %}
12 | typedef %(_mpi_comm_t)s MPI_Comm;
13 | void sayhello(MPI_Comm);
14 | """ % vars())
15 | lib = ffi.dlopen(os.path.join(_libdir, "libhelloworld.so"))
16 | 
17 | def sayhello(comm):
{% endraw %}

```
### src/dynload.c

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
13 |   (void)self; /* unused */
14 |   if (!PyArg_ParseTuple(args, (char *)"zi:dlopen",
15 |                         &filename, &mode)) return NULL;
16 |   handle = dlopen(filename, mode);
17 |   return PyLong_FromVoidPtr(handle);
18 | }
63 | }
64 | 
65 | static PyMethodDef dl_methods[] = {
66 |   { (char *)"dlopen",  dl_dlopen,  METH_VARARGS, NULL },
67 |   { (char *)"dlsym",   dl_dlsym,   METH_VARARGS, NULL },
68 |   { (char *)"dlclose", dl_dlclose, METH_O,       NULL },
{% endraw %}

```
### src/dynload.h

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
### src/lib-mpi/compat/sicortex.h

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
### src/lib-mpi/compat/pcmpi.h

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
### src/lib-mpi/compat/openmpi.h

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
### src/mpi4py/__init__.py

```python

{% raw %}
122 |     # pylint: disable=import-outside-toplevel
123 |     import os
124 |     import sys
125 |     from .dl import dlopen, dlerror, RTLD_NOW, RTLD_GLOBAL
126 | 
127 |     def lookup_dylib(name, path):
161 |     if filename is None:
162 |         raise ValueError("profiler '{0}' not found".format(name))
163 | 
164 |     handle = dlopen(filename, RTLD_NOW | RTLD_GLOBAL)
165 |     if handle:
166 |         registry = vars(profile).setdefault('registry', [])
{% endraw %}

```
### src/mpi4py/dl.pyi

```python

{% raw %}
22 |     RTLD_SELF: Final[Handle] = ...
23 |     RTLD_MAIN_ONLY: Final[Handle] = ...
24 | 
25 | def dlopen(filename: Optional[Path], mode: int) -> Handle: ...
26 | def dlclose(handle: Optional[Handle]) -> int: ...
27 | def dlsym(handle: Optional[Handle], symbol: str) -> Address: ...
{% endraw %}

```
### test/test_dl.py

```python

{% raw %}
23 |         from ctypes.util import find_library
24 |         libm = find_library('m')
25 | 
26 |         handle = dl.dlopen(libm, dl.RTLD_LOCAL|dl.RTLD_LAZY)
27 |         self.assertTrue(handle != 0)
28 |         self.assertTrue(dl.dlerror() is None)
42 |     @unittest.skipIf(pypy_lt_510 and sys.platform == 'darwin',
43 |                      'pypy(<5.10)|darwin')
44 |     def testDL2(self):
45 |         handle = dl.dlopen(None, dl.RTLD_GLOBAL|dl.RTLD_NOW)
46 |         self.assertTrue(handle != 0)
47 |         self.assertTrue(dl.dlerror() is None)
72 |         self.assertTrue(dl.dlerror() is None)
73 | 
74 |     def testDL4(self):
75 |         handle = dl.dlopen('xxxxx', dl.RTLD_LOCAL|dl.RTLD_LAZY)
76 |         self.assertTrue(handle == 0)
77 |         self.assertTrue(dl.dlerror() is not None)
{% endraw %}

```