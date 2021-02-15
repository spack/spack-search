---
name: "opencascade"
layout: package
next_package: r-reticulate
previous_package: qthreads
languages: []
---
## 7.4.0
3 / 16274 files match

 - [src/OSD/OSD_SharedLibrary.cxx](#srcosdosd_sharedlibrarycxx)
 - [src/OpenGl/OpenGl_Context.cxx](#srcopenglopengl_contextcxx)
 - [tools/TInspectorAPI/TInspectorAPI_Communicator.cxx](#toolstinspectorapitinspectorapi_communicatorcxx)

### src/OSD/OSD_SharedLibrary.cxx

```

{% raw %}
24 |  * Values for 'mode' argument in dlopen().
33 | #define _LIBDL_RLD_DLOPEN	1
37 | extern "C" {void	*dlopen(char *path, int mode);}
88 | // DlOpen:   The dlopen function provides an interface to the dynamic 
91 | // The dlopen function attempts to load filename, in the address space 
101 | // symbol binding during the dlopen call.  
102 | // The dlopen function returns a handle that is used by dlsym or 
105 | // If a NULL filename is specified, dlopen returns a handle for the main      
109 | Standard_Boolean  OSD_SharedLibrary::DlOpen(const OSD_LoadMode aMode ) {
111 |   myHandle = dlopen (myName,RTLD_LAZY);
114 |   myHandle = dlopen (myName,RTLD_NOW);
156 | // occurred from a call to dlopen, dlclose or dlsym.
244 | Standard_Boolean OSD_SharedLibrary :: DlOpen ( const OSD_LoadMode /*Mode*/ ) {
264 | }  // end OSD_SharedLibrary :: DlOpen
{% endraw %}

```
### src/OpenGl/OpenGl_Context.cxx

```

{% raw %}
239 |   myGlLibHandle = dlopen ("/System/Library/Frameworks/OpenGLES.framework/OpenGLES", RTLD_LAZY);
242 |   myGlLibHandle = dlopen ("/System/Library/Frameworks/OpenGL.framework/Versions/Current/OpenGL", RTLD_LAZY);
{% endraw %}

```
### tools/TInspectorAPI/TInspectorAPI_Communicator.cxx

```

{% raw %}
50 |   void* modLib = dlopen(aPluginLibraryName.ToCString(), RTLD_LAZY | RTLD_GLOBAL);
{% endraw %}

```