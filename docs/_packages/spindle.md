---
name: "spindle"
layout: package
next_package: spot
previous_package: sox
languages: ['c']
---
## 0.8.1
5 / 148 files match, 1 filtered matches.

 - [testsuite/test_driver.c](#testsuitetest_driverc)

### testsuite/test_driver.c

```c

{% raw %}
67 |    om_unset,
68 |    om_ldpreload,
69 |    om_dependency,
70 |    om_dlopen,
71 |    om_dlreopen,
72 |    om_reorder,
161 |    char *fullpath, *result;
162 |    test_printf("dlstart %s\n", libraries[i].libname);
163 |    fullpath = libpath(libraries[i].libname);
164 |    result = dlopen(fullpath, RTLD_LAZY | RTLD_GLOBAL);
165 |    if (libraries[i].flags & FLAGS_NOEXIST) {
166 |       if (result != 0)
172 |    }
173 |    libraries[i].opened = DLOPENED;
174 |    if (!result) {
175 |       err_printf("Failed to dlopen library %s: %s\n", fullpath, dlerror());
176 |       return;
177 |    }
221 |    }
222 | }
223 | 
224 | void dlopen_mode()
225 | {
226 |    int i;
232 | void dlreopen_mode()
233 | {
234 |    dependency_mode();
235 |    dlopen_mode();
236 | }
237 | 
385 |       case om_dependency:
386 |          dependency_mode();
387 |          break;
388 |       case om_dlopen:
389 |          dlopen_mode();
390 |          break;
391 |       case om_dlreopen:
425 |    for (i = 0; i < argc; i++) {
426 |       TEST_ARG(ldpreload);
427 |       TEST_ARG(dependency);
428 |       TEST_ARG(dlopen);
429 |       TEST_ARG(dlreopen);
430 |       TEST_ARG(reorder);
473 |       if (libraries[i].opened == UNLOADED)
474 |          continue;
475 |       if (libraries[i].opened == DLOPENED && !libraries[i].dlhandle)
476 |          err_printf("Failed to dlopen library %s\n", libraries[i].libname);
477 |       if (!libraries[i].calc_func) {
478 |          err_printf("Failed to run library constructor in %s\n", libraries[i].libname);
{% endraw %}

```