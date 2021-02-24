---
name: "gmt"
layout: package
next_package: watch
previous_package: xdm
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 6.1.0
3 / 3639 files match, 1 filtered matches.

 - [src/gmt_sharedlibs.c](#srcgmt_sharedlibsc)

### src/gmt_sharedlibs.c

```c

{% raw %}
36 | 	return (!FreeLibrary (handle));
37 | }
38 | 
39 | void *dlsym (void *handle, const char *name) {
40 | 	/* Get a symbol from dll */
41 | 	return GetProcAddress (handle, name);
{% endraw %}

```