---
name: "ltrace"
layout: package
next_package: lua
previous_package: llvm-openmp
languages: ['c']
---
## 0.7.3
6 / 262 files match, 1 filtered matches.

 - [testsuite/ltrace.minor/libdl-simple.c](#testsuiteltraceminorlibdl-simplec)

### testsuite/ltrace.minor/libdl-simple.c

```c

{% raw %}
6 | 	int (*test)(int);
7 | 	char *error;
8 | 
9 | 	handle = dlopen ("liblibdl-simple.so", RTLD_LAZY);
10 | 	if (!handle) {
11 | 		fputs (dlerror(), stderr);
{% endraw %}

```