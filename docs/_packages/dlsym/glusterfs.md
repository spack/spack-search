---
name: "glusterfs"
layout: package
next_package: gmake
previous_package: global
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 7.3
8 / 2186 files match, 6 filtered matches.

 - [libglusterfs/src/xlator.c](#libglusterfssrcxlatorc)
 - [glusterfsd/src/glusterfsd.c](#glusterfsdsrcglusterfsdc)
 - [rpc/rpc-lib/src/rpc-transport.c](#rpcrpc-libsrcrpc-transportc)
 - [xlators/features/cloudsync/src/cloudsync.c](#xlatorsfeaturescloudsyncsrccloudsyncc)
 - [xlators/features/cloudsync/src/cloudsync-plugins/src/cvlt/src/libcvlt.c](#xlatorsfeaturescloudsyncsrccloudsync-pluginssrccvltsrclibcvltc)
 - [xlators/protocol/server/src/authenticate.c](#xlatorsprotocolserversrcauthenticatec)

### libglusterfs/src/xlator.c

```c

{% raw %}
211 |     }
212 | 
213 |     /* check new struct first, and then check this */
214 |     xlapi = dlsym(handle, "xlator_api");
215 |     if (!xlapi) {
216 |         gf_msg("xlator", GF_LOG_ERROR, 0, LG_MSG_DLSYM_ERROR,
217 |                "dlsym(xlator_api) missing: %s", dlerror());
218 |         goto out;
219 |     }
248 | 
249 |     handle = xl->dlhandle;
250 | 
251 |     xlapi = dlsym(handle, "xlator_api");
252 |     if (!xlapi) {
253 |         gf_msg("xlator", GF_LOG_ERROR, 0, LG_MSG_DLSYM_ERROR,
254 |                "dlsym(xlator_api) missing: %s", dlerror());
255 |         ret = -1;
256 |         goto out;
{% endraw %}

```
### glusterfsd/src/glusterfsd.c

```c

{% raw %}
2001 |     }
2002 | 
2003 |     /* Load up the function */
2004 |     exp_file_parse = dlsym(libhandle, "exp_file_parse");
2005 |     if (!exp_file_parse) {
2006 |         gf_log("glusterfs", GF_LOG_CRITICAL,
2018 |     }
2019 | 
2020 |     /* Load up the function */
2021 |     exp_file_print = dlsym(libhandle, "exp_file_print");
2022 |     if (!exp_file_print) {
2023 |         gf_log("glusterfs", GF_LOG_CRITICAL,
2030 |     exp_file_print(file);
2031 | 
2032 |     /* Load up the function */
2033 |     exp_file_deinit = dlsym(libhandle, "exp_file_deinit");
2034 |     if (!exp_file_deinit) {
2035 |         gf_log("glusterfs", GF_LOG_CRITICAL,
2093 |     }
2094 | 
2095 |     /* Load up the function */
2096 |     ng_file_parse = dlsym(libhandle, "ng_file_parse");
2097 |     if (!ng_file_parse) {
2098 |         gf_log("glusterfs", GF_LOG_CRITICAL,
2109 |     }
2110 | 
2111 |     /* Load up the function */
2112 |     ng_file_print = dlsym(libhandle, "ng_file_print");
2113 |     if (!ng_file_print) {
2114 |         gf_log("glusterfs", GF_LOG_CRITICAL,
2121 |     ng_file_print(file);
2122 | 
2123 |     /* Load up the function */
2124 |     ng_file_deinit = dlsym(libhandle, "ng_file_deinit");
2125 |     if (!ng_file_deinit) {
2126 |         gf_log("glusterfs", GF_LOG_CRITICAL,
{% endraw %}

```
### rpc/rpc-lib/src/rpc-transport.c

```c

{% raw %}
306 | 
307 |     trans->dl_handle = handle;
308 | 
309 |     trans->ops = dlsym(handle, "tops");
310 |     if (trans->ops == NULL) {
311 |         gf_log("rpc-transport", GF_LOG_ERROR, "dlsym (rpc_transport_ops) on %s",
312 |                dlerror());
313 |         goto fail;
316 |     *VOID(&(trans->init)) = dlsym(handle, "init");
317 |     if (trans->init == NULL) {
318 |         gf_log("rpc-transport", GF_LOG_ERROR,
319 |                "dlsym (gf_rpc_transport_init) on %s", dlerror());
320 |         goto fail;
321 |     }
323 |     *VOID(&(trans->fini)) = dlsym(handle, "fini");
324 |     if (trans->fini == NULL) {
325 |         gf_log("rpc-transport", GF_LOG_ERROR,
326 |                "dlsym (gf_rpc_transport_fini) on %s", dlerror());
327 |         goto fail;
328 |     }
330 |     *VOID(&(trans->reconfigure)) = dlsym(handle, "reconfigure");
331 |     if (trans->reconfigure == NULL) {
332 |         gf_log("rpc-transport", GF_LOG_DEBUG,
333 |                "dlsym (gf_rpc_transport_reconfigure) on %s", dlerror());
334 |     }
335 | 
340 |     }
341 | 
342 |     this = THIS;
343 |     vol_opt->given_opt = dlsym(handle, "options");
344 |     if (vol_opt->given_opt == NULL) {
345 |         gf_log("rpc-transport", GF_LOG_DEBUG,
{% endraw %}

```
### xlators/features/cloudsync/src/cloudsync.c

```c

{% raw %}
131 |         (void)dlerror(); /* clear out previous error string */
132 | 
133 |         /* load library methods */
134 |         store_methods = (store_methods_t *)dlsym(handle, "store_ops");
135 |         if (!store_methods) {
136 |             gf_msg(this->name, GF_LOG_ERROR, 0, 0, "null store_methods %s",
{% endraw %}

```
### xlators/features/cloudsync/src/cloudsync-plugins/src/cvlt/src/libcvlt.c

```c

{% raw %}
86 | 
87 |     dlerror(); /* Clear any existing error */
88 | 
89 |     get_archstore_methods = dlsym(arch->handle, "get_archstore_methods");
90 |     if (!get_archstore_methods) {
91 |         gf_msg(plugin, GF_LOG_ERROR, 0, CVLT_EXTRACTION_FAILED,
{% endraw %}

```
### xlators/protocol/server/src/authenticate.c

```c

{% raw %}
59 |     }
60 |     GF_FREE(auth_file);
61 | 
62 |     authenticate = dlsym(handle, "gf_auth");
63 |     if (!authenticate) {
64 |         gf_msg("authenticate", GF_LOG_ERROR, 0, PS_MSG_AUTHENTICATE_ERROR,
65 |                "dlsym(gf_auth) on %s\n", dlerror());
66 |         dict_set(this, key, data_from_dynptr(NULL, 0));
67 |         dlclose(handle);
86 |         dlclose(handle);
87 |         return -1;
88 |     }
89 |     auth_handle->vol_opt->given_opt = dlsym(handle, "options");
90 |     if (auth_handle->vol_opt->given_opt == NULL) {
91 |         gf_msg_debug("authenticate", 0,
{% endraw %}

```