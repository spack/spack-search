---
name: "slurm"
layout: package
next_package: libestr
previous_package: libsamplerate
languages: ['cpp', 'bash']
---
## 18-08-9-1
52 / 2484 files match

 - [src/common/xlua.c](#srccommonxluac)
 - [src/common/xlua.h](#srccommonxluah)
 - [src/common/plugin.c](#srccommonpluginc)
 - [src/common/plugstack.c](#srccommonplugstackc)
 - [src/plugins/job_submit/lua/job_submit_lua.c](#srcpluginsjob_submitluajob_submit_luac)
 - [src/plugins/switch/nrt/nrt.c](#srcpluginsswitchnrtnrtc)
 - [src/plugins/switch/nrt/libpermapi/shr_64.c](#srcpluginsswitchnrtlibpermapishr_64c)
 - [src/plugins/mpi/pmi2/setup.c](#srcpluginsmpipmi2setupc)
 - [src/plugins/mpi/pmix/mpi_pmix.c](#srcpluginsmpipmixmpi_pmixc)
 - [src/plugins/mpi/pmix/pmixp_dconn_ucx.c](#srcpluginsmpipmixpmixp_dconn_ucxc)
 - [src/plugins/proctrack/sgi_job/proctrack_sgi_job.c](#srcpluginsproctracksgi_jobproctrack_sgi_jobc)
 - [src/plugins/proctrack/sgi_job/Makefile.am](#srcpluginsproctracksgi_jobmakefileam)
 - [src/plugins/proctrack/sgi_job/Makefile.in](#srcpluginsproctracksgi_jobmakefilein)
 - [src/plugins/proctrack/lua/proctrack_lua.c](#srcpluginsproctrackluaproctrack_luac)
 - [src/slurmctld/controller.c](#srcslurmctldcontrollerc)
 - [auxdir/libtool.m4](#auxdirlibtoolm4)
 - [auxdir/ltoptions.m4](#auxdirltoptionsm4)
 - [auxdir/ltmain.sh](#auxdirltmainsh)
 - [auxdir/x_ac_dlfcn.m4](#auxdirx_ac_dlfcnm4)
 - [contribs/pam_slurm_adopt/helper.c](#contribspam_slurm_adopthelperc)
 - [contribs/pam/pam_slurm.c](#contribspampam_slurmc)
 - [doc/html/preemption_plugins.shtml](#dochtmlpreemption_pluginsshtml)
 - [doc/html/acct_gather_profile_plugins.shtml](#dochtmlacct_gather_profile_pluginsshtml)
 - [doc/html/mcs_plugins.shtml](#dochtmlmcs_pluginsshtml)
 - [doc/html/core_spec_plugins.shtml](#dochtmlcore_spec_pluginsshtml)
 - [doc/html/selectplugins.shtml](#dochtmlselectpluginsshtml)
 - [doc/html/accounting_storageplugins.shtml](#dochtmlaccounting_storagepluginsshtml)
 - [doc/html/taskplugins.shtml](#dochtmltaskpluginsshtml)
 - [doc/html/node_features_plugins.shtml](#dochtmlnode_features_pluginsshtml)
 - [doc/html/checkpoint_plugins.shtml](#dochtmlcheckpoint_pluginsshtml)
 - [doc/html/slurmctld_plugstack.shtml](#dochtmlslurmctld_plugstackshtml)
 - [doc/html/switchplugins.shtml](#dochtmlswitchpluginsshtml)
 - [doc/html/acct_gather_energy_plugins.shtml](#dochtmlacct_gather_energy_pluginsshtml)
 - [doc/html/proctrack_plugins.shtml](#dochtmlproctrack_pluginsshtml)
 - [doc/html/jobacct_gatherplugins.shtml](#dochtmljobacct_gatherpluginsshtml)
 - [doc/html/topology_plugin.shtml](#dochtmltopology_pluginshtml)
 - [doc/html/launch_plugins.shtml](#dochtmllaunch_pluginsshtml)
 - [doc/html/schedplugins.shtml](#dochtmlschedpluginsshtml)
 - [doc/html/route_plugin.shtml](#dochtmlroute_pluginshtml)
 - [doc/html/job_submit_plugins.shtml](#dochtmljob_submit_pluginsshtml)
 - [doc/html/faq.shtml](#dochtmlfaqshtml)
 - [doc/html/job_container_plugins.shtml](#dochtmljob_container_pluginsshtml)
 - [doc/html/jobcompplugins.shtml](#dochtmljobcomppluginsshtml)
 - [doc/html/mpiplugins.shtml](#dochtmlmpipluginsshtml)
 - [doc/html/plugins.shtml](#dochtmlpluginsshtml)
 - [doc/html/bb_plugins.shtml](#dochtmlbb_pluginsshtml)
 - [doc/html/gres_plugins.shtml](#dochtmlgres_pluginsshtml)
 - [doc/html/crypto_plugins.shtml](#dochtmlcrypto_pluginsshtml)
 - [doc/html/power_plugins.shtml](#dochtmlpower_pluginsshtml)
 - [doc/html/priority_plugins.shtml](#dochtmlpriority_pluginsshtml)
 - [doc/html/authplugins.shtml](#dochtmlauthpluginsshtml)
 - [doc/html/ext_sensorsplugins.shtml](#dochtmlext_sensorspluginsshtml)

### src/common/xlua.c

```cpp

{% raw %}
44 |  *  Common function to dlopen() the appropriate Lua libraries, and
47 | int xlua_dlopen(void)
50 | 	 *  Need to dlopen() liblua.so with RTLD_GLOBAL in order to
56 | 	} else if (!dlopen("liblua.so",       RTLD_NOW | RTLD_GLOBAL) &&
58 | 		   !dlopen("liblua-5.3.so",   RTLD_NOW | RTLD_GLOBAL) &&
59 | 		   !dlopen("liblua5.3.so",    RTLD_NOW | RTLD_GLOBAL) &&
60 | 		   !dlopen("liblua5.3.so.0",  RTLD_NOW | RTLD_GLOBAL) &&
61 | 		   !dlopen("liblua.so.5.3",   RTLD_NOW | RTLD_GLOBAL)
63 | 		   !dlopen("liblua-5.2.so",   RTLD_NOW | RTLD_GLOBAL) &&
64 | 		   !dlopen("liblua5.2.so",    RTLD_NOW | RTLD_GLOBAL) &&
65 | 		   !dlopen("liblua5.2.so.0",  RTLD_NOW | RTLD_GLOBAL) &&
66 | 		   !dlopen("liblua.so.5.2",   RTLD_NOW | RTLD_GLOBAL)
68 | 		   !dlopen("liblua-5.1.so",   RTLD_NOW | RTLD_GLOBAL) &&
69 | 		   !dlopen("liblua5.1.so",    RTLD_NOW | RTLD_GLOBAL) &&
70 | 		   !dlopen("liblua5.1.so.0",  RTLD_NOW | RTLD_GLOBAL) &&
71 | 		   !dlopen("liblua.so.5.1",   RTLD_NOW | RTLD_GLOBAL)
{% endraw %}

```
### src/common/xlua.h

```cpp

{% raw %}
46 | int xlua_dlopen();
{% endraw %}

```
### src/common/plugin.c

```cpp

{% raw %}
86 | 		case EPLUGIN_DLOPEN_FAILED:
87 | 			return ("Dlopen of plugin file failed");
111 | 	plug = dlopen( fq_path, RTLD_LAZY );
113 | 		debug3( "plugin_peek: dlopen(%s): %s", fq_path, _dlerror() );
176 | 	plug = dlopen(fq_path, RTLD_LAZY);
178 | 		error("plugin_load_from_file: dlopen(%s): %s",
181 | 		return EPLUGIN_DLOPEN_FAILED;
292 |  * Must test plugin validity before doing dlopen() and dlsym()
{% endraw %}

```
### src/common/plugstack.c

```cpp

{% raw %}
2315 | 	void *h = dlopen(NULL, 0);
2332 | 	void *h = dlopen(NULL, 0);
2349 | 	void *h = dlopen(NULL, 0);
{% endraw %}

```
### src/plugins/job_submit/lua/job_submit_lua.c

```cpp

{% raw %}
1743 | 	 * Need to dlopen() the Lua library to ensure plugins see
1746 | 	if ((rc = xlua_dlopen()) != SLURM_SUCCESS)
{% endraw %}

```
### src/plugins/switch/nrt/nrt.c

```cpp

{% raw %}
91 | 		nrt_handle = dlopen(LIBNRT_SO, RTLD_LAZY);
{% endraw %}

```
### src/plugins/switch/nrt/libpermapi/shr_64.c

```cpp

{% raw %}
1509 | 	my_handle = dlopen(MYSELF_SO, RTLD_LAZY | RTLD_GLOBAL | RTLD_DEEPBIND);
{% endraw %}

```
### src/plugins/mpi/pmi2/setup.c

```cpp

{% raw %}
619 | 	handle = dlopen(NULL, RTLD_LAZY);
621 | 		error("mpi/pmi2: failed to dlopen()");
{% endraw %}

```
### src/plugins/mpi/pmix/mpi_pmix.c

```cpp

{% raw %}
108 | 	lib_plug = dlopen(full_path, RTLD_LAZY | RTLD_GLOBAL);
{% endraw %}

```
### src/plugins/mpi/pmix/pmixp_dconn_ucx.c

```cpp

{% raw %}
170 | 	_ucx_lib_handler = dlopen(full_path, RTLD_LAZY | RTLD_GLOBAL);
180 | 	_ucx_lib_handler = dlopen("libucp.so", RTLD_LAZY | RTLD_GLOBAL);
{% endraw %}

```
### src/plugins/proctrack/sgi_job/proctrack_sgi_job.c

```cpp

{% raw %}
97 | 	/*  We dlopen() libjob.so instead of directly linking to it
99 | 	 *   conflict with symbols in slurmd. dlopening the library
102 | 	if ((libjob_handle = dlopen ("libjob.so", RTLD_LAZY)) == NULL) {
{% endraw %}

```
### src/plugins/proctrack/sgi_job/Makefile.am

```

{% raw %}
12 | # Don't need to add -ljob because we dlopen the .so to avoid
{% endraw %}

```
### src/plugins/proctrack/sgi_job/Makefile.in

```

{% raw %}
839 | # Don't need to add -ljob because we dlopen the .so to avoid
{% endraw %}

```
### src/plugins/proctrack/lua/proctrack_lua.c

```cpp

{% raw %}
254 | 	 * Need to dlopen() the Lua library to ensure plugins see
257 | 	if ((rc = xlua_dlopen()) != SLURM_SUCCESS)
{% endraw %}

```
### src/slurmctld/controller.c

```cpp

{% raw %}
150 |  * On some systems dlopen() will generate a small number of "definitely
{% endraw %}

```
### auxdir/libtool.m4

```

{% raw %}
1820 | # _LT_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
1823 | m4_defun([_LT_TRY_DLOPEN_SELF],
1881 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
1914 | ])# _LT_TRY_DLOPEN_SELF
1917 | # LT_SYS_DLOPEN_SELF
1919 | AC_DEFUN([LT_SYS_DLOPEN_SELF],
1921 | if test yes != "$enable_dlopen"; then
1922 |   enable_dlopen=unknown
1923 |   enable_dlopen_self=unknown
1924 |   enable_dlopen_self_static=unknown
1926 |   lt_cv_dlopen=no
1927 |   lt_cv_dlopen_libs=
1931 |     lt_cv_dlopen=load_add_on
1932 |     lt_cv_dlopen_libs=
1933 |     lt_cv_dlopen_self=yes
1937 |     lt_cv_dlopen=LoadLibrary
1938 |     lt_cv_dlopen_libs=
1942 |     lt_cv_dlopen=dlopen
1943 |     lt_cv_dlopen_libs=
1948 |     AC_CHECK_LIB([dl], [dlopen],
1949 | 		[lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl],[
1950 |     lt_cv_dlopen=dyld
1951 |     lt_cv_dlopen_libs=
1952 |     lt_cv_dlopen_self=yes
1959 |     lt_cv_dlopen=dlopen
1960 |     lt_cv_dlopen_libs=
1961 |     lt_cv_dlopen_self=no
1966 | 	  [lt_cv_dlopen=shl_load],
1968 | 	    [lt_cv_dlopen=shl_load lt_cv_dlopen_libs=-ldld],
1969 | 	[AC_CHECK_FUNC([dlopen],
1970 | 	      [lt_cv_dlopen=dlopen],
1971 | 	  [AC_CHECK_LIB([dl], [dlopen],
1972 | 		[lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl],
1973 | 	    [AC_CHECK_LIB([svld], [dlopen],
1974 | 		  [lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-lsvld],
1976 | 		    [lt_cv_dlopen=dld_link lt_cv_dlopen_libs=-ldld])
1985 |   if test no = "$lt_cv_dlopen"; then
1986 |     enable_dlopen=no
1988 |     enable_dlopen=yes
1991 |   case $lt_cv_dlopen in
1992 |   dlopen)
2000 |     LIBS="$lt_cv_dlopen_libs $LIBS"
2002 |     AC_CACHE_CHECK([whether a program can dlopen itself],
2003 | 	  lt_cv_dlopen_self, [dnl
2004 | 	  _LT_TRY_DLOPEN_SELF(
2005 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
2006 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
2009 |     if test yes = "$lt_cv_dlopen_self"; then
2011 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
2012 | 	  lt_cv_dlopen_self_static, [dnl
2013 | 	  _LT_TRY_DLOPEN_SELF(
2014 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
2015 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
2025 |   case $lt_cv_dlopen_self in
2026 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
2027 |   *) enable_dlopen_self=unknown ;;
2030 |   case $lt_cv_dlopen_self_static in
2031 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
2032 |   *) enable_dlopen_self_static=unknown ;;
2035 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
2036 | 	 [Whether dlopen is supported])
2037 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
2038 | 	 [Whether dlopen of programs is supported])
2039 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
2040 | 	 [Whether dlopen of statically linked programs is supported])
2041 | ])# LT_SYS_DLOPEN_SELF
2044 | AU_ALIAS([AC_LIBTOOL_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF])
2046 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [])
6147 |     [Compiler flag to allow reflexive dlopens])
6260 |   LT_SYS_DLOPEN_SELF
{% endraw %}

```
### auxdir/ltoptions.m4

```

{% raw %}
70 |   _LT_UNLESS_OPTIONS([LT_INIT], [dlopen], [enable_dlopen=no
107 | # dlopen
109 | LT_OPTION_DEFINE([LT_INIT], [dlopen], [enable_dlopen=yes
112 | AU_DEFUN([AC_LIBTOOL_DLOPEN],
113 | [_LT_SET_OPTION([LT_INIT], [dlopen])
116 | put the 'dlopen' option into LT_INIT's first parameter.])
120 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN], [])
{% endraw %}

```
### auxdir/ltmain.sh

```bash

{% raw %}
2335 |     opt_dlopen=
2408 |         --dlopen|-dlopen)
2409 |                         opt_dlopen="${opt_dlopen+$opt_dlopen
2532 |       # Only execute mode is allowed to have -dlopen flags.
2533 |       if test -n "$opt_dlopen" && test execute != "$opt_mode"; then
2534 |         func_error "unrecognized option '-dlopen'"
3760 |   -dlopen FILE      add the directory containing FILE to the library path
3762 | This mode sets the library path environment variable according to '-dlopen'
3817 |   -dlopen FILE      '-dlpreopen' FILE if it cannot be dlopened at runtime
3826 |   -module           build a library that can dlopened
3934 |     # Handle -dlopen flags immediately.
3935 |     for file in $opt_dlopen; do
3954 | 	# Skip this library if it cannot be dlopened.
3981 | 	func_warning "'-dlopen' is ignored for non-libtool libraries and objects"
6674 | 	    dlopen_self=$dlopen_self_static
6680 | 	    dlopen_self=$dlopen_self_static
6686 | 	    dlopen_self=$dlopen_self_static
6744 | 	    elif test dlfiles = "$prev" && test yes != "$dlopen_self"; then
6834 | 		    if test yes = "$build_libtool_libs" && test yes = "$dlopen_support"; then
7001 |       -dlopen)
7439 | 	      if test yes = "$build_libtool_libs" && test yes = "$dlopen_support"; then
7507 | 	  # This library was specified with -dlopen.
7627 | 	    func_fatal_help "libraries can '-dlopen' only libtool libraries: $file"
7638 | 	passes="conv scan dlopen dlpreopen link"
7664 | 	dlopen) libs=$dlfiles ;;
7695 |       if test dlopen = "$pass"; then
7915 | 	    if test dlpreopen = "$pass" || test yes != "$dlopen_support" || test no = "$build_libtool_libs"; then
7916 | 	      # If there is no dlopen support or we're linking statically,
7944 | 	dlopen=
7974 | 	  test -n "$dlopen" && func_append dlfiles " $dlopen"
8020 | 	# This library was specified with -dlopen.
8021 | 	if test dlopen = "$pass"; then
8023 | 	    && func_fatal_error "cannot -dlopen a convenience library: '$lib'"
8025 | 	     test yes != "$dlopen_support" ||
8028 | 	    # If there is no dlname, no dlopen support or we're linking
8037 | 	fi # $pass = dlopen
8093 | 	      # (otherwise, the dlopen module name will be incorrect).  We do
8095 | 	      # We recover the dlopen module name by 'saving' the la file
8119 | 	      # Otherwise, use the dlname, so that lt_dlopen finds it.
8248 | 	  # systems (darwin).  Don't bleat about dlopened modules though!
8249 | 	  dlopenmodule=
8252 | 	      dlopenmodule=$dlpremoduletest
8256 | 	  if test -z "$dlopenmodule" && test yes = "$shouldnotlink" && test link = "$pass"; then
8353 | 		    # if the lib is a (non-dlopened) module then we cannot
8357 | 		      if test "X$dlopenmodule" != "X$lib"; then
8509 | 	      echo "*** a static module, that should work as long as the dlopening application"
8510 | 	      echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
8654 |       if test dlopen != "$pass"; then
8784 | 	func_warning "'-dlopen' is ignored for archives"
8851 | 	|| func_warning "'-dlopen self' is ignored for libtool libraries"
9548 | 	    echo "*** a static module, that should work as long as the dlopening"
9549 | 	    echo "*** application is linked with the -dlopen flag."
9567 | 	    echo "*** or is declared to -dlopen it."
10179 | 	func_warning "'-dlopen' is ignored for objects"
10299 | 	&& test unknown,unknown,unknown = "$dlopen_support,$dlopen_self,$dlopen_self_static" \
10300 | 	&& func_warning "'LT_INIT([dlopen])' not used. Assuming no dlopen support."
10981 | # The name that we can dlopen(3).
11010 | # Files to dlopen/dlpreopen
11011 | dlopen='$dlfiles'
{% endraw %}

```
### auxdir/x_ac_dlfcn.m4

```

{% raw %}
3 |   AC_MSG_CHECKING([library containing dlopen])
4 |   AC_CHECK_LIB([], [dlopen], [ac_have_dlopen=yes; DL_LIBS=""],
5 |     [AC_CHECK_LIB([dl], [dlopen], [ac_have_dlopen=yes; DL_LIBS="-ldl"],
6 |       [AC_CHECK_LIB([svdl], [dlopen], [ac_have_dlopen=yes; DL_LIBS="-lsvdl"])])])
{% endraw %}

```
### contribs/pam_slurm_adopt/helper.c

```cpp

{% raw %}
75 |  *  We open libslurm.so via dlopen () in order to pass the
167 | 	} else if ((slurm_h = dlopen(libslurmname, RTLD_NOW|RTLD_GLOBAL))) {
170 | 		_log_msg (LOG_INFO, "Unable to dlopen %s: %s\n",
177 | 	} else if ((slurm_h = dlopen(libslurmname, RTLD_NOW|RTLD_GLOBAL))) {
180 | 		_log_msg (LOG_INFO, "Unable to dlopen %s: %s\n",
184 | 	if (!(slurm_h = dlopen("libslurm.so", RTLD_NOW|RTLD_GLOBAL))) {
185 | 		_log_msg (LOG_ERR, "Unable to dlopen libslurm.so: %s\n",
{% endraw %}

```
### contribs/pam/pam_slurm.c

```cpp

{% raw %}
79 |  *  We open libslurm.so via dlopen () in order to pass the
438 | 	} else if ((slurm_h = dlopen(libslurmname, RTLD_NOW|RTLD_GLOBAL))) {
441 | 		_log_msg (LOG_INFO, "Unable to dlopen %s: %s\n",
448 | 	} else if ((slurm_h = dlopen(libslurmname, RTLD_NOW|RTLD_GLOBAL))) {
451 | 		_log_msg (LOG_INFO, "Unable to dlopen %s: %s\n",
455 | 	if (!(slurm_h = dlopen("libslurm.so", RTLD_NOW|RTLD_GLOBAL))) {
456 | 		_log_msg (LOG_ERR, "Unable to dlopen libslurm.so: %s\n",
{% endraw %}

```
### doc/html/preemption_plugins.shtml

```

{% raw %}
62 | described in the <span class="commandline">dlopen (3)</span> system library.
{% endraw %}

```
### doc/html/acct_gather_profile_plugins.shtml

```

{% raw %}
102 | described in the <span class="commandline">dlopen (3)</span> system library.
{% endraw %}

```
### doc/html/mcs_plugins.shtml

```

{% raw %}
63 | described in the <span class="commandline">dlopen (3)</span> system library.
{% endraw %}

```
### doc/html/core_spec_plugins.shtml

```

{% raw %}
65 | described in the <span class="commandline">dlopen (3)</span> system library.
{% endraw %}

```
### doc/html/selectplugins.shtml

```

{% raw %}
115 | described in the <span class="commandline">dlopen (3)</span> system library.
{% endraw %}

```
### doc/html/accounting_storageplugins.shtml

```

{% raw %}
73 | described in the <span class="commandline">dlopen (3)</span> system library.
{% endraw %}

```
### doc/html/taskplugins.shtml

```

{% raw %}
67 | described in the <span class="commandline">dlopen (3)</span> system library.
{% endraw %}

```
### doc/html/node_features_plugins.shtml

```

{% raw %}
56 | described in the <span class="commandline">dlopen (3)</span> system library.
{% endraw %}

```
### doc/html/checkpoint_plugins.shtml

```

{% raw %}
77 | described in the <span class="commandline">dlopen (3)</span> system library.
{% endraw %}

```
### doc/html/slurmctld_plugstack.shtml

```

{% raw %}
59 | described in the <span class="commandline">dlopen (3)</span> system library.
{% endraw %}

```
### doc/html/switchplugins.shtml

```

{% raw %}
88 | described in the <span class="commandline">dlopen (3)</span> system library.
{% endraw %}

```
### doc/html/acct_gather_energy_plugins.shtml

```

{% raw %}
65 | described in the <span class="commandline">dlopen (3)</span> system library.
{% endraw %}

```
### doc/html/proctrack_plugins.shtml

```

{% raw %}
91 | described in the <span class="commandline">dlopen (3)</span> system library.
{% endraw %}

```
### doc/html/jobacct_gatherplugins.shtml

```

{% raw %}
68 | described in the <span class="commandline">dlopen (3)</span> system library.
{% endraw %}

```
### doc/html/topology_plugin.shtml

```

{% raw %}
81 | described in the <span class="commandline">dlopen (3)</span> system library.
{% endraw %}

```
### doc/html/launch_plugins.shtml

```

{% raw %}
51 | described in the <span class="commandline">dlopen (3)</span> system library.
{% endraw %}

```
### doc/html/schedplugins.shtml

```

{% raw %}
84 | described in the <span class="commandline">dlopen (3)</span> system library.
{% endraw %}

```
### doc/html/route_plugin.shtml

```

{% raw %}
74 | described in the <span class="commandline">dlopen (3)</span> system library.
{% endraw %}

```
### doc/html/job_submit_plugins.shtml

```

{% raw %}
72 | described in the <span class="commandline">dlopen (3)</span> system library.
{% endraw %}

```
### doc/html/faq.shtml

```

{% raw %}
2283 | When buffer caches are flushed during a dlopen (used by Slurm to load its
{% endraw %}

```
### doc/html/job_container_plugins.shtml

```

{% raw %}
79 | described in the <span class="commandline">dlopen (3)</span> system library.
{% endraw %}

```
### doc/html/jobcompplugins.shtml

```

{% raw %}
78 | described in the <span class="commandline">dlopen (3)</span> system library.
{% endraw %}

```
### doc/html/mpiplugins.shtml

```

{% raw %}
92 | described in the <span class="commandline">dlopen (3)</span> system library.
{% endraw %}

```
### doc/html/plugins.shtml

```

{% raw %}
73 | described in the <span class="commandline">dlopen (3)</span> system library.
{% endraw %}

```
### doc/html/bb_plugins.shtml

```

{% raw %}
57 | described in the <span class="commandline">dlopen (3)</span> system library.
{% endraw %}

```
### doc/html/gres_plugins.shtml

```

{% raw %}
62 | described in the <span class="commandline">dlopen (3)</span> system library.
{% endraw %}

```
### doc/html/crypto_plugins.shtml

```

{% raw %}
78 | described in the <span class="commandline">dlopen (3)</span> system library.
{% endraw %}

```
### doc/html/power_plugins.shtml

```

{% raw %}
60 | described in the <span class="commandline">dlopen (3)</span> system library.
{% endraw %}

```
### doc/html/priority_plugins.shtml

```

{% raw %}
96 | described in the <span class="commandline">dlopen (3)</span> system library.
{% endraw %}

```
### doc/html/authplugins.shtml

```

{% raw %}
89 | described in the <span class="commandline">dlopen (3)</span> system library.
{% endraw %}

```
### doc/html/ext_sensorsplugins.shtml

```

{% raw %}
61 | described in the <span class="commandline">dlopen (3)</span> system library.
{% endraw %}

```