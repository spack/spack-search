---
name: "dmtcp"
layout: package
next_package: claw
previous_package: libxtst
languages: ['cpp', 'python']
---
## 2.5.2
23 / 648 files match

 - [src/nosyscallsreal.c](#srcnosyscallsrealc)
 - [src/syscallsreal.c](#srcsyscallsrealc)
 - [src/syscallwrappers.h](#srcsyscallwrappersh)
 - [src/dmtcp_dlsym.cpp](#srcdmtcp_dlsymcpp)
 - [src/threadsync.cpp](#srcthreadsynccpp)
 - [src/util_exec.cpp](#srcutil_execcpp)
 - [src/plugin/ipc/file/filewrappers.h](#srcpluginipcfilefilewrappersh)
 - [src/plugin/dl/dlwrappers.cpp](#srcplugindldlwrapperscpp)
 - [include/trampolines.h](#includetrampolinesh)
 - [plugin/batch-queue/rm_torque.cpp](#pluginbatch-queuerm_torquecpp)
 - [plugin/batch-queue/rm_utils.cpp](#pluginbatch-queuerm_utilscpp)
 - [plugin/batch-queue/rm_pmi.cpp](#pluginbatch-queuerm_pmicpp)
 - [plugin/batch-queue/rm_main.h](#pluginbatch-queuerm_mainh)
 - [plugin/batch-queue/pmi-drafts/hijack.cpp](#pluginbatch-queuepmi-draftshijackcpp)
 - [test/dlopen2.cpp](#testdlopen2cpp)
 - [test/dlopen1.c](#testdlopen1c)
 - [test/autotest.py](#testautotestpy)
 - [test/Makefile.in](#testmakefilein)
 - [test/plugin/sleep2/sleep2.c](#testpluginsleep2sleep2c)
 - [contrib/infiniband/infinibandwrappers.c](#contribinfinibandinfinibandwrappersc)
 - [doc/dmtcp_dlsym.txt](#docdmtcp_dlsymtxt)
 - [doc/src/plugin-tutorial.tex](#docsrcplugin-tutorialtex)
 - [doc/src/architecture-of-dmtcp.tex](#docsrcarchitecture-of-dmtcptex)

### src/nosyscallsreal.c

```cpp

{% raw %}
33 | // We should not need dlopen/dlsym
139 | /// call the libc version of this function via dlopen/dlsym
145 | /// call the libc version of this function via dlopen/dlsym
151 | /// call the libc version of this function via dlopen/dlsym
157 | /// call the libc version of this function via dlopen/dlsym
163 | /// call the libc version of this function via dlopen/dlsym
169 | /// call the libc version of this function via dlopen/dlsym
{% endraw %}

```
### src/syscallsreal.c

```cpp

{% raw %}
93 |  * 1. dlopen/dlsym: Once upon a time :-), DMTCP used to dlopen "libc.so" and
98 |  * malloc/calloc/free, etc. The reason was the fact that dlopen/dlsym/dlerror
99 |  * internally call calloc to allocate a small buffer. As can be seen, dlopen
101 |  * needs to call dlopen() to find the address of libc calloc and so this goes
105 |  *     wrappers, DMTCP was modified to not use dlopen/dlsym. Instead, a new
140 |  * a) As with scheme 1 (dlopen/dlsym) -- if there are wrappers around
192 |  * libpthread wrappers, we explicitly call dlopen() on libpthread.so. Then we
196 |  * these functions, then using dlopen()/dlsym() explicitly on libpthread will
220 | #if TRACK_DLOPEN_DLSYM_FOR_LOCKS
221 | LIB_PRIVATE void dmtcp_setThreadPerformingDlopenDlsym();
222 | LIB_PRIVATE void dmtcp_unsetThreadPerformingDlopenDlsym();
257 |  * dlopen()/dlsym()) we are are overriding any user wrappers for these
334 | #if TRACK_DLOPEN_DLSYM_FOR_LOCKS
339 |   dmtcp_setThreadPerformingDlopenDlsym();
342 | #if TRACK_DLOPEN_DLSYM_FOR_LOCKS
343 |   dmtcp_unsetThreadPerformingDlopenDlsym();
367 | void *_real_dlopen(const char *filename, int flag) {
368 |   REAL_FUNC_PASSTHROUGH_TYPED (void*, dlopen) (filename, flag);
{% endraw %}

```
### src/syscallwrappers.h

```cpp

{% raw %}
107 | LIB_PRIVATE extern __thread int thread_performing_dlopen_dlsym;
121 |   MACRO(dlopen)                             \
411 |   void *_real_dlopen(const char *filename, int flag);
{% endraw %}

```
### src/dmtcp_dlsym.cpp

```

{% raw %}
39 |  * (invoked by dlopen) tries first for a base version, and if not found,
227 |      * dlopen(), or from a call to dladdr(). In both the cases,
{% endraw %}

```
### src/threadsync.cpp

```

{% raw %}
87 | #if TRACK_DLOPEN_DLSYM_FOR_LOCKS
88 | static __thread bool _threadPerformingDlopenDlsym = false;
95 | /* The following two functions dmtcp_libdlLock{Lock,Unlock} are used by dlopen
116 | #if TRACK_DLOPEN_DLSYM_FOR_LOCKS
117 |   _threadPerformingDlopenDlsym = false;
191 | #if TRACK_DLOPEN_DLSYM_FOR_LOCKS
192 |   _threadPerformingDlopenDlsym = false;
260 | #if TRACK_DLOPEN_DLSYM_FOR_LOCKS
262 | void dmtcp_setThreadPerformingDlopenDlsym()
264 |   ThreadSync::setThreadPerformingDlopenDlsym();
268 | void dmtcp_unsetThreadPerformingDlopenDlsym()
270 |   ThreadSync::unsetThreadPerformingDlopenDlsym();
273 | bool ThreadSync::isThreadPerformingDlopenDlsym()
275 |   return _threadPerformingDlopenDlsym;
278 | void ThreadSync::setThreadPerformingDlopenDlsym()
280 |   _threadPerformingDlopenDlsym = true;
283 | void ThreadSync::unsetThreadPerformingDlopenDlsym()
285 |   _threadPerformingDlopenDlsym = false;
383 | #if TRACK_DLOPEN_DLSYM_FOR_LOCKS
384 |         isThreadPerformingDlopenDlsym() == false &&
{% endraw %}

```
### src/util_exec.cpp

```

{% raw %}
380 |    * adding dlsym_offset to the address of dlopen after the exec into the user
404 |   handle = dlopen(LIBDL_FILENAME, RTLD_NOW);
411 |    * use dlopen/dlsym.
{% endraw %}

```
### src/plugin/ipc/file/filewrappers.h

```cpp

{% raw %}
76 | //   NEXT_FNC_DEFAULT.  But that interferes with libdl.so (e.g., dlopen).
{% endraw %}

```
### src/plugin/dl/dlwrappers.cpp

```

{% raw %}
26 | #define _real_dlopen  NEXT_FNC(dlopen)
32 | /* Reason for using thread_performing_dlopen_dlsym:
34 |  * dlsym/dlopen/dlclose make a call to calloc() internally. We do not want to
35 |  * checkpoint while we are in the midst of dlopen etc. as it can lead to
41 |  * scenario, dlopen calls calloc, which then calls
44 |  * We set this variable to true, once we are inside the dlopen/dlsym/dlerror
52 |  *   When loading a shared library, dlopen will initialize the static objects
56 |  *   exclusive mode (writer lock). However, if dlopen wrapper acquires the
60 |  * EDIT: The dlopen() wrappers causes the problems with the semantics of RPATH
62 |  * plugin by detecting if we are in the middle of a dlopen by looking up the
67 | void *dlopen(const char *filename, int flag)
70 |   void *ret = _real_dlopen(filename, flag);
75 |     .Text("dlopen failed.  You may also see a message 'ERROR: ld.so:'\n"
{% endraw %}

```
### include/trampolines.h

```cpp

{% raw %}
112 |   void *handle = dlopen(LIBC_FILENAME, RTLD_NOW);
114 |     fprintf(stderr, "*** %s:%d DMTCP Internal Error: dlopen() failed.\n",
{% endraw %}

```
### plugin/batch-queue/rm_torque.cpp

```

{% raw %}
453 |     JTRACE("Initialize libtorque dlopen handler")(libpath);
455 |     _libtorque_handle = _real_dlopen(libpath.c_str(),RTLD_LAZY);
{% endraw %}

```
### plugin/batch-queue/rm_utils.cpp

```

{% raw %}
89 |     void *handle = _real_dlopen(libpath.c_str(),RTLD_LAZY);
{% endraw %}

```
### plugin/batch-queue/rm_pmi.cpp

```

{% raw %}
102 |       handle = _real_dlopen(libpath.c_str(),RTLD_LAZY);
140 | // Intel MPI uses dlopen() and dlsym() to find pmi functions.
{% endraw %}

```
### plugin/batch-queue/rm_main.h

```cpp

{% raw %}
37 | #define _real_dlopen NEXT_FNC(dlopen)
{% endraw %}

```
### plugin/batch-queue/pmi-drafts/hijack.cpp

```

{% raw %}
14 | 	handle = dlopen("/user/artempol/OpenMPI/pmi_support/lib/libpmi.so",RTLD_NOW);
{% endraw %}

```
### test/dlopen2.cpp

```

{% raw %}
0 | /* To compile, use -DLIB3 to create libdlopen-lib3.so, -DLIB4 for
1 |  * libdlopen-lib4.so, and define neither to create executable.
2 |  * To run, do:  LD_LIBRARY_PATH=. ./dlopen2
29 |       handle = dlopen("libdlopen-lib3.so", RTLD_NOW);
31 |         fprintf(stderr, "dlopen failed: %s\n", dlerror());
34 |       /* See 'man dlopen' for example:  POSIX.1-2002 prefers this workaround */
39 |       handle = dlopen("libdlopen-lib4.so", RTLD_LAZY);
41 |         fprintf(stderr, "dlopen failed: %s\n", dlerror());
44 |       /* See 'man dlopen' for example:  POSIX.1-2002 prefers this workaround */
{% endraw %}

```
### test/dlopen1.c

```cpp

{% raw %}
0 | /* To compile, use -DLIB1 to create libdlopen-lib1.so, -DLIB2 for
1 |  *   libdlopen-lib2.so, and define neither to create executable.
2 |  * To run, do:  LD_LIBRARY_PATH=. ./dlopen1
27 |       handle = dlopen("libdlopen-lib1.so", RTLD_NOW);
29 |         fprintf(stderr, "dlopen failed: %s\n", dlerror());
32 |       /* See 'man dlopen' for example:  POSIX.1-2002 prefers this workaround */
37 |       handle = dlopen("libdlopen-lib2.so", RTLD_LAZY);
39 |         fprintf(stderr, "dlopen failed: %s\n", dlerror());
42 |       /* See 'man dlopen' for example:  POSIX.1-2002 prefers this workaround */
{% endraw %}

```
### test/autotest.py

```python

{% raw %}
899 | runTest("dlopen1",        1, ["./test/dlopen1"])
900 | # Disable the dlopen2 test until we can figure out a way to handle calls to
901 | # fork/exec/wait during library intialization with dlopen().
904 | #  runTest("dlopen2",        1, ["./test/dlopen2"])
{% endraw %}

```
### test/Makefile.in

```

{% raw %}
197 | # dlopen1 will dlopen/dlclose libdlopen-lib[12].so
198 | libdlopen-lib1.so: dlopen1.c
200 | libdlopen-lib2.so: dlopen1.c
202 | dlopen1: dlopen1.c libdlopen-lib1.so libdlopen-lib2.so
205 | # dlopen2 will dlopen/dlclose libdlopen-lib[34].so
206 | libdlopen-lib3.so: dlopen2.cpp
208 | libdlopen-lib4.so: dlopen2.cpp
210 | dlopen2: dlopen2.cpp libdlopen-lib3.so libdlopen-lib4.so
{% endraw %}

```
### test/plugin/sleep2/sleep2.c

```cpp

{% raw %}
24 |     handle = dlopen("libc.so.6", RTLD_NOW);
{% endraw %}

```
### contrib/infiniband/infinibandwrappers.c

```cpp

{% raw %}
14 | void *dlopen(const char *filename, int flag) {
17 |       void *handle = NEXT_FNC(dlopen)("libdmtcp_infiniband.so", flag);
28 |   return NEXT_FNC(dlopen)(filename, flag);
{% endraw %}

```
### doc/dmtcp_dlsym.txt

```

{% raw %}
10 | by using the pseudo-handle, RTLD_NEXT.  See 'man 3 dlopen' for details.
13 |     void *handle = dlopen(RTLD_NEXT, RTLD_LAZY);
103 | In calls to dlopen, the "dynamic linker" is called.  If the dynamic linker
{% endraw %}

```
### doc/src/plugin-tutorial.tex

```

{% raw %}
8 | % TODO:  test suite from Joshua Louie (dlopen prior to main; epoll taking too long)
{% endraw %}

```
### doc/src/architecture-of-dmtcp.tex

```

{% raw %}
333 | are typically created using dlopen/dlsym.  For example, to define
{% endraw %}

```