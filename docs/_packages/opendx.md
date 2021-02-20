---
name: "opendx"
layout: package
next_package: openfast
previous_package: opencv
languages: ['c']
---
## master
8 / 3166 files match, 5 filtered matches.

 - [src/exec/hwrender/opengl/hwLoadOGL.c](#srcexechwrenderopenglhwloadoglc)
 - [src/exec/hwrender/opengl/hwPortOGL.c](#srcexechwrenderopenglhwportoglc)
 - [src/exec/hwrender/xgl/hwPortXGL.c](#srcexechwrenderxglhwportxglc)
 - [src/exec/hwrender/xgl/hwLoad.c](#srcexechwrenderxglhwloadc)
 - [src/exec/dpexec/loader.c](#srcexecdpexecloaderc)

### src/exec/hwrender/opengl/hwLoadOGL.c

```c

{% raw %}
92 |     return NULL;
93 |   }
94 | 
95 |   if ( ( HW_handle = dlopen( buff, RTLD_LAZY ) ) == NULL )
96 |   {
97 |     /* Hardware unavailable: unable to load module '%s/%s' */
{% endraw %}

```
### src/exec/hwrender/opengl/hwPortOGL.c

```c

{% raw %}
1919 |     void *( *expVer )();
1920 |     void *DX_handle;
1921 | 
1922 |     if ( !( DX_handle = dlopen( NULL, RTLD_LAZY ) ) )
1923 |     {
1924 |       DXSetError( ERROR_UNEXPECTED, dlerror() );
{% endraw %}

```
### src/exec/hwrender/xgl/hwPortXGL.c

```c

{% raw %}
2262 |     /* If the hardware rendering load module requires a newer set of
2263 |      * DX exported symbols than those available in the calling dxexec
2264 |      */
2265 |     if ( !( DX_handle = dlopen( (const char *)0, RTLD_LAZY ) ) )
2266 |     {
2267 |       DXSetError( ERROR_UNEXPECTED, dlerror() );
{% endraw %}

```
### src/exec/hwrender/xgl/hwLoad.c

```c

{% raw %}
116 | 
117 | loadlib:
118 | 
119 |   if ( ( HW_handle = dlopen( HWpath, RTLD_LAZY ) ) == NULL )
120 |   {
121 |     DXSetError( ERROR_BAD_PARAMETER, dlerror() ); /* FIX THIS */
{% endraw %}

```
### src/exec/dpexec/loader.c

```c

{% raw %}
466 |    *  filename, mode.  the mode is: RTLD_LAZY (defer binding of procs)
467 |    *  other vals are reserved for future expansion.
468 |    */
469 |   handle = dlopen( foundname, RTLD_LAZY | RTLD_GLOBAL );
470 |   if ( handle == NULL )
471 |   {
{% endraw %}

```