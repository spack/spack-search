---
name: "frontier-client"
layout: package
next_package: spades
previous_package: cvs
languages: ['cpp']
---
## 2_9_0
1 / 155 files match

 - [client/pacparser-dlopen.c](#clientpacparser-dlopenc)

### client/pacparser-dlopen.c

```cpp

{% raw %}
1 |  * pacparser dlopen interface
53 |   pp_dlhandle=dlopen("libpacparser.so.1",RTLD_LAZY);
57 |        "config error: cannot dlopen %s",dlerror());
{% endraw %}

```