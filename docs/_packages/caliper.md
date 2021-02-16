---
name: "caliper"
layout: package
next_package: libxfont
previous_package: libtool
languages: ['c']
---
## master
4 / 597 files match, 3 filtered matches.

 - [ext/gotcha/src/gotcha_dl.h](#extgotchasrcgotcha_dlh)
 - [ext/gotcha/src/gotcha_dl.c](#extgotchasrcgotcha_dlc)
 - [ext/gotcha/src/gotcha.c](#extgotchasrcgotchac)

### ext/gotcha/src/gotcha_dl.h

```c

{% raw %}
10 | extern gotcha_wrappee_handle_t orig_dlopen_handle;
{% endraw %}

```
### ext/gotcha/src/gotcha_dl.c

```c

{% raw %}
9 | gotcha_wrappee_handle_t orig_dlopen_handle;
17 |    debug_printf(3, "Trying to re-bind %s from tool %s after dlopen\n",
28 |       debug_printf(3, "Still could not prepare binding %s after dlopen\n", binding->user_binding->name);
36 | static void* dlopen_wrapper(const char* filename, int flags) {
37 |    typeof(&dlopen_wrapper) orig_dlopen = gotcha_get_wrappee(orig_dlopen_handle);
39 |    debug_printf(1, "User called dlopen(%s, 0x%x)\n", filename, (unsigned int) flags);
40 |    handle = orig_dlopen(filename,flags);
42 |    debug_printf(2, "Searching new dlopened libraries for previously-not-found exports\n");
45 |    debug_printf(2, "Updating GOT entries for new dlopened libraries\n");
68 |   {"dlopen", dlopen_wrapper, &orig_dlopen_handle},
{% endraw %}

```
### ext/gotcha/src/gotcha.c

```c

{% raw %}
317 |            debug_printf(2, "Stashing %s in notfound_binding table to re-lookup on dlopens\n",
{% endraw %}

```