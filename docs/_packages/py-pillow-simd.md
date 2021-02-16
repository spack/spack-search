---
name: "py-pillow-simd"
layout: package
next_package: ipopt
previous_package: xmlrpc-c
languages: ['c']
---
## 7.0.0.post3
2 / 328 files match, 2 filtered matches.

 - [src/_imagingft.c](#src_imagingftc)
 - [src/Tk/tkImaging.c](#srctktkimagingc)

### src/_imagingft.c

```c

{% raw %}
157 |     p_raqm.raqm = dlopen("libraqm.so.0", RTLD_LAZY);
159 |         p_raqm.raqm = dlopen("libraqm.dylib", RTLD_LAZY);
{% endraw %}

```
### src/Tk/tkImaging.c

```c

{% raw %}
423 |     main_program = dlopen(NULL, RTLD_LAZY);
444 |     tkinter_lib = dlopen(tkinter_libname, RTLD_LAZY);
447 |                 "Cannot dlopen tkinter module file");
{% endraw %}

```