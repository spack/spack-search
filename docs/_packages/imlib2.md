---
name: "imlib2"
layout: package
next_package: intel-llvm
previous_package: imagemagick
languages: ['c']
---
## 1.5.1
7 / 157 files match, 2 filtered matches.

 - [src/lib/image.c](#srclibimagec)
 - [src/lib/dynamic_filters.c](#srclibdynamic_filtersc)

### src/lib/image.c

```c

{% raw %}
570 |    l = malloc(sizeof(ImlibLoader));
571 |    l->num_formats = 0;
572 |    l->formats = NULL;
573 |    l->handle = dlopen(file, RTLD_NOW | RTLD_LOCAL);
574 |    if (!l->handle)
575 |      {
{% endraw %}

```
### src/lib/dynamic_filters.c

```c

{% raw %}
35 |    MALLOCSHOW;
36 |    ptr = malloc(sizeof(ImlibExternalFilter));
37 |    ptr->filename = strdup(file);
38 |    ptr->handle = dlopen(file, RTLD_NOW | RTLD_LOCAL);
39 |    if (!ptr->handle)
40 |      {
{% endraw %}

```