---
name: "rsync"
layout: package
next_package: hdf5
previous_package: libfabric
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 3.1.2
1 / 187 files match, 1 filtered matches.

 - [util.c](#utilc)

### util.c

```c

{% raw %}
1359 | 	if (!fn) {
1360 | 		static void *h;
1361 | 		h = dlopen("/usr/local/parasoft/insure++lite/lib.linux2/libinsure.so", RTLD_LAZY);
1362 | 		fn = dlsym(h, "_Insure_trap_error");
1363 | 	}
1364 | 
{% endraw %}

```