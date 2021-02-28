---
name: "multiverso"
layout: package
next_package: arrow
previous_package: openssl
library_name: dlopen
matches: ['dlopen']
languages: ['c']
---
## 143187
1 / 255 files match, 1 filtered matches.

 - [include/multiverso/net/mpi_net.h](#includemultiversonetmpi_neth)

### include/multiverso/net/mpi_net.h

```c

{% raw %}
34 |   static MPI_Datatype GetDataType(float*)  { return MPI_FLOAT; }
35 |   static MPI_Datatype GetDataType(double*) { return MPI_DOUBLE; }
36 | 
37 |   static void dlopen_libmpi()
38 |   {
39 |   #ifndef _WIN32
48 |     #ifdef RTLD_NOLOAD
49 |     mode |= RTLD_NOLOAD;
50 |     #endif
51 |     if (!handle) handle = dlopen("libmpi_cxx.so",   mode);
52 |   #endif
53 |   #endif
100 |     if (!inited_) {
101 |       // NOTICE: Preload libmpi with the right mode. Otherwise python will load it in 
102 |       // a private which will cause errors
103 |       dlopen_libmpi();
104 |       if (argc && *argc == 0) {
105 |         // When using multithread, giving MPI_Init_thread argv with zero length will cause errors.
{% endraw %}

```