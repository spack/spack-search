---
name: "hsakmt-roct"
layout: package
next_package: htslib
previous_package: hpx5
languages: ['c']
---
## 4.0.0
1 / 146 files match, 1 filtered matches.

 - [tests/reopen/kmtreopen.c](#testsreopenkmtreopenc)

### tests/reopen/kmtreopen.c

```c

{% raw %}
89 |         handle = dlopen("libhsakmt.so", RTLD_LAZY);
91 |             fprintf(stderr, "dlopen failed: %s\n", dlerror());
{% endraw %}

```