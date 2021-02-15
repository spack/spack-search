---
name: "libical"
layout: package
next_package: libhio
previous_package: liboldx
languages: ['cpp']
---
## 3.0.8
1 / 985 files match

 - [src/libicalss/icalset.c](#srclibicalssicalsetc)

### src/libicalss/icalset.c

```cpp

{% raw %}
47 | /* #define _DLOPEN_TEST */
48 | #if defined(_DLOPEN_TEST)
134 | #if defined(_DLOPEN_TEST)
150 |     if ((modh = dlopen(file, RTLD_NOW)) == 0) {
151 |         perror("dlopen");
244 | #if defined(_DLOPEN_TEST)
{% endraw %}

```