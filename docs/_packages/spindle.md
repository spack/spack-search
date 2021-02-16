---
name: "spindle"
layout: package
next_package: 3proxy
previous_package: ncurses
languages: ['c']
---
## 0.8.1
5 / 148 files match

 - [testsuite/test_driver.c](#testsuitetest_driverc)

### testsuite/test_driver.c

```c

{% raw %}
70 |    om_dlopen,
164 |    result = dlopen(fullpath, RTLD_LAZY | RTLD_GLOBAL);
175 |       err_printf("Failed to dlopen library %s: %s\n", fullpath, dlerror());
224 | void dlopen_mode()
235 |    dlopen_mode();
388 |       case om_dlopen:
389 |          dlopen_mode();
428 |       TEST_ARG(dlopen);
476 |          err_printf("Failed to dlopen library %s\n", libraries[i].libname);
{% endraw %}

```