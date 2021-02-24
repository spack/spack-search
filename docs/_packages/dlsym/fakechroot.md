---
name: "fakechroot"
layout: package
next_package: alsa-lib
previous_package: stat
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 2.20.1
4 / 293 files match, 1 filtered matches.

 - [src/libfakechroot.c](#srclibfakechrootc)

### src/libfakechroot.c

```c

{% raw %}
142 | LOCAL fakechroot_wrapperfn_t fakechroot_loadfunc (struct fakechroot_wrapper * w)
143 | {
144 |     char *msg;
145 |     if (!(w->nextfunc = dlsym(RTLD_NEXT, w->name))) {;
146 |         msg = dlerror();
147 |         fprintf(stderr, "%s: %s: %s\n", PACKAGE, w->name, msg != NULL ? msg : "unresolved symbol");
{% endraw %}

```