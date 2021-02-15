---
name: "virtualgl"
layout: package
next_package: otf
previous_package: rccl
languages: ['html', 'cpp']
---
## 2.5.2
14 / 497 files match

 - [ChangeLog.md](#changelogmd)
 - [CMakeLists.txt](#cmakeliststxt)
 - [server/vglrun.in](#servervglrunin)
 - [server/TransPlugin.cpp](#servertransplugincpp)
 - [server/faker-sym.h](#serverfaker-symh)
 - [server/faker.cpp](#serverfakercpp)
 - [server/dlfakerut.c](#serverdlfakerutc)
 - [server/servertest.in](#serverservertestin)
 - [server/dlfaker.c](#serverdlfakerc)
 - [server/faker-sym.cpp](#serverfaker-symcpp)
 - [server/CMakeLists.txt](#servercmakeliststxt)
 - [server/faker-mapfile.c](#serverfaker-mapfilec)
 - [doc/apprecipes.txt](#docapprecipestxt)
 - [doc/index.html](#docindexhtml)

### ChangeLog.md

```

{% raw %}
25 | OpenGL functions via dlopen()/dlsym(), would fail to load the "real" GLX/OpenGL
30 | 6. The interposed `dlopen()` function in the Linux version of libdlfaker.so
32 | to `dlopen()`.  This prevents an issue whereby an application could call
33 | `dlopen(..., *|RTLD_DEEPBIND)` to load a shared library that uses OpenGL or
900 | `dlopen()`.  In previous versions of VirtualGL, any calls to
901 | `dlopen("*libGL*", ...)` would be replaced with a call to
902 | `dlopen("librrfaker.so", ...)`.  This caused problems with VisIt, which has a
904 | matching criteria has been changed such that `dlopen()` only overrides calls to
905 | `dlopen("libGL\.*", ...)` or `dlopen("*/libGL\.*", ...)`.
910 | 4. VirtualGL's interposed version of `dlopen()` will now modify calls to
911 | `dlopen("libdl*", ...)` as well as `dlopen("libGL*", ...)`.  This is to work
918 | 6. Moved `dlopen()` back into a separate faker library (libdlfaker.so.)
1631 | ahead of VirtualGL in the link order.  libdlfaker.so intercepts `dlopen()`
1632 | calls from an application and, if the application is trying to use `dlopen()`
{% endraw %}

```
### CMakeLists.txt

```

{% raw %}
341 | 		"Base name for VirtualGL's dlopen() interposer library (default: ${DEFAULT_VGL_DLFAKER_NAME})")
{% endraw %}

```
### server/vglrun.in

```

{% raw %}
54 | 	echo "-nodl     : Don't interpose the dlopen() function.  dlopen() is normally"
55 | 	echo "            interposed to force applications that use dlopen() to load libGL"
57 | 	echo "            applications that link directly with libGL, disabling the dlopen()"
{% endraw %}

```
### server/TransPlugin.cpp

```

{% raw %}
49 | 	dllhnd=dlopen(filename, RTLD_NOW);
{% endraw %}

```
### server/faker-sym.h

```cpp

{% raw %}
621 | typedef	void* (*_dlopenType)(const char *, int);
622 | void *_vgl_dlopen(const char *, int);
623 | SYMDEF(dlopen);
{% endraw %}

```
### server/faker.cpp

```

{% raw %}
184 | // This is the "real" version of dlopen(), which is called by the interposed
185 | // version of dlopen() in libdlfaker.  Can't recall why this is here and not
188 | void *_vgl_dlopen(const char *file, int mode)
190 | 	if(!__dlopen)
193 | 		if(!__dlopen)
196 | 			__dlopen=(_dlopenType)dlsym(RTLD_NEXT, "dlopen");
198 | 			if(!__dlopen)
200 | 				vglout.print("[VGL] ERROR: Could not load function \"dlopen\"\n");
206 | 	return __dlopen(file, mode);
{% endraw %}

```
### server/dlfakerut.c

```cpp

{% raw %}
67 | 		gldllhnd=dlopen(temps, RTLD_NOW);
69 | 	else gldllhnd=dlopen("libGL.so", RTLD_NOW);
116 | /* Test whether libvglfaker's version of dlopen() is discriminating enough.
126 | 	fprintf(stderr, "dlopen() name matching test:\n");
127 | 	gldllhnd=dlopen("libGLdlfakerut.so", RTLD_NOW);
156 | 	gldllhnd=dlopen("libdeepbindtest.so", RTLD_NOW|RTLD_DEEPBIND);
200 | 	test("dlopen() test");
{% endraw %}

```
### server/servertest.in

```

{% raw %}
35 | 		echo "Testing without dlopen() interposer"
{% endraw %}

```
### server/dlfaker.c

```cpp

{% raw %}
21 | extern void *_vgl_dlopen(const char *, int);
24 | /* If an application uses dlopen()/dlsym() to load functions from libGL or
26 |    intercept dlopen() and return a handle to itself rather than a handle to
29 |    NOTE: If the application tries to use dlopen() to obtain a handle to libdl,
34 | void *dlopen(const char *filename, int flag)
48 | 		fprintf(stderr, "[VGL] dlopen (filename=%s flag=%d",
67 | 				"[VGL] NOTICE: Replacing dlopen(\"%s\") with dlopen(\"%s\")\n",
69 | 		retval=_vgl_dlopen(env, flag);
75 | 			fprintf(stderr, "[VGL] NOTICE: Replacing dlopen(\"%s\") with dlopen(\"lib"VGL_DLFAKER_NAME".so\")\n",
77 | 		retval=_vgl_dlopen("lib"VGL_DLFAKER_NAME".so", flag);
79 | 	else retval=_vgl_dlopen(filename, flag);
87 | 			fprintf(stderr, "[VGL] NOTICE: dlopen(\"%s\") failed.\n", filename);
88 | 			fprintf(stderr, "[VGL]    Trying dlopen(\"%s\")\n", temps);
90 | 		retval=_vgl_dlopen(temps, flag);
{% endraw %}

```
### server/faker-sym.cpp

```

{% raw %}
100 | 			void *dllhnd=_vgl_dlopen(fconfig.gllib, RTLD_LAZY);
177 | 			void *dllhnd=_vgl_dlopen(fconfig.x11lib, RTLD_LAZY);
219 | 			void *dllhnd=_vgl_dlopen(fconfig.id##lib, RTLD_LAZY);  \
241 | 				dllhnd=_vgl_dlopen(libName, RTLD_LAZY);  \
{% endraw %}

```
### server/CMakeLists.txt

```

{% raw %}
86 | 		# dlopen()/dlsym()), --as-needed prevents the linker from adding a
{% endraw %}

```
### server/faker-mapfile.c

```cpp

{% raw %}
137 | 		_vgl_dlopen;
{% endraw %}

```
### doc/apprecipes.txt

```

{% raw %}
130 | 		''dlopen()'' function (which it does by default), this causes the actual \
131 | 		''dlopen()'' system calls to come from ''libdlfaker.so'', so ''$ORIGIN'' \
133 | 		installed.  This causes the ''dlopen()'' calls within the Intel ICD to \
{% endraw %}

```
### doc/index.html

```html

{% raw %}
2301 |     <td class="standard">The Intel OpenCL installable client driver (ICD) is linked with a run-time library search path (rpath) of <code>$ORIGIN</code>, which would normally have the same effect as adding the directory in which the ICD is installed (default: <code>/opt/intel/opencl/lib64</code> on 64-bit systems) to <code>LD_LIBRARY_PATH</code>.  However, when VirtualGL is interposing the <code>dlopen()</code> function (which it does by default), this causes the actual <code>dlopen()</code> system calls to come from <code>libdlfaker.so</code>, so <code>$ORIGIN</code> will resolve to the directory in which the VirtualGL faker libraries are installed.  This causes the <code>dlopen()</code> calls within the Intel ICD to fail, and because the ICD apparently does not check the return value of those calls, a segfault occurs.  The workaround is simply to add the Intel ICD library path to <code>LD_LIBRARY_PATH</code>, which is most easily accomplished with <code>vglrun&nbsp;-ld</code>.</td>
{% endraw %}

```