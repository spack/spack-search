---
name: "activeharmony"
layout: package
next_package: adios2
previous_package: ace
languages: ['c']
---
## 4.6.0
5 / 312 files match, 3 filtered matches.

 - [example/code_generation/gemm.c](#examplecode_generationgemmc)
 - [src/hinfo.c](#srchinfoc)
 - [src/hplugin.c](#srchpluginc)

### example/code_generation/gemm.c

```c

{% raw %}
393 | {
394 |     char* err_str;
395 | 
396 |     flib_eval = dlopen(filename, RTLD_LAZY);
397 |     err_str = dlerror();
398 |     if (err_str) {
{% endraw %}

```
### src/hinfo.c

```c

{% raw %}
236 |     case HINFO_INFO:
237 |         if (strchr(cmd_arg, '/')) {
238 |             // Argument includes path information.  Open the file directly.
239 |             handle = dlopen(cmd_arg, RTLD_LAZY | RTLD_LOCAL);
240 |             if (!handle) {
241 |                 fprintf(stderr, "Could not dlopen %s: %s\n",
242 |                             cmd_arg, dlerror());
243 |                 goto error;
428 |         if (!fname)
429 |             break;
430 | 
431 |         handle = dlopen(fname, RTLD_LAZY | RTLD_LOCAL);
432 |         if (handle) {
433 |             char* base = basename(fname);
501 |         if (by_filename) {
502 |             tail = strrchr(fname, '/');
503 |             if (tail && strcmp(++tail, name) == 0) {
504 |                 handle = dlopen(fname, RTLD_LAZY | RTLD_LOCAL);
505 |                 if (!handle) {
506 |                     fprintf(stderr, "Could not dlopen %s: %s\n",
507 |                             tail, dlerror());
508 |                 }
510 |             }
511 |         }
512 |         else {
513 |             handle = dlopen(fname, RTLD_LAZY | RTLD_LOCAL);
514 |             if (handle) {
515 |                 char* title = dlsym(handle, "harmony_layer_name");
{% endraw %}

```
### src/hplugin.c

```c

{% raw %}
43 |     // Tabula rasa.
44 |     memset(plugin, 0, sizeof(*plugin));
45 | 
46 |     plugin->handle = dlopen(filename, RTLD_LAZY | RTLD_LOCAL);
47 |     if (!plugin->handle) {
48 |         errstr = dlerror();
{% endraw %}

```