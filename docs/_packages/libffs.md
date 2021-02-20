---
name: "libffs"
layout: package
next_package: libfuse
previous_package: libfastcommon
languages: ['c']
---
## 1.5
1 / 214 files match, 1 filtered matches.

 - [cod/standard.c](#codstandardc)

### cod/standard.c

```c

{% raw %}
683 |     char *name = malloc(strlen(libname) + strlen(LIBRARY_EXT) + 1);
684 |     strcpy(name, libname);
685 |     strcat(name, LIBRARY_EXT);
686 |     void *handle = dlopen(name, RTLD_LAZY);
687 |     free(name);
688 |     while(externs[i].extern_name) {
{% endraw %}

```