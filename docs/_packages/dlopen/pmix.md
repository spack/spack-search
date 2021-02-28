---
name: "pmix"
layout: package
next_package: zfs
previous_package: cdo
library_name: dlopen
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## master
17 / 896 files match, 8 filtered matches.

 - [src/mca/base/base.h](#srcmcabasebaseh)
 - [src/mca/base/pmix_mca_base_open.c](#srcmcabasepmix_mca_base_openc)
 - [src/mca/base/pmix_mca_base_component_find.c](#srcmcabasepmix_mca_base_component_findc)
 - [src/mca/pdl/plibltdl/pdl_libltdl_module.c](#srcmcapdlplibltdlpdl_libltdl_modulec)
 - [src/mca/pdl/pdlopen/pdl_pdlopen_module.c](#srcmcapdlpdlopenpdl_pdlopen_modulec)
 - [src/mca/pdl/pdlopen/pdl_pdlopen.h](#srcmcapdlpdlopenpdl_pdlopenh)
 - [src/mca/pdl/pdlopen/pdl_pdlopen_component.c](#srcmcapdlpdlopenpdl_pdlopen_componentc)
 - [src/tools/pmix_info/support.c](#srctoolspmix_infosupportc)

### src/mca/base/base.h

```c

{% raw %}
69 | PMIX_EXPORT extern char *pmix_mca_base_component_path;
70 | PMIX_EXPORT extern bool pmix_mca_base_component_show_load_errors;
71 | PMIX_EXPORT extern bool pmix_mca_base_component_track_load_errors;
72 | PMIX_EXPORT extern bool pmix_mca_base_component_disable_dlopen;
73 | PMIX_EXPORT extern char *pmix_mca_base_system_default_path;
74 | PMIX_EXPORT extern char *pmix_mca_base_user_default_path;
{% endraw %}

```
### src/mca/base/pmix_mca_base_open.c

```c

{% raw %}
50 | char *pmix_mca_base_user_default_path = NULL;
51 | bool pmix_mca_base_component_show_load_errors = (bool) PMIX_SHOW_LOAD_ERRORS_DEFAULT;
52 | bool pmix_mca_base_component_track_load_errors = false;
53 | bool pmix_mca_base_component_disable_dlopen = false;
54 | 
55 | static char *pmix_mca_base_verbose = NULL;
127 |                                         PMIX_MCA_BASE_VAR_SCOPE_READONLY,
128 |                                         &pmix_mca_base_component_track_load_errors);
129 | 
130 |     pmix_mca_base_component_disable_dlopen = false;
131 |     var_id = pmix_mca_base_var_register("pmix", "mca", "base", "component_disable_dlopen",
132 |                                    "Whether to attempt to disable opening dynamic components or not",
133 |                                    PMIX_MCA_BASE_VAR_TYPE_BOOL, NULL, 0, PMIX_MCA_BASE_VAR_FLAG_NONE,
134 |                                    PMIX_INFO_LVL_9,
135 |                                    PMIX_MCA_BASE_VAR_SCOPE_READONLY,
136 |                                    &pmix_mca_base_component_disable_dlopen);
137 |     (void) pmix_mca_base_var_register_synonym(var_id, "pmix", "mca", NULL, "component_disable_dlopen",
138 |                                               PMIX_MCA_BASE_VAR_SYN_FLAG_DEPRECATED);
139 | 
{% endraw %}

```
### src/mca/base/pmix_mca_base_component_find.c

```c

{% raw %}
135 | 
136 | #if PMIX_HAVE_PDL_SUPPORT
137 |     /* Find any available dynamic components in the specified directory */
138 |     if (open_dso_components && !pmix_mca_base_component_disable_dlopen) {
139 |         find_dyn_components(directory, framework, (const char**)requested_component_names,
140 |                             include_mode);
{% endraw %}

```
### src/mca/pdl/plibltdl/pdl_libltdl_module.c

```c

{% raw %}
32 |     pmix_pdl_plibltpdl_component_t *c = &mca_pdl_plibltpdl_component;
33 | 
34 |     if (use_ext && private_namespace) {
35 |         local_handle = lt_dlopenadvise(fname, c->advise_private_ext);
36 |     } else if (use_ext && !private_namespace) {
37 |         local_handle = lt_dlopenadvise(fname, c->advise_public_ext);
38 |     } else if (!use_ext && private_namespace) {
39 |         local_handle = lt_dlopenadvise(fname, c->advise_private_noext);
40 |     } else if (!use_ext && !private_namespace) {
41 |         local_handle = lt_dlopenadvise(fname, c->advise_public_noext);
42 |     }
43 | #else
44 |     if (use_ext) {
45 |         local_handle = lt_dlopenext(fname);
46 |     } else {
47 |         local_handle = lt_dlopen(fname);
48 |     }
49 | #endif
{% endraw %}

```
### src/mca/pdl/pdlopen/pdl_pdlopen_module.c

```c

{% raw %}
31 | /*
32 |  * Trivial helper function to avoid replicating code
33 |  */
34 | static void do_pdlopen(const char *fname, int flags,
35 |                       void **handle, char **err_msg)
36 | {
48 | }
49 | 
50 | 
51 | static int pdlopen_open(const char *fname, bool use_ext, bool private_namespace,
52 |                        pmix_pdl_handle_t **handle, char **err_msg)
53 | {
72 |         int i;
73 |         char *ext;
74 | 
75 |         for (i = 0, ext = mca_pdl_pdlopen_component.filename_suffixes[i];
76 |              NULL != ext;
77 |              ext = mca_pdl_pdlopen_component.filename_suffixes[++i]) {
78 |             char *name;
79 | 
101 |             }
102 | 
103 |             /* Yes, the file exists -- try to dlopen it.  If we can't
104 |                dlopen it, bail. */
105 |             do_pdlopen(name, flags, &local_handle, err_msg);
106 |             free(name);
107 |             break;
111 |     /* Otherwise, the caller does not want to use filename extensions,
112 |        so just use the single filename that the caller provided */
113 |     else {
114 |         do_pdlopen(fname, flags, &local_handle, err_msg);
115 |     }
116 | 
117 |     if (NULL != local_handle) {
118 |         *handle = calloc(1, sizeof(pmix_pdl_handle_t));
119 |         (*handle)->dlopen_handle = local_handle;
120 | 
121 | #if PMIX_ENABLE_DEBUG
131 | }
132 | 
133 | 
134 | static int pdlopen_lookup(pmix_pdl_handle_t *handle, const char *symbol,
135 |                          void **ptr, char **err_msg)
136 | {
137 |     assert(handle);
138 |     assert(handle->dlopen_handle);
139 |     assert(symbol);
140 |     assert(ptr);
151 | }
152 | 
153 | 
154 | static int pdlopen_close(pmix_pdl_handle_t *handle)
155 | {
156 |     assert(handle);
157 | 
158 |     int ret;
159 |     ret = dlclose(handle->dlopen_handle);
160 | 
161 | #if PMIX_ENABLE_DEBUG
170 |  * Scan all the files in a directory (or path) and invoke a callback
171 |  * on each one.
172 |  */
173 | static int pdlopen_foreachfile(const char *search_path,
174 |                               int (*func)(const char *filename, void *data),
175 |                               void *data)
281 | /*
282 |  * Module definition
283 |  */
284 | pmix_pdl_base_module_t pmix_pdl_pdlopen_module = {
285 |     .open = pdlopen_open,
286 |     .lookup = pdlopen_lookup,
287 |     .close = pdlopen_close,
288 |     .foreachfile = pdlopen_foreachfile
289 | };
290 | 
{% endraw %}

```
### src/mca/pdl/pdlopen/pdl_pdlopen.h

```c

{% raw %}
14 | 
15 | #include "src/mca/pdl/pdl.h"
16 | 
17 | extern pmix_pdl_base_module_t pmix_pdl_pdlopen_module;
18 | 
19 | /*
22 |  * If we're debugging, keep a copy of the name of the file we've opened.
23 |  */
24 | struct pmix_pdl_handle_t {
25 |     void *dlopen_handle;
26 | #if PMIX_ENABLE_DEBUG
27 |     void *filename;
33 | 
34 |     char *filename_suffixes_mca_storage;
35 |     char **filename_suffixes;
36 | } pmix_pdl_pdlopen_component_t;
37 | 
38 | extern pmix_pdl_pdlopen_component_t mca_pdl_pdlopen_component;
39 | 
40 | #endif /* PMIX_PDL_PDLOPEN */
{% endraw %}

```
### src/mca/pdl/pdlopen/pdl_pdlopen_component.c

```c

{% raw %}
22 | /*
23 |  * Public string showing the sysinfo ompi_linux component version number
24 |  */
25 | const char *pmix_pdl_pdlopen_component_version_string =
26 |     "PMIX pdl pdlopen MCA component version " PMIX_VERSION;
27 | 
28 | 
29 | /*
30 |  * Local functions
31 |  */
32 | static int pdlopen_component_register(void);
33 | static int pdlopen_component_open(void);
34 | static int pdlopen_component_close(void);
35 | static int pdlopen_component_query(pmix_mca_base_module_t **module, int *priority);
36 | 
37 | /*
39 |  * and pointers to our public functions in it
40 |  */
41 | 
42 | pmix_pdl_pdlopen_component_t mca_pdl_pdlopen_component = {
43 | 
44 |     /* Fill in the mca_pdl_base_component_t */
50 |             PMIX_PDL_BASE_VERSION_1_0_0,
51 | 
52 |             /* Component name and version */
53 |             .pmix_mca_component_name = "pdlopen",
54 |             PMIX_MCA_BASE_MAKE_VERSION(component, PMIX_MAJOR_VERSION, PMIX_MINOR_VERSION,
55 |                                        PMIX_RELEASE_VERSION),
56 | 
57 |             /* Component functions */
58 |             .pmix_mca_register_component_params = pdlopen_component_register,
59 |             .pmix_mca_open_component = pdlopen_component_open,
60 |             .pmix_mca_close_component = pdlopen_component_close,
61 |             .pmix_mca_query_component = pdlopen_component_query,
62 |         },
63 | 
72 | };
73 | 
74 | 
75 | static int pdlopen_component_register(void)
76 | {
77 |     int ret;
78 | 
79 |     mca_pdl_pdlopen_component.filename_suffixes_mca_storage = ".so,.dylib,.dll,.sl";
80 |     ret =
81 |         pmix_mca_base_component_var_register(&mca_pdl_pdlopen_component.base.base_version,
82 |                                              "filename_suffixes",
83 |                                              "Comma-delimited list of filename suffixes that the pdlopen component will try",
84 |                                              PMIX_MCA_BASE_VAR_TYPE_STRING,
85 |                                              NULL,
87 |                                              PMIX_MCA_BASE_VAR_FLAG_SETTABLE,
88 |                                              PMIX_INFO_LVL_5,
89 |                                              PMIX_MCA_BASE_VAR_SCOPE_LOCAL,
90 |                                              &mca_pdl_pdlopen_component.filename_suffixes_mca_storage);
91 |     if (ret < 0) {
92 |         return ret;
93 |     }
94 |     mca_pdl_pdlopen_component.filename_suffixes =
95 |         pmix_argv_split(mca_pdl_pdlopen_component.filename_suffixes_mca_storage,
96 |                         ',');
97 | 
98 |     return PMIX_SUCCESS;
99 | }
100 | 
101 | static int pdlopen_component_open(void)
102 | {
103 |     return PMIX_SUCCESS;
104 | }
105 | 
106 | 
107 | static int pdlopen_component_close(void)
108 | {
109 |     if (NULL != mca_pdl_pdlopen_component.filename_suffixes) {
110 |         pmix_argv_free(mca_pdl_pdlopen_component.filename_suffixes);
111 |         mca_pdl_pdlopen_component.filename_suffixes = NULL;
112 |     }
113 | 
115 | }
116 | 
117 | 
118 | static int pdlopen_component_query(pmix_mca_base_module_t **module, int *priority)
119 | {
120 |     /* The priority value is somewhat meaningless here; by
{% endraw %}

```
### src/tools/pmix_info/support.c

```c

{% raw %}
1372 |     }
1373 | 
1374 |     pmix_info_out("Internal debug support", "option:debug", debug);
1375 |     pmix_info_out("dl support", "option:dlopen", have_dl);
1376 |     pmix_info_out("Symbol vis. support", "options:visibility", symbol_visibility);
1377 |     pmix_info_out("Manpages built", "options:man-pages", manpages);
{% endraw %}

```