---
name: "lighttpd"
layout: package
next_package: likwid
previous_package: libyogrt
languages: ['c']
---
## 1.4.53
32 / 384 files match, 1 filtered matches.

 - [src/plugin.c](#srcpluginc)

### src/plugin.c

```c

{% raw %}
225 | 
226 | 		}
227 | #else
228 | 		if (NULL == (p->lib = dlopen(srv->tmp_buf->ptr, RTLD_NOW|RTLD_GLOBAL))) {
229 | 			log_error_write(srv, __FILE__, __LINE__, "sbs", "dlopen() failed for:",
230 | 				srv->tmp_buf, dlerror());
231 | 
{% endraw %}

```