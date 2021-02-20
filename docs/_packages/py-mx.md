---
name: "py-mx"
layout: package
next_package: py-mypy
previous_package: py-mpi4py
languages: ['c']
---
## 3.2.8
2 / 254 files match, 1 filtered matches.

 - [mx/Tools/mxTools/mxTools.c](#mxtoolsmxtoolsmxtoolsc)

### mx/Tools/mxTools/mxTools.c

```c

{% raw %}
43 | /* Needed for mxTools_dlopen(); HAVE_DL_LIB is defined by the
44 |    egenix_mx_base.py setup script if the dl library can be
45 |    found. HAVE_DLOPEN is defined by Python's configure script, if
46 |    dlopen() is available. */
47 | #if defined(HAVE_DL_LIB) && !defined(HAVE_DLOPEN)
48 | # define HAVE_DLOPEN 1
2230 | 
2231 | #ifdef HAVE_DLOPEN
2232 | 
2233 | Py_C_Function( mxTools_dlopen,
2234 | 	       "dlopen(libname, mode)\n\n"
2235 | 	       "Load the shared lib libname using the flags given in mode.\n"
2236 | 	       "mode defaults to Python's standard dlopenflags."
2237 | 	       )
2238 | {
2239 |     char *libname;
2240 | #if HAVE_INTERPRETER_DLOPENFLAGS
2241 |     int mode = PyThreadState_GET()->interp->dlopenflags;
2242 | #else
2243 | # ifdef RTLD_NOW
2250 |     
2251 |     Py_Get2Args("s|i", libname, mode);
2252 | 
2253 |     handle = dlopen(libname, mode);
2254 |     if (handle == NULL) {
2255 | 	/* Get error information */
2256 | 	const char *error = dlerror();
2257 | 	if (error == NULL)
2258 | 	    error = "unknown dlopen() error";
2259 | 	Py_Error(PyExc_OSError, error);
2260 |     }
2662 |     Py_MethodListEntry("setproctitle", mxTools_setproctitle),
2663 | #endif
2664 | #ifdef HAVE_DLOPEN
2665 |     Py_MethodListEntry("dlopen",  mxTools_dlopen),
2666 | #endif
2667 | #ifdef INCLUDE_FUNSTUFF
{% endraw %}

```