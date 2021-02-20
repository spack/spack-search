---
name: "icedtea"
layout: package
next_package: igraph
previous_package: icarus
languages: ['c']
---
## 3.4.0
70 / 50289 files match, 34 filtered matches.

 - [jdk_src/src/solaris/bin/java_md_solinux.c](#jdk_srcsrcsolarisbinjava_md_solinuxc)
 - [jdk_src/src/solaris/native/sun/jdga/dgalock.c](#jdk_srcsrcsolarisnativesunjdgadgalockc)
 - [jdk_src/src/solaris/native/sun/nio/fs/MagicFileTypeDetector.c](#jdk_srcsrcsolarisnativesunniofsmagicfiletypedetectorc)
 - [jdk_src/src/solaris/native/sun/nio/fs/GnomeFileTypeDetector.c](#jdk_srcsrcsolarisnativesunniofsgnomefiletypedetectorc)
 - [jdk_src/src/solaris/native/sun/nio/ch/sctp/SctpNet.c](#jdk_srcsrcsolarisnativesunniochsctpsctpnetc)
 - [jdk_src/src/solaris/native/sun/java2d/x11/X11SurfaceData.c](#jdk_srcsrcsolarisnativesunjava2dx11x11surfacedatac)
 - [jdk_src/src/solaris/native/sun/java2d/x11/XRBackendNative.c](#jdk_srcsrcsolarisnativesunjava2dx11xrbackendnativec)
 - [jdk_src/src/solaris/native/sun/java2d/opengl/OGLFuncs_md.h](#jdk_srcsrcsolarisnativesunjava2dopengloglfuncs_mdh)
 - [jdk_src/src/solaris/native/sun/security/smartcardio/pcsc_md.c](#jdk_srcsrcsolarisnativesunsecuritysmartcardiopcsc_mdc)
 - [jdk_src/src/solaris/native/sun/security/jgss/wrapper/NativeFunc.c](#jdk_srcsrcsolarisnativesunsecurityjgsswrappernativefuncc)
 - [jdk_src/src/solaris/native/sun/security/pkcs11/j2secmod_md.c](#jdk_srcsrcsolarisnativesunsecuritypkcs11j2secmod_mdc)
 - [jdk_src/src/solaris/native/sun/security/pkcs11/wrapper/p11_md.c](#jdk_srcsrcsolarisnativesunsecuritypkcs11wrapperp11_mdc)
 - [jdk_src/src/solaris/native/sun/xawt/gnome_interface.c](#jdk_srcsrcsolarisnativesunxawtgnome_interfacec)
 - [jdk_src/src/solaris/native/sun/awt/fontpath.c](#jdk_srcsrcsolarisnativesunawtfontpathc)
 - [jdk_src/src/solaris/native/sun/awt/awt_LoadLibrary.c](#jdk_srcsrcsolarisnativesunawtawt_loadlibraryc)
 - [jdk_src/src/solaris/native/sun/awt/gtk2_interface.c](#jdk_srcsrcsolarisnativesunawtgtk2_interfacec)
 - [jdk_src/src/solaris/native/sun/awt/awt_Mlib.c](#jdk_srcsrcsolarisnativesunawtawt_mlibc)
 - [jdk_src/src/solaris/native/sun/awt/gtk3_interface.c](#jdk_srcsrcsolarisnativesunawtgtk3_interfacec)
 - [jdk_src/src/solaris/native/sun/awt/CUPSfuncs.c](#jdk_srcsrcsolarisnativesunawtcupsfuncsc)
 - [jdk_src/src/solaris/native/sun/awt/awt_UNIXToolkit.c](#jdk_srcsrcsolarisnativesunawtawt_unixtoolkitc)
 - [jdk_src/src/solaris/native/sun/awt/awt_GraphicsEnv.c](#jdk_srcsrcsolarisnativesunawtawt_graphicsenvc)
 - [jdk_src/src/solaris/native/sun/net/spi/DefaultProxySelector.c](#jdk_srcsrcsolarisnativesunnetspidefaultproxyselectorc)
 - [jdk_src/src/solaris/native/common/jni_util_md.c](#jdk_srcsrcsolarisnativecommonjni_util_mdc)
 - [jdk_src/src/solaris/native/java/lang/java_props_macosx.c](#jdk_srcsrcsolarisnativejavalangjava_props_macosxc)
 - [jdk_src/src/solaris/demo/jvmti/hprof/hprof_md.c](#jdk_srcsrcsolarisdemojvmtihprofhprof_mdc)
 - [jdk_src/src/solaris/npt/npt_md.h](#jdk_srcsrcsolarisnptnpt_mdh)
 - [jdk_src/src/solaris/back/linker_md.c](#jdk_srcsrcsolarisbacklinker_mdc)
 - [jdk_src/src/macosx/bin/java_md_macosx.c](#jdk_srcsrcmacosxbinjava_md_macosxc)
 - [jdk_src/src/macosx/native/sun/java2d/opengl/OGLFuncs_md.h](#jdk_srcsrcmacosxnativesunjava2dopengloglfuncs_mdh)
 - [jdk_src/test/sun/management/jmxremote/bootstrap/launcher.c](#jdk_srctestsunmanagementjmxremotebootstraplauncherc)
 - [shenandoah_src/src/share/tools/hsdis/hsdis-demo.c](#shenandoah_srcsrcsharetoolshsdishsdis-democ)
 - [shenandoah_src/agent/src/share/native/sadis.c](#shenandoah_srcagentsrcsharenativesadisc)
 - [hotspot_src/src/share/tools/hsdis/hsdis-demo.c](#hotspot_srcsrcsharetoolshsdishsdis-democ)
 - [hotspot_src/agent/src/share/native/sadis.c](#hotspot_srcagentsrcsharenativesadisc)

### jdk_src/src/solaris/bin/java_md_solinux.c

```c

{% raw %}
842 | 
843 |     JLI_TraceLauncher("JVM path is %s\n", jvmpath);
844 | 
845 |     libjvm = dlopen(jvmpath, RTLD_NOW + RTLD_GLOBAL);
846 |     if (libjvm == NULL) {
847 | #if defined(__solaris__) && defined(__sparc) && !defined(_LP64) /* i.e. 32-bit sparc */
1004 |             JLI_ReportErrorMessage(JRE_ERROR13);
1005 |             return NULL;
1006 |         }
1007 |         hSplashLib = dlopen(splashPath, RTLD_LAZY | RTLD_GLOBAL);
1008 |         JLI_TraceLauncher("Info: loaded %s\n", splashPath);
1009 |     }
{% endraw %}

```
### jdk_src/src/solaris/native/sun/jdga/dgalock.c

```c

{% raw %}
86 | static void Solaris_DGA_XineramaInit(Display *display) {
87 |     void * handle = NULL;
88 |     if (IsXineramaOn == NULL) {
89 |         handle = dlopen(JNI_LIB_NAME("xinerama"), RTLD_NOW);
90 |         if (handle != NULL) {
91 |             void *sym = dlsym(handle, "IsXineramaOn");
129 |         strcat(libName, visid.name);
130 |         strcat(libName,".so");
131 |         /* we use RTLD_NOW because of bug 4032715 */
132 |         handle = dlopen(libName, RTLD_NOW);
133 |         if (handle != 0) {
134 |             JDgaStatus ret = JDGA_FAILED;
{% endraw %}

```
### jdk_src/src/solaris/native/sun/nio/fs/MagicFileTypeDetector.c

```c

{% raw %}
51 | Java_sun_nio_fs_MagicFileTypeDetector_initialize0
52 |     (JNIEnv* env, jclass this)
53 | {
54 |     magic_handle = dlopen("libmagic.so", RTLD_LAZY);
55 |     if (magic_handle == NULL) {
56 |         magic_handle = dlopen("libmagic.so.1", RTLD_LAZY);
57 |         if (magic_handle == NULL) {
58 |             return JNI_FALSE;
{% endraw %}

```
### jdk_src/src/solaris/native/sun/nio/fs/GnomeFileTypeDetector.c

```c

{% raw %}
88 | {
89 |     void* gio_handle;
90 | 
91 |     gio_handle = dlopen("libgio-2.0.so", RTLD_LAZY);
92 |     if (gio_handle == NULL) {
93 |         gio_handle = dlopen("libgio-2.0.so.0", RTLD_LAZY);
94 |         if (gio_handle == NULL) {
95 |             return JNI_FALSE;
159 | {
160 |     void* vfs_handle;
161 | 
162 |     vfs_handle = dlopen("libgnomevfs-2.so", RTLD_LAZY);
163 |     if (vfs_handle == NULL) {
164 |         vfs_handle = dlopen("libgnomevfs-2.so.0", RTLD_LAZY);
165 |     }
166 |     if (vfs_handle == NULL) {
{% endraw %}

```
### jdk_src/src/solaris/native/sun/nio/ch/sctp/SctpNet.c

```c

{% raw %}
61 | jboolean loadSocketExtensionFuncs
62 |   (JNIEnv* env) {
63 | #ifndef USE_SYSTEM_SCTP
64 |     if (dlopen(nativeSctpLib, RTLD_GLOBAL | RTLD_LAZY) == NULL) {
65 |         JNU_ThrowByName(env, "java/lang/UnsupportedOperationException",
66 |               dlerror());
{% endraw %}

```
### jdk_src/src/solaris/native/sun/java2d/x11/X11SurfaceData.c

```c

{% raw %}
168 | 
169 |     if (tryDGA && (getenv("NO_J2D_DGA") == NULL)) {
170 |     /* we use RTLD_NOW because of bug 4032715 */
171 |         lib = dlopen(JNI_LIB_NAME("sunwjdga"), RTLD_NOW);
172 |     }
173 | 
{% endraw %}

```
### jdk_src/src/solaris/native/sun/java2d/x11/XRBackendNative.c

```c

{% raw %}
147 |     }
148 | 
149 | #if defined(__solaris__) || defined(_AIX)
150 |     xrenderlib = dlopen("libXrender.so",RTLD_GLOBAL|RTLD_LAZY);
151 |     if (xrenderlib != NULL) {
152 | 
{% endraw %}

```
### jdk_src/src/solaris/native/sun/java2d/opengl/OGLFuncs_md.h

```c

{% raw %}
117 |         if (libGLPath == NULL) { \
118 |             libGLPath = VERSIONED_JNI_LIB_NAME("GL", "1"); \
119 |         } \
120 |         OGL_LIB_HANDLE = dlopen(libGLPath, RTLD_LAZY | RTLD_LOCAL); \
121 |     } \
122 |     if (OGL_LIB_HANDLE) { \
{% endraw %}

```
### jdk_src/src/solaris/native/sun/security/smartcardio/pcsc_md.c

```c

{% raw %}
97 |         throwNullPointerException(env, "PCSC library name is null");
98 |         return;
99 |     }
100 |     hModule = dlopen(libName, RTLD_LAZY);
101 |     (*env)->ReleaseStringUTFChars(env, jLibName, libName);
102 | 
{% endraw %}

```
### jdk_src/src/solaris/native/sun/security/jgss/wrapper/NativeFunc.c

```c

{% raw %}
74 |     failed = FALSE;
75 |     error = NULL;
76 | 
77 |     gssLib = dlopen(libName, RTLD_NOW);
78 |     if (gssLib == NULL) {
79 |         failed = TRUE;
{% endraw %}

```
### jdk_src/src/solaris/native/sun/security/pkcs11/j2secmod_md.c

```c

{% raw %}
55 | 
56 |     // look up existing handle only, do not load
57 | #if defined(AIX)
58 |     void *hModule = dlopen(libName, RTLD_LAZY);
59 | #else
60 |     void *hModule = dlopen(libName, RTLD_NOLOAD);
61 | #endif
62 |     dprintf2("-handle for %s: %u\n", libName, hModule);
74 |     }
75 | 
76 |     dprintf1("-lib %s\n", libName);
77 |     hModule = dlopen(libName, RTLD_LAZY);
78 |     (*env)->ReleaseStringUTFChars(env, jLibName, libName);
79 |     dprintf2("-handle: %u (0X%X)\n", hModule, hModule);
{% endraw %}

```
### jdk_src/src/solaris/native/sun/security/pkcs11/wrapper/p11_md.c

```c

{% raw %}
98 |      */
99 |     dlerror(); /* clear any old error message not fetched */
100 | #ifdef DEBUG
101 |     hModule = dlopen(libraryNameStr, RTLD_NOW);
102 | #else
103 |     hModule = dlopen(libraryNameStr, RTLD_LAZY);
104 | #endif /* DEBUG */
105 | 
{% endraw %}

```
### jdk_src/src/solaris/native/sun/xawt/gnome_interface.c

```c

{% raw %}
35 |      // trying to open the gnomevfs. VERSIONED_JNI_LIB_NAME
36 |      // macros formats the library name in a system specific manner
37 |      // see jdk/src/solaris/javavm/export/jvm_md.h for more details
38 |      vfs_handle = dlopen(VERSIONED_JNI_LIB_NAME("gnomevfs-2", "0"), RTLD_LAZY);
39 |      if (vfs_handle == NULL) {
40 |          // if we cannot load the library using a version assumed by JNI
41 |          // we are trying to load the library without a version suffix
42 |          vfs_handle = dlopen(JNI_LIB_NAME("gnomevfs-2"), RTLD_LAZY);
43 |          if (vfs_handle == NULL) {
44 |  #ifdef INTERNAL_BUILD
64 |      // call gonme_vfs_init()
65 |      (*gnome_vfs_init)();
66 | 
67 |      gnome_handle = dlopen(VERSIONED_JNI_LIB_NAME("gnome-2", "0"), RTLD_LAZY);
68 |      if (gnome_handle == NULL) {
69 |          gnome_handle = dlopen(JNI_LIB_NAME("gnome-2"), RTLD_LAZY);
70 |          if (gnome_handle == NULL) {
71 |  #ifdef INTERNAL_BUILD
{% endraw %}

```
### jdk_src/src/solaris/native/sun/awt/fontpath.c

```c

{% raw %}
616 |      * case the user has installed a private version of the library and if that
617 |      * doesn't succeed, we try the version from /opt/freeware/lib/libfontconfig.a
618 |      */
619 |     libfontconfig = dlopen("libfontconfig.so", RTLD_LOCAL|RTLD_LAZY);
620 |     if (libfontconfig == NULL) {
621 |         libfontconfig = dlopen("/opt/freeware/lib/libfontconfig.a(libfontconfig.so.1)", RTLD_MEMBER|RTLD_LOCAL|RTLD_LAZY);
622 |         if (libfontconfig == NULL) {
623 |             return NULL;
631 |      * certain symbols - and functionality - to be available.
632 |      * Also add explicit search for .so.1 in case .so symlink doesn't exist.
633 |      */
634 |     libfontconfig = dlopen(FONTCONFIG_DLL_VERSIONED, RTLD_LOCAL|RTLD_LAZY);
635 |     if (libfontconfig == NULL) {
636 |         libfontconfig = dlopen(FONTCONFIG_DLL, RTLD_LOCAL|RTLD_LAZY);
637 |         if (libfontconfig == NULL) {
638 |             return NULL;
{% endraw %}

```
### jdk_src/src/solaris/native/sun/awt/awt_LoadLibrary.c

```c

{% raw %}
167 |                                "(Ljava/lang/String;)V",
168 |                                jbuf);
169 | 
170 |     awtHandle = dlopen(buf, RTLD_LAZY | RTLD_GLOBAL);
171 | 
172 |     return JNI_VERSION_1_2;
{% endraw %}

```
### jdk_src/src/solaris/native/sun/awt/gtk2_interface.c

```c

{% raw %}
321 | 
322 | #ifdef RTLD_NOLOAD
323 |         /* Just check if gtk libs are already in the process space */
324 |         lib = dlopen(lib_name, RTLD_LAZY | RTLD_NOLOAD);
325 |         if (!load || lib != NULL) {
326 |             return lib != NULL;
333 | #endif
334 | #endif
335 | 
336 |         lib = dlopen(lib_name, RTLD_LAZY | RTLD_LOCAL);
337 |         if (lib == NULL) {
338 |             return FALSE;
497 |     int (*io_handler)();
498 |     char *gtk_modules_env;
499 | 
500 |     gtk2_libhandle = dlopen(lib_name, RTLD_LAZY | RTLD_LOCAL);
501 |     if (gtk2_libhandle == NULL) {
502 |         return FALSE;
503 |     }
504 | 
505 |     gthread_libhandle = dlopen(GTHREAD_LIB_VERSIONED, RTLD_LAZY | RTLD_LOCAL);
506 |     if (gthread_libhandle == NULL) {
507 |         gthread_libhandle = dlopen(GTHREAD_LIB, RTLD_LAZY | RTLD_LOCAL);
508 |         if (gthread_libhandle == NULL)
509 |             return FALSE;
{% endraw %}

```
### jdk_src/src/solaris/native/sun/awt/awt_Mlib.c

```c

{% raw %}
67 |         ((strncmp(name.machine, "sun4v" , 5) == 0) &&
68 |          (getenv("USE_VIS_ON_SUN4V") != NULL)))
69 |     {
70 |         handle = dlopen(JNI_LIB_NAME("mlib_image_v"), RTLD_LAZY);
71 |     }
72 | 
73 |     if (handle == NULL) {
74 |         handle = dlopen(JNI_LIB_NAME("mlib_image"), RTLD_LAZY);
75 |     }
76 | 
77 |     if (handle == NULL) {
78 |         if (s_timeIt || s_verbose) {
79 |             printf ("error in dlopen: %s", dlerror());
80 |         }
81 |         return MLIB_FAILURE;
{% endraw %}

```
### jdk_src/src/solaris/native/sun/awt/gtk3_interface.c

```c

{% raw %}
93 |         return TRUE;
94 |     } else {
95 | #ifdef RTLD_NOLOAD
96 |         void *lib = dlopen(lib_name, RTLD_LAZY | RTLD_NOLOAD);
97 |         if (!load || lib != NULL) {
98 |             return lib != NULL;
104 |         /* probably not worth it because most AIX servers don't have GTK libs anyway */
105 | #endif
106 | #endif
107 |         return dlopen(lib_name, RTLD_LAZY | RTLD_LOCAL) != NULL;
108 |     }
109 | }
255 |     int (*handler)();
256 |     int (*io_handler)();
257 |     char *gtk_modules_env;
258 |     gtk3_libhandle = dlopen(lib_name, RTLD_LAZY | RTLD_LOCAL);
259 |     if (gtk3_libhandle == NULL) {
260 |         return FALSE;
{% endraw %}

```
### jdk_src/src/solaris/native/sun/awt/CUPSfuncs.c

```c

{% raw %}
65 | JNIEXPORT jboolean JNICALL
66 | Java_sun_print_CUPSPrinter_initIDs(JNIEnv *env,
67 |                                          jobject printObj) {
68 |   void *handle = dlopen(VERSIONED_JNI_LIB_NAME("cups", "2"),
69 |                         RTLD_LAZY | RTLD_GLOBAL);
70 | 
71 |   if (handle == NULL) {
72 |     handle = dlopen(JNI_LIB_NAME("cups"), RTLD_LAZY | RTLD_GLOBAL);
73 |     if (handle == NULL) {
74 |       return JNI_FALSE;
{% endraw %}

```
### jdk_src/src/solaris/native/sun/awt/awt_UNIXToolkit.c

```c

{% raw %}
231 | {
232 |     typedef void (*SplashClose_t)();
233 |     SplashClose_t splashClose;
234 |     void* hSplashLib = dlopen(0, RTLD_LAZY);
235 |     if (!hSplashLib) {
236 |         return;
{% endraw %}

```
### jdk_src/src/solaris/native/sun/awt/awt_GraphicsEnv.c

```c

{% raw %}
426 |     if (XQueryExtension(awt_display, "RENDER",
427 |                         &major_opcode, &first_event, &first_error))
428 |     {
429 |         xrenderLibHandle = dlopen("libXrender.so.1", RTLD_LAZY | RTLD_GLOBAL);
430 | 
431 | #ifdef MACOSX
435 | #endif
436 | 
437 |         if (xrenderLibHandle == NULL) {
438 |             xrenderLibHandle = dlopen(XRENDER_LIB,
439 |                                       RTLD_LAZY | RTLD_GLOBAL);
440 |         }
441 | 
442 | #ifndef __linux__ /* SOLARIS */
443 |         if (xrenderLibHandle == NULL) {
444 |             xrenderLibHandle = dlopen("/usr/sfw/lib/libXrender.so.1",
445 |                                       RTLD_LAZY | RTLD_GLOBAL);
446 |         }
593 |     XineramaQueryScreensFunc* XineramaQueryScreens = NULL;
594 | 
595 |     /* load library */
596 |     libHandle = dlopen(VERSIONED_JNI_LIB_NAME("Xinerama", "1"),
597 |                        RTLD_LAZY | RTLD_GLOBAL);
598 |     if (libHandle == NULL) {
599 |         libHandle = dlopen(JNI_LIB_NAME("Xinerama"), RTLD_LAZY | RTLD_GLOBAL);
600 |     }
601 |     if (libHandle != NULL) {
646 |     XineramaGetInfoFunc* XineramaSolarisFunc = NULL;
647 | 
648 |     /* load library */
649 |     libHandle = dlopen(JNI_LIB_NAME("Xext"), RTLD_LAZY | RTLD_GLOBAL);
650 |     if (libHandle != NULL) {
651 |         XineramaSolarisFunc = (XineramaGetInfoFunc*)dlsym(libHandle, XineramaGetInfoName);
1679 | {
1680 |     int rr_maj_ver = 0, rr_min_ver = 0;
1681 | 
1682 |     void *pLibRandR = dlopen(VERSIONED_JNI_LIB_NAME("Xrandr", "2"),
1683 |                              RTLD_LAZY | RTLD_LOCAL);
1684 |     if (pLibRandR == NULL) {
1685 |         pLibRandR = dlopen(JNI_LIB_NAME("Xrandr"), RTLD_LAZY | RTLD_LOCAL);
1686 |     }
1687 |     if (pLibRandR == NULL) {
{% endraw %}

```
### jdk_src/src/solaris/native/sun/net/spi/DefaultProxySelector.c

```c

{% raw %}
130 |     /**
131 |      * Let's try to load GConf-2 library
132 |      */
133 |     if (dlopen(JNI_LIB_NAME("gconf-2"), RTLD_GLOBAL | RTLD_LAZY) != NULL ||
134 |         dlopen(VERSIONED_JNI_LIB_NAME("gconf-2", "4"),
135 |                RTLD_GLOBAL | RTLD_LAZY) != NULL)
136 |     {
315 | static int initGProxyResolver() {
316 |     void *gio_handle;
317 | 
318 |     gio_handle = dlopen("libgio-2.0.so", RTLD_LAZY);
319 |     if (!gio_handle) {
320 |         gio_handle = dlopen("libgio-2.0.so.0", RTLD_LAZY);
321 |         if (!gio_handle) {
322 |             return 0;
{% endraw %}

```
### jdk_src/src/solaris/native/common/jni_util_md.c

```c

{% raw %}
49 |         return procHandle;
50 |     }
51 | #ifdef __APPLE__
52 |     procHandle = (void*)dlopen(NULL, RTLD_FIRST);
53 | #else
54 |     procHandle = (void*)dlopen(NULL, RTLD_LAZY);
55 | #endif
56 |     return procHandle;
{% endraw %}

```
### jdk_src/src/solaris/native/java/lang/java_props_macosx.c

```c

{% raw %}
39 | static void *getJRSFramework() {
40 |     static void *jrsFwk = NULL;
41 |     if (jrsFwk == NULL) {
42 |        jrsFwk = dlopen("/System/Library/Frameworks/JavaVM.framework/Frameworks/JavaRuntimeSupport.framework/JavaRuntimeSupport", RTLD_LAZY | RTLD_LOCAL);
43 |     }
44 |     return jrsFwk;
{% endraw %}

```
### jdk_src/src/solaris/demo/jvmti/hprof/hprof_md.c

```c

{% raw %}
436 | {
437 |     void * result;
438 | 
439 |     result = dlopen(name, RTLD_LAZY);
440 |     if (result == NULL) {
441 |         (void)strncpy(err_buf, dlerror(), err_buflen-2);
{% endraw %}

```
### jdk_src/src/solaris/npt/npt_md.h

```c

{% raw %}
42 |                                                                         \
43 |         if ( (pnpt) == NULL ) NPT_ERROR("NptEnv* is NULL");             \
44 |         *(pnpt) = NULL;                                                 \
45 |         _handle =  dlopen(path, RTLD_LAZY);                             \
46 |         if ( _handle == NULL ) NPT_ERROR("Cannot open library");        \
47 |         _sym = dlsym(_handle, "nptInitialize");                         \
{% endraw %}

```
### jdk_src/src/solaris/back/linker_md.c

```c

{% raw %}
121 | {
122 |     void * result;
123 | #ifdef NATIVE
124 |     result = dlopen(name, RTLD_LAZY);
125 | #else
126 |     sysMonitorEnter(greenThreadSelf(), &_dl_lock);
127 |     result = dlopen(name, RTLD_NOW);
128 |     sysMonitorExit(greenThreadSelf(), &_dl_lock);
129 |     /*
{% endraw %}

```
### jdk_src/src/macosx/bin/java_md_macosx.c

```c

{% raw %}
668 | 
669 |     JLI_TraceLauncher("JVM path is %s\n", jvmpath);
670 | 
671 |     libjvm = dlopen(jvmpath, RTLD_NOW + RTLD_GLOBAL);
672 |     if (libjvm == NULL) {
673 |         JLI_ReportErrorMessage(DLL_ERROR1, __LINE__);
762 |     JavaVM * jvm = NULL;
763 | 
764 |     // The handle is good for both the launcher and the libosxapp.dylib
765 |     void * handle = dlopen(NULL, RTLD_LAZY | RTLD_GLOBAL);
766 |     if (handle) {
767 |         typedef JavaVM* (*JLI_GetJavaVMInstance_t)();
815 |             return NULL;
816 |         }
817 | 
818 |         hSplashLib = dlopen(splashPath, RTLD_LAZY | RTLD_GLOBAL);
819 |         // It's OK if dlopen() fails. The splash screen library binary file
820 |         // might have been stripped out from the JRE image to reduce its size
{% endraw %}

```
### jdk_src/src/macosx/native/sun/java2d/opengl/OGLFuncs_md.h

```c

{% raw %}
35 | #define OGL_LIB_IS_UNINITIALIZED() \
36 |     (OGL_LIB_HANDLE == NULL)
37 | #define OGL_OPEN_LIB() \
38 |     OGL_LIB_HANDLE = dlopen("/System/Library/Frameworks/OpenGL.framework/Versions/Current/Libraries/libGL.dylib", RTLD_LAZY | RTLD_GLOBAL)
39 | #define OGL_CLOSE_LIB() \
40 |     dlclose(OGL_LIB_HANDLE)
{% endraw %}

```
### jdk_src/test/sun/management/jmxremote/bootstrap/launcher.c

```c

{% raw %}
33 | typedef jint (*create_vm_func)(JavaVM **, void**, void*);
34 | 
35 | void *JNU_FindCreateJavaVM(char *vmlibpath) {
36 |     void *libVM = dlopen(vmlibpath, RTLD_LAZY);
37 |     if (libVM == NULL) {
38 |         return NULL;
{% endraw %}

```
### shenandoah_src/src/share/tools/hsdis/hsdis-demo.c

```c

{% raw %}
112 |       const char* next_lib = (*next_in_path++);
113 |       if (next_lib == NULL)
114 |         return "cannot find plugin "HSDIS_NAME LIB_EXT;
115 |       dllib = dlopen(next_lib, RTLD_LAZY);
116 |     }
117 |   }
{% endraw %}

```
### shenandoah_src/agent/src/share/native/sadis.c

```c

{% raw %}
134 |   }
135 | #else
136 |   void* hsdis_handle;
137 |   hsdis_handle = dlopen(libname, RTLD_LAZY | RTLD_GLOBAL);
138 |   if (hsdis_handle == NULL) {
139 |     snprintf(buffer, sizeof(buffer), "%s%s", jrepath, libname);
140 |     hsdis_handle = dlopen(buffer, RTLD_LAZY | RTLD_GLOBAL);
141 |   }
142 |   if (hsdis_handle != NULL) {
{% endraw %}

```
### hotspot_src/src/share/tools/hsdis/hsdis-demo.c

```c

{% raw %}
112 |       const char* next_lib = (*next_in_path++);
113 |       if (next_lib == NULL)
114 |         return "cannot find plugin "HSDIS_NAME LIB_EXT;
115 |       dllib = dlopen(next_lib, RTLD_LAZY);
116 |     }
117 |   }
{% endraw %}

```
### hotspot_src/agent/src/share/native/sadis.c

```c

{% raw %}
134 |   }
135 | #else
136 |   void* hsdis_handle;
137 |   hsdis_handle = dlopen(libname, RTLD_LAZY | RTLD_GLOBAL);
138 |   if (hsdis_handle == NULL) {
139 |     snprintf(buffer, sizeof(buffer), "%s%s", jrepath, libname);
140 |     hsdis_handle = dlopen(buffer, RTLD_LAZY | RTLD_GLOBAL);
141 |   }
142 |   if (hsdis_handle != NULL) {
{% endraw %}

```