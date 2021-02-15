---
name: "ocaml"
layout: package
next_package: poppler
previous_package: php
languages: ['cpp']
---
## 4.03.0
6 / 2293 files match

 - [byterun/unix.c](#byterununixc)
 - [byterun/win32.c](#byterunwin32c)
 - [byterun/dynlink.c](#byterundynlinkc)
 - [byterun/caml/osdeps.h](#byteruncamlosdepsh)
 - [config/s-templ.h](#configs-templh)
 - [asmrun/natdynlink.c](#asmrunnatdynlinkc)

### byterun/unix.c

```cpp

{% raw %}
215 | void * caml_dlopen(char * libname, int for_execution, int global)
219 |   return flexdll_dlopen(libname, flags);
234 |   return flexdll_dlsym(flexdll_dlopen(NULL,0), name);
243 | /* Use normal dlopen */
255 | void * caml_dlopen(char * libname, int for_execution, int global)
257 |   return dlopen(libname, RTLD_NOW | (global ? RTLD_GLOBAL : RTLD_LOCAL)
294 | void * caml_dlopen(char * libname, int for_execution, int global)
{% endraw %}

```
### byterun/win32.c

```cpp

{% raw %}
198 | void * caml_dlopen(char * libname, int for_execution, int global)
203 |   handle = flexdll_dlopen(libname, flags);
223 |   return flexdll_dlsym(flexdll_dlopen(NULL,0), name);
233 | void * caml_dlopen(char * libname, int for_execution, int global)
{% endraw %}

```
### byterun/dynlink.c

```cpp

{% raw %}
125 |   handle = caml_dlopen(realname, 1, 1);
201 | /** dlopen interface for the bytecode linker **/
215 |   handle = caml_dlopen(p, Int_val(mode), 1);
{% endraw %}

```
### byterun/caml/osdeps.h

```cpp

{% raw %}
62 | extern void * caml_dlopen(char * libname, int for_execution, int global);
{% endraw %}

```
### config/s-templ.h

```cpp

{% raw %}
52 |    via dlopen() is available. */
{% endraw %}

```
### asmrun/natdynlink.c

```cpp

{% raw %}
62 |   handle = caml_dlopen(p, 1, Int_val(global));
133 |   handle = caml_dlopen(p, 1, 1);
{% endraw %}

```