---
name: "elfutils"
layout: package
next_package: aspell
previous_package: libpam
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 0.180
1 / 1398 files match, 1 filtered matches.

 - [libdwfl/debuginfod-client.c](#libdwfldebuginfod-clientc)

### libdwfl/debuginfod-client.c

```c

{% raw %}
107 | 
108 |   if (debuginfod_so != NULL)
109 |     {
110 |       fp_debuginfod_begin = dlsym (debuginfod_so, "debuginfod_begin");
111 |       fp_debuginfod_find_executable = dlsym (debuginfod_so,
112 | 					     "debuginfod_find_executable");
113 |       fp_debuginfod_find_debuginfo = dlsym (debuginfod_so,
114 | 					    "debuginfod_find_debuginfo");
115 |       fp_debuginfod_end = dlsym (debuginfod_so, "debuginfod_end");
116 | 
117 |       /* We either get them all, or we get none.  */
{% endraw %}

```