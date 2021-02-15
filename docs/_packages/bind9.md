---
name: "bind9"
layout: package
next_package: aria2
previous_package: py-setuptools
languages: ['yaml', 'cpp', 'bash']
---
## 9_14_6
57 / 3884 files match

 - [HISTORY.md](#historymd)
 - [config.h.in](#confighin)
 - [configure.ac](#configureac)
 - [config.h.win32](#confighwin32)
 - [ltmain.sh](#ltmainsh)
 - [.gitlab-ci.yml](#gitlab-ciyml)
 - [bin/named/main.c](#binnamedmainc)
 - [bin/named/Makefile.in](#binnamedmakefilein)
 - [bin/named/include/dlz/dlz_dlopen_driver.h](#binnamedincludedlzdlz_dlopen_driverh)
 - [bin/named/unix/dlz_dlopen_driver.c](#binnamedunixdlz_dlopen_driverc)
 - [bin/named/unix/Makefile.in](#binnamedunixmakefilein)
 - [bin/named/win32/named.vcxproj.filters.in](#binnamedwin32namedvcxprojfiltersin)
 - [bin/named/win32/named.vcxproj.in](#binnamedwin32namedvcxprojin)
 - [bin/named/win32/dlz_dlopen_driver.c](#binnamedwin32dlz_dlopen_driverc)
 - [bin/tests/.gitignore](#bintestsgitignore)
 - [bin/tests/system/feature-test.c](#bintestssystemfeature-testc)
 - [bin/tests/system/filter-aaaa/prereq.sh](#bintestssystemfilter-aaaaprereqsh)
 - [bin/tests/system/rpz/dnsrps.c](#bintestssystemrpzdnsrpsc)
 - [bin/tests/system/checkconf/altdlz.conf](#bintestssystemcheckconfaltdlzconf)
 - [bin/tests/system/dyndb/prereq.sh](#bintestssystemdyndbprereqsh)
 - [bin/tests/system/dyndb/driver/driver.c](#bintestssystemdyndbdriverdriverc)
 - [bin/tests/system/dlzexternal/driver.h](#bintestssystemdlzexternaldriverh)
 - [bin/tests/system/dlzexternal/prereq.sh](#bintestssystemdlzexternalprereqsh)
 - [bin/tests/system/dlzexternal/driver.c](#bintestssystemdlzexternaldriverc)
 - [bin/tests/system/dlzexternal/ns1/dlzs.conf.in](#bintestssystemdlzexternalns1dlzsconfin)
 - [lib/ns/hooks.c](#libnshooksc)
 - [lib/ns/include/ns/hooks.h](#libnsincludenshooksh)
 - [lib/isc/unix/pk11_api.c](#libiscunixpk11_apic)
 - [lib/dns/dyndb.c](#libdnsdyndbc)
 - [lib/dns/include/dns/librpz.h](#libdnsincludednslibrpzh)
 - [lib/dns/include/dns/dlz_dlopen.h](#libdnsincludednsdlz_dlopenh)
 - [lib/dns/include/dns/dyndb.h](#libdnsincludednsdyndbh)
 - [lib/dns/include/dns/dnsrps.h](#libdnsincludednsdnsrpsh)
 - [lib/dns/include/dns/Makefile.in](#libdnsincludednsmakefilein)
 - [m4/libtool.m4](#m4libtoolm4)
 - [m4/ltoptions.m4](#m4ltoptionsm4)
 - [contrib/dlz/example/dlz_example.c](#contribdlzexampledlz_examplec)
 - [contrib/dlz/example/named.conf](#contribdlzexamplenamedconf)
 - [contrib/dlz/drivers/rules.in](#contribdlzdriversrulesin)
 - [contrib/dlz/modules/include/dlz_minimal.h](#contribdlzmodulesincludedlz_minimalh)
 - [contrib/dlz/modules/ldap/dlz_ldap_dynamic.c](#contribdlzmodulesldapdlz_ldap_dynamicc)
 - [contrib/dlz/modules/ldap/testing/named.conf](#contribdlzmodulesldaptestingnamedconf)
 - [contrib/dlz/modules/sqlite3/dlz_sqlite3_dynamic.c](#contribdlzmodulessqlite3dlz_sqlite3_dynamicc)
 - [contrib/dlz/modules/sqlite3/testing/named.conf](#contribdlzmodulessqlite3testingnamedconf)
 - [contrib/dlz/modules/mysqldyn/dlz_mysqldyn_mod.c](#contribdlzmodulesmysqldyndlz_mysqldyn_modc)
 - [contrib/dlz/modules/mysqldyn/testing/named.conf](#contribdlzmodulesmysqldyntestingnamedconf)
 - [contrib/dlz/modules/perl/dlz_perl_driver.c](#contribdlzmodulesperldlz_perl_driverc)
 - [contrib/dlz/modules/perl/testing/named.conf](#contribdlzmodulesperltestingnamedconf)
 - [contrib/dlz/modules/filesystem/dlz_filesystem_dynamic.c](#contribdlzmodulesfilesystemdlz_filesystem_dynamicc)
 - [contrib/dlz/modules/wildcard/dlz_wildcard_dynamic.c](#contribdlzmoduleswildcarddlz_wildcard_dynamicc)
 - [contrib/dlz/modules/wildcard/testing/named.conf](#contribdlzmoduleswildcardtestingnamedconf)
 - [contrib/dlz/modules/mysql/dlz_mysql_dynamic.c](#contribdlzmodulesmysqldlz_mysql_dynamicc)
 - [contrib/dlz/modules/mysql/testing/named.conf](#contribdlzmodulesmysqltestingnamedconf)
 - [contrib/dlz/modules/bdbhpt/dlz_bdbhpt_dynamic.c](#contribdlzmodulesbdbhptdlz_bdbhpt_dynamicc)
 - [contrib/dlz/modules/bdbhpt/README.md](#contribdlzmodulesbdbhptreadmemd)
 - [contrib/dlz/modules/bdbhpt/testing/named.conf](#contribdlzmodulesbdbhpttestingnamedconf)
 - [doc/arm/dlz.xml](#docarmdlzxml)

### HISTORY.md

```

{% raw %}
330 | - The DLZ "dlopen" driver is now built by default.
332 |   for the DLZ "dlopen" driver.
{% endraw %}

```
### config.h.in

```

{% raw %}
11 | /* 0=no DNSRPS 1=static link 2=dlopen() */
83 | /* Define to 1 if you have the `dlopen' function. */
84 | #undef HAVE_DLOPEN
482 | /* Define to allow building of objects for dlopen(). */
483 | #undef ISC_DLZ_DLOPEN
{% endraw %}

```
### configure.ac

```

{% raw %}
2635 | # to build an object that can be dlopen()'ed, but this is necessary
2646 | AC_ARG_WITH([dlopen],
2647 | 	    AS_HELP_STRING([--with-dlopen=ARG],
2649 | 	    [], [with_dlopen="auto"])
2653 | # If PIC is disabled, dlopen must also be
2656 |       [AS_CASE([$with_dlopen],
2657 | 	       [auto],[with_dlopen="no"],
2658 | 	       [yes],[AC_MSG_ERROR([--with-dlopen requires PIC])])])
2660 | AS_CASE([$with_dlopen],
2662 | 	  AC_SEARCH_LIBS([dlopen],[dl])
2663 | 	  AC_CHECK_FUNCS([dlopen dlclose dlsym],
2664 | 			 [with_dlopen="yes"],
2665 | 			 [with_dlopen="no"])
2668 | AS_IF([test "$with_dlopen" = "yes"],
2730 | 	      AC_DEFINE([ISC_DLZ_DLOPEN], [1],
2731 | 			[Define to allow building of objects for dlopen().])
2749 | # modern C compiler.  It is enabled on systems with dlopen() and librpz.so.
2773 | 	      [enable_librpz_dl="$enableval"], [enable_librpz_dl="$with_dlopen"])
2775 | AS_IF([test "$enable_librpz_dl" = "yes" -a "$with_dlopen" = "no"],
2776 |       [AC_MSG_ERROR([DNS Response Policy Service delayed link requires dlopen to be enabled])])
2793 | 	# Add librpz.so to linked libraries if we are not using dlopen()
2799 | 		   [0=no DNSRPS  1=static link  2=dlopen()])
2808 | 	      [AC_MSG_ERROR([dlopen and librpz.so needed for DNSRPS])])
2810 | 	      [AC_MSG_ERROR([dlopen and librpz.so needed for DNSRPS])])
{% endraw %}

```
### config.h.win32

```

{% raw %}
116 |  * Define to 1 if you want to use the DLZ "dlopen" driver
118 |  * LoadLibrary() instead of dlopen()).
120 | #define ISC_DLZ_DLOPEN 1
{% endraw %}

```
### ltmain.sh

```bash

{% raw %}
2262 |     opt_dlopen=
2323 |         --dlopen|-dlopen)
2324 |                         opt_dlopen="${opt_dlopen+$opt_dlopen
2440 |       # Only execute mode is allowed to have -dlopen flags.
2441 |       if test -n "$opt_dlopen" && test execute != "$opt_mode"; then
2442 |         func_error "unrecognized option '-dlopen'"
3668 |   -dlopen FILE      add the directory containing FILE to the library path
3670 | This mode sets the library path environment variable according to '-dlopen'
3725 |   -dlopen FILE      '-dlpreopen' FILE if it cannot be dlopened at runtime
3734 |   -module           build a library that can dlopened
3842 |     # Handle -dlopen flags immediately.
3843 |     for file in $opt_dlopen; do
3862 | 	# Skip this library if it cannot be dlopened.
3889 | 	func_warning "'-dlopen' is ignored for non-libtool libraries and objects"
6582 | 	    dlopen_self=$dlopen_self_static
6588 | 	    dlopen_self=$dlopen_self_static
6594 | 	    dlopen_self=$dlopen_self_static
6652 | 	    elif test dlfiles = "$prev" && test yes != "$dlopen_self"; then
6742 | 		    if test yes = "$build_libtool_libs" && test yes = "$dlopen_support"; then
6909 |       -dlopen)
7343 | 	      if test yes = "$build_libtool_libs" && test yes = "$dlopen_support"; then
7411 | 	  # This library was specified with -dlopen.
7531 | 	    func_fatal_help "libraries can '-dlopen' only libtool libraries: $file"
7542 | 	passes="conv scan dlopen dlpreopen link"
7568 | 	dlopen) libs=$dlfiles ;;
7596 |       if test dlopen = "$pass"; then
7816 | 	    if test dlpreopen = "$pass" || test yes != "$dlopen_support" || test no = "$build_libtool_libs"; then
7817 | 	      # If there is no dlopen support or we're linking statically,
7845 | 	dlopen=
7875 | 	  test -n "$dlopen" && func_append dlfiles " $dlopen"
7921 | 	# This library was specified with -dlopen.
7922 | 	if test dlopen = "$pass"; then
7924 | 	    && func_fatal_error "cannot -dlopen a convenience library: '$lib'"
7926 | 	     test yes != "$dlopen_support" ||
7929 | 	    # If there is no dlname, no dlopen support or we're linking
7938 | 	fi # $pass = dlopen
7994 | 	      # (otherwise, the dlopen module name will be incorrect).  We do
7996 | 	      # We recover the dlopen module name by 'saving' the la file
8020 | 	      # Otherwise, use the dlname, so that lt_dlopen finds it.
8149 | 	  # systems (darwin).  Don't bleat about dlopened modules though!
8150 | 	  dlopenmodule=
8153 | 	      dlopenmodule=$dlpremoduletest
8157 | 	  if test -z "$dlopenmodule" && test yes = "$shouldnotlink" && test link = "$pass"; then
8254 | 		    # if the lib is a (non-dlopened) module then we cannot
8258 | 		      if test "X$dlopenmodule" != "X$lib"; then
8410 | 	      echo "*** a static module, that should work as long as the dlopening application"
8411 | 	      echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
8555 |       if test dlopen != "$pass"; then
8685 | 	func_warning "'-dlopen' is ignored for archives"
8752 | 	|| func_warning "'-dlopen self' is ignored for libtool libraries"
9446 | 	    echo "*** a static module, that should work as long as the dlopening"
9447 | 	    echo "*** application is linked with the -dlopen flag."
9465 | 	    echo "*** or is declared to -dlopen it."
10077 | 	func_warning "'-dlopen' is ignored for objects"
10197 | 	&& test unknown,unknown,unknown = "$dlopen_support,$dlopen_self,$dlopen_self_static" \
10198 | 	&& func_warning "'LT_INIT([dlopen])' not used. Assuming no dlopen support."
10879 | # The name that we can dlopen(3).
10908 | # Files to dlopen/dlpreopen
10909 | dlopen='$dlfiles'
{% endraw %}

```
### .gitlab-ci.yml

```yaml

{% raw %}
624 |     EXTRA_CONFIGURE: "--with-libidn2 --without-libtool --with-dlopen"
{% endraw %}

```
### bin/named/main.c

```cpp

{% raw %}
52 | #include <dlz/dlz_dlopen_driver.h>
1175 | #ifdef ISC_DLZ_DLOPEN
1177 | 	 * Register the DLZ "dlopen" driver.
1179 | 	result = dlz_dlopen_init(named_g_mctx);
1181 | 		named_main_earlyfatal("dlz_dlopen_init() failed: %s",
1255 | #ifdef ISC_DLZ_DLOPEN
1257 | 	 * Unregister "dlopen" DLZ driver.
1259 | 	dlz_dlopen_clear();
{% endraw %}

```
### bin/named/Makefile.in

```

{% raw %}
98 | UOBJS =		unix/os.@O@ unix/dlz_dlopen_driver.@O@
{% endraw %}

```
### bin/named/include/dlz/dlz_dlopen_driver.h

```cpp

{% raw %}
12 | #ifndef DLZ_DLOPEN_DRIVER_H
13 | #define DLZ_DLOPEN_DRIVER_H
16 | dlz_dlopen_init(isc_mem_t *mctx);
19 | dlz_dlopen_clear(void);
{% endraw %}

```
### bin/named/unix/dlz_dlopen_driver.c

```cpp

{% raw %}
25 | #include <dns/dlz_dlopen.h>
34 | #include <dlz/dlz_dlopen_driver.h>
36 | #ifdef ISC_DLZ_DLOPEN
37 | static dns_sdlzimplementation_t *dlz_dlopen = NULL;
40 | typedef struct dlopen_data {
51 | 	dlz_dlopen_version_t *dlz_version;
52 | 	dlz_dlopen_create_t *dlz_create;
53 | 	dlz_dlopen_findzonedb_t *dlz_findzonedb;
54 | 	dlz_dlopen_lookup_t *dlz_lookup;
55 | 	dlz_dlopen_authority_t *dlz_authority;
56 | 	dlz_dlopen_allnodes_t *dlz_allnodes;
57 | 	dlz_dlopen_allowzonexfr_t *dlz_allowzonexfr;
58 | 	dlz_dlopen_newversion_t *dlz_newversion;
59 | 	dlz_dlopen_closeversion_t *dlz_closeversion;
60 | 	dlz_dlopen_configure_t *dlz_configure;
61 | 	dlz_dlopen_ssumatch_t *dlz_ssumatch;
62 | 	dlz_dlopen_addrdataset_t *dlz_addrdataset;
63 | 	dlz_dlopen_subrdataset_t *dlz_subrdataset;
64 | 	dlz_dlopen_delrdataset_t *dlz_delrdataset;
65 | 	dlz_dlopen_destroy_t *dlz_destroy;
66 | } dlopen_data_t;
86 | static void dlopen_log(int level, const char *fmt, ...)
101 | dlopen_dlz_allnodes(const char *zone, void *driverarg, void *dbdata,
104 | 	dlopen_data_t *cd = (dlopen_data_t *) dbdata;
122 | dlopen_dlz_allowzonexfr(void *driverarg, void *dbdata, const char *name,
125 | 	dlopen_data_t *cd = (dlopen_data_t *) dbdata;
142 | dlopen_dlz_authority(const char *zone, void *driverarg, void *dbdata,
145 | 	dlopen_data_t *cd = (dlopen_data_t *) dbdata;
161 | dlopen_dlz_findzonedb(void *driverarg, void *dbdata, const char *name,
165 | 	dlopen_data_t *cd = (dlopen_data_t *) dbdata;
178 | dlopen_dlz_lookup(const char *zone, const char *name, void *driverarg,
183 | 	dlopen_data_t *cd = (dlopen_data_t *) dbdata;
199 | dl_load_symbol(dlopen_data_t *cd, const char *symbol, bool mandatory) {
202 | 		dlopen_log(ISC_LOG_ERROR,
203 | 			   "dlz_dlopen: library '%s' is missing "
210 |  * Called at startup for each dlopen zone in named.conf
213 | dlopen_dlz_create(const char *dlzname, unsigned int argc, char *argv[],
216 | 	dlopen_data_t *cd;
219 | 	int dlopen_flags = 0;
224 | 		dlopen_log(ISC_LOG_ERROR,
225 | 			   "dlz_dlopen driver for '%s' needs a path to "
259 | 	dlopen_flags = RTLD_NOW|RTLD_GLOBAL;
271 | 	dlopen_flags |= RTLD_DEEPBIND;
274 | 	cd->dl_handle = dlopen(cd->dl_path, dlopen_flags);
276 | 		dlopen_log(ISC_LOG_ERROR,
277 | 			   "dlz_dlopen failed to open library '%s' - %s",
284 | 	cd->dlz_version = (dlz_dlopen_version_t *)
286 | 	cd->dlz_create = (dlz_dlopen_create_t *)
288 | 	cd->dlz_lookup = (dlz_dlopen_lookup_t *)
290 | 	cd->dlz_findzonedb = (dlz_dlopen_findzonedb_t *)
303 | 	cd->dlz_allowzonexfr = (dlz_dlopen_allowzonexfr_t *)
305 | 	cd->dlz_allnodes = (dlz_dlopen_allnodes_t *)
308 | 	cd->dlz_authority = (dlz_dlopen_authority_t *)
310 | 	cd->dlz_newversion = (dlz_dlopen_newversion_t *)
312 | 	cd->dlz_closeversion = (dlz_dlopen_closeversion_t *)
315 | 	cd->dlz_configure = (dlz_dlopen_configure_t *)
317 | 	cd->dlz_ssumatch = (dlz_dlopen_ssumatch_t *)
319 | 	cd->dlz_addrdataset = (dlz_dlopen_addrdataset_t *)
321 | 	cd->dlz_subrdataset = (dlz_dlopen_subrdataset_t *)
323 | 	cd->dlz_delrdataset = (dlz_dlopen_delrdataset_t *)
325 | 	cd->dlz_destroy = (dlz_dlopen_destroy_t *)
330 | 	if (cd->version < (DLZ_DLOPEN_VERSION - DLZ_DLOPEN_AGE) ||
331 | 	    cd->version > DLZ_DLOPEN_VERSION)
333 | 		dlopen_log(ISC_LOG_ERROR,
334 | 			   "dlz_dlopen: %s: incorrect driver API version %d, "
336 | 			   cd->dl_path, cd->version, DLZ_DLOPEN_VERSION);
351 | 				"log", dlopen_log,
365 | 	dlopen_log(ISC_LOG_ERROR, "dlz_dlopen of '%s' failed", dlzname);
372 | 	if (dlopen_flags != 0) {
389 | dlopen_dlz_destroy(void *driverarg, void *dbdata) {
390 | 	dlopen_data_t *cd = (dlopen_data_t *) dbdata;
425 | dlopen_dlz_newversion(const char *zone, void *driverarg, void *dbdata,
428 | 	dlopen_data_t *cd = (dlopen_data_t *) dbdata;
446 | dlopen_dlz_closeversion(const char *zone, bool commit,
449 | 	dlopen_data_t *cd = (dlopen_data_t *) dbdata;
467 | dlopen_dlz_configure(dns_view_t *view, dns_dlzdb_t *dlzdb,
470 | 	dlopen_data_t *cd = (dlopen_data_t *) dbdata;
492 | dlopen_dlz_ssumatch(const char *signer, const char *name, const char *tcpaddr,
496 | 	dlopen_data_t *cd = (dlopen_data_t *) dbdata;
517 | dlopen_dlz_addrdataset(const char *name, const char *rdatastr,
520 | 	dlopen_data_t *cd = (dlopen_data_t *) dbdata;
539 | dlopen_dlz_subrdataset(const char *name, const char *rdatastr,
542 | 	dlopen_data_t *cd = (dlopen_data_t *) dbdata;
561 | dlopen_dlz_delrdataset(const char *name, const char *type,
564 | 	dlopen_data_t *cd = (dlopen_data_t *) dbdata;
580 | static dns_sdlzmethods_t dlz_dlopen_methods = {
581 | 	dlopen_dlz_create,
582 | 	dlopen_dlz_destroy,
583 | 	dlopen_dlz_findzonedb,
584 | 	dlopen_dlz_lookup,
585 | 	dlopen_dlz_authority,
586 | 	dlopen_dlz_allnodes,
587 | 	dlopen_dlz_allowzonexfr,
588 | 	dlopen_dlz_newversion,
589 | 	dlopen_dlz_closeversion,
590 | 	dlopen_dlz_configure,
591 | 	dlopen_dlz_ssumatch,
592 | 	dlopen_dlz_addrdataset,
593 | 	dlopen_dlz_subrdataset,
594 | 	dlopen_dlz_delrdataset
602 | dlz_dlopen_init(isc_mem_t *mctx) {
603 | #ifndef ISC_DLZ_DLOPEN
609 | 	dlopen_log(2, "Registering DLZ_dlopen driver");
611 | 	result = dns_sdlzregister("dlopen", &dlz_dlopen_methods, NULL,
615 | 				  mctx, &dlz_dlopen);
633 | dlz_dlopen_clear(void) {
634 | #ifdef ISC_DLZ_DLOPEN
635 | 	dlopen_log(2, "Unregistering DLZ_dlopen driver");
636 | 	if (dlz_dlopen != NULL)
637 | 		dns_sdlzunregister(&dlz_dlopen);
{% endraw %}

```
### bin/named/unix/Makefile.in

```

{% raw %}
22 | OBJS =		os.@O@ dlz_dlopen_driver.@O@
24 | SRCS =		os.c dlz_dlopen_driver.c
{% endraw %}

```
### bin/named/win32/named.vcxproj.filters.in

```

{% raw %}
17 |     <ClCompile Include="dlz_dlopen_driver.c">
{% endraw %}

```
### bin/named/win32/named.vcxproj.in

```

{% raw %}
122 |     <ClCompile Include="dlz_dlopen_driver.c" />
{% endraw %}

```
### bin/named/win32/dlz_dlopen_driver.c

```cpp

{% raw %}
24 | #include <dns/dlz_dlopen.h>
33 | #include <dlz/dlz_dlopen_driver.h>
35 | #ifdef ISC_DLZ_DLOPEN
36 | static dns_sdlzimplementation_t *dlz_dlopen = NULL;
39 | typedef struct dlopen_data {
50 | 	dlz_dlopen_version_t *dlz_version;
51 | 	dlz_dlopen_create_t *dlz_create;
52 | 	dlz_dlopen_findzonedb_t *dlz_findzonedb;
53 | 	dlz_dlopen_lookup_t *dlz_lookup;
54 | 	dlz_dlopen_authority_t *dlz_authority;
55 | 	dlz_dlopen_allnodes_t *dlz_allnodes;
56 | 	dlz_dlopen_allowzonexfr_t *dlz_allowzonexfr;
57 | 	dlz_dlopen_newversion_t *dlz_newversion;
58 | 	dlz_dlopen_closeversion_t *dlz_closeversion;
59 | 	dlz_dlopen_configure_t *dlz_configure;
60 | 	dlz_dlopen_ssumatch_t *dlz_ssumatch;
61 | 	dlz_dlopen_addrdataset_t *dlz_addrdataset;
62 | 	dlz_dlopen_subrdataset_t *dlz_subrdataset;
63 | 	dlz_dlopen_delrdataset_t *dlz_delrdataset;
64 | 	dlz_dlopen_destroy_t *dlz_destroy;
65 | } dlopen_data_t;
85 | static void dlopen_log(int level, const char *fmt, ...)
100 | dlopen_dlz_allnodes(const char *zone, void *driverarg, void *dbdata,
103 | 	dlopen_data_t *cd = (dlopen_data_t *) dbdata;
121 | dlopen_dlz_allowzonexfr(void *driverarg, void *dbdata, const char *name,
124 | 	dlopen_data_t *cd = (dlopen_data_t *) dbdata;
141 | dlopen_dlz_authority(const char *zone, void *driverarg, void *dbdata,
144 | 	dlopen_data_t *cd = (dlopen_data_t *) dbdata;
160 | dlopen_dlz_findzonedb(void *driverarg, void *dbdata, const char *name,
164 | 	dlopen_data_t *cd = (dlopen_data_t *) dbdata;
177 | dlopen_dlz_lookup(const char *zone, const char *name, void *driverarg,
182 | 	dlopen_data_t *cd = (dlopen_data_t *) dbdata;
198 | dl_load_symbol(dlopen_data_t *cd, const char *symbol, bool mandatory) {
201 | 		dlopen_log(ISC_LOG_ERROR,
202 | 			   "dlz_dlopen: library '%s' is missing "
209 |  * Called at startup for each dlopen zone in named.conf
212 | dlopen_dlz_create(const char *dlzname, unsigned int argc, char *argv[],
215 | 	dlopen_data_t *cd;
223 | 		dlopen_log(ISC_LOG_ERROR,
224 | 			   "dlz_dlopen driver for '%s' needs a path to "
262 | 		dlopen_log(ISC_LOG_ERROR,
263 | 			   "dlz_dlopen failed to open library '%s' - %u",
270 | 	cd->dlz_version = (dlz_dlopen_version_t *)
272 | 	cd->dlz_create = (dlz_dlopen_create_t *)
274 | 	cd->dlz_lookup = (dlz_dlopen_lookup_t *)
276 | 	cd->dlz_findzonedb = (dlz_dlopen_findzonedb_t *)
289 | 	cd->dlz_allowzonexfr = (dlz_dlopen_allowzonexfr_t *)
291 | 	cd->dlz_allnodes = (dlz_dlopen_allnodes_t *)
294 | 	cd->dlz_authority = (dlz_dlopen_authority_t *)
296 | 	cd->dlz_newversion = (dlz_dlopen_newversion_t *)
298 | 	cd->dlz_closeversion = (dlz_dlopen_closeversion_t *)
301 | 	cd->dlz_configure = (dlz_dlopen_configure_t *)
303 | 	cd->dlz_ssumatch = (dlz_dlopen_ssumatch_t *)
305 | 	cd->dlz_addrdataset = (dlz_dlopen_addrdataset_t *)
307 | 	cd->dlz_subrdataset = (dlz_dlopen_subrdataset_t *)
309 | 	cd->dlz_delrdataset = (dlz_dlopen_delrdataset_t *)
314 | 	if (cd->version < (DLZ_DLOPEN_VERSION - DLZ_DLOPEN_AGE) ||
315 | 	    cd->version > DLZ_DLOPEN_VERSION)
317 | 		dlopen_log(ISC_LOG_ERROR,
318 | 			   "dlz_dlopen: %s: incorrect driver API version %d, "
320 | 			   cd->dl_path, cd->version, DLZ_DLOPEN_VERSION);
335 | 				"log", dlopen_log,
351 | 	dlopen_log(ISC_LOG_ERROR, "dlz_dlopen of '%s' failed", dlzname);
374 | dlopen_dlz_destroy(void *driverarg, void *dbdata) {
375 | 	dlopen_data_t *cd = (dlopen_data_t *) dbdata;
405 | dlopen_dlz_newversion(const char *zone, void *driverarg, void *dbdata,
408 | 	dlopen_data_t *cd = (dlopen_data_t *) dbdata;
426 | dlopen_dlz_closeversion(const char *zone, bool commit,
429 | 	dlopen_data_t *cd = (dlopen_data_t *) dbdata;
447 | dlopen_dlz_configure(dns_view_t *view, dns_dlzdb_t *dlzdb,
450 | 	dlopen_data_t *cd = (dlopen_data_t *) dbdata;
472 | dlopen_dlz_ssumatch(const char *signer, const char *name, const char *tcpaddr,
476 | 	dlopen_data_t *cd = (dlopen_data_t *) dbdata;
497 | dlopen_dlz_addrdataset(const char *name, const char *rdatastr,
500 | 	dlopen_data_t *cd = (dlopen_data_t *) dbdata;
519 | dlopen_dlz_subrdataset(const char *name, const char *rdatastr,
522 | 	dlopen_data_t *cd = (dlopen_data_t *) dbdata;
541 | dlopen_dlz_delrdataset(const char *name, const char *type,
544 | 	dlopen_data_t *cd = (dlopen_data_t *) dbdata;
560 | static dns_sdlzmethods_t dlz_dlopen_methods = {
561 | 	dlopen_dlz_create,
562 | 	dlopen_dlz_destroy,
563 | 	dlopen_dlz_findzonedb,
564 | 	dlopen_dlz_lookup,
565 | 	dlopen_dlz_authority,
566 | 	dlopen_dlz_allnodes,
567 | 	dlopen_dlz_allowzonexfr,
568 | 	dlopen_dlz_newversion,
569 | 	dlopen_dlz_closeversion,
570 | 	dlopen_dlz_configure,
571 | 	dlopen_dlz_ssumatch,
572 | 	dlopen_dlz_addrdataset,
573 | 	dlopen_dlz_subrdataset,
574 | 	dlopen_dlz_delrdataset
582 | dlz_dlopen_init(isc_mem_t *mctx) {
583 | #ifndef ISC_DLZ_DLOPEN
589 | 	dlopen_log(2, "Registering DLZ_dlopen driver");
591 | 	result = dns_sdlzregister("dlopen", &dlz_dlopen_methods, NULL,
595 | 				  mctx, &dlz_dlopen);
613 | dlz_dlopen_clear(void) {
614 | #ifdef ISC_DLZ_DLOPEN
615 | 	dlopen_log(2, "Unregistering DLZ_dlopen driver");
616 | 	if (dlz_dlopen != NULL)
617 | 		dns_sdlzunregister(&dlz_dlopen);
{% endraw %}

```
### bin/tests/.gitignore

```

{% raw %}
7 | dlopen
{% endraw %}

```
### bin/tests/system/feature-test.c

```cpp

{% raw %}
43 | 	fprintf(stderr, "	--have-dlopen\n");
114 | 	if (strcmp(argv[1], "--have-dlopen") == 0) {
115 | #if defined(HAVE_DLOPEN) && defined(ISC_DLZ_DLOPEN)
{% endraw %}

```
### bin/tests/system/filter-aaaa/prereq.sh

```bash

{% raw %}
14 | $FEATURETEST --have-dlopen ||  {
15 |         echo_i "dlopen() not supported - skipping filter-aaaa test"
{% endraw %}

```
### bin/tests/system/rpz/dnsrps.c

```cpp

{% raw %}
12 |  * -a		exit(0) if dnsrps is available or dlopen() msg if not
{% endraw %}

```
### bin/tests/system/checkconf/altdlz.conf

```

{% raw %}
12 | 	database "dlopen driver.so";
{% endraw %}

```
### bin/tests/system/dyndb/prereq.sh

```bash

{% raw %}
14 | $FEATURETEST --have-dlopen ||  {
15 |         echo_i "dlopen() not supported - skipping dyndb test"
{% endraw %}

```
### bin/tests/system/dyndb/driver/driver.c

```cpp

{% raw %}
74 | 	 * Depending on how dlopen() was called, we may not have
{% endraw %}

```
### bin/tests/system/dlzexternal/driver.h

```cpp

{% raw %}
16 | dlz_dlopen_version_t dlz_version;
17 | dlz_dlopen_create_t dlz_create;
18 | dlz_dlopen_destroy_t dlz_destroy;
19 | dlz_dlopen_findzonedb_t dlz_findzonedb;
20 | dlz_dlopen_lookup_t dlz_lookup;
21 | dlz_dlopen_allowzonexfr_t dlz_allowzonexfr;
22 | dlz_dlopen_allnodes_t dlz_allnodes;
23 | dlz_dlopen_newversion_t dlz_newversion;
24 | dlz_dlopen_closeversion_t dlz_closeversion;
25 | dlz_dlopen_configure_t dlz_configure;
26 | dlz_dlopen_ssumatch_t dlz_ssumatch;
27 | dlz_dlopen_addrdataset_t dlz_addrdataset;
28 | dlz_dlopen_subrdataset_t dlz_subrdataset;
29 | dlz_dlopen_delrdataset_t dlz_delrdataset;
{% endraw %}

```
### bin/tests/system/dlzexternal/prereq.sh

```bash

{% raw %}
14 | $FEATURETEST --have-dlopen ||  {
15 |         echo_i "dlopen() not supported - skipping dlzexternal test"
{% endraw %}

```
### bin/tests/system/dlzexternal/driver.c

```cpp

{% raw %}
31 | #include <dns/dlz_dlopen.h>
71 | 	/* Helper functions from the dlz_dlopen driver */
202 | 	return (DLZ_DLOPEN_VERSION);
206 |  * Remember a helper function from the bind9 dlz_dlopen driver
{% endraw %}

```
### bin/tests/system/dlzexternal/ns1/dlzs.conf.in

```

{% raw %}
12 | 	database "dlopen ../driver.@SO@ example.nil";
16 | 	database "dlopen ../driver.@SO@ alternate.nil";
20 | 	database "dlopen ../driver.@SO@ other.nil";
25 | 	database "dlopen ../driver.@SO@ zone.nil";
30 | 	database "dlopen ../driver.@SO@ .";
{% endraw %}

```
### lib/ns/hooks.c

```cpp

{% raw %}
99 | #if HAVE_DLFCN_H && HAVE_DLOPEN
154 | 	handle = dlopen(modpath, flags);
162 | 			      "failed to dlopen() plugin '%s': %s",
{% endraw %}

```
### lib/ns/include/ns/hooks.h

```cpp

{% raw %}
320 |  * Prepare the plugin location to be passed to dlopen() based on the plugin
{% endraw %}

```
### lib/isc/unix/pk11_api.c

```cpp

{% raw %}
44 | 	hPK11 = dlopen(pk11_get_lib_name(), RTLD_NOW);
48 | 			 "dlopen(\"%s\") failed: %s\n",
144 | 		hPK11 = dlopen(pk11_get_lib_name(), RTLD_NOW);
147 | 			 "dlopen(\"%s\") failed: %s\n",
{% endraw %}

```
### lib/dns/dyndb.c

```cpp

{% raw %}
85 | #if HAVE_DLFCN_H && HAVE_DLOPEN
139 | 	handle = dlopen(filename, flags);
{% endraw %}

```
### lib/dns/include/dns/librpz.h

```cpp

{% raw %}
49 |  * Allow either ordinary or dlopen() linking.
802 |  * This is the dlopen() interface to librpz.
876 |  * @param[in,out] dl_handle: NULL or pointer to new dlopen handle
894 | 				 "dlopen(NULL): %s", dlerror());
905 | 	handle = dlopen(NULL, RTLD_NOW | RTLD_LOCAL);
923 | 			 "librpz not linked and no dlopen() path provided");
927 | 	handle = dlopen(path, RTLD_NOW | RTLD_LOCAL);
929 | 		snprintf(emsg->c, sizeof(librpz_emsg_t), "dlopen(%s): %s",
947 |  * Statically link to the librpz.so DSO on systems without dlopen()
{% endraw %}

```
### lib/dns/include/dns/dlz_dlopen.h

```cpp

{% raw %}
12 | /*! \file dns/dlz_dlopen.h */
14 | #ifndef DLZ_DLOPEN_H
15 | #define DLZ_DLOPEN_H
29 | #define DLZ_DLOPEN_VERSION 3
30 | #define DLZ_DLOPEN_AGE 0
33 |  * dlz_dlopen_version() is required for all DLZ external drivers. It
34 |  * should return DLZ_DLOPEN_VERSION
36 | typedef int dlz_dlopen_version_t(unsigned int *flags);
39 |  * dlz_dlopen_create() is required for all DLZ external drivers.
41 | typedef isc_result_t dlz_dlopen_create_t(const char *dlzname,
48 |  * dlz_dlopen_destroy() is optional, and will be called when the
51 | typedef void dlz_dlopen_destroy_t(void *dbdata);
54 |  * dlz_dlopen_findzonedb() is required for all DLZ external drivers
56 | typedef isc_result_t dlz_dlopen_findzonedb_t(void *dbdata,
62 |  * dlz_dlopen_lookup() is required for all DLZ external drivers
64 | typedef isc_result_t dlz_dlopen_lookup_t(const char *zone,
72 |  * dlz_dlopen_authority is optional() if dlz_dlopen_lookup()
75 | typedef isc_result_t dlz_dlopen_authority_t(const char *zone,
80 |  * dlz_dlopen_allowzonexfr() is optional, and should be supplied if
83 | typedef isc_result_t dlz_dlopen_allowzonexfr_t(void *dbdata,
88 |  * dlz_dlopen_allnodes() is optional, but must be supplied if supply a
89 |  * dlz_dlopen_allowzonexfr() function
91 | typedef isc_result_t dlz_dlopen_allnodes_t(const char *zone,
96 |  * dlz_dlopen_newversion() is optional. It should be supplied if you
99 | typedef isc_result_t dlz_dlopen_newversion_t(const char *zone,
107 | typedef void dlz_dlopen_closeversion_t(const char *zone,
113 |  * dlz_dlopen_configure() is optional, but must be supplied if you
116 | typedef isc_result_t dlz_dlopen_configure_t(dns_view_t *view,
121 |  * dlz_dlopen_setclientcallback() is optional, but must be supplied if you
125 | typedef isc_result_t dlz_dlopen_setclientcallback_t(dns_view_t *view,
130 |  * dlz_dlopen_ssumatch() is optional, but must be supplied if you want
133 | typedef bool dlz_dlopen_ssumatch_t(const char *signer,
143 |  * dlz_dlopen_addrdataset() is optional, but must be supplied if you
146 | typedef isc_result_t dlz_dlopen_addrdataset_t(const char *name,
152 |  * dlz_dlopen_subrdataset() is optional, but must be supplied if you
155 | typedef isc_result_t dlz_dlopen_subrdataset_t(const char *name,
161 |  * dlz_dlopen_delrdataset() is optional, but must be supplied if you
164 | typedef isc_result_t dlz_dlopen_delrdataset_t(const char *name,
{% endraw %}

```
### lib/dns/include/dns/dyndb.h

```cpp

{% raw %}
109 |  * This loads a dyndb module using dlopen() or equivalent, calls its register
{% endraw %}

```
### lib/dns/include/dns/dnsrps.h

```cpp

{% raw %}
26 |  * Error message if dlopen(librpz) failed.
{% endraw %}

```
### lib/dns/include/dns/Makefile.in

```

{% raw %}
19 | 		dlz.h dlz_dlopen.h dns64.h dnsrps.h dnssec.h ds.h dsdigest.h \
{% endraw %}

```
### m4/libtool.m4

```

{% raw %}
1821 | # _LT_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
1824 | m4_defun([_LT_TRY_DLOPEN_SELF],
1882 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
1915 | ])# _LT_TRY_DLOPEN_SELF
1918 | # LT_SYS_DLOPEN_SELF
1920 | AC_DEFUN([LT_SYS_DLOPEN_SELF],
1922 | if test yes != "$enable_dlopen"; then
1923 |   enable_dlopen=unknown
1924 |   enable_dlopen_self=unknown
1925 |   enable_dlopen_self_static=unknown
1927 |   lt_cv_dlopen=no
1928 |   lt_cv_dlopen_libs=
1932 |     lt_cv_dlopen=load_add_on
1933 |     lt_cv_dlopen_libs=
1934 |     lt_cv_dlopen_self=yes
1938 |     lt_cv_dlopen=LoadLibrary
1939 |     lt_cv_dlopen_libs=
1943 |     lt_cv_dlopen=dlopen
1944 |     lt_cv_dlopen_libs=
1949 |     AC_CHECK_LIB([dl], [dlopen],
1950 | 		[lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl],[
1951 |     lt_cv_dlopen=dyld
1952 |     lt_cv_dlopen_libs=
1953 |     lt_cv_dlopen_self=yes
1960 |     lt_cv_dlopen=dlopen
1961 |     lt_cv_dlopen_libs=
1962 |     lt_cv_dlopen_self=no
1967 | 	  [lt_cv_dlopen=shl_load],
1969 | 	    [lt_cv_dlopen=shl_load lt_cv_dlopen_libs=-ldld],
1970 | 	[AC_CHECK_FUNC([dlopen],
1971 | 	      [lt_cv_dlopen=dlopen],
1972 | 	  [AC_CHECK_LIB([dl], [dlopen],
1973 | 		[lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl],
1974 | 	    [AC_CHECK_LIB([svld], [dlopen],
1975 | 		  [lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-lsvld],
1977 | 		    [lt_cv_dlopen=dld_link lt_cv_dlopen_libs=-ldld])
1986 |   if test no = "$lt_cv_dlopen"; then
1987 |     enable_dlopen=no
1989 |     enable_dlopen=yes
1992 |   case $lt_cv_dlopen in
1993 |   dlopen)
2001 |     LIBS="$lt_cv_dlopen_libs $LIBS"
2003 |     AC_CACHE_CHECK([whether a program can dlopen itself],
2004 | 	  lt_cv_dlopen_self, [dnl
2005 | 	  _LT_TRY_DLOPEN_SELF(
2006 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
2007 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
2010 |     if test yes = "$lt_cv_dlopen_self"; then
2012 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
2013 | 	  lt_cv_dlopen_self_static, [dnl
2014 | 	  _LT_TRY_DLOPEN_SELF(
2015 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
2016 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
2026 |   case $lt_cv_dlopen_self in
2027 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
2028 |   *) enable_dlopen_self=unknown ;;
2031 |   case $lt_cv_dlopen_self_static in
2032 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
2033 |   *) enable_dlopen_self_static=unknown ;;
2036 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
2037 | 	 [Whether dlopen is supported])
2038 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
2039 | 	 [Whether dlopen of programs is supported])
2040 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
2041 | 	 [Whether dlopen of statically linked programs is supported])
2042 | ])# LT_SYS_DLOPEN_SELF
2045 | AU_ALIAS([AC_LIBTOOL_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF])
2047 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [])
6122 |     [Compiler flag to allow reflexive dlopens])
6235 |   LT_SYS_DLOPEN_SELF
{% endraw %}

```
### m4/ltoptions.m4

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
### contrib/dlz/example/dlz_example.c

```cpp

{% raw %}
57 | 	/* Helper functions from the dlz_dlopen driver */
190 | 	return (DLZ_DLOPEN_VERSION);
194 |  * Remember a helper function from the bind9 dlz_dlopen driver
{% endraw %}

```
### contrib/dlz/example/named.conf

```

{% raw %}
61 | 	database "dlopen ./dlz_example.so example.nil";
{% endraw %}

```
### contrib/dlz/drivers/rules.in

```

{% raw %}
42 | dlz_dlopen_driver.@O@: ${DLZ_DRIVER_DIR}/dlz_dlopen_driver.c ${DLZ_DRIVER_DIR}/include/dlz/dlz_dlopen_driver.h
43 | 	${LIBTOOL_MODE_COMPILE} ${CC} ${ALL_CFLAGS} -c ${DLZ_DRIVER_DIR}/dlz_dlopen_driver.c
{% endraw %}

```
### contrib/dlz/modules/include/dlz_minimal.h

```cpp

{% raw %}
43 |  * Define DLZ_DLOPEN_VERSION to different values to use older versions
46 | #ifndef DLZ_DLOPEN_VERSION
47 | #define DLZ_DLOPEN_VERSION 3
48 | #define DLZ_DLOPEN_AGE 0
92 | #if DLZ_DLOPEN_VERSION > 1
131 | #endif /* DLZ_DLOPEN_VERSION > 1 */
134 |  * Method definitions for callbacks provided by the dlopen driver
149 | #if DLZ_DLOPEN_VERSION < 3
152 | #else /* DLZ_DLOPEN_VERSION >= 3 */
156 | #endif /* DLZ_DLOPEN_VERSION */
164 |  * return DLZ_DLOPEN_VERSION.  'flags' is updated to indicate capabilities
189 | #if DLZ_DLOPEN_VERSION < 3
192 | #else /* DLZ_DLOPEN_VERSION >= 3 */
197 | #endif /* DLZ_DLOPEN_VERSION */
202 | #if DLZ_DLOPEN_VERSION == 1
206 | #else /* DLZ_DLOPEN_VERSION > 1 */
212 | #endif /* DLZ_DLOPEN_VERSION */
254 | #if DLZ_DLOPEN_VERSION < 3
257 | #else /* DLZ_DLOPEN_VERSION >= 3 */
260 | #endif /* DLZ_DLOPEN_VERSION */
{% endraw %}

```
### contrib/dlz/modules/ldap/dlz_ldap_dynamic.c

```cpp

{% raw %}
96 | 	/* Helper functions from the dlz_dlopen driver */
105 | #if DLZ_DLOPEN_VERSION < 3
812 | #if DLZ_DLOPEN_VERSION < 3
837 | #if DLZ_DLOPEN_VERSION < 3
847 | #if DLZ_DLOPEN_VERSION >= 3
854 | #if DLZ_DLOPEN_VERSION == 1
866 | #if DLZ_DLOPEN_VERSION >= 2
1202 | 	return (DLZ_DLOPEN_VERSION);
1206 |  * Register a helper function from the bind9 dlz_dlopen driver
{% endraw %}

```
### contrib/dlz/modules/ldap/testing/named.conf

```

{% raw %}
38 | 	database "dlopen ../dlz_ldap_dynamic.so 2
{% endraw %}

```
### contrib/dlz/modules/sqlite3/dlz_sqlite3_dynamic.c

```cpp

{% raw %}
85 | 	/* Helper functions from the dlz_dlopen driver */
1088 | 	return (DLZ_DLOPEN_VERSION);
1092 |  * Register a helper function from the bind9 dlz_dlopen driver
{% endraw %}

```
### contrib/dlz/modules/sqlite3/testing/named.conf

```

{% raw %}
38 | 	database "dlopen ../dlz_sqlite3_dynamic.so
{% endraw %}

```
### contrib/dlz/modules/mysqldyn/dlz_mysqldyn_mod.c

```cpp

{% raw %}
237 | 	/* Helper functions from the dlz_dlopen driver */
866 |  * Remember a helper function from the bind9 dlz_dlopen driver
891 | 	return (DLZ_DLOPEN_VERSION);
1484 | #if DLZ_DLOPEN_VERSION < 3
1487 | #else /* DLZ_DLOPEN_VERSION >= 3 */
1490 | #endif /* DLZ_DLOPEN_VERSION */
1527 | #if DLZ_DLOPEN_VERSION >= 3
{% endraw %}

```
### contrib/dlz/modules/mysqldyn/testing/named.conf

```

{% raw %}
40 | 	database "dlopen ../dlz_mysqldyn_mod.so BindDB localhost root password";
{% endraw %}

```
### contrib/dlz/modules/perl/dlz_perl_driver.c

```cpp

{% raw %}
126 |  * remember a helper function, from the bind9 dlz_dlopen driver
142 | 	return DLZ_DLOPEN_VERSION;
312 | #if DLZ_DLOPEN_VERSION < 3
329 | #if DLZ_DLOPEN_VERSION >= 3
383 | #if DLZ_DLOPEN_VERSION == 1
407 | #if DLZ_DLOPEN_VERSION >= 2
{% endraw %}

```
### contrib/dlz/modules/perl/testing/named.conf

```

{% raw %}
27 | 	database "dlopen ../dlz_perl_driver.so dlz_perl_example.pm dlz_perl_example";
{% endraw %}

```
### contrib/dlz/modules/filesystem/dlz_filesystem_dynamic.c

```cpp

{% raw %}
71 | 	/* Helper functions from the dlz_dlopen driver */
692 | #if DLZ_DLOPEN_VERSION < 3
709 | #if DLZ_DLOPEN_VERSION >= 3
738 | #if DLZ_DLOPEN_VERSION == 1
758 | #if DLZ_DLOPEN_VERSION >= 2
959 | 	return (DLZ_DLOPEN_VERSION);
963 |  * Register a helper function from the bind9 dlz_dlopen driver
{% endraw %}

```
### contrib/dlz/modules/wildcard/dlz_wildcard_dynamic.c

```cpp

{% raw %}
95 | 	/* Helper functions from the dlz_dlopen driver */
190 | #if DLZ_DLOPEN_VERSION < 3
203 | #if DLZ_DLOPEN_VERSION >= 3
219 | #if DLZ_DLOPEN_VERSION == 1
239 | #if DLZ_DLOPEN_VERSION >= 2
520 | 	return (DLZ_DLOPEN_VERSION);
524 |  * Register a helper function from the bind9 dlz_dlopen driver
{% endraw %}

```
### contrib/dlz/modules/wildcard/testing/named.conf

```

{% raw %}
43 | 	database "dlopen ../dlz_wildcard_dynamic.so
{% endraw %}

```
### contrib/dlz/modules/mysql/dlz_mysql_dynamic.c

```cpp

{% raw %}
91 | 	/* Helper functions from the dlz_dlopen driver */
1087 | 	return (DLZ_DLOPEN_VERSION);
1091 |  * Register a helper function from the bind9 dlz_dlopen driver
{% endraw %}

```
### contrib/dlz/modules/mysql/testing/named.conf

```

{% raw %}
38 | 	database "dlopen ../dlz_mysql_dynamic.so
{% endraw %}

```
### contrib/dlz/modules/bdbhpt/dlz_bdbhpt_dynamic.c

```cpp

{% raw %}
82 |  * inherit from the dlz_dlopen driver
92 | 	/* Helper functions from the dlz_dlopen driver */
242 | #if DLZ_DLOPEN_VERSION >= 3
460 | #if DLZ_DLOPEN_VERSION < 3
478 | #if DLZ_DLOPEN_VERSION >= 3
522 | #if DLZ_DLOPEN_VERSION == 1
543 | #if DLZ_DLOPEN_VERSION >= 2
804 | 	return (DLZ_DLOPEN_VERSION);
808 |  * Register a helper function from the bind9 dlz_dlopen driver
{% endraw %}

```
### contrib/dlz/modules/bdbhpt/README.md

```

{% raw %}
9 | found in the Bind 9 source tree into the new DLZ dlopen driver API.
13 | * Support both v1 (Bind 9.8) and v2 (Bind 9.9) of the dlopen() DLZ API
19 |  * Bind 9.8 or higher with the DLZ dlopen driver enabled
50 |         database "dlopen /usr/lib/bind9/dlz_bdbhpt_dynamic.so T /var/cache/bind/dlz dnsdata.db";
56 | 1. dlopen - Use the dlopen DLZ driver to dynamically load our compiled
{% endraw %}

```
### contrib/dlz/modules/bdbhpt/testing/named.conf

```

{% raw %}
38 |         database "dlopen ../dlz_bdbhpt_dynamic.so T . test.db";
{% endraw %}

```
### doc/arm/dlz.xml

```

{% raw %}
31 |     dynamically at runtime, via the DLZ "dlopen" driver, which acts as a
33 |     "dlopen" driver is linked into <command>named</command> by default, so configure options
59 | 	database "dlopen driver.so <option>args</option>";
66 |       loaded at runtime by the dlopen DLZ driver.  Multiple
89 | 	database "dlopen driver.so <option>args</option>";
105 |       loaded at runtime by the "dlopen" DLZ driver.
112 | 	database "dlopen driver.so example.nil";
{% endraw %}

```