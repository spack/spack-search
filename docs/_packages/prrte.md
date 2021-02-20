---
name: "prrte"
layout: package
next_package: psi4
previous_package: procps-ng
languages: ['c']
---
## develop
17 / 1121 files match, 8 filtered matches.

 - [src/mca/base/base.h](#srcmcabasebaseh)
 - [src/mca/base/prte_mca_base_open.c](#srcmcabaseprte_mca_base_openc)
 - [src/mca/base/prte_mca_base_component_find.c](#srcmcabaseprte_mca_base_component_findc)
 - [src/mca/prtedl/dlopen/prtedl_dlopen.h](#srcmcaprtedldlopenprtedl_dlopenh)
 - [src/mca/prtedl/dlopen/prtedl_dlopen_module.c](#srcmcaprtedldlopenprtedl_dlopen_modulec)
 - [src/mca/prtedl/dlopen/prtedl_dlopen_component.c](#srcmcaprtedldlopenprtedl_dlopen_componentc)
 - [src/mca/prtedl/libltdl/prtedl_libltdl_module.c](#srcmcaprtedllibltdlprtedl_libltdl_modulec)
 - [src/tools/prte_info/param.c](#srctoolsprte_infoparamc)

### src/mca/base/base.h

```c

{% raw %}
72 | PRTE_EXPORT extern char *prte_mca_base_component_path;
73 | PRTE_EXPORT extern bool prte_mca_base_component_show_load_errors;
74 | PRTE_EXPORT extern bool prte_mca_base_component_track_load_errors;
75 | PRTE_EXPORT extern bool prte_mca_base_component_disable_dlopen;
76 | PRTE_EXPORT extern char *prte_mca_base_system_default_path;
77 | PRTE_EXPORT extern char *prte_mca_base_user_default_path;
{% endraw %}

```
### src/mca/base/prte_mca_base_open.c

```c

{% raw %}
57 | bool prte_mca_base_component_show_load_errors =
58 |     (bool) PRTE_SHOW_LOAD_ERRORS_DEFAULT;
59 | bool prte_mca_base_component_track_load_errors = false;
60 | bool prte_mca_base_component_disable_dlopen = false;
61 | 
62 | static char *prte_mca_base_verbose = NULL;
135 |                                 PRTE_MCA_BASE_VAR_SCOPE_READONLY,
136 |                                 &prte_mca_base_component_track_load_errors);
137 | 
138 |     prte_mca_base_component_disable_dlopen = false;
139 |     prte_mca_base_var_register("prte", "mca", "base", "component_disable_dlopen",
140 |                                 "Whether to attempt to disable opening dynamic components or not",
141 |                                 PRTE_MCA_BASE_VAR_TYPE_BOOL, NULL, 0,
142 |                                 PRTE_MCA_BASE_VAR_FLAG_NONE,
143 |                                 PRTE_INFO_LVL_9,
144 |                                 PRTE_MCA_BASE_VAR_SCOPE_READONLY,
145 |                                 &prte_mca_base_component_disable_dlopen);
146 | 
147 |     /* What verbosity level do we want for the default 0 stream? */
{% endraw %}

```
### src/mca/base/prte_mca_base_component_find.c

```c

{% raw %}
135 | 
136 | #if PRTE_HAVE_DL_SUPPORT
137 |     /* Find any available dynamic components in the specified directory */
138 |     if (open_dso_components && !prte_mca_base_component_disable_dlopen) {
139 |         find_dyn_components(directory, framework, (const char**)requested_component_names,
140 |                             include_mode);
{% endraw %}

```
### src/mca/prtedl/dlopen/prtedl_dlopen.h

```c

{% raw %}
16 | 
17 | #include "src/mca/prtedl/prtedl.h"
18 | 
19 | PRTE_EXPORT extern prte_prtedl_base_module_t prte_prtedl_dlopen_module;
20 | 
21 | /*
24 |  * If we're debugging, keep a copy of the name of the file we've opened.
25 |  */
26 | struct prte_dl_handle_t {
27 |     void *dlopen_handle;
28 | #if PRTE_ENABLE_DEBUG
29 |     void *filename;
35 | 
36 |     char *filename_suffixes_mca_storage;
37 |     char **filename_suffixes;
38 | } prte_prtedl_dlopen_component_t;
39 | 
40 | PRTE_EXPORT extern prte_prtedl_dlopen_component_t prte_prtedl_dlopen_component;
41 | 
42 | #endif /* PRTE_DL_DLOPEN */
{% endraw %}

```
### src/mca/prtedl/dlopen/prtedl_dlopen_module.c

```c

{% raw %}
34 | /*
35 |  * Trivial helper function to avoid replicating code
36 |  */
37 | static void do_dlopen(const char *fname, int flags,
38 |                       void **handle, char **err_msg)
39 | {
51 | }
52 | 
53 | 
54 | static int dlopen_open(const char *fname, bool use_ext, bool private_namespace,
55 |                        prte_dl_handle_t **handle, char **err_msg)
56 | {
73 |         int i, rc;
74 |         char *ext;
75 | 
76 |         for (i = 0, ext = prte_prtedl_dlopen_component.filename_suffixes[i];
77 |              NULL != ext;
78 |              ext = prte_prtedl_dlopen_component.filename_suffixes[++i]) {
79 |             char *name;
80 | 
98 |             }
99 | 
100 |             /* Yes, the file exists -- try to prtedlopen it.  If we can't
101 |                prtedlopen it, bail. */
102 |             do_dlopen(name, flags, &local_handle, err_msg);
103 |             free(name);
104 |             break;
108 |     /* Otherwise, the caller does not want to use filename extensions,
109 |        so just use the single filename that the caller provided */
110 |     else {
111 |         do_dlopen(fname, flags, &local_handle, err_msg);
112 |     }
113 | 
114 |     if (NULL != local_handle) {
115 |         *handle = calloc(1, sizeof(prte_dl_handle_t));
116 |         (*handle)->dlopen_handle = local_handle;
117 | 
118 | #if PRTE_ENABLE_DEBUG
128 | }
129 | 
130 | 
131 | static int dlopen_lookup(prte_dl_handle_t *handle, const char *symbol,
132 |                          void **ptr, char **err_msg)
133 | {
134 |     assert(handle);
135 |     assert(handle->dlopen_handle);
136 |     assert(symbol);
137 |     assert(ptr);
148 | }
149 | 
150 | 
151 | static int dlopen_close(prte_dl_handle_t *handle)
152 | {
153 |     assert(handle);
154 | 
155 |     int ret;
156 |     ret = dlclose(handle->dlopen_handle);
157 | 
158 | #if PRTE_ENABLE_DEBUG
167 |  * Scan all the files in a directory (or path) and invoke a callback
168 |  * on each one.
169 |  */
170 | static int dlopen_foreachfile(const char *search_path,
171 |                               int (*func)(const char *filename, void *data),
172 |                               void *data)
274 | /*
275 |  * Module definition
276 |  */
277 | prte_prtedl_base_module_t prte_prtedl_dlopen_module = {
278 |     .open = dlopen_open,
279 |     .lookup = dlopen_lookup,
280 |     .close = dlopen_close,
281 |     .foreachfile = dlopen_foreachfile
282 | };
283 | 
{% endraw %}

```
### src/mca/prtedl/dlopen/prtedl_dlopen_component.c

```c

{% raw %}
24 | /*
25 |  * Public string showing the sysinfo ompi_linux component version number
26 |  */
27 | const char *prte_prtedl_dlopen_component_version_string =
28 |     "PRTE prtedl dlopen MCA component version " PRTE_VERSION;
29 | 
30 | 
31 | /*
32 |  * Local functions
33 |  */
34 | static int dlopen_component_register(void);
35 | static int dlopen_component_open(void);
36 | static int dlopen_component_close(void);
37 | static int dlopen_component_query(prte_mca_base_module_t **module, int *priority);
38 | 
39 | /*
41 |  * and pointers to our public functions in it
42 |  */
43 | 
44 | prte_prtedl_dlopen_component_t prte_prtedl_dlopen_component = {
45 | 
46 |     /* Fill in the mca_prtedl_base_component_t */
52 |             PRTE_DL_BASE_VERSION_1_0_0,
53 | 
54 |             /* Component name and version */
55 |             .mca_component_name = "dlopen",
56 |             PRTE_MCA_BASE_MAKE_VERSION(component, PRTE_MAJOR_VERSION, PRTE_MINOR_VERSION,
57 |                                         PRTE_RELEASE_VERSION),
58 | 
59 |             /* Component functions */
60 |             .mca_register_component_params = dlopen_component_register,
61 |             .mca_open_component = dlopen_component_open,
62 |             .mca_close_component = dlopen_component_close,
63 |             .mca_query_component = dlopen_component_query,
64 |         },
65 | 
74 | };
75 | 
76 | 
77 | static int dlopen_component_register(void)
78 | {
79 |     int ret;
80 | 
81 |     prte_prtedl_dlopen_component.filename_suffixes_mca_storage = ".so,.dylib,.dll,.sl";
82 |     ret =
83 |         prte_mca_base_component_var_register(&prte_prtedl_dlopen_component.base.base_version,
84 |                                         "filename_suffixes",
85 |                                         "Comma-delimited list of filename suffixes that the PRTE dlopen component will try",
86 |                                         PRTE_MCA_BASE_VAR_TYPE_STRING,
87 |                                         NULL,
89 |                                         PRTE_MCA_BASE_VAR_FLAG_SETTABLE,
90 |                                         PRTE_INFO_LVL_5,
91 |                                         PRTE_MCA_BASE_VAR_SCOPE_LOCAL,
92 |                                         &prte_prtedl_dlopen_component.filename_suffixes_mca_storage);
93 |     if (ret < 0) {
94 |         return ret;
95 |     }
96 |     prte_prtedl_dlopen_component.filename_suffixes =
97 |         prte_argv_split(prte_prtedl_dlopen_component.filename_suffixes_mca_storage,
98 |                         ',');
99 | 
100 |     return PRTE_SUCCESS;
101 | }
102 | 
103 | static int dlopen_component_open(void)
104 | {
105 |     return PRTE_SUCCESS;
106 | }
107 | 
108 | 
109 | static int dlopen_component_close(void)
110 | {
111 |     if (NULL != prte_prtedl_dlopen_component.filename_suffixes) {
112 |         prte_argv_free(prte_prtedl_dlopen_component.filename_suffixes);
113 |         prte_prtedl_dlopen_component.filename_suffixes = NULL;
114 |     }
115 | 
117 | }
118 | 
119 | 
120 | static int dlopen_component_query(prte_mca_base_module_t **module, int *priority)
121 | {
122 |     /* The priority value is somewhat meaningless here; by
{% endraw %}

```
### src/mca/prtedl/libltdl/prtedl_libltdl_module.c

```c

{% raw %}
34 |     prte_prtedl_libltdl_component_t *c = &prte_prtedl_libltdl_component;
35 | 
36 |     if (use_ext && private_namespace) {
37 |         local_handle = lt_dlopenadvise(fname, c->advise_private_ext);
38 |     } else if (use_ext && !private_namespace) {
39 |         local_handle = lt_dlopenadvise(fname, c->advise_public_ext);
40 |     } else if (!use_ext && private_namespace) {
41 |         local_handle = lt_dlopenadvise(fname, c->advise_private_noext);
42 |     } else if (!use_ext && !private_namespace) {
43 |         local_handle = lt_dlopenadvise(fname, c->advise_public_noext);
44 |     }
45 | #else
46 |     if (use_ext) {
47 |         local_handle = lt_dlopenext(fname);
48 |     } else {
49 |         local_handle = lt_dlopen(fname);
50 |     }
51 | #endif
{% endraw %}

```
### src/tools/prte_info/param.c

```c

{% raw %}
407 |     }
408 | 
409 |     prte_info_out("Internal debug support", "option:debug", debug);
410 |     prte_info_out("dl support", "option:dlopen", have_dl);
411 |     prte_info_out("prun default --prefix", "prun:prefix_by_default",
412 |                   prun_prefix_by_default);
{% endraw %}

```