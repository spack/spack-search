---
name: "py-pillow"
layout: package
next_package: py-pillow-simd
previous_package: py-petsc4py
languages: ['c']
---
## 6.2.0
2 / 1062 files match, 2 filtered matches.

 - [src/_imagingft.c](#src_imagingftc)
 - [src/Tk/tkImaging.c](#srctktkimagingc)

### src/_imagingft.c

```c

{% raw %}
155 | 
156 |     /* Microsoft needs a totally different system */
157 | #if !defined(_MSC_VER)
158 |     p_raqm.raqm = dlopen("libraqm.so.0", RTLD_LAZY);
159 |     if (!p_raqm.raqm) {
160 |         p_raqm.raqm = dlopen("libraqm.dylib", RTLD_LAZY);
161 |     }
162 | #else
{% endraw %}

```
### src/Tk/tkImaging.c

```c

{% raw %}
428 |     PyObject *pModule = NULL, *pString = NULL;
429 | 
430 |     /* Try loading from the main program namespace first */
431 |     main_program = dlopen(NULL, RTLD_LAZY);
432 |     if (_func_loader(main_program) == 0) {
433 |         dlclose(main_program);
449 |     if (tkinter_libname == NULL) {
450 |         goto exit;
451 |     }
452 |     tkinter_lib = dlopen(tkinter_libname, RTLD_LAZY);
453 |     if (tkinter_lib == NULL) {
454 |         PyErr_SetString(PyExc_RuntimeError,
455 |                 "Cannot dlopen tkinter module file");
456 |         goto exit;
457 |     }
{% endraw %}

```