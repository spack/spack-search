---
name: "libfuse"
layout: package
next_package: libgpuarray
previous_package: libffs
languages: ['c']
---
## 3.9.2
1 / 93 files match, 1 filtered matches.

 - [lib/fuse.c](#libfusec)

### lib/fuse.c

```c

{% raw %}
265 | 		goto out;
266 | 	}
267 | 
268 | 	so->handle = dlopen(tmp, RTLD_NOW);
269 | 	if (so->handle == NULL) {
270 | 		fuse_log(FUSE_LOG_ERR, "fuse: dlopen(%s) failed: %s\n",
271 | 			tmp, dlerror());
272 | 		goto out_free_so;
{% endraw %}

```