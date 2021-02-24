---
name: "libkcapi"
layout: package
next_package: neuron
previous_package: rust
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 1.1.4
1 / 103 files match, 1 filtered matches.

 - [apps/kcapi-hasher.c](#appskcapi-hasherc)

### apps/kcapi-hasher.c

```c

{% raw %}
741 | 		}
742 | 
743 | 		memset(selfname, 0, sizeof(selfname));
744 | 		sym = dlsym(dl, "kcapi_md_init");
745 | 		if (sym == NULL || !dladdr(sym, &info)) {
746 | 			fprintf(stderr, "finding symbol kcapi_md_init failed\n");
{% endraw %}

```