---
name: "py-mpi4py"
layout: package
next_package: icarus
previous_package: libxt
languages: ['python', 'c']
---
## develop
11 / 393 files match

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
176 |     log.info("checking for dlopen() availability ...")
181 |     ok = config_cmd.check_function('dlopen',
{% endraw %}

```
### demo/wrap-cffi/helloworld.py

```python

{% raw %}
15 | lib = ffi.dlopen(os.path.join(_libdir, "libhelloworld.so"))
{% endraw %}

```
### src/dynload.c

```c

{% raw %}
8 | dl_dlopen(PyObject *self, PyObject *args)
14 |   if (!PyArg_ParseTuple(args, (char *)"zi:dlopen",
16 |   handle = dlopen(filename, mode);
66 |   { (char *)"dlopen",  dl_dlopen,  METH_VARARGS, NULL },
{% endraw %}

```
### src/dynload.h

```c

{% raw %}
43 |   extern void *dlopen(const char *, int);
{% endraw %}

```
### src/lib-mpi/compat/sicortex.h

```c

{% raw %}
5 | static void PyMPI_SCMPI_dlopen_libslurm(void)
7 |   (void)dlopen("libslurm.so", RTLD_NOW|RTLD_GLOBAL|RTLD_NOLOAD);
13 |   PyMPI_SCMPI_dlopen_libslurm();
22 |   PyMPI_SCMPI_dlopen_libslurm();
{% endraw %}

```
### src/lib-mpi/compat/pcmpi.h

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
### src/lib-mpi/compat/openmpi.h

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
### src/mpi4py/__init__.py

```python

{% raw %}
125 |     from .dl import dlopen, dlerror, RTLD_NOW, RTLD_GLOBAL
164 |     handle = dlopen(filename, RTLD_NOW | RTLD_GLOBAL)
{% endraw %}

```
### src/mpi4py/dl.pyi

```python

{% raw %}
25 | def dlopen(filename: Optional[Path], mode: int) -> Handle: ...
{% endraw %}

```
### test/test_dl.py

```python

{% raw %}
26 |         handle = dl.dlopen(libm, dl.RTLD_LOCAL|dl.RTLD_LAZY)
45 |         handle = dl.dlopen(None, dl.RTLD_GLOBAL|dl.RTLD_NOW)
75 |         handle = dl.dlopen('xxxxx', dl.RTLD_LOCAL|dl.RTLD_LAZY)
{% endraw %}

```