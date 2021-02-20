---
name: "py-pillow-simd"
layout: package
next_package: py-pygments
previous_package: py-pillow
languages: ['c']
---
## 7.0.0.post3
2 / 328 files match, 2 filtered matches.

 - [src/_imagingft.c](#src_imagingftc)
 - [src/Tk/tkImaging.c](#srctktkimagingc)

### src/_imagingft.c

```c

{% raw %}
154 | 
155 |     /* Microsoft needs a totally different system */
156 | #if !defined(_MSC_VER)
157 |     p_raqm.raqm = dlopen("libraqm.so.0", RTLD_LAZY);
158 |     if (!p_raqm.raqm) {
159 |         p_raqm.raqm = dlopen("libraqm.dylib", RTLD_LAZY);
160 |     }
161 | #else
{% endraw %}

```
### src/Tk/tkImaging.c

```c

{% raw %}
420 |     PyObject *pModule = NULL, *pString = NULL;
421 | 
422 |     /* Try loading from the main program namespace first */
423 |     main_program = dlopen(NULL, RTLD_LAZY);
424 |     if (_func_loader(main_program) == 0) {
425 |         dlclose(main_program);
441 |     if (tkinter_libname == NULL) {
442 |         goto exit;
443 |     }
444 |     tkinter_lib = dlopen(tkinter_libname, RTLD_LAZY);
445 |     if (tkinter_lib == NULL) {
446 |         PyErr_SetString(PyExc_RuntimeError,
447 |                 "Cannot dlopen tkinter module file");
448 |         goto exit;
449 |     }
{% endraw %}

```