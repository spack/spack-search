---
name: "icedtea"
layout: package
next_package: darshan-util
previous_package: lzma
languages: ['c']
---
## 3.4.0
70 / 50289 files match

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
845 |     libjvm = dlopen(jvmpath, RTLD_NOW + RTLD_GLOBAL);
1007 |         hSplashLib = dlopen(splashPath, RTLD_LAZY | RTLD_GLOBAL);
{% endraw %}

```
### jdk_src/src/solaris/native/sun/jdga/dgalock.c

```c

{% raw %}
89 |         handle = dlopen(JNI_LIB_NAME("xinerama"), RTLD_NOW);
132 |         handle = dlopen(libName, RTLD_NOW);
{% endraw %}

```
### jdk_src/src/solaris/native/sun/nio/fs/MagicFileTypeDetector.c

```c

{% raw %}
54 |     magic_handle = dlopen("libmagic.so", RTLD_LAZY);
56 |         magic_handle = dlopen("libmagic.so.1", RTLD_LAZY);
{% endraw %}

```
### jdk_src/src/solaris/native/sun/nio/fs/GnomeFileTypeDetector.c

```c

{% raw %}
91 |     gio_handle = dlopen("libgio-2.0.so", RTLD_LAZY);
93 |         gio_handle = dlopen("libgio-2.0.so.0", RTLD_LAZY);
162 |     vfs_handle = dlopen("libgnomevfs-2.so", RTLD_LAZY);
164 |         vfs_handle = dlopen("libgnomevfs-2.so.0", RTLD_LAZY);
{% endraw %}

```
### jdk_src/src/solaris/native/sun/nio/ch/sctp/SctpNet.c

```c

{% raw %}
64 |     if (dlopen(nativeSctpLib, RTLD_GLOBAL | RTLD_LAZY) == NULL) {
{% endraw %}

```
### jdk_src/src/solaris/native/sun/java2d/x11/X11SurfaceData.c

```c

{% raw %}
171 |         lib = dlopen(JNI_LIB_NAME("sunwjdga"), RTLD_NOW);
{% endraw %}

```
### jdk_src/src/solaris/native/sun/java2d/x11/XRBackendNative.c

```c

{% raw %}
150 |     xrenderlib = dlopen("libXrender.so",RTLD_GLOBAL|RTLD_LAZY);
{% endraw %}

```
### jdk_src/src/solaris/native/sun/java2d/opengl/OGLFuncs_md.h

```c

{% raw %}
120 |         OGL_LIB_HANDLE = dlopen(libGLPath, RTLD_LAZY | RTLD_LOCAL); \
{% endraw %}

```
### jdk_src/src/solaris/native/sun/security/smartcardio/pcsc_md.c

```c

{% raw %}
100 |     hModule = dlopen(libName, RTLD_LAZY);
{% endraw %}

```
### jdk_src/src/solaris/native/sun/security/jgss/wrapper/NativeFunc.c

```c

{% raw %}
77 |     gssLib = dlopen(libName, RTLD_NOW);
{% endraw %}

```
### jdk_src/src/solaris/native/sun/security/pkcs11/j2secmod_md.c

```c

{% raw %}
58 |     void *hModule = dlopen(libName, RTLD_LAZY);
60 |     void *hModule = dlopen(libName, RTLD_NOLOAD);
77 |     hModule = dlopen(libName, RTLD_LAZY);
{% endraw %}

```
### jdk_src/src/solaris/native/sun/security/pkcs11/wrapper/p11_md.c

```c

{% raw %}
101 |     hModule = dlopen(libraryNameStr, RTLD_NOW);
103 |     hModule = dlopen(libraryNameStr, RTLD_LAZY);
{% endraw %}

```
### jdk_src/src/solaris/native/sun/xawt/gnome_interface.c

```c

{% raw %}
38 |      vfs_handle = dlopen(VERSIONED_JNI_LIB_NAME("gnomevfs-2", "0"), RTLD_LAZY);
42 |          vfs_handle = dlopen(JNI_LIB_NAME("gnomevfs-2"), RTLD_LAZY);
67 |      gnome_handle = dlopen(VERSIONED_JNI_LIB_NAME("gnome-2", "0"), RTLD_LAZY);
69 |          gnome_handle = dlopen(JNI_LIB_NAME("gnome-2"), RTLD_LAZY);
{% endraw %}

```
### jdk_src/src/solaris/native/sun/awt/fontpath.c

```c

{% raw %}
619 |     libfontconfig = dlopen("libfontconfig.so", RTLD_LOCAL|RTLD_LAZY);
621 |         libfontconfig = dlopen("/opt/freeware/lib/libfontconfig.a(libfontconfig.so.1)", RTLD_MEMBER|RTLD_LOCAL|RTLD_LAZY);
634 |     libfontconfig = dlopen(FONTCONFIG_DLL_VERSIONED, RTLD_LOCAL|RTLD_LAZY);
636 |         libfontconfig = dlopen(FONTCONFIG_DLL, RTLD_LOCAL|RTLD_LAZY);
{% endraw %}

```
### jdk_src/src/solaris/native/sun/awt/awt_LoadLibrary.c

```c

{% raw %}
170 |     awtHandle = dlopen(buf, RTLD_LAZY | RTLD_GLOBAL);
{% endraw %}

```
### jdk_src/src/solaris/native/sun/awt/gtk2_interface.c

```c

{% raw %}
324 |         lib = dlopen(lib_name, RTLD_LAZY | RTLD_NOLOAD);
336 |         lib = dlopen(lib_name, RTLD_LAZY | RTLD_LOCAL);
500 |     gtk2_libhandle = dlopen(lib_name, RTLD_LAZY | RTLD_LOCAL);
505 |     gthread_libhandle = dlopen(GTHREAD_LIB_VERSIONED, RTLD_LAZY | RTLD_LOCAL);
507 |         gthread_libhandle = dlopen(GTHREAD_LIB, RTLD_LAZY | RTLD_LOCAL);
{% endraw %}

```
### jdk_src/src/solaris/native/sun/awt/awt_Mlib.c

```c

{% raw %}
70 |         handle = dlopen(JNI_LIB_NAME("mlib_image_v"), RTLD_LAZY);
74 |         handle = dlopen(JNI_LIB_NAME("mlib_image"), RTLD_LAZY);
79 |             printf ("error in dlopen: %s", dlerror());
{% endraw %}

```
### jdk_src/src/solaris/native/sun/awt/gtk3_interface.c

```c

{% raw %}
96 |         void *lib = dlopen(lib_name, RTLD_LAZY | RTLD_NOLOAD);
107 |         return dlopen(lib_name, RTLD_LAZY | RTLD_LOCAL) != NULL;
258 |     gtk3_libhandle = dlopen(lib_name, RTLD_LAZY | RTLD_LOCAL);
{% endraw %}

```
### jdk_src/src/solaris/native/sun/awt/CUPSfuncs.c

```c

{% raw %}
68 |   void *handle = dlopen(VERSIONED_JNI_LIB_NAME("cups", "2"),
72 |     handle = dlopen(JNI_LIB_NAME("cups"), RTLD_LAZY | RTLD_GLOBAL);
{% endraw %}

```
### jdk_src/src/solaris/native/sun/awt/awt_UNIXToolkit.c

```c

{% raw %}
234 |     void* hSplashLib = dlopen(0, RTLD_LAZY);
{% endraw %}

```
### jdk_src/src/solaris/native/sun/awt/awt_GraphicsEnv.c

```c

{% raw %}
429 |         xrenderLibHandle = dlopen("libXrender.so.1", RTLD_LAZY | RTLD_GLOBAL);
438 |             xrenderLibHandle = dlopen(XRENDER_LIB,
444 |             xrenderLibHandle = dlopen("/usr/sfw/lib/libXrender.so.1",
596 |     libHandle = dlopen(VERSIONED_JNI_LIB_NAME("Xinerama", "1"),
599 |         libHandle = dlopen(JNI_LIB_NAME("Xinerama"), RTLD_LAZY | RTLD_GLOBAL);
649 |     libHandle = dlopen(JNI_LIB_NAME("Xext"), RTLD_LAZY | RTLD_GLOBAL);
1682 |     void *pLibRandR = dlopen(VERSIONED_JNI_LIB_NAME("Xrandr", "2"),
1685 |         pLibRandR = dlopen(JNI_LIB_NAME("Xrandr"), RTLD_LAZY | RTLD_LOCAL);
{% endraw %}

```
### jdk_src/src/solaris/native/sun/net/spi/DefaultProxySelector.c

```c

{% raw %}
133 |     if (dlopen(JNI_LIB_NAME("gconf-2"), RTLD_GLOBAL | RTLD_LAZY) != NULL ||
134 |         dlopen(VERSIONED_JNI_LIB_NAME("gconf-2", "4"),
318 |     gio_handle = dlopen("libgio-2.0.so", RTLD_LAZY);
320 |         gio_handle = dlopen("libgio-2.0.so.0", RTLD_LAZY);
{% endraw %}

```
### jdk_src/src/solaris/native/common/jni_util_md.c

```c

{% raw %}
52 |     procHandle = (void*)dlopen(NULL, RTLD_FIRST);
54 |     procHandle = (void*)dlopen(NULL, RTLD_LAZY);
{% endraw %}

```
### jdk_src/src/solaris/native/java/lang/java_props_macosx.c

```c

{% raw %}
42 |        jrsFwk = dlopen("/System/Library/Frameworks/JavaVM.framework/Frameworks/JavaRuntimeSupport.framework/JavaRuntimeSupport", RTLD_LAZY | RTLD_LOCAL);
{% endraw %}

```
### jdk_src/src/solaris/demo/jvmti/hprof/hprof_md.c

```c

{% raw %}
439 |     result = dlopen(name, RTLD_LAZY);
{% endraw %}

```
### jdk_src/src/solaris/npt/npt_md.h

```c

{% raw %}
45 |         _handle =  dlopen(path, RTLD_LAZY);                             \
{% endraw %}

```
### jdk_src/src/solaris/back/linker_md.c

```c

{% raw %}
124 |     result = dlopen(name, RTLD_LAZY);
127 |     result = dlopen(name, RTLD_NOW);
{% endraw %}

```
### jdk_src/src/macosx/bin/java_md_macosx.c

```c

{% raw %}
671 |     libjvm = dlopen(jvmpath, RTLD_NOW + RTLD_GLOBAL);
765 |     void * handle = dlopen(NULL, RTLD_LAZY | RTLD_GLOBAL);
818 |         hSplashLib = dlopen(splashPath, RTLD_LAZY | RTLD_GLOBAL);
{% endraw %}

```
### jdk_src/src/macosx/native/sun/java2d/opengl/OGLFuncs_md.h

```c

{% raw %}
38 |     OGL_LIB_HANDLE = dlopen("/System/Library/Frameworks/OpenGL.framework/Versions/Current/Libraries/libGL.dylib", RTLD_LAZY | RTLD_GLOBAL)
{% endraw %}

```
### jdk_src/test/sun/management/jmxremote/bootstrap/launcher.c

```c

{% raw %}
36 |     void *libVM = dlopen(vmlibpath, RTLD_LAZY);
{% endraw %}

```
### shenandoah_src/src/share/tools/hsdis/hsdis-demo.c

```c

{% raw %}
115 |       dllib = dlopen(next_lib, RTLD_LAZY);
{% endraw %}

```
### shenandoah_src/agent/src/share/native/sadis.c

```c

{% raw %}
137 |   hsdis_handle = dlopen(libname, RTLD_LAZY | RTLD_GLOBAL);
140 |     hsdis_handle = dlopen(buffer, RTLD_LAZY | RTLD_GLOBAL);
{% endraw %}

```
### hotspot_src/src/share/tools/hsdis/hsdis-demo.c

```c

{% raw %}
115 |       dllib = dlopen(next_lib, RTLD_LAZY);
{% endraw %}

```
### hotspot_src/agent/src/share/native/sadis.c

```c

{% raw %}
137 |   hsdis_handle = dlopen(libname, RTLD_LAZY | RTLD_GLOBAL);
140 |     hsdis_handle = dlopen(buffer, RTLD_LAZY | RTLD_GLOBAL);
{% endraw %}

```