---
name: "libblastrampoline"
layout: package
next_package: libbsd
previous_package: lftp
library_name: dlopen
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 2.2.0
5 / 272 files match, 1 filtered matches.

 - [src/dl_utils.c](#srcdl_utilsc)

### src/dl_utils.c

```c

{% raw %}
35 | #else
36 |     // If we have `RTLD_DEEPBIND`, use it!
37 | #if defined(RTLD_DEEPBIND)
38 |     new_handle = dlopen(path, RTLD_NOW | RTLD_LOCAL | RTLD_DEEPBIND);
39 | #else
40 |     new_handle = dlopen(path, RTLD_NOW | RTLD_LOCAL);
41 | #endif
42 | #endif
{% endraw %}

```