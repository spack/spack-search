---
name: "libkcapi"
layout: package
next_package: libmicrohttpd
previous_package: libiberty
library_name: dlopen
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 1.1.4
1 / 103 files match, 1 filtered matches.

 - [apps/kcapi-hasher.c](#appskcapi-hasherc)

### apps/kcapi-hasher.c

```c

{% raw %}
733 | 		memset(selfname, 0, sizeof(selfname));
734 | 		snprintf(selfname, (sizeof(selfname) - 1), "libkcapi.so.%u",
735 | 		         KCAPI_MAJVERSION);
736 | 		dl = dlopen(selfname, RTLD_NODELETE|RTLD_NOLOAD|RTLD_LAZY);
737 | 		if (dl == NULL) {
738 | 			fprintf(stderr, "dlopen of file %s failed\n", selfname);
739 | 			ret = -EFAULT;
740 | 			goto out;
{% endraw %}

```