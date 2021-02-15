---
name: "py-mx"
layout: package
next_package: texinfo
previous_package: diffutils
languages: ['cpp', 'python']
---
## 3.2.8
2 / 254 files match

 - [egenix_mx_base.py](#egenix_mx_basepy)
 - [mx/Tools/mxTools/mxTools.c](#mxtoolsmxtoolsmxtoolsc)

### egenix_mx_base.py

```python

{% raw %}
274 |         # The optional mx.Tools.dlopen() function needs the dl lib in
{% endraw %}

```
### mx/Tools/mxTools/mxTools.c

```cpp

{% raw %}
43 | /* Needed for mxTools_dlopen(); HAVE_DL_LIB is defined by the
45 |    found. HAVE_DLOPEN is defined by Python's configure script, if
46 |    dlopen() is available. */
47 | #if defined(HAVE_DL_LIB) && !defined(HAVE_DLOPEN)
48 | # define HAVE_DLOPEN 1
50 | #ifdef HAVE_DLOPEN
141 | #ifdef HAVE_DLOPEN
2231 | #ifdef HAVE_DLOPEN
2233 | Py_C_Function( mxTools_dlopen,
2234 | 	       "dlopen(libname, mode)\n\n"
2236 | 	       "mode defaults to Python's standard dlopenflags."
2240 | #if HAVE_INTERPRETER_DLOPENFLAGS
2241 |     int mode = PyThreadState_GET()->interp->dlopenflags;
2253 |     handle = dlopen(libname, mode);
2258 | 	    error = "unknown dlopen() error";
2664 | #ifdef HAVE_DLOPEN
2665 |     Py_MethodListEntry("dlopen",  mxTools_dlopen),
2732 |     /* dlopen() mode flags */
{% endraw %}

```