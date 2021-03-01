---
name: "nginx"
layout: package
next_package: ngspice
previous_package: nfs-ganesha
library_name: dlopen
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 1.15.6
3 / 330 files match, 1 filtered matches.

 - [src/core/nginx.c](#srccorenginxc)

### src/core/nginx.c

```c

{% raw %}
1519 |         return NGX_CONF_ERROR;
1520 |     }
1521 | 
1522 |     handle = ngx_dlopen(file.data);
1523 |     if (handle == NULL) {
1524 |         ngx_conf_log_error(NGX_LOG_EMERG, cf, 0,
1525 |                            ngx_dlopen_n " \"%s\" failed (%s)",
1526 |                            file.data, ngx_dlerror());
1527 |         return NGX_CONF_ERROR;
{% endraw %}

```