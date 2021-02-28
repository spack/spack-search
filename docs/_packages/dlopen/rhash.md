---
name: "rhash"
layout: package
next_package: meson
previous_package: bcftools
library_name: dlopen
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 1.3.5
1 / 155 files match, 1 filtered matches.

 - [librhash/plug_openssl.c](#librhashplug_opensslc)

### librhash/plug_openssl.c

```c

{% raw %}
148 | 
149 | 	SetErrorMode(oldErrorMode); /* restore error mode */
150 | #else
151 | 	void* handle = dlopen("libcrypto.so", RTLD_NOW);
152 | 	if (!handle) handle = dlopen("libcrypto.so.1.1", RTLD_NOW);
153 | 	if (!handle) handle = dlopen("libcrypto.so.1.0.2", RTLD_NOW);
154 | 	if (!handle) handle = dlopen("libcrypto.so.1.0.0", RTLD_NOW);
155 | 	if (!handle) handle = dlopen("libcrypto.so.0.9.8", RTLD_NOW);
156 | #endif
157 | 
{% endraw %}

```