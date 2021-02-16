---
name: "rhash"
layout: package
next_package: hunspell
previous_package: simgrid
languages: ['c']
---
## 1.3.5
1 / 155 files match, 1 filtered matches.

 - [librhash/plug_openssl.c](#librhashplug_opensslc)

### librhash/plug_openssl.c

```c

{% raw %}
151 | 	void* handle = dlopen("libcrypto.so", RTLD_NOW);
152 | 	if (!handle) handle = dlopen("libcrypto.so.1.1", RTLD_NOW);
153 | 	if (!handle) handle = dlopen("libcrypto.so.1.0.2", RTLD_NOW);
154 | 	if (!handle) handle = dlopen("libcrypto.so.1.0.0", RTLD_NOW);
155 | 	if (!handle) handle = dlopen("libcrypto.so.0.9.8", RTLD_NOW);
{% endraw %}

```