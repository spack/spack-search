---
name: "fakechroot"
layout: package
next_package: nix
previous_package: fio
library_name: dlopen
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 2.20.1
9 / 293 files match, 1 filtered matches.

 - [src/dlopen.c](#srcdlopenc)

### src/dlopen.c

```c

{% raw %}
24 | #include "libfakechroot.h"
25 | 
26 | 
27 | wrapper(dlopen, void *, (const char * filename, int flag))
28 | {
29 |     char fakechroot_abspath[FAKECHROOT_PATH_MAX];
30 |     char fakechroot_buf[FAKECHROOT_PATH_MAX];
31 |     debug("dlopen(\"%s\", %d)", filename, flag);
32 |     if (filename && strchr(filename, '/') != NULL) {
33 |         expand_chroot_path(filename);
34 |         debug("dlopen(\"%s\", %d)", filename, flag);
35 |     }
36 |     return nextcall(dlopen)(filename, flag);
37 | }
38 | 
{% endraw %}

```