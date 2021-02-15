---
name: "libssh"
layout: package
next_package: berkeley-db
previous_package: thepeg
languages: []
---
## 0.8.5
1 / 320 files match

 - [tests/valgrind.supp](#testsvalgrindsupp)

### tests/valgrind.supp

```

{% raw %}
20 |    glibc_dlopen_getdelim_selinux
31 |    glibc_dlopen_alloc
35 |    fun:dlopen@@GLIBC_2.2.5
138 |    openssl_FIPS_dlopen_leak
143 |    fun:dlopen*
{% endraw %}

```