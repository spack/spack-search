---
name: "stat"
layout: package
next_package: swipl
previous_package: sst-macro
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 4.0.2
3 / 275 files match, 1 filtered matches.

 - [src/dysect/libDysectAPI/include/LibDysectAPI.h](#srcdysectlibdysectapiincludelibdysectapih)

### src/dysect/libDysectAPI/include/LibDysectAPI.h

```c

{% raw %}
92 |       dlerror();
93 |       *method = (T) dlsym(libraryHandle, name);
94 | 
95 |       const char *dlsym_error = dlerror();
96 |       if(dlsym_error) {
97 |         fprintf(stderr, "Cannot load symbol '%s': %s\n", name, dlsym_error);
98 |         dlclose(libraryHandle);
99 | 
{% endraw %}

```