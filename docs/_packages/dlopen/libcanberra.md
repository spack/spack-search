---
name: "libcanberra"
layout: package
next_package: libfabric
previous_package: libbsd
library_name: dlopen
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 0.30
5 / 98 files match, 1 filtered matches.

 - [src/dso.c](#srcdsoc)

### src/dso.c

```c

{% raw %}
126 |                 return CA_ERROR_OOM;
127 | 
128 |         errno = 0;
129 |         p->module = lt_dlopenext(mn);
130 |         ca_free(mn);
131 | 
{% endraw %}

```