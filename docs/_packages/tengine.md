---
name: "tengine"
layout: package
next_package: thepeg
previous_package: tcl
languages: ['c']
---
## 2.3.0
4 / 1238 files match, 1 filtered matches.

 - [src/core/nginx.c](#srccorenginxc)

### src/core/nginx.c

```c

{% raw %}
1595 |         return NGX_CONF_ERROR;
1596 |     }
1597 | 
1598 |     handle = ngx_dlopen(file.data);
1599 |     if (handle == NULL) {
1600 |         ngx_conf_log_error(NGX_LOG_EMERG, cf, 0,
1601 |                            ngx_dlopen_n " \"%s\" failed (%s)",
1602 |                            file.data, ngx_dlerror());
1603 |         return NGX_CONF_ERROR;
{% endraw %}

```