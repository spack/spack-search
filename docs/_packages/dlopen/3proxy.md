---
name: "3proxy"
layout: package
next_package: ace
previous_package: None
library_name: dlopen
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 0.8.13
1 / 166 files match, 1 filtered matches.

 - [src/conf.c](#srcconfc)

### src/conf.c

```c

{% raw %}
1292 | 	return (*(PLUGINFUNC)fp)(&pluginlink, argc - 2, (char **)argv + 2);
1293 | #else	
1294 | 	void *hi, *fp;
1295 | 	hi = dlopen((char *)argv[1], RTLD_LAZY);
1296 | 	if(!hi) return 1;
1297 | 	fp = dlsym(hi, (char *)argv[2]);
{% endraw %}

```