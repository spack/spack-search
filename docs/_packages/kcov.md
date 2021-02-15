---
name: "kcov"
layout: package
next_package: gettext
previous_package: opa-psm2
languages: ['cpp', 'python']
---
## 38
5 / 283 files match

 - [src/solib-parser/lib.c](#srcsolib-parserlibc)
 - [tests/CMakeLists.txt](#testscmakeliststxt)
 - [tests/dlopen/dlopen.cc](#testsdlopendlopencc)
 - [tests/dlopen/dlopen-main.cc](#testsdlopendlopen-maincc)
 - [tests/tools/compiled.py](#teststoolscompiledpy)

### src/solib-parser/lib.c

```cpp

{% raw %}
103 | static void *(*orig_dlopen)(const char *, int);
104 | void *dlopen(const char *filename, int flag)
108 | 	if (!orig_dlopen)
109 | 		orig_dlopen = dlsym(RTLD_NEXT, "dlopen");
111 | 	out = orig_dlopen(filename, flag);
{% endraw %}

```
### tests/CMakeLists.txt

```

{% raw %}
145 | add_executable(dlopen dlopen/dlopen.cc dlopen/dlopen-main.cc)
146 | target_link_libraries(dlopen "${DL_LIBRARY}")
{% endraw %}

```
### tests/dlopen/dlopen.cc

```cpp

{% raw %}
4 | void do_dlopen()
9 | 	handle = dlopen("libshared_library.so", RTLD_LAZY);
11 | 		printf("Can't dlopen\n");
{% endraw %}

```
### tests/dlopen/dlopen-main.cc

```cpp

{% raw %}
4 | extern void do_dlopen();
8 | 	do_dlopen();
{% endraw %}

```
### tests/tools/compiled.py

```python

{% raw %}
411 | class dlopen(testbase.KcovTestCase):
415 |         noKcovRv,o = self.do(testbase.testbuild + "/dlopen", False)
416 |         rv,o = self.do(testbase.kcov + " " + testbase.outbase + "/kcov " + testbase.testbuild + "/dlopen", False)
419 |         dom = parse_cobertura.parseFile(testbase.outbase + "/kcov/dlopen/cobertura.xml")
420 |         assert parse_cobertura.hitsPerLine(dom, "dlopen.cc", 11) == 1
421 |         assert parse_cobertura.hitsPerLine(dom, "dlopen.cc", 12) == 0
426 | class dlopen_in_ignored_source_file(testbase.KcovTestCase):
430 |         rv,o = self.do(testbase.kcov + " --exclude-pattern=dlopen.cc " + testbase.outbase + "/kcov " + testbase.testbuild + "/dlopen", False)
431 |         dom = parse_cobertura.parseFile(testbase.outbase + "/kcov/dlopen/cobertura.xml")
432 |         assert parse_cobertura.hitsPerLine(dom, "dlopen-main.cc", 10) == 1
{% endraw %}

```