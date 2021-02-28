---
name: "zfs"
layout: package
next_package: pythia8
previous_package: pmix
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 0.8.2
3 / 3305 files match, 1 filtered matches.

 - [lib/libzpool/util.c](#liblibzpoolutilc)

### lib/libzpool/util.c

```c

{% raw %}
184 | 	zpoolhdl = dlopen("libzpool.so", RTLD_LAZY);
185 | 	if (zpoolhdl != NULL) {
186 | 		uint32_t *var;
187 | 		var = dlsym(zpoolhdl, varname);
188 | 		if (var == NULL) {
189 | 			fprintf(stderr, "Global variable '%s' does not exist "
{% endraw %}

```