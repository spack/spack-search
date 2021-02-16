---
name: "openssh"
layout: package
next_package: py-pyopenssl
previous_package: py-shapely
languages: ['c']
---
## 7.9p1
2 / 674 files match, 1 filtered matches.

 - [ssh-pkcs11.c](#ssh-pkcs11c)

### ssh-pkcs11.c

```c

{% raw %}
610 | 	if ((handle = dlopen(provider_id, RTLD_NOW)) == NULL) {
611 | 		error("dlopen %s failed: %s", provider_id, dlerror());
{% endraw %}

```