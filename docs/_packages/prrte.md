---
name: "prrte"
layout: package
next_package: libxscrnsaver
previous_package: sdl2
languages: ['c']
---
## develop
17 / 1121 files match

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
75 | PRTE_EXPORT extern bool prte_mca_base_component_disable_dlopen;
{% endraw %}

```
### src/mca/base/prte_mca_base_open.c

```c

{% raw %}
60 | bool prte_mca_base_component_disable_dlopen = false;
138 |     prte_mca_base_component_disable_dlopen = false;
139 |     prte_mca_base_var_register("prte", "mca", "base", "component_disable_dlopen",
145 |                                 &prte_mca_base_component_disable_dlopen);
{% endraw %}

```
### src/mca/base/prte_mca_base_component_find.c

```c

{% raw %}
138 |     if (open_dso_components && !prte_mca_base_component_disable_dlopen) {
{% endraw %}

```
### src/mca/prtedl/dlopen/prtedl_dlopen.h

```c

{% raw %}
19 | PRTE_EXPORT extern prte_prtedl_base_module_t prte_prtedl_dlopen_module;
27 |     void *dlopen_handle;
38 | } prte_prtedl_dlopen_component_t;
40 | PRTE_EXPORT extern prte_prtedl_dlopen_component_t prte_prtedl_dlopen_component;
{% endraw %}

```
### src/mca/prtedl/dlopen/prtedl_dlopen_module.c

```c

{% raw %}
37 | static void do_dlopen(const char *fname, int flags,
54 | static int dlopen_open(const char *fname, bool use_ext, bool private_namespace,
76 |         for (i = 0, ext = prte_prtedl_dlopen_component.filename_suffixes[i];
78 |              ext = prte_prtedl_dlopen_component.filename_suffixes[++i]) {
101 |                prtedlopen it, bail. */
102 |             do_dlopen(name, flags, &local_handle, err_msg);
111 |         do_dlopen(fname, flags, &local_handle, err_msg);
116 |         (*handle)->dlopen_handle = local_handle;
131 | static int dlopen_lookup(prte_dl_handle_t *handle, const char *symbol,
135 |     assert(handle->dlopen_handle);
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

```c

{% raw %}
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
{% endraw %}

```
### src/mca/prtedl/libltdl/prtedl_libltdl_module.c

```c

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

```c

{% raw %}
410 |     prte_info_out("dl support", "option:dlopen", have_dl);
{% endraw %}

```