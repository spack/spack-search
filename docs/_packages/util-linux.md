---
name: "util-linux"
layout: package
next_package: util-linux-uuid
previous_package: unixodbc
languages: ['c']
---
## 2.36
10 / 1188 files match, 1 filtered matches.

 - [libmount/src/context_veritydev.c](#libmountsrccontext_veritydevc)

### libmount/src/context_veritydev.c

```c

{% raw %}
29 | 	if ((dl_error = dlerror()) == NULL)
30 | 		return sym;
31 | 
32 | 	DBG(VERITY, ul_debugobj(cxt, "veritydev specific options detected but cannot dlopen symbol %s: %s", name, dl_error));
33 | 	*rc = -ENOTSUP;
34 | 
243 | #ifdef RTLD_DEEPBIND
244 | 		dl_flags |= RTLD_DEEPBIND;
245 | #endif
246 | 		dl = dlopen("libcryptsetup.so.12", dl_flags);
247 | 		if (!dl) {
248 | 			DBG(VERITY, ul_debugobj(cxt, "veritydev specific options detected but cannot dlopen libcryptsetup"));
249 | 			rc = -ENOTSUP;
250 | 		}
430 | 		return -EINVAL;
431 | 
432 | #ifdef CRYPTSETUP_VIA_DLOPEN
433 | 	dl = dlopen("libcryptsetup.so.12", dl_flags);
434 | 	if (!dl) {
435 | 		DBG(VERITY, ul_debugobj(cxt, "veritydev specific options detected but cannot dlopen libcryptsetup"));
436 | 		return -ENOTSUP;
437 | 	}
{% endraw %}

```