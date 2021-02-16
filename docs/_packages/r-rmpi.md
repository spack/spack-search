---
name: "r-rmpi"
layout: package
next_package: r-rsqlite
previous_package: r-rhtslib
languages: ['c']
---
## 0.6-9
1 / 74 files match, 1 filtered matches.

 - [src/Rmpi.c](#srcrmpic)

### src/Rmpi.c

```c

{% raw %}
76 |     if (!dlopen("libmpi.so.1", RTLD_GLOBAL | RTLD_LAZY) 
77 | 	&& !dlopen("libmpi.so.0", RTLD_GLOBAL | RTLD_LAZY)
78 | 	&& !dlopen("libmpi.so", RTLD_GLOBAL | RTLD_LAZY)) {
{% endraw %}

```