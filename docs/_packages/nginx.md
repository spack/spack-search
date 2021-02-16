---
name: "nginx"
layout: package
next_package: libtlx
previous_package: steps
languages: ['c']
---
## 1.15.6
3 / 330 files match

 - [src/core/nginx.c](#srccorenginxc)

### src/core/nginx.c

```c

{% raw %}
1522 |     handle = ngx_dlopen(file.data);
1525 |                            ngx_dlopen_n " \"%s\" failed (%s)",
{% endraw %}

```