---
name: "lighttpd"
layout: package
next_package: p11-kit
previous_package: vtable-dumper
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 1.4.53
3 / 384 files match, 1 filtered matches.

 - [src/plugin.c](#srcpluginc)

### src/plugin.c

```c

{% raw %}
260 | 
261 | #else
262 | #if 1
263 | 		init = (int (*)(plugin *))(intptr_t)dlsym(p->lib, srv->tmp_buf->ptr);
264 | #else
265 | 		*(void **)(&init) = dlsym(p->lib, srv->tmp_buf->ptr);
267 | 		if (NULL == init) {
268 | 			const char *error = dlerror();
269 | 			if (error != NULL) {
270 | 				log_error_write(srv, __FILE__, __LINE__, "ss", "dlsym:", error);
271 | 			} else {
272 | 				log_error_write(srv, __FILE__, __LINE__, "ss", "dlsym symbol not found:", srv->tmp_buf->ptr);
273 | 			}
274 | 
{% endraw %}

```