---
name: "py-mx"
layout: package
next_package: texinfo
previous_package: diffutils
languages: ['c']
---
## 3.2.8
2 / 254 files match

 - [mx/Tools/mxTools/mxTools.c](#mxtoolsmxtoolsmxtoolsc)

### mx/Tools/mxTools/mxTools.c

```c

{% raw %}
46 |    dlopen() is available. */
2233 | Py_C_Function( mxTools_dlopen,
2234 | 	       "dlopen(libname, mode)\n\n"
2236 | 	       "mode defaults to Python's standard dlopenflags."
2241 |     int mode = PyThreadState_GET()->interp->dlopenflags;
2253 |     handle = dlopen(libname, mode);
2258 | 	    error = "unknown dlopen() error";
2665 |     Py_MethodListEntry("dlopen",  mxTools_dlopen),
{% endraw %}

```