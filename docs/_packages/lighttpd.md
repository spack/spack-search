---
name: "lighttpd"
layout: package
next_package: libxaw3d
previous_package: raft
languages: ['c']
---
## 1.4.53
32 / 384 files match

 - [src/plugin.c](#srcpluginc)

### src/plugin.c

```c

{% raw %}
228 | 		if (NULL == (p->lib = dlopen(srv->tmp_buf->ptr, RTLD_NOW|RTLD_GLOBAL))) {
229 | 			log_error_write(srv, __FILE__, __LINE__, "sbs", "dlopen() failed for:",
{% endraw %}

```