---
name: "glusterfs"
layout: package
next_package: tau
previous_package: gflags
library_name: dlopen
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 7.3
14 / 2186 files match, 8 filtered matches.

 - [libglusterfs/src/xlator.c](#libglusterfssrcxlatorc)
 - [glusterfsd/src/glusterfsd.c](#glusterfsdsrcglusterfsdc)
 - [rpc/rpc-lib/src/rpc-transport.h](#rpcrpc-libsrcrpc-transporth)
 - [rpc/rpc-lib/src/rpc-transport.c](#rpcrpc-libsrcrpc-transportc)
 - [xlators/features/cloudsync/src/cloudsync.c](#xlatorsfeaturescloudsyncsrccloudsyncc)
 - [xlators/features/cloudsync/src/cloudsync-plugins/src/cvlt/src/libcvlt.h](#xlatorsfeaturescloudsyncsrccloudsync-pluginssrccvltsrclibcvlth)
 - [xlators/features/cloudsync/src/cloudsync-plugins/src/cvlt/src/libcvlt.c](#xlatorsfeaturescloudsyncsrccloudsync-pluginssrccvltsrclibcvltc)
 - [xlators/protocol/server/src/authenticate.c](#xlatorsprotocolserversrcauthenticatec)

### libglusterfs/src/xlator.c

```c

{% raw %}
203 | 
204 |     gf_msg_trace("xlator", 0, "attempt to load file %s", name);
205 | 
206 |     handle = dlopen(name, RTLD_NOW);
207 |     if (!handle) {
208 |         gf_msg("xlator", GF_LOG_WARNING, 0, LG_MSG_DLOPEN_FAILED, "%s",
367 | 
368 |     gf_msg_trace("xlator", 0, "attempt to load file %s", name);
369 | 
370 |     handle = dlopen(name, RTLD_NOW);
371 |     if (!handle) {
372 |         gf_msg("xlator", GF_LOG_WARNING, 0, LG_MSG_DLOPEN_FAILED, "%s",
{% endraw %}

```
### glusterfsd/src/glusterfsd.c

```c

{% raw %}
1990 |     }
1991 | 
1992 |     /* Load up the library */
1993 |     libhandle = dlopen(libpathfull, RTLD_NOW);
1994 |     if (!libhandle) {
1995 |         gf_log("glusterfs", GF_LOG_CRITICAL,
2084 |         goto out;
2085 |     }
2086 |     /* Load up the library */
2087 |     libhandle = dlopen(libpathfull, RTLD_NOW);
2088 |     if (!libhandle) {
2089 |         gf_log("glusterfs", GF_LOG_CRITICAL,
{% endraw %}

```
### rpc/rpc-lib/src/rpc-transport.h

```c

{% raw %}
193 | 
194 |     struct list_head list;
195 |     int bind_insecure;
196 |     void *dl_handle; /* handle of dlopen() */
197 |     char *ssl_name;
198 |     dict_t *clnt_options; /* store options received from
{% endraw %}

```
### rpc/rpc-lib/src/rpc-transport.c

```c

{% raw %}
294 | 
295 |     gf_log("rpc-transport", GF_LOG_DEBUG, "attempt to load file %s", name);
296 | 
297 |     handle = dlopen(name, RTLD_NOW);
298 |     if (handle == NULL) {
299 |         gf_log("rpc-transport", GF_LOG_ERROR, "%s", dlerror());
{% endraw %}

```
### xlators/features/cloudsync/src/cloudsync.c

```c

{% raw %}
105 |             goto out;
106 |         }
107 | 
108 |         handle = dlopen(libpath, RTLD_NOW);
109 |         if (!handle) {
110 |             gf_msg(this->name, GF_LOG_WARNING, 0, 0,
{% endraw %}

```
### xlators/features/cloudsync/src/cloudsync-plugins/src/cvlt/src/libcvlt.h

```c

{% raw %}
53 | struct _archive {
54 |     gf_lock_t lock;                /* lock for controlling access   */
55 |     xlator_t *xl;                  /* xlator                        */
56 |     void *handle;                  /* handle returned from dlopen   */
57 |     int32_t nreqs;                 /* num requests active           */
58 |     struct mem_pool *req_pool;     /* pool for requests             */
{% endraw %}

```
### xlators/features/cloudsync/src/cloudsync-plugins/src/cvlt/src/libcvlt.c

```c

{% raw %}
77 | 
78 |     VALIDATE_OR_GOTO(arch, err);
79 | 
80 |     arch->handle = dlopen(LIBARCHIVE_SO, RTLD_NOW);
81 |     if (!arch->handle) {
82 |         gf_msg(plugin, GF_LOG_ERROR, 0, CVLT_DLOPEN_FAILED,
{% endraw %}

```
### xlators/protocol/server/src/authenticate.c

```c

{% raw %}
48 |         return -1;
49 |     }
50 | 
51 |     handle = dlopen(auth_file, RTLD_LAZY);
52 |     if (!handle) {
53 |         gf_msg("authenticate", GF_LOG_ERROR, 0, PS_MSG_AUTHENTICATE_ERROR,
54 |                "dlopen(%s): %s\n", auth_file, dlerror());
55 |         dict_set(this, key, data_from_dynptr(NULL, 0));
56 |         GF_FREE(auth_file);
{% endraw %}

```