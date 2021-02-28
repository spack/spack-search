---
name: "rhash"
layout: package
next_package: meson
previous_package: bcftools
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 1.3.5
1 / 155 files match, 1 filtered matches.

 - [librhash/plug_openssl.c](#librhashplug_opensslc)

### librhash/plug_openssl.c

```c

{% raw %}
124 | 		(pinit_t)GetProcAddress(handle, #name "_Init") : 0);
125 | #else  /* _WIN32 */
126 | #define LOAD_ADDR(n, name) \
127 | 	p##name##_final = (os_fin_t)dlsym(handle, #name "_Final"); \
128 | 	rhash_openssl_methods[n].update = (pupdate_t)dlsym(handle, #name "_Update"); \
129 | 	rhash_openssl_methods[n].init = (rhash_openssl_methods[n].update && p##name##_final ? \
130 | 		(pinit_t)dlsym(handle, #name "_Init") : 0);
131 | #endif /* _WIN32 */
132 | 
{% endraw %}

```