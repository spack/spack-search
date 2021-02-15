---
name: "openresty"
layout: package
next_package: tix
previous_package: rsync
languages: ['cpp']
---
## 1.13.6.2
7 / 2240 files match

 - [bundle/LuaJIT-2.1-20180420/src/lib_package.c](#bundleluajit-21-20180420srclib_packagec)
 - [bundle/LuaJIT-2.1-20180420/src/lj_clib.c](#bundleluajit-21-20180420srclj_clibc)
 - [bundle/nginx-1.13.6/src/core/nginx.c](#bundlenginx-1136srccorenginxc)
 - [bundle/nginx-1.13.6/src/core/nginx.c.orig](#bundlenginx-1136srccorenginxcorig)
 - [bundle/nginx-1.13.6/src/core/ngx_core.h](#bundlenginx-1136srccorengx_coreh)
 - [bundle/nginx-1.13.6/src/os/unix/ngx_dlopen.h](#bundlenginx-1136srcosunixngx_dlopenh)
 - [bundle/nginx-1.13.6/src/os/win32/ngx_dlopen.h](#bundlenginx-1136srcoswin32ngx_dlopenh)

### bundle/LuaJIT-2.1-20180420/src/lib_package.c

```cpp

{% raw %}
34 | #if LJ_TARGET_DLOPEN
45 |   void *lib = dlopen(path, RTLD_NOW | (gl ? RTLD_GLOBAL : RTLD_LOCAL));
{% endraw %}

```
### bundle/LuaJIT-2.1-20180420/src/lj_clib.c

```cpp

{% raw %}
22 | #if LJ_TARGET_DLOPEN
117 |   void *h = dlopen(clib_extname(L, name),
123 |       h = dlopen(name, RTLD_LAZY | (global?RTLD_GLOBAL:RTLD_LOCAL));
{% endraw %}

```
### bundle/nginx-1.13.6/src/core/nginx.c

```cpp

{% raw %}
28 | #if (NGX_HAVE_DLOPEN)
1501 | #if (NGX_HAVE_DLOPEN)
1526 |     handle = ngx_dlopen(file.data);
1529 |                            ngx_dlopen_n " \"%s\" failed (%s)",
1580 | #if (NGX_HAVE_DLOPEN)
{% endraw %}

```
### bundle/nginx-1.13.6/src/core/nginx.c.orig

```

{% raw %}
28 | #if (NGX_HAVE_DLOPEN)
1496 | #if (NGX_HAVE_DLOPEN)
1521 |     handle = ngx_dlopen(file.data);
1524 |                            ngx_dlopen_n " \"%s\" failed (%s)",
1575 | #if (NGX_HAVE_DLOPEN)
{% endraw %}

```
### bundle/nginx-1.13.6/src/core/ngx_core.h

```cpp

{% raw %}
54 | #include <ngx_dlopen.h>
{% endraw %}

```
### bundle/nginx-1.13.6/src/os/unix/ngx_dlopen.h

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
### bundle/nginx-1.13.6/src/os/win32/ngx_dlopen.h

```cpp

{% raw %}
7 | #ifndef _NGX_DLOPEN_H_INCLUDED_
8 | #define _NGX_DLOPEN_H_INCLUDED_
15 | #define NGX_HAVE_DLOPEN  1
18 | #define ngx_dlopen(path)           LoadLibrary((char *) path)
19 | #define ngx_dlopen_n               "LoadLibrary()"
31 | #endif /* _NGX_DLOPEN_H_INCLUDED_ */
{% endraw %}

```