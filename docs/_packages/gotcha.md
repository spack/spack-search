---
name: "gotcha"
layout: package
next_package: gpdb
previous_package: goblin-hmc-sim
languages: ['c']
---
## 0.0.2
5 / 64 files match, 1 filtered matches.

 - [test/dlopen/test_dlopen.c](#testdlopentest_dlopenc)

### test/dlopen/test_dlopen.c

```c

{% raw %}
48 |    int had_error = 0;
49 |    int result;
50 | 
51 |    result = gotcha_wrap(funcs, 2, "dlopen_test");
52 |    if (result != 0) {
53 |       fprintf(stderr, "ERROR: gotcha_wrap returned error code %d\n", result);
54 |       return -1;
55 |    }
56 | 
57 |    libnum = dlopen("libnum.so", RTLD_NOW);
58 |    if (!libnum) {
59 |       fprintf(stderr, "ERROR: Test failed to dlopen libnum.so\n");
60 |       return -1;
61 |    }
{% endraw %}

```