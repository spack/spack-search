---
name: "pmix"
layout: package
next_package: taskflow
previous_package: libarchive
languages: ['c']
---
## master
17 / 896 files match

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
72 | PMIX_EXPORT extern bool pmix_mca_base_component_disable_dlopen;
{% endraw %}

```
### src/mca/base/pmix_mca_base_open.c

```c

{% raw %}
53 | bool pmix_mca_base_component_disable_dlopen = false;
130 |     pmix_mca_base_component_disable_dlopen = false;
131 |     var_id = pmix_mca_base_var_register("pmix", "mca", "base", "component_disable_dlopen",
136 |                                    &pmix_mca_base_component_disable_dlopen);
137 |     (void) pmix_mca_base_var_register_synonym(var_id, "pmix", "mca", NULL, "component_disable_dlopen",
{% endraw %}

```
### src/mca/base/pmix_mca_base_component_find.c

```c

{% raw %}
138 |     if (open_dso_components && !pmix_mca_base_component_disable_dlopen) {
{% endraw %}

```
### src/mca/pdl/plibltdl/pdl_libltdl_module.c

```c

{% raw %}
35 |         local_handle = lt_dlopenadvise(fname, c->advise_private_ext);
37 |         local_handle = lt_dlopenadvise(fname, c->advise_public_ext);
39 |         local_handle = lt_dlopenadvise(fname, c->advise_private_noext);
41 |         local_handle = lt_dlopenadvise(fname, c->advise_public_noext);
45 |         local_handle = lt_dlopenext(fname);
47 |         local_handle = lt_dlopen(fname);
{% endraw %}

```
### src/mca/pdl/pdlopen/pdl_pdlopen_module.c

```c

{% raw %}
34 | static void do_pdlopen(const char *fname, int flags,
51 | static int pdlopen_open(const char *fname, bool use_ext, bool private_namespace,
75 |         for (i = 0, ext = mca_pdl_pdlopen_component.filename_suffixes[i];
77 |              ext = mca_pdl_pdlopen_component.filename_suffixes[++i]) {
104 |                dlopen it, bail. */
105 |             do_pdlopen(name, flags, &local_handle, err_msg);
114 |         do_pdlopen(fname, flags, &local_handle, err_msg);
119 |         (*handle)->dlopen_handle = local_handle;
134 | static int pdlopen_lookup(pmix_pdl_handle_t *handle, const char *symbol,
138 |     assert(handle->dlopen_handle);
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

```c

{% raw %}
17 | extern pmix_pdl_base_module_t pmix_pdl_pdlopen_module;
25 |     void *dlopen_handle;
36 | } pmix_pdl_pdlopen_component_t;
38 | extern pmix_pdl_pdlopen_component_t mca_pdl_pdlopen_component;
{% endraw %}

```
### src/mca/pdl/pdlopen/pdl_pdlopen_component.c

```c

{% raw %}
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
{% endraw %}

```
### src/tools/pmix_info/support.c

```c

{% raw %}
1375 |     pmix_info_out("dl support", "option:dlopen", have_dl);
{% endraw %}

```