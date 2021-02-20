---
name: "nfs-utils"
layout: package
next_package: nginx
previous_package: nfs-ganesha
languages: ['c']
---
## 2.4.1
5 / 387 files match, 1 filtered matches.

 - [support/nfsidmap/libnfsidmap.c](#supportnfsidmaplibnfsidmapc)

### support/nfsidmap/libnfsidmap.c

```c

{% raw %}
238 | 
239 | 	snprintf(plgname, sizeof(plgname), "%s/%s.so", PATH_PLUGINS, method);
240 | 
241 | 	dl = dlopen(plgname, RTLD_NOW | RTLD_LOCAL);
242 | 	if (dl == NULL) {
243 | 		IDMAP_LOG(1, ("libnfsidmap: Unable to load plugin: %s",
{% endraw %}

```