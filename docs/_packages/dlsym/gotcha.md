---
name: "gotcha"
layout: package
next_package: slurm
previous_package: libxsmm
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 0.0.2
2 / 64 files match, 1 filtered matches.

 - [test/dlopen/test_dlopen.c](#testdlopentest_dlopenc)

### test/dlopen/test_dlopen.c

```c

{% raw %}
61 |    }
62 | 
63 |    /* Test 1: Check if a dlsym generated indirect call gets re-routed by gotcha */
64 |    retfour = (int (*)(void)) dlsym(libnum, "return_four");
65 |    if (retfour() != 4) {
66 |       fprintf(stderr, "ERROR: dlsym returned original function, not wrapped\n");
67 |       had_error = -1;
68 |    }
69 | 
70 |    /* Test 2: Does a call in a dlopen'd library get rerouted by gotcha */
71 |    test_retfive = (int (*)(void)) dlsym(libnum, "test_return_five");
72 |    if (test_retfive() != 5) {
73 |       fprintf(stderr, "ERROR: call to return_five in libnum.so was not wrapped by correct_return_five\n");
{% endraw %}

```