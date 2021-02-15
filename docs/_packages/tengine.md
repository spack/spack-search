---
name: "tengine"
layout: package
next_package: diffutils
previous_package: saws
languages: ['cpp']
---
## 2.3.0
4 / 1238 files match

 - [src/core/nginx.c](#srccorenginxc)
 - [src/core/ngx_core.h](#srccorengx_coreh)
 - [src/event/ngx_dlopen.h](#srceventngx_dlopenh)
 - [src/os/unix/ngx_dlopen.h](#srcosunixngx_dlopenh)

### src/core/nginx.c

```cpp

{% raw %}
28 | #if (NGX_HAVE_DLOPEN)
1573 | #if (NGX_HAVE_DLOPEN)
1598 |     handle = ngx_dlopen(file.data);
1601 |                            ngx_dlopen_n " \"%s\" failed (%s)",
1652 | #if (NGX_HAVE_DLOPEN)
{% endraw %}

```
### src/core/ngx_core.h

```cpp

{% raw %}
58 | #include <ngx_dlopen.h>
{% endraw %}

```
### src/event/ngx_dlopen.h

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