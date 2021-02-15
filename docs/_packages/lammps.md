---
name: "lammps"
layout: package
next_package: go
previous_package: energyplus
languages: ['cpp']
---
## master
8 / 10134 files match

 - [src/USER-MOLFILE/molfile_interface.cpp](#srcuser-molfilemolfile_interfacecpp)
 - [lib/kokkos/core/src/impl/Kokkos_Profiling.cpp](#libkokkoscoresrcimplkokkos_profilingcpp)
 - [lib/molfile/vmdplugin.h](#libmolfilevmdpluginh)
 - [lib/molfile/Makefile.lammps](#libmolfilemakefilelammps)
 - [examples/COUPLE/plugin/liblammpsplugin.c](#examplescouplepluginliblammpspluginc)
 - [tools/valgrind/OpenMP.supp](#toolsvalgrindopenmpsupp)
 - [tools/valgrind/OpenMPI.supp](#toolsvalgrindopenmpisupp)
 - [doc/utils/sphinx-config/false_positives.txt](#docutilssphinx-configfalse_positivestxt)

### src/USER-MOLFILE/molfile_interface.cpp

```

{% raw %}
265 |   static void *my_dlopen(const char *fname) {
337 |   static void *my_dlopen(const char *fname) {
338 |     return dlopen(fname, RTLD_NOW);
451 |   dso = my_dlopen(filename);
{% endraw %}

```
### lib/kokkos/core/src/impl/Kokkos_Profiling.cpp

```

{% raw %}
350 |     firstProfileLibrary = dlopen(profileLibraryName, RTLD_NOW | RTLD_GLOBAL);
355 |       std::cerr << "dlopen(" << profileLibraryName
{% endraw %}

```
### lib/molfile/vmdplugin.h

```cpp

{% raw %}
49 |  *  and fini routines via dlopen() or similar operating system interfaces.
178 |  * This API is optional; if found by dlopen, it will be called after first
{% endraw %}

```
### lib/molfile/Makefile.lammps

```

{% raw %}
13 | # like dlopen(), dlsym() and so on for dynamic linking of executable
{% endraw %}

```
### examples/COUPLE/plugin/liblammpsplugin.c

```cpp

{% raw %}
31 |   handle = dlopen(lib,RTLD_NOW|RTLD_GLOBAL);
{% endraw %}

```
### tools/valgrind/OpenMP.supp

```

{% raw %}
6 |    fun:dlopen*
{% endraw %}

```
### tools/valgrind/OpenMPI.supp

```

{% raw %}
186 |    OpenMPI_dlopen_strdup1
192 |    fun:dlopen*
195 |    OpenMPI_dlopen_strdup2
204 |    OpenMPI_dlopen_strdup3
{% endraw %}

```
### doc/utils/sphinx-config/false_positives.txt

```

{% raw %}
687 | dlopen
{% endraw %}

```