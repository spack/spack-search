---
name: "prrte"
layout: package
next_package: libxscrnsaver
previous_package: sdl2
languages: ['cpp']
---
## develop
17 / 1121 files match

 - [configure.ac](#configureac)
 - [config/prte_configure_options.m4](#configprte_configure_optionsm4)
 - [src/mca/plm/alps/plm_alps_module.c](#srcmcaplmalpsplm_alps_modulec)
 - [src/mca/base/base.h](#srcmcabasebaseh)
 - [src/mca/base/prte_mca_base_component_repository.c](#srcmcabaseprte_mca_base_component_repositoryc)
 - [src/mca/base/prte_mca_base_open.c](#srcmcabaseprte_mca_base_openc)
 - [src/mca/base/prte_mca_base_component_find.c](#srcmcabaseprte_mca_base_component_findc)
 - [src/mca/prtedl/configure.m4](#srcmcaprtedlconfigurem4)
 - [src/mca/prtedl/prtedl.h](#srcmcaprtedlprtedlh)
 - [src/mca/prtedl/dlopen/prtedl_dlopen.h](#srcmcaprtedldlopenprtedl_dlopenh)
 - [src/mca/prtedl/dlopen/configure.m4](#srcmcaprtedldlopenconfigurem4)
 - [src/mca/prtedl/dlopen/prtedl_dlopen_module.c](#srcmcaprtedldlopenprtedl_dlopen_modulec)
 - [src/mca/prtedl/dlopen/prtedl_dlopen_component.c](#srcmcaprtedldlopenprtedl_dlopen_componentc)
 - [src/mca/prtedl/dlopen/Makefile.am](#srcmcaprtedldlopenmakefileam)
 - [src/mca/prtedl/libltdl/configure.m4](#srcmcaprtedllibltdlconfigurem4)
 - [src/mca/prtedl/libltdl/prtedl_libltdl_module.c](#srcmcaprtedllibltdlprtedl_libltdl_modulec)
 - [src/tools/prte_info/param.c](#srctoolsprte_infoparamc)

### configure.ac

```

{% raw %}
1057 | LT_INIT([dlopen win32-dll])
{% endraw %}

```
### config/prte_configure_options.m4

```

{% raw %}
164 | # Do we want to allow DLOPEN?
167 | AC_MSG_CHECKING([if want dlopen support])
168 | AC_ARG_ENABLE([dlopen],
169 |     [AC_HELP_STRING([--enable-dlopen],
170 |                     [Whether build should attempt to use dlopen (or
172 |                      Disabling dlopen implies --disable-mca-dso.
174 | if test "$enable_dlopen" = "no" ; then
177 |     PRTE_ENABLE_DLOPEN_SUPPORT=0
180 |     PRTE_ENABLE_DLOPEN_SUPPORT=1
183 | AC_DEFINE_UNQUOTED(PRTE_ENABLE_DLOPEN_SUPPORT, $PRTE_ENABLE_DLOPEN_SUPPORT,
184 |     [Whether we want to enable dlopen support])
{% endraw %}

```
### src/mca/plm/alps/plm_alps_module.c

```cpp

{% raw %}
288 |      * stuff below is necessary in the event that we've sadly configured PRTE with --disable-dlopen,
{% endraw %}

```
### src/mca/base/base.h

```cpp

{% raw %}
75 | PRTE_EXPORT extern bool prte_mca_base_component_disable_dlopen;
{% endraw %}

```
### src/mca/base/prte_mca_base_component_repository.c

```cpp

{% raw %}
540 |     /* no dlopen support */
{% endraw %}

```
### src/mca/base/prte_mca_base_open.c

```cpp

{% raw %}
60 | bool prte_mca_base_component_disable_dlopen = false;
138 |     prte_mca_base_component_disable_dlopen = false;
139 |     prte_mca_base_var_register("prte", "mca", "base", "component_disable_dlopen",
145 |                                 &prte_mca_base_component_disable_dlopen);
{% endraw %}

```
### src/mca/base/prte_mca_base_component_find.c

```cpp

{% raw %}
138 |     if (open_dso_components && !prte_mca_base_component_disable_dlopen) {
{% endraw %}

```
### src/mca/prtedl/configure.m4

```

{% raw %}
23 |     # If --disable-prtedlopen was used, then have all the components fail
27 |     AS_IF([test "$enable_prtedlopen" = "no"],
32 |     # If we found no suitable static prtedl component and prtedlopen support
35 |            test "$enable_prtedlopen" != "no"],
38 |            AC_MSG_WARN([specify --disable-prtedlopen to configure.])
42 |     # happen if --disable-prtedlopen was *not* specified), do some more
{% endraw %}

```
### src/mca/prtedl/prtedl.h

```cpp

{% raw %}
20 |  * This framework provides portable access to prtedlopen- and prtedlsym-like
42 |  * along with a simple component that supports prtedlopen/prtedlsym on POSIX
{% endraw %}

```
### src/mca/prtedl/dlopen/prtedl_dlopen.h

```cpp

{% raw %}
12 | #ifndef PRTE_DL_DLOPEN
13 | #define PRTE_DL_DLOPEN
19 | PRTE_EXPORT extern prte_prtedl_base_module_t prte_prtedl_dlopen_module;
27 |     void *dlopen_handle;
38 | } prte_prtedl_dlopen_component_t;
40 | PRTE_EXPORT extern prte_prtedl_dlopen_component_t prte_prtedl_dlopen_component;
42 | #endif /* PRTE_DL_DLOPEN */
{% endraw %}

```
### src/mca/prtedl/dlopen/configure.m4

```

{% raw %}
12 | AC_DEFUN([MCA_prte_prtedl_dlopen_PRIORITY], [80])
17 | AC_DEFUN([MCA_prte_prtedl_dlopen_COMPILE_MODE], [
23 | # MCA_prtedl_dlopen_CONFIG([action-if-can-compile],
26 | AC_DEFUN([MCA_prte_prtedl_dlopen_CONFIG],[
27 |     AC_CONFIG_FILES([src/mca/prtedl/dlopen/Makefile])
31 |     AC_ARG_ENABLE([prtedl-dlopen],
32 |         [AS_HELP_STRING([--disable-prtedl-dlopen],
33 |             [Disable the "dlopen" PRTE DL component (and probably force the use of the "libltdl" DL component).  This option should really only be used by PRTE developers.  You are probably actually looking for the "--disable-prtedlopen" option, which disables all dlopen-like functionality from PRTE.])
36 |     prte_prtedl_prtedlopen_happy=no
37 |     AS_IF([test "$enable_prtedl_prtedlopen" != "no"],
38 |           [PRTE_CHECK_PACKAGE([prte_prtedl_dlopen],
41 |               [dlopen],
45 |               [prte_prtedl_dlopen_happy=yes],
46 |               [prte_prtedl_dlopen_happy=no])
49 |     AS_IF([test "$prte_prtedl_dlopen_happy" = "yes"],
50 |           [prtedl_dlopen_ADD_LIBS=$prte_prtedl_dlopen_LIBS
51 |            prtedl_dlopen_WRAPPER_EXTRA_LIBS=$prte_prtedl_dlopen_LIBS
55 |     AC_SUBST(prte_prtedl_dlopen_LIBS)
{% endraw %}

```
### src/mca/prtedl/dlopen/prtedl_dlopen_module.c

```cpp

{% raw %}
31 | #include "prtedl_dlopen.h"
37 | static void do_dlopen(const char *fname, int flags,
42 |     *handle = dlopen(fname, flags);
54 | static int dlopen_open(const char *fname, bool use_ext, bool private_namespace,
61 |     /* Setup the prtedlopen flags */
76 |         for (i = 0, ext = prte_prtedl_dlopen_component.filename_suffixes[i];
78 |              ext = prte_prtedl_dlopen_component.filename_suffixes[++i]) {
100 |             /* Yes, the file exists -- try to prtedlopen it.  If we can't
101 |                prtedlopen it, bail. */
102 |             do_dlopen(name, flags, &local_handle, err_msg);
111 |         do_dlopen(fname, flags, &local_handle, err_msg);
116 |         (*handle)->dlopen_handle = local_handle;
131 | static int dlopen_lookup(prte_dl_handle_t *handle, const char *symbol,
135 |     assert(handle->dlopen_handle);
139 |     *ptr = dlsym(handle->dlopen_handle, symbol);
151 | static int dlopen_close(prte_dl_handle_t *handle)
156 |     ret = dlclose(handle->dlopen_handle);
170 | static int dlopen_foreachfile(const char *search_path,
277 | prte_prtedl_base_module_t prte_prtedl_dlopen_module = {
278 |     .open = dlopen_open,
279 |     .lookup = dlopen_lookup,
280 |     .close = dlopen_close,
281 |     .foreachfile = dlopen_foreachfile
{% endraw %}

```
### src/mca/prtedl/dlopen/prtedl_dlopen_component.c

```cpp

{% raw %}
21 | #include "prtedl_dlopen.h"
27 | const char *prte_prtedl_dlopen_component_version_string =
28 |     "PRTE prtedl dlopen MCA component version " PRTE_VERSION;
34 | static int dlopen_component_register(void);
35 | static int dlopen_component_open(void);
36 | static int dlopen_component_close(void);
37 | static int dlopen_component_query(prte_mca_base_module_t **module, int *priority);
44 | prte_prtedl_dlopen_component_t prte_prtedl_dlopen_component = {
55 |             .mca_component_name = "dlopen",
60 |             .mca_register_component_params = dlopen_component_register,
61 |             .mca_open_component = dlopen_component_open,
62 |             .mca_close_component = dlopen_component_close,
63 |             .mca_query_component = dlopen_component_query,
77 | static int dlopen_component_register(void)
81 |     prte_prtedl_dlopen_component.filename_suffixes_mca_storage = ".so,.dylib,.dll,.sl";
83 |         prte_mca_base_component_var_register(&prte_prtedl_dlopen_component.base.base_version,
85 |                                         "Comma-delimited list of filename suffixes that the PRTE dlopen component will try",
92 |                                         &prte_prtedl_dlopen_component.filename_suffixes_mca_storage);
96 |     prte_prtedl_dlopen_component.filename_suffixes =
97 |         prte_argv_split(prte_prtedl_dlopen_component.filename_suffixes_mca_storage,
103 | static int dlopen_component_open(void)
109 | static int dlopen_component_close(void)
111 |     if (NULL != prte_prtedl_dlopen_component.filename_suffixes) {
112 |         prte_argv_free(prte_prtedl_dlopen_component.filename_suffixes);
113 |         prte_prtedl_dlopen_component.filename_suffixes = NULL;
120 | static int dlopen_component_query(prte_mca_base_module_t **module, int *priority)
125 |     *priority = prte_prtedl_dlopen_component.base.priority;
126 |     *module = &prte_prtedl_dlopen_module.super;
{% endraw %}

```
### src/mca/prtedl/dlopen/Makefile.am

```

{% raw %}
13 |         prtedl_dlopen.h \
14 |         prtedl_dlopen_component.c \
15 |         prtedl_dlopen_module.c
19 | noinst_LTLIBRARIES = libmca_prtedl_dlopen.la
21 | libmca_prtedl_dlopen_la_SOURCES = $(sources)
22 | libmca_prtedl_dlopen_la_LDFLAGS = -module -avoid-version
23 | libmca_prtedl_dlopen_la_LIBADD = $(prte_prtedl_dlopen_LIBS)
{% endraw %}

```
### src/mca/prtedl/libltdl/configure.m4

```

{% raw %}
79 |                   [lt_prtedlopen],
{% endraw %}

```
### src/mca/prtedl/libltdl/prtedl_libltdl_module.c

```cpp

{% raw %}
37 |         local_handle = lt_dlopenadvise(fname, c->advise_private_ext);
39 |         local_handle = lt_dlopenadvise(fname, c->advise_public_ext);
41 |         local_handle = lt_dlopenadvise(fname, c->advise_private_noext);
43 |         local_handle = lt_dlopenadvise(fname, c->advise_public_noext);
47 |         local_handle = lt_dlopenext(fname);
49 |         local_handle = lt_dlopen(fname);
{% endraw %}

```
### src/tools/prte_info/param.c

```cpp

{% raw %}
410 |     prte_info_out("dl support", "option:dlopen", have_dl);
{% endraw %}

```