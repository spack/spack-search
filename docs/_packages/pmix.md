---
name: "pmix"
layout: package
next_package: taskflow
previous_package: libarchive
languages: ['yaml', 'cpp']
---
## master
17 / 896 files match

 - [.travis.yml](#travisyml)
 - [Makefile.am](#makefileam)
 - [config/pmix.m4](#configpmixm4)
 - [src/mca/base/base.h](#srcmcabasebaseh)
 - [src/mca/base/pmix_mca_base_component_repository.c](#srcmcabasepmix_mca_base_component_repositoryc)
 - [src/mca/base/pmix_mca_base_open.c](#srcmcabasepmix_mca_base_openc)
 - [src/mca/base/pmix_mca_base_component_find.c](#srcmcabasepmix_mca_base_component_findc)
 - [src/mca/pdl/configure.m4](#srcmcapdlconfigurem4)
 - [src/mca/pdl/pdl.h](#srcmcapdlpdlh)
 - [src/mca/pdl/plibltdl/configure.m4](#srcmcapdlplibltdlconfigurem4)
 - [src/mca/pdl/plibltdl/pdl_libltdl_module.c](#srcmcapdlplibltdlpdl_libltdl_modulec)
 - [src/mca/pdl/pdlopen/configure.m4](#srcmcapdlpdlopenconfigurem4)
 - [src/mca/pdl/pdlopen/pdl_pdlopen_module.c](#srcmcapdlpdlopenpdl_pdlopen_modulec)
 - [src/mca/pdl/pdlopen/pdl_pdlopen.h](#srcmcapdlpdlopenpdl_pdlopenh)
 - [src/mca/pdl/pdlopen/Makefile.am](#srcmcapdlpdlopenmakefileam)
 - [src/mca/pdl/pdlopen/pdl_pdlopen_component.c](#srcmcapdlpdlopenpdl_pdlopen_componentc)
 - [src/tools/pmix_info/support.c](#srctoolspmix_infosupportc)

### .travis.yml

```yaml

{% raw %}
27 |         - DISTCHECK_CONFIGURE_FLAGS="$PRRTE_CONFIGURE_ARGS --disable-dlopen"
{% endraw %}

```
### Makefile.am

```

{% raw %}
29 | AM_DISTCHECK_CONFIGURE_FLAGS = --disable-dlopen
{% endraw %}

```
### config/pmix.m4

```

{% raw %}
990 |     # do we want dlopen support ?
991 |     AC_MSG_CHECKING([if want dlopen support])
992 |     AC_ARG_ENABLE([dlopen],
993 |         [AC_HELP_STRING([--enable-dlopen],
994 |                         [Whether build should attempt to use dlopen (or
997 |     AS_IF([test "$enable_dlopen" = "unknown"],
998 |           [AC_MSG_WARN([enable_dlopen variable has been overwritten by configure])
1001 |     AS_IF([test "$enable_dlopen" = "no"],
1004 |            PMIX_ENABLE_DLOPEN_SUPPORT=0
1006 |           [PMIX_ENABLE_DLOPEN_SUPPORT=1
1008 |     AC_DEFINE_UNQUOTED(PMIX_ENABLE_DLOPEN_SUPPORT, $PMIX_ENABLE_DLOPEN_SUPPORT,
1009 |                       [Whether we want to enable dlopen support])
1314 | # see if they want to disable non-RTLD_GLOBAL dlopen
1315 | AC_MSG_CHECKING([if want to support dlopen of non-global namespaces])
1316 | AC_ARG_ENABLE([nonglobal-dlopen],
1317 |               AC_HELP_STRING([--enable-nonglobal-dlopen],
1318 |                              [enable non-global dlopen (default: enabled)]))
1319 | if test "$enable_nonglobal_dlopen" = "no"; then
1328 | # devel headers, then default nonglobal-dlopen to false
1329 | AS_IF([test -z "$enable_nonglobal_dlopen" && test "x$pmix_mode" = "xembedded" && test $WANT_INSTALL_HEADERS -eq 0 && test $pmix_need_libpmix -eq 1],
{% endraw %}

```
### src/mca/base/base.h

```cpp

{% raw %}
72 | PMIX_EXPORT extern bool pmix_mca_base_component_disable_dlopen;
{% endraw %}

```
### src/mca/base/pmix_mca_base_component_repository.c

```cpp

{% raw %}
539 |     /* no dlopen support */
{% endraw %}

```
### src/mca/base/pmix_mca_base_open.c

```cpp

{% raw %}
53 | bool pmix_mca_base_component_disable_dlopen = false;
130 |     pmix_mca_base_component_disable_dlopen = false;
131 |     var_id = pmix_mca_base_var_register("pmix", "mca", "base", "component_disable_dlopen",
136 |                                    &pmix_mca_base_component_disable_dlopen);
137 |     (void) pmix_mca_base_var_register_synonym(var_id, "pmix", "mca", NULL, "component_disable_dlopen",
{% endraw %}

```
### src/mca/base/pmix_mca_base_component_find.c

```cpp

{% raw %}
138 |     if (open_dso_components && !pmix_mca_base_component_disable_dlopen) {
{% endraw %}

```
### src/mca/pdl/configure.m4

```

{% raw %}
25 |     # If --disable-dlopen was used, then have all the components fail
29 |     AS_IF([test $PMIX_ENABLE_DLOPEN_SUPPORT -eq 0],
34 |     # If we found no suitable static pdl component and dlopen support
37 |            test $PMIX_ENABLE_DLOPEN_SUPPORT -eq 1],
40 |            AC_MSG_WARN([specify --disable-dlopen to configure.])
44 |     # happen if --disable-dlopen was *not* specified), do some more
{% endraw %}

```
### src/mca/pdl/pdl.h

```cpp

{% raw %}
20 |  * This framework provides portable access to dlopen- and dlsym-like
42 |  * along with a simple component that supports dlopen/dlsym on POSIX
{% endraw %}

```
### src/mca/pdl/plibltdl/configure.m4

```

{% raw %}
79 |                   [lt_dlopen],
{% endraw %}

```
### src/mca/pdl/plibltdl/pdl_libltdl_module.c

```cpp

{% raw %}
35 |         local_handle = lt_dlopenadvise(fname, c->advise_private_ext);
37 |         local_handle = lt_dlopenadvise(fname, c->advise_public_ext);
39 |         local_handle = lt_dlopenadvise(fname, c->advise_private_noext);
41 |         local_handle = lt_dlopenadvise(fname, c->advise_public_noext);
45 |         local_handle = lt_dlopenext(fname);
47 |         local_handle = lt_dlopen(fname);
{% endraw %}

```
### src/mca/pdl/pdlopen/configure.m4

```

{% raw %}
14 | AC_DEFUN([MCA_pmix_pdl_pdlopen_PRIORITY], [80])
19 | AC_DEFUN([MCA_pmix_pdl_pdlopen_COMPILE_MODE], [
25 | # MCA_pmix_pdl_pdlopen_POST_CONFIG()
27 | AC_DEFUN([MCA_pmix_pdl_pdlopen_POST_CONFIG],[
33 |            LDFLAGS="$LDFLAGS $pmix_pdl_pdlopen_ADD_LDFLAGS"
34 |            LIBS="$LIBS $pmix_pdl_pdlopen_ADD_LIBS"
38 | # MCA_pdl_pdlopen_CONFIG([action-if-can-compile],
41 | AC_DEFUN([MCA_pmix_pdl_pdlopen_CONFIG],[
42 |     AC_CONFIG_FILES([src/mca/pdl/pdlopen/Makefile])
46 |     AC_ARG_ENABLE([dl-dlopen],
47 |         [AS_HELP_STRING([--disable-dl-dlopen],
48 |                         [Disable the "dlopen" PDL component (and probably force the use of the "libltdl" PDL component).])
51 |     pmix_pdl_pdlopen_happy=no
52 |     AS_IF([test "$enable_dl_dlopen" != "no"],
53 |           [PMIX_CHECK_PACKAGE([pmix_pdl_pdlopen],
56 |               [dlopen],
60 |               [pmix_pdl_pdlopen_happy=yes],
61 |               [pmix_pdl_pdlopen_happy=no])
64 |     AS_IF([test "$pmix_pdl_pdlopen_happy" = "yes"],
65 |           [pmix_pdl_pdlopen_ADD_LIBS=$pmix_pdl_pdlopen_LIBS
69 |     AC_SUBST(pmix_pdl_pdlopen_LIBS)
{% endraw %}

```
### src/mca/pdl/pdlopen/pdl_pdlopen_module.c

```cpp

{% raw %}
28 | #include "pdl_pdlopen.h"
34 | static void do_pdlopen(const char *fname, int flags,
39 |     *handle = dlopen(fname, flags);
51 | static int pdlopen_open(const char *fname, bool use_ext, bool private_namespace,
60 |     /* Setup the dlopen flags */
75 |         for (i = 0, ext = mca_pdl_pdlopen_component.filename_suffixes[i];
77 |              ext = mca_pdl_pdlopen_component.filename_suffixes[++i]) {
103 |             /* Yes, the file exists -- try to dlopen it.  If we can't
104 |                dlopen it, bail. */
105 |             do_pdlopen(name, flags, &local_handle, err_msg);
114 |         do_pdlopen(fname, flags, &local_handle, err_msg);
119 |         (*handle)->dlopen_handle = local_handle;
134 | static int pdlopen_lookup(pmix_pdl_handle_t *handle, const char *symbol,
138 |     assert(handle->dlopen_handle);
142 |     *ptr = dlsym(handle->dlopen_handle, symbol);
154 | static int pdlopen_close(pmix_pdl_handle_t *handle)
159 |     ret = dlclose(handle->dlopen_handle);
173 | static int pdlopen_foreachfile(const char *search_path,
284 | pmix_pdl_base_module_t pmix_pdl_pdlopen_module = {
285 |     .open = pdlopen_open,
286 |     .lookup = pdlopen_lookup,
287 |     .close = pdlopen_close,
288 |     .foreachfile = pdlopen_foreachfile
{% endraw %}

```
### src/mca/pdl/pdlopen/pdl_pdlopen.h

```cpp

{% raw %}
10 | #ifndef PMIX_PDL_PDLOPEN
11 | #define PMIX_PDL_PDLOPEN
17 | extern pmix_pdl_base_module_t pmix_pdl_pdlopen_module;
25 |     void *dlopen_handle;
36 | } pmix_pdl_pdlopen_component_t;
38 | extern pmix_pdl_pdlopen_component_t mca_pdl_pdlopen_component;
40 | #endif /* PMIX_PDL_PDLOPEN */
{% endraw %}

```
### src/mca/pdl/pdlopen/Makefile.am

```

{% raw %}
12 |         pdl_pdlopen.h \
13 |         pdl_pdlopen_component.c \
14 |         pdl_pdlopen_module.c
18 | noinst_LTLIBRARIES = libmca_pdl_pdlopen.la
20 | libmca_pdl_pdlopen_la_SOURCES = $(sources)
21 | libmca_pdl_pdlopen_la_LDFLAGS = -module -avoid-version
22 | libmca_pdl_pdlopen_la_LIBADD = $(pmix_pdl_pdlopen_LIBS)
{% endraw %}

```
### src/mca/pdl/pdlopen/pdl_pdlopen_component.c

```cpp

{% raw %}
19 | #include "pdl_pdlopen.h"
25 | const char *pmix_pdl_pdlopen_component_version_string =
26 |     "PMIX pdl pdlopen MCA component version " PMIX_VERSION;
32 | static int pdlopen_component_register(void);
33 | static int pdlopen_component_open(void);
34 | static int pdlopen_component_close(void);
35 | static int pdlopen_component_query(pmix_mca_base_module_t **module, int *priority);
42 | pmix_pdl_pdlopen_component_t mca_pdl_pdlopen_component = {
53 |             .pmix_mca_component_name = "pdlopen",
58 |             .pmix_mca_register_component_params = pdlopen_component_register,
59 |             .pmix_mca_open_component = pdlopen_component_open,
60 |             .pmix_mca_close_component = pdlopen_component_close,
61 |             .pmix_mca_query_component = pdlopen_component_query,
75 | static int pdlopen_component_register(void)
79 |     mca_pdl_pdlopen_component.filename_suffixes_mca_storage = ".so,.dylib,.dll,.sl";
81 |         pmix_mca_base_component_var_register(&mca_pdl_pdlopen_component.base.base_version,
83 |                                              "Comma-delimited list of filename suffixes that the pdlopen component will try",
90 |                                              &mca_pdl_pdlopen_component.filename_suffixes_mca_storage);
94 |     mca_pdl_pdlopen_component.filename_suffixes =
95 |         pmix_argv_split(mca_pdl_pdlopen_component.filename_suffixes_mca_storage,
101 | static int pdlopen_component_open(void)
107 | static int pdlopen_component_close(void)
109 |     if (NULL != mca_pdl_pdlopen_component.filename_suffixes) {
110 |         pmix_argv_free(mca_pdl_pdlopen_component.filename_suffixes);
111 |         mca_pdl_pdlopen_component.filename_suffixes = NULL;
118 | static int pdlopen_component_query(pmix_mca_base_module_t **module, int *priority)
123 |     *priority = mca_pdl_pdlopen_component.base.priority;
124 |     *module = &pmix_pdl_pdlopen_module.super;
{% endraw %}

```
### src/tools/pmix_info/support.c

```cpp

{% raw %}
1375 |     pmix_info_out("dl support", "option:dlopen", have_dl);
{% endraw %}

```