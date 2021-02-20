---
name: "openssh"
layout: package
next_package: openssl
previous_package: openscenegraph
languages: ['c']
---
## 7.9p1
2 / 674 files match, 1 filtered matches.

 - [ssh-pkcs11.c](#ssh-pkcs11c)

### ssh-pkcs11.c

```c

{% raw %}
607 | 		goto fail;
608 | 	}
609 | 	/* open shared pkcs11-libarary */
610 | 	if ((handle = dlopen(provider_id, RTLD_NOW)) == NULL) {
611 | 		error("dlopen %s failed: %s", provider_id, dlerror());
612 | 		goto fail;
613 | 	}
{% endraw %}

```