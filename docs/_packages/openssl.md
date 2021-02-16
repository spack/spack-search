---
name: "openssl"
layout: package
next_package: qemu
previous_package: libeatmydata
languages: ['c']
---
## 1.1.1i
5 / 3040 files match

 - [crypto/rand/rand_vms.c](#cryptorandrand_vmsc)
 - [crypto/dso/dso_dlfcn.c](#cryptodsodso_dlfcnc)

### crypto/rand/rand_vms.c

```c

{% raw %}
524 |         get_entropy_address = dlsym(dlopen(PUBLIC_VECTORS, 0), GET_ENTROPY);
{% endraw %}

```
### crypto/dso/dso_dlfcn.c

```c

{% raw %}
115 |     ptr = dlopen(filename, flags);
446 |     void *ret = NULL, *handle = dlopen(NULL, RTLD_LAZY);
{% endraw %}

```