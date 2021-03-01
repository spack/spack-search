---
name: "libyogrt"
layout: package
next_package: lighttpd
previous_package: libxsmm
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 1.20-2
3 / 60 files match, 1 filtered matches.

 - [src/yogrt.c](#srcyogrtc)

### src/yogrt.c

```c

{% raw %}
272 | 		return 0;
273 | 	}
274 | 
275 | 	backend.init =      dlsym(backend_handle, "internal_init");
276 | 	backend.name =      dlsym(backend_handle, "internal_backend_name");
277 | 	backend.remaining = dlsym(backend_handle, "internal_get_rem_time");
278 | 	backend.rank =      dlsym(backend_handle, "internal_get_rank");
279 | 	backend.fudge =     dlsym(backend_handle, "internal_fudge");
280 | 
281 | 	if (backend.init != NULL)
{% endraw %}

```