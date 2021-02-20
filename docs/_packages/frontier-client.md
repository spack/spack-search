---
name: "frontier-client"
layout: package
next_package: fuse-overlayfs
previous_package: freebayes
languages: ['c']
---
## 2_9_0
1 / 155 files match, 1 filtered matches.

 - [client/pacparser-dlopen.c](#clientpacparser-dlopenc)

### client/pacparser-dlopen.c

```c

{% raw %}
50 | 
51 |   /* add .1 on the end because if the API ever changes in an incompatible
52 |    * way they're supposed to change it to .2  */
53 |   pp_dlhandle=dlopen("libpacparser.so.1",RTLD_LAZY);
54 |   if(!pp_dlhandle)
55 |    {
56 |     frontier_setErrorMsg(__FILE__,__LINE__,
57 |        "config error: cannot dlopen %s",dlerror());
58 |     return FRONTIER_ECFG;
59 |    }
{% endraw %}

```