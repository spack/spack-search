---
name: "imlib2"
layout: package
next_package: rdma-core
previous_package: gts
languages: ['c']
---
## 1.5.1
7 / 157 files match, 2 filtered matches.

 - [src/lib/image.c](#srclibimagec)
 - [src/lib/dynamic_filters.c](#srclibdynamic_filtersc)

### src/lib/image.c

```c

{% raw %}
573 |    l->handle = dlopen(file, RTLD_NOW | RTLD_LOCAL);
{% endraw %}

```
### src/lib/dynamic_filters.c

```c

{% raw %}
38 |    ptr->handle = dlopen(file, RTLD_NOW | RTLD_LOCAL);
{% endraw %}

```