---
name: "py-petsc4py"
layout: package
next_package: wrk
previous_package: mpich
languages: ['cpp']
---
## develop
1 / 221 files match

 - [src/include/compat/mpi.h](#srcincludecompatmpih)

### src/include/compat/mpi.h

```cpp

{% raw %}
8 |  * library with appropriate flags to 'dlopen()' ensuring global
12 | #if !defined(OPENMPI_DLOPEN_LIBMPI) && defined(OMPI_MAJOR_VERSION)
14 | #define OPENMPI_DLOPEN_LIBMPI 0
18 | #ifndef OPENMPI_DLOPEN_LIBMPI
19 | #define OPENMPI_DLOPEN_LIBMPI 1
22 | #if OPENMPI_DLOPEN_LIBMPI
23 | #if HAVE_DLOPEN
53 |   extern void *dlopen(const char *, int);
76 | static void * my_dlopen(const char *name, int mode) {
96 |   handle = dlopen(name, mode);
97 |   printf("dlopen(\"%s\",0x%X) -> %p\n", name, mode, handle);
101 | #define dlopen my_dlopen
104 | static void OPENMPI_dlopen_libmpi(void)
115 |   if (!handle) handle = dlopen("libmpi.40.dylib", mode);
117 |   if (!handle) handle = dlopen("libmpi.20.dylib", mode);
119 |   if (!handle) handle = dlopen("libmpi.12.dylib", mode);
121 |   if (!handle) handle = dlopen("libmpi.1.dylib", mode);
123 |   if (!handle) handle = dlopen("libmpi.0.dylib", mode);
126 |   if (!handle) handle = dlopen("libmpi.dylib", mode);
134 |   if (!handle) handle = dlopen("libmpi_ibm.so.2", mode);
135 |   if (!handle) handle = dlopen("libmpi_ibm.so.1", mode);
136 |   if (!handle) handle = dlopen("libmpi_ibm.so", mode);
138 |   if (!handle) handle = dlopen("libmpi.so.40", mode);
140 |   if (!handle) handle = dlopen("libmpi.so.20", mode);
142 |   if (!handle) handle = dlopen("libmpi.so.12", mode);
144 |   if (!handle) handle = dlopen("libmpi.so.1", mode);
146 |   if (!handle) handle = dlopen("libmpi.so.0", mode);
149 |   if (!handle) handle = dlopen("libmpi.so", mode);
157 |   OPENMPI_dlopen_libmpi();
163 | #endif /* HAVE_DLOPEN */
164 | #endif /* OPENMPI_DLOPEN_LIBMPI */
{% endraw %}

```