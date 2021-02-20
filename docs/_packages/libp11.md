---
name: "libp11"
layout: package
next_package: libpam
previous_package: libnl
languages: ['c']
---
## 0.4.10
2 / 85 files match, 1 filtered matches.

 - [src/libpkcs11.c](#srclibpkcs11c)

### src/libpkcs11.c

```c

{% raw %}
63 | #ifdef WIN32
64 | 	mod->handle = LoadLibraryA(mspec);
65 | #else
66 | 	mod->handle = dlopen(mspec, RTLD_LAZY | RTLD_LOCAL);
67 | #endif
68 | 
{% endraw %}

```