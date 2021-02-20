---
name: "ntirpc"
layout: package
next_package: nvhpc
previous_package: nspr
languages: ['c']
---
## 3.0
2 / 199 files match, 1 filtered matches.

 - [src/lttng/main.c](#srclttngmainc)

### src/lttng/main.c

```c

{% raw %}
52 | #include "lttng/xprt.h"
53 | 
54 | /* This is a hack to make older versions of LTTng link */
55 | struct lttng_ust_tracepoint_dlopen tracepoint_dlopen
56 | 	__attribute__((weak));
57 | 
{% endraw %}

```