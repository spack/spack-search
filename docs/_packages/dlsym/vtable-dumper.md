---
name: "vtable-dumper"
layout: package
next_package: lighttpd
previous_package: laszip
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 1.0
1 / 2 files match, 1 filtered matches.

 - [dump-vtable.c](#dump-vtablec)

### dump-vtable.c

```c

{% raw %}
175 |     printf("%s\n", demngl);
176 |     free(demngl);
177 |     
178 |     vtablep = dlsym(dlhndl, vtable->name);
179 |     
180 |     vtbaseoffset = vtablep->cat1.baseoffset;
{% endraw %}

```