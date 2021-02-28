---
name: "librdkafka"
layout: package
next_package: guile
previous_package: wt
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 1.5.0
3 / 511 files match, 2 filtered matches.

 - [src/rddl.c](#srcrddlc)
 - [tests/sockem.c](#testssockemc)

### src/rddl.c

```c

{% raw %}
162 |            char *errstr, size_t errstr_size) {
163 |         void *func;
164 | #if WITH_LIBDL
165 |         func = dlsym((void *)handle, symbol);
166 | #elif defined(_WIN32)
167 |         func = GetProcAddress((HMODULE)handle, symbol);
{% endraw %}

```
### tests/sockem.c

```c

{% raw %}
196 |                 fprintf(stderr, "%% libsockem pre-loaded (%s)\n",
197 |                         sockem_conf_str);
198 | #ifdef LIBSOCKEM_PRELOAD
199 |         sockem_orig_connect = dlsym(RTLD_NEXT, "connect");
200 |         sockem_orig_close = dlsym(RTLD_NEXT, "close");
201 | #endif
202 | }
{% endraw %}

```