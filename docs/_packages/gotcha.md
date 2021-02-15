---
name: "gotcha"
layout: package
next_package: libdmx
previous_package: pango
languages: ['yaml', 'cpp']
---
## 0.0.2
5 / 64 files match

 - [.travis.yml](#travisyml)
 - [README.md](#readmemd)
 - [test/CMakeLists.txt](#testcmakeliststxt)
 - [test/dlopen/test_dlopen.c](#testdlopentest_dlopenc)
 - [test/dlopen/CMakeLists.txt](#testdlopencmakeliststxt)

### .travis.yml

```yaml

{% raw %}
82 |   - ctest --verbose -E dlopen
{% endraw %}

```
### README.md

```

{% raw %}
20 |   * Gotcha does not yet support dlopen, either wrapping symbols looked up by dlsym or modifying dlopen'd libraries.
{% endraw %}

```
### test/CMakeLists.txt

```

{% raw %}
3 | add_subdirectory(dlopen)
{% endraw %}

```
### test/dlopen/test_dlopen.c

```cpp

{% raw %}
51 |    result = gotcha_wrap(funcs, 2, "dlopen_test");
57 |    libnum = dlopen("libnum.so", RTLD_NOW);
59 |       fprintf(stderr, "ERROR: Test failed to dlopen libnum.so\n");
70 |    /* Test 2: Does a call in a dlopen'd library get rerouted by gotcha */
{% endraw %}

```
### test/dlopen/CMakeLists.txt

```

{% raw %}
1 | add_executable(test_dlopen test_dlopen.c)
2 | target_link_libraries(test_dlopen gotcha dl)
3 | gotcha_add_test(dlopen_test test_dlopen)
{% endraw %}

```