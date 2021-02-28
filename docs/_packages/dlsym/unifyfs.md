---
name: "unifyfs"
layout: package
next_package: parsec
previous_package: dyninst
library_name: dlsym
matches: ['dlsym', 'dlopen', 'dlmopen']
languages: ['c']
---
## 0.9.1
3 / 259 files match, 1 filtered matches.

 - [client/src/unifyfs-internal.h](#clientsrcunifyfs-internalh)

### client/src/unifyfs-internal.h

```c

{% raw %}
177 | #define MAP_OR_FAIL(func) \
178 |         if (!(__real_ ## func)) \
179 |         { \
180 |             __real_ ## func = dlsym(RTLD_NEXT, #func); \
181 |             if (!(__real_ ## func)) { \
182 |                fprintf(stderr, "UNIFYFS failed to map symbol: %s\n", #func); \
{% endraw %}

```