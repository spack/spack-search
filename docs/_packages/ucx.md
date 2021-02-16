---
name: "ucx"
layout: package
next_package: py-sphinx
previous_package: harminv
languages: ['c']
---
## 1.4.0
9 / 590 files match

 - [src/ucm/util/reloc.c](#srcucmutilrelocc)
 - [test/mpi/test_memhooks.c](#testmpitest_memhooksc)
 - [test/apps/dlopen.c](#testappsdlopenc)

### src/ucm/util/reloc.c

```c

{% raw %}
48 | static void * (*ucm_reloc_orig_dlopen)(const char *, int) = NULL;
271 | static void *ucm_dlopen(const char *filename, int flag)
276 |     if (ucm_reloc_orig_dlopen == NULL) {
277 |         ucm_fatal("ucm_reloc_orig_dlopen is NULL");
281 |     handle = ucm_reloc_orig_dlopen(filename, flag);
291 |             ucm_debug("in dlopen(), re-applying '%s' to %p", patch->symbol,
300 | static ucm_reloc_patch_t ucm_reloc_dlopen_patch = {
301 |     .symbol = "dlopen",
302 |     .value  = ucm_dlopen
326 | static ucs_status_t ucm_reloc_install_dlopen()
335 |     ucm_reloc_orig_dlopen = ucm_reloc_get_orig(ucm_reloc_dlopen_patch.symbol,
336 |                                                ucm_reloc_dlopen_patch.value);
338 |     status = ucm_reloc_apply_patch(&ucm_reloc_dlopen_patch);
343 |     ucs_list_add_tail(&ucm_reloc_patch_list, &ucm_reloc_dlopen_patch.list);
358 |     status = ucm_reloc_install_dlopen();
{% endraw %}

```
### test/mpi/test_memhooks.c

```c

{% raw %}
107 |     void *dl = dlopen(lib_path, RTLD_LAZY);
{% endraw %}

```
### test/apps/dlopen.c

```c

{% raw %}
18 |     handle = dlopen(filename, RTLD_LAZY);
{% endraw %}

```