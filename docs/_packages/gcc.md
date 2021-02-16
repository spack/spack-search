---
name: "gcc"
layout: package
next_package: log4c
previous_package: re2c
languages: ['java', 'cpp', 'c']
---
## 6.1.0
112 / 94447 files match

 - [gcc/plugin.c](#gccpluginc)
 - [gcc/config/rs6000/aix.h](#gccconfigrs6000aixh)
 - [gcc/jit/jit-playback.h](#gccjitjit-playbackh)
 - [gcc/jit/jit-playback.c](#gccjitjit-playbackc)
 - [gcc/testsuite/c-c++-common/tsan/tsan_barrier.h](#gcctestsuitec-c++-commontsantsan_barrierh)
 - [gcc/testsuite/g++.dg/asan/dlclose-test-1-so.cc](#gcctestsuiteg++dgasandlclose-test-1-socc)
 - [gcc/testsuite/g++.dg/tsan/tsan_barrier.h](#gcctestsuiteg++dgtsantsan_barrierh)
 - [gcc/testsuite/jit.dg/verify-dynamic-library.c](#gcctestsuitejitdgverify-dynamic-libraryc)
 - [libjava/prims.cc](#libjavaprimscc)
 - [libjava/classpath/native/jni/midi-dssi/gnu_javax_sound_midi_dssi_DSSIMidiDeviceProvider.c](#libjavaclasspathnativejnimidi-dssignu_javax_sound_midi_dssi_dssimidideviceproviderc)
 - [libjava/classpath/include/gnu_javax_sound_midi_dssi_DSSIMidiDeviceProvider.h](#libjavaclasspathincludegnu_javax_sound_midi_dssi_dssimidideviceproviderh)
 - [libjava/classpath/tools/toolwrapper.c](#libjavaclasspathtoolstoolwrapperc)
 - [libjava/classpath/gnu/javax/sound/midi/dssi/DSSIMidiDeviceProvider.java](#libjavaclasspathgnujavaxsoundmididssidssimidideviceproviderjava)
 - [libjava/classpath/gnu/javax/sound/midi/dssi/DSSISynthesizer.java](#libjavaclasspathgnujavaxsoundmididssidssisynthesizerjava)
 - [libjava/libltdl/ltdl.h](#libjavalibltdlltdlh)
 - [libjava/libltdl/ltdl.c](#libjavalibltdlltdlc)
 - [libjava/java/lang/natRuntime.cc](#libjavajavalangnatruntimecc)
 - [libjava/java/net/natVMURLConnection.cc](#libjavajavanetnatvmurlconnectioncc)
 - [libjava/gnu/gcj/runtime/natSharedLibLoader.cc](#libjavagnugcjruntimenatsharedlibloadercc)
 - [libjava/gnu/javax/sound/midi/dssi/DSSIMidiDeviceProvider.h](#libjavagnujavaxsoundmididssidssimidideviceproviderh)
 - [libstdc++-v3/testsuite/ext/mt_allocator/22309_thread.cc](#libstdc++-v3testsuiteextmt_allocator22309_threadcc)
 - [libstdc++-v3/testsuite/18_support/bad_exception/23591_thread-1.c](#libstdc++-v3testsuite18_supportbad_exception23591_thread-1c)
 - [boehm-gc/threadlibs.c](#boehm-gcthreadlibsc)
 - [boehm-gc/dyn_load.c](#boehm-gcdyn_loadc)
 - [boehm-gc/gc_dlopen.c](#boehm-gcgc_dlopenc)
 - [boehm-gc/include/gc_pthread_redirects.h](#boehm-gcincludegc_pthread_redirectsh)
 - [intl/libgnuintl.h](#intllibgnuintlh)
 - [libvtv/vtv_utils.h](#libvtvvtv_utilsh)
 - [libvtv/testsuite/other-tests/dlopen.cc](#libvtvtestsuiteother-testsdlopencc)
 - [libvtv/testsuite/other-tests/dlopen_mt.cc](#libvtvtestsuiteother-testsdlopen_mtcc)
 - [libcilkrts/runtime/sysdep-unix.c](#libcilkrtsruntimesysdep-unixc)
 - [libsanitizer/sanitizer_common/sanitizer_linux.h](#libsanitizersanitizer_commonsanitizer_linuxh)
 - [libsanitizer/sanitizer_common/sanitizer_unwind_linux_libcdep.cc](#libsanitizersanitizer_commonsanitizer_unwind_linux_libcdepcc)
 - [libgcc/config/darwin-crt3.c](#libgccconfigdarwin-crt3c)
 - [lto-plugin/lto-symtab.c](#lto-pluginlto-symtabc)
 - [libgomp/target.c](#libgomptargetc)
 - [libgomp/plugin/plugin-hsa.c](#libgomppluginplugin-hsac)

### gcc/plugin.c

```c

{% raw %}
575 |      dlopen.  */
576 |   dl_handle = dlopen (plugin->full_name, RTLD_NOW | RTLD_GLOBAL);
{% endraw %}

```
### gcc/config/rs6000/aix.h

```c

{% raw %}
70 |    This handles the case where a library is loaded through dlopen(), and also
{% endraw %}

```
### gcc/jit/jit-playback.h

```c

{% raw %}
286 |   dlopen_built_dso ();
{% endraw %}

```
### gcc/jit/jit-playback.c

```c

{% raw %}
1730 |        and load it in memory (via dlopen), wrapping the result up as
1839 |     Convert the .s file to a .so DSO, and load it in memory (via dlopen),
1849 |   m_result = dlopen_built_dso ();
2537 | dlopen_built_dso ()
2548 |   handle = dlopen (m_tempdir->get_path_so_file (),
{% endraw %}

```
### gcc/testsuite/c-c++-common/tsan/tsan_barrier.h

```c

{% raw %}
9 |   void *h = dlopen ("libpthread.so.0", RTLD_LAZY);
{% endraw %}

```
### gcc/testsuite/g++.dg/asan/dlclose-test-1-so.cc

```cpp

{% raw %}
25 | void at_dlopen() {
26 |   printf("%s: I am being dlopened\n", __FILE__);
{% endraw %}

```
### gcc/testsuite/g++.dg/tsan/tsan_barrier.h

```c

{% raw %}
9 |   void *h = dlopen ("libpthread.so.0", RTLD_LAZY);
{% endraw %}

```
### gcc/testsuite/jit.dg/verify-dynamic-library.c

```c

{% raw %}
13 |   handle = dlopen ("./output-of-test-compile-to-dynamic-library.c.so",
17 |       fprintf (stderr, "dlopen failed: %s\n", dlerror());
{% endraw %}

```
### libjava/prims.cc

```cpp

{% raw %}
1400 |   lt_dlhandle lib = lt_dlopenext (name);
{% endraw %}

```
### libjava/classpath/native/jni/midi-dssi/gnu_javax_sound_midi_dssi_DSSIMidiDeviceProvider.c

```c

{% raw %}
52 | Java_gnu_javax_sound_midi_dssi_DSSIMidiDeviceProvider_dlopen_1 
64 |   handle = dlopen(filename, RTLD_NOW);
{% endraw %}

```
### libjava/classpath/include/gnu_javax_sound_midi_dssi_DSSIMidiDeviceProvider.h

```c

{% raw %}
12 | JNIEXPORT jlong JNICALL Java_gnu_javax_sound_midi_dssi_DSSIMidiDeviceProvider_dlopen_1 (JNIEnv *env, jclass, jstring);
{% endraw %}

```
### libjava/classpath/tools/toolwrapper.c

```c

{% raw %}
174 |   libjvm_handle = lt_dlopenext (LIBJVM);
{% endraw %}

```
### libjava/classpath/gnu/javax/sound/midi/dssi/DSSIMidiDeviceProvider.java

```java

{% raw %}
86 |   static native long dlopen_(String soname);
100 |      long sohandle = dlopen_(soname);
{% endraw %}

```
### libjava/classpath/gnu/javax/sound/midi/dssi/DSSISynthesizer.java

```java

{% raw %}
504 |     sohandle = DSSIMidiDeviceProvider.dlopen_(soname);
{% endraw %}

```
### libjava/libltdl/ltdl.h

```c

{% raw %}
170 | LT_SCOPE	lt_dlhandle lt_dlopen		LT_PARAMS((const char *filename));
171 | LT_SCOPE	lt_dlhandle lt_dlopenext	LT_PARAMS((const char *filename));
244 |   int	ref_count;		/* number of times lt_dlopened minus
314 |     LT_ERROR(DLOPEN_NOT_SUPPORTED,  "dlopen support not available")	\
{% endraw %}

```
### libjava/libltdl/ltdl.c

```c

{% raw %}
846 |   lt_dlloader	       *loader;		/* dlopening interface */
1113 |   lt_module   module   = dlopen (filename, LT_GLOBAL | LT_LAZY_OR_NOW);
2174 | static	int	try_dlopen	      LT_PARAMS((lt_dlhandle *handle,
2176 | static	int	tryall_dlopen	      LT_PARAMS((lt_dlhandle *handle,
2219 |       errors += lt_dlloader_add (lt_dlloader_next (0), &sys_dl, "dlopen");
2222 |       errors += lt_dlloader_add (lt_dlloader_next (0), &sys_shl, "dlopen");
2225 |       errors += lt_dlloader_add (lt_dlloader_next (0), &sys_wll, "dlopen");
2228 |       errors += lt_dlloader_add (lt_dlloader_next (0), &sys_bedl, "dlopen");
2364 | tryall_dlopen (handle, filename, useloader)
2467 | tryall_dlopen_module (handle, prefix, dirname, dlname)
2505 |       error += tryall_dlopen_module (handle,
2508 |   else if (tryall_dlopen (handle, filename, NULL) != 0)
2527 |      we want the preopened version of it, even if a dlopenable
2529 |   if (old_name && tryall_dlopen (handle, old_name, "dlpreload") == 0)
2540 | 	  if (tryall_dlopen_module (handle,
2548 | 	  if (tryall_dlopen_module (handle, dir, objdir, dlname) == 0)
2554 | 	  if (tryall_dlopen_module (handle,
2793 |   if (tryall_dlopen (handle, filename,NULL) != 0)
2955 | 	  handle->deplibs[j] = lt_dlopenext(names[depcount-1-i]);
3050 | try_dlopen (phandle, filename)
3081 |       if (tryall_dlopen (&newhandle, 0, NULL) != 0)
3387 |           if (tryall_dlopen (&newhandle, filename, NULL) != 0)
3426 | lt_dlopen (filename)
3433 |   if (try_dlopen (&handle, filename) != 0)
3458 | lt_dlopenext (filename)
3469 |       return lt_dlopen (filename);
3485 |       return lt_dlopen (filename);
3495 |   errors = try_dlopen (&handle, tmp);
3525 |   errors = try_dlopen (&handle, tmp);
3732 |    passing to lt_dlopenext.  The extensions are stripped so that
3735 |    then the same directories that lt_dlopen would search are examined.  */
{% endraw %}

```
### libjava/java/lang/natRuntime.cc

```cpp

{% raw %}
179 |     h = do_search ? lt_dlopenext (lib_name) : lt_dlopen (lib_name);
243 |   lt_dlhandle h = lt_dlopenext (buf);
258 |   lt_dlopen (NULL);
{% endraw %}

```
### libjava/java/net/natVMURLConnection.cc

```cpp

{% raw %}
34 |   lt_dlhandle handle = lt_dlopenext ("libmagic.so");
{% endraw %}

```
### libjava/gnu/gcj/runtime/natSharedLibLoader.cc

```cpp

{% raw %}
96 |   void *h = dlopen(lname, flags);
{% endraw %}

```
### libjava/gnu/javax/sound/midi/dssi/DSSIMidiDeviceProvider.h

```c

{% raw %}
47 |   static jlong dlopen_(::java::lang::String *);
{% endraw %}

```
### libstdc++-v3/testsuite/ext/mt_allocator/22309_thread.cc

```cpp

{% raw %}
26 | check_dlopen(void*& h)
29 |   void* tmp = dlopen("./testsuite_shared.so", RTLD_LAZY);
84 |   check_dlopen(h);
{% endraw %}

```
### libstdc++-v3/testsuite/18_support/bad_exception/23591_thread-1.c

```c

{% raw %}
33 |   lib = dlopen("./testsuite_shared.so", RTLD_NOW);
36 |       printf("dlopen failed: %s\n", strerror(errno));
{% endraw %}

```
### boehm-gc/threadlibs.c

```c

{% raw %}
7 | 	printf("-Wl,--wrap -Wl,dlopen "
{% endraw %}

```
### boehm-gc/dyn_load.c

```c

{% raw %}
40 |       && defined(dlopen) && !defined(GC_USE_LD_WRAP)
169 | 	  void* startupSyms = dlopen(0, RTLD_LAZY);
296 | 	--> fix mutual exclusion with dlopen
{% endraw %}

```
### boehm-gc/gc_dlopen.c

```c

{% raw %}
48 |   static void disable_gc_for_dlopen()
65 |   void * __wrap_dlopen(const char *path, int mode)
67 |   void * GC_dlopen(path, mode)
75 |       disable_gc_for_dlopen();
78 |       result = (void *)__real_dlopen(path, mode);
80 |       result = dlopen(path, mode);
83 |       GC_enable(); /* undoes disable_gc_for_dlopen */
{% endraw %}

```
### boehm-gc/include/gc_pthread_redirects.h

```c

{% raw %}
23 |   void * GC_dlopen(const char *path, int mode);
{% endraw %}

```
### intl/libgnuintl.h

```c

{% raw %}
75 |      4. in the dlopen()ed shared libraries, in the order in which they were
76 |         dlopen()ed.
{% endraw %}

```
### libvtv/vtv_utils.h

```c

{% raw %}
55 |    disturb the order of calls to dlopen.  Changing the order of dlopen
{% endraw %}

```
### libvtv/testsuite/other-tests/dlopen.cc

```cpp

{% raw %}
21 |   void * dlhandle = dlopen(so_name, RTLD_NOW);
24 |       fprintf(stderr, "dlopen %s error: %s\n", so_name, dlerror());
30 |       fprintf(stderr, "dlopen %s dlsym error: %s\n", so_name, dlerror());
{% endraw %}

```
### libvtv/testsuite/other-tests/dlopen_mt.cc

```cpp

{% raw %}
25 | void do_dlopen(int so_num)
30 |   void * dlhandle = dlopen(so_name, RTLD_NOW);
33 |       fprintf(stderr, "dlopen so:%s error: %s\n", so_name, dlerror());
53 | void * do_dlopens(void * ptid)
63 |           do_dlopen((NUM_SOS_PER_THREAD * *(int *)ptid) + i);
92 |     if (pthread_create(&thread_ids[t], NULL, do_dlopens, &thread_nids[t]) != 0)
{% endraw %}

```
### libcilkrts/runtime/sysdep-unix.c

```c

{% raw %}
794 |     void* handle = dlopen( get_runtime_path(), RTLD_GLOBAL|RTLD_LAZY );
{% endraw %}

```
### libsanitizer/sanitizer_common/sanitizer_linux.h

```c

{% raw %}
20 | struct link_map;  // Opaque type returned by dlopen().
{% endraw %}

```
### libsanitizer/sanitizer_common/sanitizer_unwind_linux_libcdep.cc

```cpp

{% raw %}
48 |   void *p = dlopen("libcorkscrew.so", RTLD_LAZY);
{% endraw %}

```
### libgcc/config/darwin-crt3.c

```c

{% raw %}
270 |       handle = dlopen ("/usr/lib/libSystem.B.dylib", RTLD_NOLOAD);
{% endraw %}

```
### lto-plugin/lto-symtab.c

```c

{% raw %}
139 |   plugin_handle = dlopen (name, RTLD_LAZY);
{% endraw %}

```
### libgomp/target.c

```c

{% raw %}
2352 |   void *plugin_handle = dlopen (plugin_name, RTLD_LAZY);
{% endraw %}

```
### libgomp/plugin/plugin-hsa.c

```c

{% raw %}
689 |   void *f = dlopen (file_name, RTLD_NOW);
{% endraw %}

```