---
name: "libical"
layout: package
next_package: libhio
previous_package: liboldx
languages: ['c']
---
## 3.0.8
1 / 985 files match

 - [src/libicalss/icalset.c](#srclibicalssicalsetc)

### src/libicalss/icalset.c

```c

{% raw %}
150 |     if ((modh = dlopen(file, RTLD_NOW)) == 0) {
151 |         perror("dlopen");
{% endraw %}

```