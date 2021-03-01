---
name: "libmicrohttpd"
layout: package
next_package: libpam
previous_package: libkcapi
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 0.9.71
5 / 394 files match, 1 filtered matches.

 - [src/lib/daemon_options.c](#srclibdaemon_optionsc)

### src/lib/daemon_options.c

```c

{% raw %}
370 |       (daemon->tls_backend_lib = dlopen (filename,
371 |                                          RTLD_NOW | RTLD_LOCAL)))
372 |     return MHD_SC_TLS_BACKEND_UNSUPPORTED; /* plugin not found */
373 |   if (NULL == (init = dlsym (daemon->tls_backend_lib,
374 |                              "MHD_TLS_init_" MHD_TLS_ABI_VERSION_STR)))
375 | 
{% endraw %}

```