---
name: "tcl-tclxml"
layout: package
next_package: argobots
previous_package: sbml
languages: []
---
## 3.2
2 / 175 files match

 - [autom4te.cache/output.0](#autom4tecacheoutput0)
 - [tclconfig/tcl.m4](#tclconfigtclm4)

### autom4te.cache/output.0

```

{% raw %}
7377 |     { echo "$as_me:$LINENO: checking for dlopen in -ldl" >&5
7378 | echo $ECHO_N "checking for dlopen in -ldl... $ECHO_C" >&6; }
7379 | if test "${ac_cv_lib_dl_dlopen+set}" = set; then
7397 | char dlopen ();
7401 | return dlopen ();
7424 |   ac_cv_lib_dl_dlopen=yes
7429 | 	ac_cv_lib_dl_dlopen=no
7436 | { echo "$as_me:$LINENO: result: $ac_cv_lib_dl_dlopen" >&5
7437 | echo "${ECHO_T}$ac_cv_lib_dl_dlopen" >&6; }
7438 | if test $ac_cv_lib_dl_dlopen = yes; then
8972 | 	    # dlopen is in -lc on QNX
8978 | 	    # Note, dlopen is available only on SCO 3.2.5 and greater. However,
{% endraw %}

```
### tclconfig/tcl.m4

```

{% raw %}
963 |     AC_CHECK_LIB(dl, dlopen, have_dl=yes, have_dl=no)
1789 | 	    # dlopen is in -lc on QNX
1795 | 	    # Note, dlopen is available only on SCO 3.2.5 and greater. However,
{% endraw %}

```