---
name: "nginx"
layout: package
next_package: libtlx
previous_package: steps
languages: ['cpp']
---
## 1.15.6
3 / 330 files match

 - [src/core/nginx.c](#srccorenginxc)
 - [src/core/ngx_core.h](#srccorengx_coreh)
 - [src/os/unix/ngx_dlopen.h](#srcosunixngx_dlopenh)

### src/core/nginx.c

```cpp

{% raw %}
28 | #if (NGX_HAVE_DLOPEN)
1497 | #if (NGX_HAVE_DLOPEN)
1522 |     handle = ngx_dlopen(file.data);
1525 |                            ngx_dlopen_n " \"%s\" failed (%s)",
1576 | #if (NGX_HAVE_DLOPEN)
{% endraw %}

```
### src/core/ngx_core.h

```cpp

{% raw %}
55 | #include <ngx_dlopen.h>
{% endraw %}

```
### src/os/unix/ngx_dlopen.h

```cpp

{% raw %}
7 | #ifndef _NGX_DLOPEN_H_INCLUDED_
8 | #define _NGX_DLOPEN_H_INCLUDED_
15 | #define ngx_dlopen(path)           dlopen((char *) path, RTLD_NOW | RTLD_GLOBAL)
16 | #define ngx_dlopen_n               "dlopen()"
25 | #if (NGX_HAVE_DLOPEN)
30 | #endif /* _NGX_DLOPEN_H_INCLUDED_ */
{% endraw %}

```