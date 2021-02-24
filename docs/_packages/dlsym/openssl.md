---
name: "openssl"
layout: package
next_package: procps
previous_package: bcftools
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 1.1.1i
3 / 3040 files match, 2 filtered matches.

 - [crypto/rand/rand_vms.c](#cryptorandrand_vmsc)
 - [crypto/dso/dso_dlfcn.c](#cryptodsodso_dlfcnc)

### crypto/rand/rand_vms.c

```c

{% raw %}
521 | static int init_get_entropy_address(void)
522 | {
523 |     if (get_entropy_address_flag == 0)
524 |         get_entropy_address = dlsym(dlopen(PUBLIC_VECTORS, 0), GET_ENTROPY);
525 |     get_entropy_address_flag = 1;
526 |     return get_entropy_address != NULL;
{% endraw %}

```
### crypto/dso/dso_dlfcn.c

```c

{% raw %}
182 |         DSOerr(DSO_F_DLFCN_BIND_FUNC, DSO_R_NULL_HANDLE);
183 |         return NULL;
184 |     }
185 |     u.dlret = dlsym(ptr, symname);
186 |     if (u.dlret == NULL) {
187 |         DSOerr(DSO_F_DLFCN_BIND_FUNC, DSO_R_SYM_FAILURE);
446 |     void *ret = NULL, *handle = dlopen(NULL, RTLD_LAZY);
447 | 
448 |     if (handle) {
449 |         ret = dlsym(handle, name);
450 |         dlclose(handle);
451 |     }
{% endraw %}

```