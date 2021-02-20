---
name: "netperf"
layout: package
next_package: nettle
previous_package: netdata
languages: ['c']
---
## 2.6.0
1 / 120 files match, 1 filtered matches.

 - [src/netsec_linux.c](#srcnetsec_linuxc)

### src/netsec_linux.c

```c

{% raw %}
81 | find_security_info(int *enabled, int *type, char **specific) {
82 | 
83 |   /* first, might it be selinux? */
84 |   messiah = dlopen("libselinux.so", RTLD_LAZY);
85 |   if (NULL != messiah) {
86 |     dlerror();
{% endraw %}

```