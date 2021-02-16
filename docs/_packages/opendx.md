---
name: "opendx"
layout: package
next_package: breseq
previous_package: py-astropy
languages: ['c']
---
## master
8 / 3166 files match

 - [src/exec/hwrender/opengl/hwLoadOGL.c](#srcexechwrenderopenglhwloadoglc)
 - [src/exec/hwrender/opengl/hwPortOGL.c](#srcexechwrenderopenglhwportoglc)
 - [src/exec/hwrender/xgl/hwPortXGL.c](#srcexechwrenderxglhwportxglc)
 - [src/exec/hwrender/xgl/hwLoad.c](#srcexechwrenderxglhwloadc)
 - [src/exec/dpexec/loader.c](#srcexecdpexecloaderc)

### src/exec/hwrender/opengl/hwLoadOGL.c

```c

{% raw %}
95 |   if ( ( HW_handle = dlopen( buff, RTLD_LAZY ) ) == NULL )
{% endraw %}

```
### src/exec/hwrender/opengl/hwPortOGL.c

```c

{% raw %}
1922 |     if ( !( DX_handle = dlopen( NULL, RTLD_LAZY ) ) )
{% endraw %}

```
### src/exec/hwrender/xgl/hwPortXGL.c

```c

{% raw %}
2265 |     if ( !( DX_handle = dlopen( (const char *)0, RTLD_LAZY ) ) )
{% endraw %}

```
### src/exec/hwrender/xgl/hwLoad.c

```c

{% raw %}
119 |   if ( ( HW_handle = dlopen( HWpath, RTLD_LAZY ) ) == NULL )
{% endraw %}

```
### src/exec/dpexec/loader.c

```c

{% raw %}
469 |   handle = dlopen( foundname, RTLD_LAZY | RTLD_GLOBAL );
{% endraw %}

```