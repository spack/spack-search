---
name: "libfastcommon"
layout: package
next_package: libffs
previous_package: libfabric
languages: ['c']
---
## 1.0.40
1 / 108 files match, 1 filtered matches.

 - [src/ini_file_reader.c](#srcini_file_readerc)

### src/ini_file_reader.c

```c

{% raw %}
883 |         return ENOENT;
884 |     }
885 | 
886 |     dlhandle = dlopen(library, RTLD_LAZY);
887 |     if (dlhandle == NULL)
888 |     {
889 |         logError("file: "__FILE__", line: %d, "
890 |                 "dlopen %s fail, error info: %s",
891 |                 __LINE__, library != NULL ? library : "",
892 |                 dlerror());
{% endraw %}

```