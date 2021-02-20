---
name: "efivar"
layout: package
next_package: elfutils
previous_package: e2fsprogs
languages: ['c']
---
## 35
1 / 92 files match, 1 filtered matches.

 - [src/guid.c](#srcguidc)

### src/guid.c

```c

{% raw %}
249 | __attribute__((__visibility__ ("default")))
250 | efi_symbol_to_guid(const char *symbol, efi_guid_t *guid)
251 | {
252 | 	void *dlh = dlopen(NULL, RTLD_LAZY);
253 | 	if (!dlh)
254 | 		return -1;
{% endraw %}

```