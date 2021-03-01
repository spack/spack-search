---
name: "pmdk"
layout: package
next_package: pmix
previous_package: plumed
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 1.7
18 / 4145 files match, 5 filtered matches.

 - [src/common/dlsym.h](#srccommondlsymh)
 - [src/common/set.c](#srccommonsetc)
 - [src/test/vmmalloc_init/vmmalloc_init.c](#srctestvmmalloc_initvmmalloc_initc)
 - [src/test/pmem_map_file/mocks_posix.c](#srctestpmem_map_filemocks_posixc)
 - [src/jemalloc/src/mutex.c](#srcjemallocsrcmutexc)

### src/common/dlsym.h

```c

{% raw %}
66 |  * util_dlsym -- calls real dlsym()
67 |  */
68 | static inline void *
69 | util_dlsym(void *handle, const char *symbol)
70 | {
71 | 	LOG(3, "handle %p symbol %s", handle, symbol);
72 | 
73 | 	return dlsym(handle, symbol);
74 | }
75 | 
110 |  * util_dlsym -- empty function
111 |  */
112 | static inline void *
113 | util_dlsym(void *handle, const char *symbol)
114 | {
115 | 	errno = ENOSYS;
{% endraw %}

```
### src/common/set.c

```c

{% raw %}
236 | 		goto err;
237 | 	}
238 | 
239 | 	Rpmem_create = util_dlsym(Rpmem_handle_remote, "rpmem_create");
240 | 	if (util_dl_check_error(Rpmem_create, "dlsym")) {
241 | 		ERR("symbol 'rpmem_create' not found");
242 | 		goto err;
243 | 	}
244 | 
245 | 	Rpmem_open = util_dlsym(Rpmem_handle_remote, "rpmem_open");
246 | 	if (util_dl_check_error(Rpmem_open, "dlsym")) {
247 | 		ERR("symbol 'rpmem_open' not found");
248 | 		goto err;
249 | 	}
250 | 
251 | 	Rpmem_close = util_dlsym(Rpmem_handle_remote, "rpmem_close");
252 | 	if (util_dl_check_error(Rpmem_close, "dlsym")) {
253 | 		ERR("symbol 'rpmem_close' not found");
254 | 		goto err;
255 | 	}
256 | 
257 | 	Rpmem_persist = util_dlsym(Rpmem_handle_remote, "rpmem_persist");
258 | 	if (util_dl_check_error(Rpmem_persist, "dlsym")) {
259 | 		ERR("symbol 'rpmem_persist' not found");
260 | 		goto err;
261 | 	}
262 | 
263 | 	Rpmem_deep_persist = util_dlsym(Rpmem_handle_remote,
264 | 			"rpmem_deep_persist");
265 | 	if (util_dl_check_error(Rpmem_deep_persist, "dlsym")) {
266 | 		ERR("symbol 'rpmem_deep_persist' not found");
267 | 		goto err;
268 | 	}
269 | 
270 | 	Rpmem_read = util_dlsym(Rpmem_handle_remote, "rpmem_read");
271 | 	if (util_dl_check_error(Rpmem_read, "dlsym")) {
272 | 		ERR("symbol 'rpmem_read' not found");
273 | 		goto err;
274 | 	}
275 | 
276 | 	Rpmem_remove = util_dlsym(Rpmem_handle_remote, "rpmem_remove");
277 | 	if (util_dl_check_error(Rpmem_remove, "dlsym")) {
278 | 		ERR("symbol 'rpmem_remove' not found");
279 | 		goto err;
280 | 	}
281 | 
282 | 	Rpmem_set_attr = util_dlsym(Rpmem_handle_remote, "rpmem_set_attr");
283 | 	if (util_dl_check_error(Rpmem_set_attr, "dlsym")) {
284 | 		ERR("symbol 'rpmem_set_attr' not found");
285 | 		goto err;
{% endraw %}

```
### src/test/vmmalloc_init/vmmalloc_init.c

```c

{% raw %}
71 | 			UT_OUT("dlopen: %s", dlerror());
72 | 		UT_ASSERTne(handle, NULL);
73 | 
74 | 		Falloc = dlsym(handle, "falloc");
75 | 		UT_ASSERTne(Falloc, NULL);
76 | 	}
{% endraw %}

```
### src/test/pmem_map_file/mocks_posix.c

```c

{% raw %}
50 | 	static int (*posix_fallocate_ptr)(int fd, os_off_t offset, off_t len);
51 | 
52 | 	if (posix_fallocate_ptr == NULL)
53 | 		posix_fallocate_ptr = dlsym(RTLD_NEXT, "posix_fallocate");
54 | 
55 | 	if (len > MAX_LEN)
69 | 	static int (*ftruncate_ptr)(int fd, os_off_t len);
70 | 
71 | 	if (ftruncate_ptr == NULL)
72 | 		ftruncate_ptr = dlsym(RTLD_NEXT, "ftruncate");
73 | 
74 | 	if (len > MAX_LEN) {
{% endraw %}

```
### src/jemalloc/src/mutex.c

```c

{% raw %}
34 | pthread_create_once(void)
35 | {
36 | 
37 | 	pthread_create_fptr = dlsym(RTLD_NEXT, "pthread_create");
38 | 	if (pthread_create_fptr == NULL) {
39 | 		malloc_write("<jemalloc>: Error in dlsym(RTLD_NEXT, "
40 | 		    "\"pthread_create\")\n");
41 | 		abort();
{% endraw %}

```