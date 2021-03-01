---
name: "libblastrampoline"
layout: package
next_package: None
previous_package: None
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 2.2.0
4 / 272 files match, 1 filtered matches.

 - [src/dl_utils.c](#srcdl_utilsc)

### src/dl_utils.c

```c

{% raw %}
64 | #if defined(_OS_WINDOWS_)
65 |     return GetProcAddress((HMODULE) handle, symbol_name);
66 | #else
67 |     return dlsym((void *)handle, symbol_name);
68 | #endif
69 | }
{% endraw %}

```