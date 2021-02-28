---
name: "adiak"
layout: package
next_package: cpuinfo
previous_package: eztrace
library_name: dlsym
matches: ['dlsym']
languages: ['c']
---
## 0.1.1
1 / 601 files match, 1 filtered matches.

 - [src/adksys_glibc.c](#srcadksys_glibcc)

### src/adksys_glibc.c

```c

{% raw %}
52 |    void *result;
53 |    
54 |    dlerror();
55 |    result = dlsym(RTLD_DEFAULT, "public_adiak");
56 |    if (dlerror())
57 |       return NULL;
{% endraw %}

```