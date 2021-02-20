---
name: "libical"
layout: package
next_package: libkcapi
previous_package: libibumad
languages: ['c']
---
## 3.0.8
1 / 985 files match, 1 filtered matches.

 - [src/libicalss/icalset.c](#srclibicalssicalsetc)

### src/libicalss/icalset.c

```c

{% raw %}
147 |     char *dlerr;
148 |     icalset *icalset_init_ptr;
149 | 
150 |     if ((modh = dlopen(file, RTLD_NOW)) == 0) {
151 |         perror("dlopen");
152 |         return 0;
153 |     }
{% endraw %}

```