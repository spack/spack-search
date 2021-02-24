---
name: "curl"
layout: package
next_package: libcanberra
previous_package: boost
library_name: dlopen
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 7.60.0
5 / 1678 files match, 1 filtered matches.

 - [packages/vms/report_openssl_version.c](#packagesvmsreport_openssl_versionc)

### packages/vms/report_openssl_version.c

```c

{% raw %}
51 |        exit(1);
52 |    }
53 | 
54 |    libptr = dlopen(argv[1], 0);
55 | 
56 |    ssl_version = (const char * (*)(int))dlsym(libptr, "SSLeay_version");
{% endraw %}

```