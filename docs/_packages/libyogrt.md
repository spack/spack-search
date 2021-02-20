---
name: "libyogrt"
layout: package
next_package: lighttpd
previous_package: libxvmc
languages: ['c']
---
## 1.20-2
4 / 60 files match, 1 filtered matches.

 - [src/yogrt.c](#srcyogrtc)

### src/yogrt.c

```c

{% raw %}
267 | #endif
268 | 	debug3("Will use %s.\n", path);
269 | 
270 | 	if ((backend_handle = dlopen(path, flags)) == NULL) {
271 | 		error("dlopen failed: %s\n", dlerror());
272 | 		return 0;
273 | 	}
{% endraw %}

```