---
name: "openssl"
layout: package
next_package: procps
previous_package: bcftools
library_name: dlopen
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 1.1.1i
5 / 3040 files match, 2 filtered matches.

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
112 |     if (filename[strlen(filename) - 1] == ')')
113 |         flags |= RTLD_MEMBER;
114 | # endif
115 |     ptr = dlopen(filename, flags);
116 |     if (ptr == NULL) {
117 |         DSOerr(DSO_F_DLFCN_LOAD, DSO_R_LOAD_FAILED);
443 | 
444 | static void *dlfcn_globallookup(const char *name)
445 | {
446 |     void *ret = NULL, *handle = dlopen(NULL, RTLD_LAZY);
447 | 
448 |     if (handle) {
{% endraw %}

```