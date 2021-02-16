---
name: "util-linux-uuid"
layout: package
next_package: ompt-openmp
previous_package: cpuinfo
languages: ['c']
---
## 2.36
10 / 1188 files match, 1 filtered matches.

 - [libmount/src/context_veritydev.c](#libmountsrccontext_veritydevc)

### libmount/src/context_veritydev.c

```c

{% raw %}
32 | 	DBG(VERITY, ul_debugobj(cxt, "veritydev specific options detected but cannot dlopen symbol %s: %s", name, dl_error));
246 | 		dl = dlopen("libcryptsetup.so.12", dl_flags);
248 | 			DBG(VERITY, ul_debugobj(cxt, "veritydev specific options detected but cannot dlopen libcryptsetup"));
433 | 	dl = dlopen("libcryptsetup.so.12", dl_flags);
435 | 		DBG(VERITY, ul_debugobj(cxt, "veritydev specific options detected but cannot dlopen libcryptsetup"));
{% endraw %}

```