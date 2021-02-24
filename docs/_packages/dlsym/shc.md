---
name: "shc"
layout: package
next_package: collectd
previous_package: wt
library_name: dlsym
matches: ['dlsym']
languages: ['c']
---
## 4.0.3
1 / 16 files match, 1 filtered matches.

 - [src/shc.c](#srcshcc)

### src/shc.c

```c

{% raw %}
204 | "\"    int n;\",",
205 | "\"\",",
206 | "\"    if (!real___libc_start_main) {\",",
207 | "\"        real___libc_start_main = dlsym(RTLD_NEXT, \\\"__libc_start_main\\\");\",",
208 | "\"        if (!real___libc_start_main) abort();\",",
209 | "\"    }\",",
{% endraw %}

```