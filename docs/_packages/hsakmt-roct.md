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
86 |     for (i = 0; i < 5; i++) {
87 |         printf("Iteration %d:\n  Loading libhsakmt.so\n", i+1);
88 | 
89 |         handle = dlopen("libhsakmt.so", RTLD_LAZY);
90 |         if (handle == NULL) {
91 |             fprintf(stderr, "dlopen failed: %s\n", dlerror());
92 |             exit(1);
93 |         }
{% endraw %}

```