---
name: "hsakmt-roct"
layout: package
next_package: shadow
previous_package: fftw
languages: ['cpp']
---
## 4.0.0
1 / 146 files match

 - [tests/reopen/kmtreopen.c](#testsreopenkmtreopenc)

### tests/reopen/kmtreopen.c

```cpp

{% raw %}
89 |         handle = dlopen("libhsakmt.so", RTLD_LAZY);
91 |             fprintf(stderr, "dlopen failed: %s\n", dlerror());
{% endraw %}

```