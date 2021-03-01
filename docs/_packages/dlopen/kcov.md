---
name: "kcov"
layout: package
next_package: keepalived
previous_package: kaldi
library_name: dlopen
matches: ['dlsym', 'dlopen']
languages: ['cpp', 'python', 'c']
---
## 38
5 / 283 files match, 4 filtered matches.

 - [src/solib-parser/lib.c](#srcsolib-parserlibc)
 - [tests/dlopen/dlopen.cc](#testsdlopendlopencc)
 - [tests/dlopen/dlopen-main.cc](#testsdlopendlopen-maincc)
 - [tests/tools/compiled.py](#teststoolscompiledpy)

### src/solib-parser/lib.c

```c

{% raw %}
100 | 			);
101 | }
102 | 
103 | static void *(*orig_dlopen)(const char *, int);
104 | void *dlopen(const char *filename, int flag)
105 | {
106 | 	void *out;
107 | 
108 | 	if (!orig_dlopen)
109 | 		orig_dlopen = dlsym(RTLD_NEXT, "dlopen");
110 | 
111 | 	out = orig_dlopen(filename, flag);
112 | 
113 | 	parse_solibs();
{% endraw %}

```
### tests/dlopen/dlopen.cc

```cpp

{% raw %}
1 | #include <stdio.h>
2 | #include <stdlib.h>
3 | 
4 | void do_dlopen()
5 | {
6 | 	void *handle;
7 | 	int (*sym)(int);
8 | 
9 | 	handle = dlopen("libshared_library.so", RTLD_LAZY);
10 | 	if (!handle) {
11 | 		printf("Can't dlopen\n");
12 | 		exit(1);
13 | 	}
{% endraw %}

```
### tests/dlopen/dlopen-main.cc

```cpp

{% raw %}
1 | #include <stdlib.h>
2 | #include <unistd.h>
3 | 
4 | extern void do_dlopen();
5 | 
6 | int main(int argc, const char *argv[])
7 | {
8 | 	do_dlopen();
9 | 	sleep(1);
10 | 
{% endraw %}

```
### tests/tools/compiled.py

```python

{% raw %}
408 |         dom = parse_cobertura.parseFile(testbase.outbase + "/kcov/main-collect-only/cobertura.xml")
409 |         assert parse_cobertura.hitsPerLine(dom, "main.cc", 1) == 1
410 | 
411 | class dlopen(testbase.KcovTestCase):
412 |     @unittest.expectedFailure
413 |     def runTest(self):
414 |         self.setUp()
415 |         noKcovRv,o = self.do(testbase.testbuild + "/dlopen", False)
416 |         rv,o = self.do(testbase.kcov + " " + testbase.outbase + "/kcov " + testbase.testbuild + "/dlopen", False)
417 | 
418 |         assert noKcovRv == rv
419 |         dom = parse_cobertura.parseFile(testbase.outbase + "/kcov/dlopen/cobertura.xml")
420 |         assert parse_cobertura.hitsPerLine(dom, "dlopen.cc", 11) == 1
421 |         assert parse_cobertura.hitsPerLine(dom, "dlopen.cc", 12) == 0
422 |         assert parse_cobertura.hitsPerLine(dom, "solib.c", 5) == 1
423 |         assert parse_cobertura.hitsPerLine(dom, "solib.c", 12) == 0
424 | 
425 | 
426 | class dlopen_in_ignored_source_file(testbase.KcovTestCase):
427 |     @unittest.expectedFailure
428 |     def runTest(self):
429 |         self.setUp()
430 |         rv,o = self.do(testbase.kcov + " --exclude-pattern=dlopen.cc " + testbase.outbase + "/kcov " + testbase.testbuild + "/dlopen", False)
431 |         dom = parse_cobertura.parseFile(testbase.outbase + "/kcov/dlopen/cobertura.xml")
432 |         assert parse_cobertura.hitsPerLine(dom, "dlopen-main.cc", 10) == 1
433 |         assert parse_cobertura.hitsPerLine(dom, "solib.c", 5) == 1
434 |         assert parse_cobertura.hitsPerLine(dom, "solib.c", 12) == 0
{% endraw %}

```