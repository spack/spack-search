---
name: "ucx"
layout: package
next_package: None
previous_package: None
library_name: dlopen
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 1.4.0
9 / 590 files match, 3 filtered matches.

 - [src/ucm/util/reloc.c](#srcucmutilrelocc)
 - [test/mpi/test_memhooks.c](#testmpitest_memhooksc)
 - [test/apps/dlopen.c](#testappsdlopenc)

### src/ucm/util/reloc.c

```c

{% raw %}
45 | 
46 | /* List of patches to be applied to additional libraries */
47 | static UCS_LIST_HEAD(ucm_reloc_patch_list);
48 | static void * (*ucm_reloc_orig_dlopen)(const char *, int) = NULL;
49 | static pthread_mutex_t ucm_reloc_patch_list_lock = PTHREAD_MUTEX_INITIALIZER;
50 | 
268 |     return ctx.status;
269 | }
270 | 
271 | static void *ucm_dlopen(const char *filename, int flag)
272 | {
273 |     ucm_reloc_patch_t *patch;
274 |     void *handle;
275 | 
276 |     if (ucm_reloc_orig_dlopen == NULL) {
277 |         ucm_fatal("ucm_reloc_orig_dlopen is NULL");
278 |         return NULL;
279 |     }
280 | 
281 |     handle = ucm_reloc_orig_dlopen(filename, flag);
282 |     if (handle != NULL) {
283 |         /*
288 |          */
289 |         pthread_mutex_lock(&ucm_reloc_patch_list_lock);
290 |         ucs_list_for_each(patch, &ucm_reloc_patch_list, list) {
291 |             ucm_debug("in dlopen(), re-applying '%s' to %p", patch->symbol,
292 |                       patch->value);
293 |             ucm_reloc_apply_patch(patch);
297 |     return handle;
298 | }
299 | 
300 | static ucm_reloc_patch_t ucm_reloc_dlopen_patch = {
301 |     .symbol = "dlopen",
302 |     .value  = ucm_dlopen
303 | };
304 | 
323 | }
324 | 
325 | /* called with lock held */
326 | static ucs_status_t ucm_reloc_install_dlopen()
327 | {
328 |     static int installed = 0;
332 |         return UCS_OK;
333 |     }
334 | 
335 |     ucm_reloc_orig_dlopen = ucm_reloc_get_orig(ucm_reloc_dlopen_patch.symbol,
336 |                                                ucm_reloc_dlopen_patch.value);
337 | 
338 |     status = ucm_reloc_apply_patch(&ucm_reloc_dlopen_patch);
339 |     if (status != UCS_OK) {
340 |         return status;
341 |     }
342 | 
343 |     ucs_list_add_tail(&ucm_reloc_patch_list, &ucm_reloc_dlopen_patch.list);
344 | 
345 |     installed = 1;
355 |      */
356 |     pthread_mutex_lock(&ucm_reloc_patch_list_lock);
357 | 
358 |     status = ucm_reloc_install_dlopen();
359 |     if (status != UCS_OK) {
360 |         goto out_unlock;
{% endraw %}

```
### test/mpi/test_memhooks.c

```c

{% raw %}
104 | 
105 | void* open_dyn_lib(const char *lib_path)
106 | {
107 |     void *dl = dlopen(lib_path, RTLD_LAZY);
108 |     char *error;
109 | 
{% endraw %}

```
### test/apps/dlopen.c

```c

{% raw %}
15 |     void *handle;
16 | 
17 |     printf("opening '%s'\n", filename);
18 |     handle = dlopen(filename, RTLD_LAZY);
19 |     if (handle == NULL) {
20 |         fprintf(stderr, "failed to open %s: %m\n", filename);
{% endraw %}

```