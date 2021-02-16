---
name: "gotcha"
layout: package
next_package: libdmx
previous_package: pango
languages: ['c']
---
## 0.0.2
5 / 64 files match, 1 filtered matches.

 - [test/dlopen/test_dlopen.c](#testdlopentest_dlopenc)

### test/dlopen/test_dlopen.c

```c

{% raw %}
51 |    result = gotcha_wrap(funcs, 2, "dlopen_test");
57 |    libnum = dlopen("libnum.so", RTLD_NOW);
59 |       fprintf(stderr, "ERROR: Test failed to dlopen libnum.so\n");
{% endraw %}

```