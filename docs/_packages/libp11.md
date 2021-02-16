---
name: "libp11"
layout: package
next_package: sfcgal
previous_package: harfbuzz
languages: ['c']
---
## 0.4.10
2 / 85 files match, 1 filtered matches.

 - [src/libpkcs11.c](#srclibpkcs11c)

### src/libpkcs11.c

```c

{% raw %}
66 | 	mod->handle = dlopen(mspec, RTLD_LAZY | RTLD_LOCAL);
{% endraw %}

```