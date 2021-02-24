---
name: "nginx"
layout: package
next_package: mpc
previous_package: bear
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 1.15.6
2 / 330 files match, 1 filtered matches.

 - [src/core/nginx.c](#srccorenginxc)

### src/core/nginx.c

```c

{% raw %}
1530 |     cln->handler = ngx_unload_module;
1531 |     cln->data = handle;
1532 | 
1533 |     modules = ngx_dlsym(handle, "ngx_modules");
1534 |     if (modules == NULL) {
1535 |         ngx_conf_log_error(NGX_LOG_EMERG, cf, 0,
1536 |                            ngx_dlsym_n " \"%V\", \"%s\" failed (%s)",
1537 |                            &value[1], "ngx_modules", ngx_dlerror());
1538 |         return NGX_CONF_ERROR;
1539 |     }
1540 | 
1541 |     names = ngx_dlsym(handle, "ngx_module_names");
1542 |     if (names == NULL) {
1543 |         ngx_conf_log_error(NGX_LOG_EMERG, cf, 0,
1544 |                            ngx_dlsym_n " \"%V\", \"%s\" failed (%s)",
1545 |                            &value[1], "ngx_module_names", ngx_dlerror());
1546 |         return NGX_CONF_ERROR;
1547 |     }
1548 | 
1549 |     order = ngx_dlsym(handle, "ngx_module_order");
1550 | 
1551 |     for (i = 0; modules[i]; i++) {
{% endraw %}

```