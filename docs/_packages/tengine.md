---
name: "tengine"
layout: package
next_package: diffutils
previous_package: saws
languages: ['c']
---
## 2.3.0
4 / 1238 files match, 1 filtered matches.

 - [src/core/nginx.c](#srccorenginxc)

### src/core/nginx.c

```c

{% raw %}
1598 |     handle = ngx_dlopen(file.data);
1601 |                            ngx_dlopen_n " \"%s\" failed (%s)",
{% endraw %}

```