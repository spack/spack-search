---
name: "libmicrohttpd"
layout: package
next_package: libmonitor
previous_package: libmesh
languages: ['c']
---
## 0.9.71
6 / 394 files match, 1 filtered matches.

 - [src/lib/daemon_options.c](#srclibdaemon_optionsc)

### src/lib/daemon_options.c

```c

{% raw %}
367 |   if (0 >= res)
368 |     return MHD_SC_TLS_BACKEND_UNSUPPORTED; /* string too long? */
369 |   if (NULL ==
370 |       (daemon->tls_backend_lib = dlopen (filename,
371 |                                          RTLD_NOW | RTLD_LOCAL)))
372 |     return MHD_SC_TLS_BACKEND_UNSUPPORTED; /* plugin not found */
{% endraw %}

```