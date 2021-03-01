---
name: "fakechroot"
layout: package
next_package: gdb
previous_package: None
library_name: dlmopen
matches: ['dlsym', 'dlopen', 'dlmopen']
languages: ['c']
---
## 2.20.1
5 / 293 files match, 1 filtered matches.

 - [src/dlmopen.c](#srcdlmopenc)

### src/dlmopen.c

```c

{% raw %}
26 | #include "libfakechroot.h"
27 | 
28 | 
29 | wrapper(dlmopen, void *, (Lmid_t nsid, const char * filename, int flag))
30 | {
31 |     char fakechroot_abspath[FAKECHROOT_PATH_MAX];
32 |     char fakechroot_buf[FAKECHROOT_PATH_MAX];
33 |     debug("dlmopen(&nsid, \"%s\", %d)", filename, flag);
34 |     expand_chroot_path(filename);
35 |     return nextcall(dlmopen)(nsid, filename, flag);
36 | }
37 | 
{% endraw %}

```