---
name: "libkcapi"
layout: package
next_package: liblbxutil
previous_package: libexif
languages: ['c']
---
## 1.1.4
1 / 103 files match

 - [apps/kcapi-hasher.c](#appskcapi-hasherc)

### apps/kcapi-hasher.c

```c

{% raw %}
736 | 		dl = dlopen(selfname, RTLD_NODELETE|RTLD_NOLOAD|RTLD_LAZY);
738 | 			fprintf(stderr, "dlopen of file %s failed\n", selfname);
{% endraw %}

```