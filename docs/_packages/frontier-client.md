---
name: "frontier-client"
layout: package
next_package: fuse-overlayfs
previous_package: foundationdb
languages: ['c']
---
## 2_9_0
1 / 155 files match, 1 filtered matches.

 - [client/pacparser-dlopen.c](#clientpacparser-dlopenc)

### client/pacparser-dlopen.c

```c

{% raw %}
53 |   pp_dlhandle=dlopen("libpacparser.so.1",RTLD_LAZY);
57 |        "config error: cannot dlopen %s",dlerror());
{% endraw %}

```