---
name: "intel-pin"
layout: package
next_package: mongo-c-driver
previous_package: singularity-legacy
languages: ['html', 'cpp']
---
## 3.14
36 / 4391 files match

 - [source/tools/AttachDetach/secondary_attach_app.cpp](#sourcetoolsattachdetachsecondary_attach_appcpp)
 - [source/tools/AttachDetach/reattach_probed_app.cpp](#sourcetoolsattachdetachreattach_probed_appcpp)
 - [source/tools/AttachDetach/attachReattachThreadDetachCallbacks_app.cpp](#sourcetoolsattachdetachattachreattachthreaddetachcallbacks_appcpp)
 - [source/tools/AttachDetach/detach_probed_app.cpp](#sourcetoolsattachdetachdetach_probed_appcpp)
 - [source/tools/AttachDetach/main_attach_app.cpp](#sourcetoolsattachdetachmain_attach_appcpp)
 - [source/tools/AttachDetach/reattach_jit_app.cpp](#sourcetoolsattachdetachreattach_jit_appcpp)
 - [source/tools/AttachDetach/launchReattachThreadDetachCallbacks_app.cpp](#sourcetoolsattachdetachlaunchreattachthreaddetachcallbacks_appcpp)
 - [source/tools/MemTranslate/malloc_translation_app.c](#sourcetoolsmemtranslatemalloc_translation_appc)
 - [source/tools/Replay/ia32_cross_os_replay.reference](#sourcetoolsreplayia32_cross_os_replayreference)
 - [source/tools/Replay/ia32_cross_os_replay.record](#sourcetoolsreplayia32_cross_os_replayrecord)
 - [source/tools/Debugger/makefile.rules](#sourcetoolsdebuggermakefilerules)
 - [source/tools/Debugger/dlopen-dlclose.c](#sourcetoolsdebuggerdlopen-dlclosec)
 - [source/tools/ToolUnitTests/dltest.c](#sourcetoolstoolunittestsdltestc)
 - [source/tools/ToolUnitTests/dltest2.c](#sourcetoolstoolunittestsdltest2c)
 - [source/tools/ToolUnitTests/main_dll.cpp](#sourcetoolstoolunittestsmain_dllcpp)
 - [source/tools/ToolUnitTests/security_w_pin_dll_load.cpp](#sourcetoolstoolunittestssecurity_w_pin_dll_loadcpp)
 - [source/tools/ToolUnitTests/dlclose_app.cpp](#sourcetoolstoolunittestsdlclose_appcpp)
 - [source/tools/Probes/tpss_lin_libc_tool.cpp](#sourcetoolsprobestpss_lin_libc_toolcpp)
 - [source/tools/Probes/dltest_unix.c](#sourcetoolsprobesdltest_unixc)
 - [source/tools/Probes/malloctrace2.cpp](#sourcetoolsprobesmalloctrace2cpp)
 - [source/tools/Probes/tpss_lin_libc.c](#sourcetoolsprobestpss_lin_libcc)
 - [source/tools/Probes/tpss_lin_libdl.cpp](#sourcetoolsprobestpss_lin_libdlcpp)
 - [source/tools/Probes/unloadtest_unix.c](#sourcetoolsprobesunloadtest_unixc)
 - [source/tools/Tests/sourceLocation_app.cpp](#sourcetoolstestssourcelocation_appcpp)
 - [source/tools/ImageTests/l_imageLoad_app.cpp](#sourcetoolsimagetestsl_imageload_appcpp)
 - [source/tools/ImageTests/imageUnload_app.c](#sourcetoolsimagetestsimageunload_appc)
 - [source/tools/ImageTests/full_path_app.cpp](#sourcetoolsimagetestsfull_path_appcpp)
 - [source/tools/ImageTests/split_image_linux_app.cpp](#sourcetoolsimagetestssplit_image_linux_appcpp)
 - [source/tools/ImageTests/launchReattachImageLoadCallbacks_app.cpp](#sourcetoolsimagetestslaunchreattachimageloadcallbacks_appcpp)
 - [source/tools/ImageTests/attachReattachImageLoadCallbacks_app.cpp](#sourcetoolsimagetestsattachreattachimageloadcallbacks_appcpp)
 - [source/tools/ImageTests/images_on_attach_app.cpp](#sourcetoolsimagetestsimages_on_attach_appcpp)
 - [extras/crt/include/dlfcn.h](#extrascrtincludedlfcnh)
 - [extras/crt/include/nsswitch.h](#extrascrtincludensswitchh)
 - [extras/crt/include/android/dlext.h](#extrascrtincludeandroiddlexth)
 - [extras/crt/include/freebsd/3rd-party/sys/sys/elf_common.h](#extrascrtincludefreebsd3rd-partysyssyself_commonh)
 - [doc/html/group__KNOBS.html](#dochtmlgroup__knobshtml)

### source/tools/AttachDetach/secondary_attach_app.cpp

```

{% raw %}
47 |     void *handle = dlopen(imageToLoad, RTLD_LAZY); 
{% endraw %}

```
### source/tools/AttachDetach/reattach_probed_app.cpp

```

{% raw %}
61 | void * thread_dlopen_func (void *arg)
67 |         void *handle = dlopen("libmy_dll" DLL_SUFFIX, RTLD_LAZY);
96 |         pthread_create (&h[0], 0, thread_dlopen_func, 0);
{% endraw %}

```
### source/tools/AttachDetach/attachReattachThreadDetachCallbacks_app.cpp

```

{% raw %}
117 |         void *handle = dlopen(argv[argc-2], RTLD_LAZY); // argv[argc-2] is First imageName
128 |         handle = dlopen(argv[argc-1], RTLD_LAZY);   // argv[argc-1] is Second imageName
{% endraw %}

```
### source/tools/AttachDetach/detach_probed_app.cpp

```

{% raw %}
53 | void * thread_dlopen_func (void *arg)
58 |         void *handle = dlopen("libm" DLL_SUFFIX, RTLD_LAZY);
81 |     pthread_create (&h[0], 0, thread_dlopen_func, 0);
{% endraw %}

```
### source/tools/AttachDetach/main_attach_app.cpp

```

{% raw %}
105 |         void *handle = dlopen(imageToLoad, RTLD_LAZY);
{% endraw %}

```
### source/tools/AttachDetach/reattach_jit_app.cpp

```

{% raw %}
53 | void * thread_dlopen_func (void *arg)
59 |         void *handle = dlopen("libmy_dll.so", RTLD_LAZY);
90 |         pthread_create (&h[0], 0, thread_dlopen_func, 0);
{% endraw %}

```
### source/tools/AttachDetach/launchReattachThreadDetachCallbacks_app.cpp

```

{% raw %}
79 | 	void *handle = dlopen(argv[1], RTLD_LAZY);
92 |     handle = dlopen(argv[2], RTLD_LAZY);
{% endraw %}

```
### source/tools/MemTranslate/malloc_translation_app.c

```cpp

{% raw %}
141 |     void *handle = dlopen(file, RTLD_NOW | RTLD_LOCAL);
{% endraw %}

```
### source/tools/Replay/ia32_cross_os_replay.reference

```

{% raw %}
626 | Function '__libc_dlopen_mode' loaded at 56f57510
{% endraw %}

```
### source/tools/Replay/ia32_cross_os_replay.record

```

{% raw %}
616 | 	'__libc_dlopen_mode' 56f57510
{% endraw %}

```
### source/tools/Debugger/makefile.rules

```

{% raw %}
87 |                  dlopen-dlclose
201 |         APP_ROOTS := $(filter-out dlopen-dlclose, $(APP_ROOTS))
1829 | gdb-svr4-libraries-extension.test: $(OBJDIR)dlopen-dlclose$(EXE_SUFFIX) $(OBJDIR)library-load-tool$(PINTOOL_SUFFIX)
1831 | 	    $(OBJDIR)dlopen-dlclose$(EXE_SUFFIX) `$(CXX) $(COMP_OBJ) /dev/null -print-file-name=libm.so` > $(OBJDIR)$(@:.test=.out) &
1838 | 	$(DBG) $(DBG_CMD_SRC_FLAG) $(OBJDIR)$(@:.test=.$(DBG_STR)in) $(DBG_CMD_MORE_FLAGS) $(OBJDIR)dlopen-dlclose$(EXE_SUFFIX) \
{% endraw %}

```
### source/tools/Debugger/dlopen-dlclose.c

```cpp

{% raw %}
41 |     void *handle = dlopen(file, RTLD_NOW | RTLD_LOCAL);
{% endraw %}

```
### source/tools/ToolUnitTests/dltest.c

```cpp

{% raw %}
32 |     handle = dlopen(name, RTLD_LAZY);
{% endraw %}

```
### source/tools/ToolUnitTests/dltest2.c

```cpp

{% raw %}
34 |     handle = dlopen(name, RTLD_LAZY);
{% endraw %}

```
### source/tools/ToolUnitTests/main_dll.cpp

```

{% raw %}
139 |     VOID * module = dlopen("dynamic_secondary_dll.dll", RTLD_NOW);
{% endraw %}

```
### source/tools/ToolUnitTests/security_w_pin_dll_load.cpp

```

{% raw %}
35 |     void * dllHandle = dlopen("dynamic_secondary_dll.dll", RTLD_NOW);
{% endraw %}

```
### source/tools/ToolUnitTests/dlclose_app.cpp

```

{% raw %}
27 |     handle = dlopen(name, RTLD_LAZY);
{% endraw %}

```
### source/tools/Probes/tpss_lin_libc_tool.cpp

```

{% raw %}
175 | extern AFUNPTR fptr__libc_dlopen_mode;
309 | void my__libc_dlopen_mode();
1521 |         RTN rtn__libc_dlopen_mode = RTN_FindByName(img, "__libc_dlopen_mode");
1522 |         if (RTN_Valid(rtn__libc_dlopen_mode) && RTN_IsSafeForProbedReplacement(rtn__libc_dlopen_mode))
1524 |             OutFile << CurrentTime() << "Inserting probe for __libc_dlopen_mode at " << RTN_Address(rtn__libc_dlopen_mode) << endl;
1526 |             AFUNPTR fptr = (RTN_ReplaceProbed(rtn__libc_dlopen_mode, AFUNPTR(my__libc_dlopen_mode)));
1527 |             fptr__libc_dlopen_mode = fptr;
{% endraw %}

```
### source/tools/Probes/dltest_unix.c

```cpp

{% raw %}
25 |     handle = dlopen(name, RTLD_LAZY);
{% endraw %}

```
### source/tools/Probes/malloctrace2.cpp

```

{% raw %}
15 |  In this example I call dlopen before main().
57 | typedef typeof(dlopen) * DlopenType;
68 | DlopenType AppDlopen = 0;
103 | /* I'm calling dlopen before main.
105 |  * But the earliest point you can call dlopen is after init of libc
110 |     // inject libmallocwrappers.so into application by executing application dlopen
112 |     MallocTraceHandle = AppDlopen(SHARED_LIB("libmallocwrappers"), RTLD_LAZY);
130 |         // Get the function pointer for the application dlopen:
131 |         // dlopen@@GLIBC_2.1 is the official, versioned name.
144 | # define DLOPEN_VERSION "GLIBC_2.2.5"
147 | # define DLOPEN_VERSION "GLIBC_2.1"
153 |         RTN dlopenRtn = RTN_FindByName(img, "dlopen@@" DLOPEN_VERSION);
154 |         if (!RTN_Valid(dlopenRtn))
156 |             dlopenRtn = RTN_FindByName(img, "dlopen@" DLOPEN_VERSION);
159 |         if (!RTN_Valid(dlopenRtn))
162 |             dlopenRtn = RTN_FindByName(img, "dlopen");
165 |         ASSERTX(RTN_Valid(dlopenRtn));
166 |         AppDlopen = DlopenType(RTN_Funptr(dlopenRtn));
185 |         RTN dlopenRtn = RTN_FindByName(img, C_MANGLE("dlopen") );
190 |         // In some systems, dlsym and dlopen symbols don't exist.
192 |         if (!RTN_Valid(dlsymRtn) && !RTN_Valid(dlopenRtn))
194 |             cerr << "Error: dlsym and dlopen not found" << endl;
198 |         AppDlopen = DlopenType(RTN_Funptr(dlopenRtn));
230 |     catch init() of libc and call dlopen after init() is done
{% endraw %}

```
### source/tools/Probes/tpss_lin_libc.c

```cpp

{% raw %}
335 | VOID_PTR (*fptr__libc_dlopen_mode)(const CHAR_PTR __name, int __mode);
1389 | VOID_PTR  my__libc_dlopen_mode(const CHAR_PTR __name, int __mode) 
1391 |     printFunctionCalled("my__libc_dlopen_mode");
1392 |     VOID_PTR  res = fptr__libc_dlopen_mode(__name, __mode);
{% endraw %}

```
### source/tools/Probes/tpss_lin_libdl.cpp

```

{% raw %}
69 | VOID_PTR (*fptrdlopen)(__const CHAR_PTR __file, int  __mode);
87 | VOID_PTR mydlopen(__const CHAR_PTR __file, int __mode)
89 |    OutFile << CurrentTime() << "mydlopen called " << endl;
91 |    VOID_PTR res = fptrdlopen(__file, __mode);
172 |         RTN rtndlopen = RTN_FindByName(img, "dlopen");
173 |         if (RTN_Valid(rtndlopen) && RTN_IsSafeForProbedReplacement(rtndlopen))
175 |             OutFile << CurrentTime() << "Inserting probe for dlopen at " << RTN_Address(rtndlopen) << endl;
177 |             AFUNPTR fptr = (RTN_ReplaceProbed(rtndlopen, AFUNPTR(mydlopen)));
178 |             fptrdlopen = (VOID_PTR (*)(__const CHAR_PTR , int ))fptr;
{% endraw %}

```
### source/tools/Probes/unloadtest_unix.c

```cpp

{% raw %}
25 |     handle = dlopen(name, RTLD_LAZY);
{% endraw %}

```
### source/tools/Tests/sourceLocation_app.cpp

```

{% raw %}
32 | void* DLopen(const char* filename) {
33 |     void* handle = dlopen(filename, RTLD_LAZY);
70 |     void* handle1 = DLopen(argv[1]);            // open image1
71 |     void* handle2 = DLopen(argv[2]);            // open image2
{% endraw %}

```
### source/tools/ImageTests/l_imageLoad_app.cpp

```

{% raw %}
36 |     void* dlh = dlopen(filename, RTLD_LAZY);
{% endraw %}

```
### source/tools/ImageTests/imageUnload_app.c

```cpp

{% raw %}
18 |     void* dlh = dlopen(filename, RTLD_LAZY);
{% endraw %}

```
### source/tools/ImageTests/full_path_app.cpp

```

{% raw %}
35 |     handle = dlopen(argv[1], RTLD_LAZY);
{% endraw %}

```
### source/tools/ImageTests/split_image_linux_app.cpp

```

{% raw %}
75 |     void* hDll = dlopen(argv[1], RTLD_LAZY | RTLD_GLOBAL);
{% endraw %}

```
### source/tools/ImageTests/launchReattachImageLoadCallbacks_app.cpp

```

{% raw %}
35 |     void *handle = dlopen(argv[1], RTLD_LAZY);
48 |     handle = dlopen(argv[2], RTLD_LAZY);
{% endraw %}

```
### source/tools/ImageTests/attachReattachImageLoadCallbacks_app.cpp

```

{% raw %}
115 |         void *handle = dlopen(argv[1], RTLD_LAZY);
128 |         handle = dlopen(argv[2], RTLD_LAZY);
{% endraw %}

```
### source/tools/ImageTests/images_on_attach_app.cpp

```

{% raw %}
56 |     const void *libutil = dlopen("libutil.so.1", RTLD_LAZY);
62 |     const void *usrlibptr = dlopen(usrlib, RTLD_LAZY);
{% endraw %}

```
### extras/crt/include/dlfcn.h

```cpp

{% raw %}
60 | extern void*        dlopen(const char*  filename, int flag);
{% endraw %}

```
### extras/crt/include/nsswitch.h

```cpp

{% raw %}
203 | 	void		*handle;	/* handle from dlopen() */
{% endraw %}

```
### extras/crt/include/android/dlext.h

```cpp

{% raw %}
51 |   /* Instruct dlopen to use library_fd instead of opening file by name.
72 | extern void* android_dlopen_ext(const char* filename, int flag, const android_dlextinfo* extinfo);
{% endraw %}

```
### extras/crt/include/freebsd/3rd-party/sys/sys/elf_common.h

```cpp

{% raw %}
767 | #define	DF_1_NOOPEN     0x00000040	/* Do not allow loading on dlopen() */
{% endraw %}

```
### doc/html/group__KNOBS.html

```html

{% raw %}
99 |  <b>deepbind:</b> (Linux only) Load the tool with the RTLD_DEEPBIND flag to make it a self-contained library. For more information see the dlopen man pages.   </td></tr>
{% endraw %}

```