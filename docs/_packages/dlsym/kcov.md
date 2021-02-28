---
name: "kcov"
layout: package
next_package: llvm
previous_package: 3proxy
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['cpp', 'c']
---
## 38
3 / 283 files match, 3 filtered matches.

 - [src/engines/bash-execve-redirector.c](#srcenginesbash-execve-redirectorc)
 - [src/solib-parser/lib.c](#srcsolib-parserlibc)
 - [tests/dlopen/dlopen.cc](#testsdlopendlopencc)

### src/engines/bash-execve-redirector.c

```c

{% raw %}
38 | 	{ '-', 'x', '\0' };
39 | 
40 | 	if (!orig_execve)
41 | 		orig_execve = dlsym(RTLD_NEXT, "execve");
42 | 
43 | 	sizeRead = peek_file(filename, startBytes, sizeof(startBytes));
{% endraw %}

```
### src/solib-parser/lib.c

```c

{% raw %}
106 | 	void *out;
107 | 
108 | 	if (!orig_dlopen)
109 | 		orig_dlopen = dlsym(RTLD_NEXT, "dlopen");
110 | 
111 | 	out = orig_dlopen(filename, flag);
{% endraw %}

```
### tests/dlopen/dlopen.cc

```cpp

{% raw %}
13 | 	}
14 | 
15 | 	dlerror();
16 | 	sym = (int (*)(int))dlsym(handle, "vobb");
17 | 	if (!sym) {
18 | 		printf("No symbol\n");
{% endraw %}

```