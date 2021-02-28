---
name: "curl"
layout: package
next_package: dpdk
previous_package: libcanberra
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 7.60.0
3 / 1678 files match, 1 filtered matches.

 - [packages/vms/report_openssl_version.c](#packagesvmsreport_openssl_versionc)

### packages/vms/report_openssl_version.c

```c

{% raw %}
53 | 
54 |    libptr = dlopen(argv[1], 0);
55 | 
56 |    ssl_version = (const char * (*)(int))dlsym(libptr, "SSLeay_version");
57 |    if ((void *)ssl_version == NULL) {
58 |       ssl_version = (const char * (*)(int))dlsym(libptr, "ssleay_version");
59 |       if ((void *)ssl_version == NULL) {
60 |          ssl_version = (const char * (*)(int))dlsym(libptr, "SSLEAY_VERSION");
61 |       }
62 |    }
{% endraw %}

```