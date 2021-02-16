---
name: "py-pillow"
layout: package
next_package: herwig3
previous_package: glew
languages: ['c']
---
## 6.2.0
2 / 1062 files match

 - [src/_imagingft.c](#src_imagingftc)
 - [src/Tk/tkImaging.c](#srctktkimagingc)

### src/_imagingft.c

```c

{% raw %}
158 |     p_raqm.raqm = dlopen("libraqm.so.0", RTLD_LAZY);
160 |         p_raqm.raqm = dlopen("libraqm.dylib", RTLD_LAZY);
{% endraw %}

```
### src/Tk/tkImaging.c

```c

{% raw %}
431 |     main_program = dlopen(NULL, RTLD_LAZY);
452 |     tkinter_lib = dlopen(tkinter_libname, RTLD_LAZY);
455 |                 "Cannot dlopen tkinter module file");
{% endraw %}

```