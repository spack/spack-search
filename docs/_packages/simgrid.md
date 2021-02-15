---
name: "simgrid"
layout: package
next_package: rhash
previous_package: libgpg-error
languages: []
---
## 3.16
10 / 2355 files match

 - [CMakeLists.txt](#cmakeliststxt)
 - [src/simgrid/sg_config.cpp](#srcsimgridsg_configcpp)
 - [src/smpi/smpi_global.cpp](#srcsmpismpi_globalcpp)
 - [src/simix/smx_context.cpp](#srcsimixsmx_contextcpp)
 - [teshsuite/smpi/CMakeLists.txt](#teshsuitesmpicmakeliststxt)
 - [teshsuite/smpi/mpich3-test/coll/CMakeLists.txt](#teshsuitesmpimpich3-testcollcmakeliststxt)
 - [teshsuite/smpi/privatization/privatization_dlopen.tesh](#teshsuitesmpiprivatizationprivatization_dlopentesh)
 - [tools/simgrid.supp](#toolssimgridsupp)
 - [doc/doxygen/FAQ.doc](#docdoxygenfaqdoc)
 - [doc/doxygen/options.doc](#docdoxygenoptionsdoc)

### CMakeLists.txt

```

{% raw %}
137 | ### Set the library providing dlopen
{% endraw %}

```
### src/simgrid/sg_config.cpp

```

{% raw %}
516 |                             "How we should privatize global variable at runtime (no, yes, mmap, dlopen).");
{% endraw %}

```
### src/smpi/smpi_global.cpp

```

{% raw %}
450 |     else if (std::strcmp(smpi_privatize_option, "dlopen") == 0)
451 |       smpi_privatize_global_variables = SMPI_PRIVATIZE_DLOPEN;
464 |       XBT_INFO("Mixing mmap privatization is broken on FreeBSD, switching to dlopen privatization instead.");
465 |       smpi_privatize_global_variables = SMPI_PRIVATIZE_DLOPEN;
556 |   if (smpi_privatize_global_variables == SMPI_PRIVATIZE_DLOPEN) {
608 |         void* handle = dlopen(target_executable.c_str(), RTLD_LAZY | RTLD_LOCAL | RTLD_DEEPBIND);
612 |           xbt_die("dlopen failed: %s (errno: %d -- %s)", dlerror(), errno, strerror(errno));
625 |     void* handle = dlopen(executable, RTLD_LAZY | RTLD_LOCAL | RTLD_DEEPBIND);
627 |       xbt_die("dlopen failed for %s: %s (errno: %d -- %s)", executable, dlerror(), errno, strerror(errno));
{% endraw %}

```
### src/simix/smx_context.cpp

```

{% raw %}
110 |       strcmp(xbt_cfg_get_string("smpi/privatization"), "dlopen") == 0) {
111 |     XBT_WARN("dlopen+thread broken on Apple and BSD. Switching to raw contexts.");
117 |     XBT_WARN("mmap broken on FreeBSD, but dlopen+thread broken too. Switching to dlopen+raw contexts.");
{% endraw %}

```
### teshsuite/smpi/CMakeLists.txt

```

{% raw %}
37 |                                     ${CMAKE_CURRENT_SOURCE_DIR}/privatization/privatization_dlopen.tesh                             PARENT_SCOPE)
125 |     ADD_TESH_FACTORIES(tesh-smpi-privatization-dlopen  "thread;ucontext;raw;boost"   --setenv bindir=${CMAKE_BINARY_DIR}/teshsuite/smpi/privatization --cd ${CMAKE_HOME_DIRECTORY}/teshsuite/smpi/privatization privatization_dlopen.tesh)
{% endraw %}

```
### teshsuite/smpi/mpich3-test/coll/CMakeLists.txt

```

{% raw %}
233 |   # Test MPICH selector: dlopen privatization and PTHREAD if exists (without priv and with raw if not)
235 |     ADD_TEST(test-smpi-mpich3-coll-mpich-thread-dlopen ${CMAKE_COMMAND} -E chdir ${CMAKE_BINARY_DIR}/teshsuite/smpi/mpich3-test/coll ${PERL_EXECUTABLE} ${CMAKE_HOME_DIRECTORY}/teshsuite/smpi/mpich3-test/runtests ${TESH_OPTION} -mpiexec=${CMAKE_BINARY_DIR}/smpi_script/bin/smpirun -srcdir=${CMAKE_HOME_DIRECTORY}/teshsuite/smpi/mpich3-test/coll -tests=testlist -execarg=--cfg=contexts/factory:thread -execarg=--cfg=smpi/coll_selector:mpich -execarg=--cfg=smpi/privatization:dlopen)
236 |     SET_TESTS_PROPERTIES(test-smpi-mpich3-coll-mpich-thread-dlopen PROPERTIES PASS_REGULAR_EXPRESSION "tests passed!")
244 |   # Test MVAPICH2 selector: dlopen privatization and UCONTEXT if exists (without priv and with raw if not)
246 |     ADD_TEST(test-smpi-mpich3-coll-mvapich2-ucontext-dlopen ${CMAKE_COMMAND} -E chdir ${CMAKE_BINARY_DIR}/teshsuite/smpi/mpich3-test/coll ${PERL_EXECUTABLE} ${CMAKE_HOME_DIRECTORY}/teshsuite/smpi/mpich3-test/runtests ${TESH_OPTION} -mpiexec=${CMAKE_BINARY_DIR}/smpi_script/bin/smpirun -srcdir=${CMAKE_HOME_DIRECTORY}/teshsuite/smpi/mpich3-test/coll -tests=testlist -execarg=--cfg=contexts/factory:ucontext -execarg=--cfg=smpi/coll_selector:mvapich2 -execarg=--cfg=smpi/privatization:dlopen)
247 |     SET_TESTS_PROPERTIES(test-smpi-mpich3-coll-mvapich2-ucontext-dlopen PROPERTIES PASS_REGULAR_EXPRESSION "tests passed!")
255 |   # Test IMPI selector: always raw, with dlopen if priv exists
258 |       ADD_TEST(test-smpi-mpich3-coll-impi-raw-dlopen ${CMAKE_COMMAND} -E chdir ${CMAKE_BINARY_DIR}/teshsuite/smpi/mpich3-test/coll ${PERL_EXECUTABLE} ${CMAKE_HOME_DIRECTORY}/teshsuite/smpi/mpich3-test/runtests ${TESH_OPTION} -mpiexec=${CMAKE_BINARY_DIR}/smpi_script/bin/smpirun -srcdir=${CMAKE_HOME_DIRECTORY}/teshsuite/smpi/mpich3-test/coll -tests=testlist -execarg=--cfg=contexts/factory:raw -execarg=--cfg=smpi/coll_selector:impi -execarg=--cfg=smpi/privatization:dlopen)
259 |       SET_TESTS_PROPERTIES(test-smpi-mpich3-coll-impi-raw-dlopen  PROPERTIES PASS_REGULAR_EXPRESSION "tests passed!")
{% endraw %}

```
### teshsuite/smpi/privatization/privatization_dlopen.tesh

```

{% raw %}
0 | p Test privatization with dlopen
3 | $ ${bindir:=.}/../../../smpi_script/bin/smpirun -hostfile ../hostfile -platform ../../../examples/platforms/small_platform.xml -np 32 ${bindir:=.}/privatization --log=smpi_kernel.thres:warning --log=xbt_cfg.thres:warning --cfg=smpi/privatization:dlopen --log=simix_context.thres:error
{% endraw %}

```
### tools/simgrid.supp

```

{% raw %}
20 |    Memory leak in libc/dlopen with -pthread
27 |    fun:do_dlopen
30 |    fun:__libc_dlopen_mode
43 | #There seems to be an issue with libc using an uninitialized value somewhere in dlopen
74 | #SMPI leaks the dlopen handle used for loading the program
76 |    dlopen handle leaks (1/2)
81 |    fun:dlopen@@GLIBC_*
87 |    dlopen handle leaks (2/2)
92 |    fun:dlopen@@GLIBC_*
{% endraw %}

```
### doc/doxygen/FAQ.doc

```

{% raw %}
563 | ==8414==    by 0x415102D: __libc_dlopen_mode (in /lib/tls/i686/cmov/libc-2.3.6.so)
584 |    fun:do_dlopen
586 |    fun:__libc_dlopen_mode
{% endraw %}

```
### doc/doxygen/options.doc

```

{% raw %}
960 | executions using the dlopen privatization schema, as missing binary
1031 |   - <b>dlopen</b>: Link multiple times against the binary.\n  
{% endraw %}

```