---
name: "gccxml"
layout: package
next_package: gdb
previous_package: gcc
languages: ['c']
---
## latest
5 / 2115 files match, 2 filtered matches.

 - [GCC/gcc/sys-protos.h](#gccgccsys-protosh)
 - [GCC/gcc/config/darwin-crt3.c](#gccgccconfigdarwin-crt3c)

### GCC/gcc/sys-protos.h

```c

{% raw %}
233 | extern div_t                  div(int, int);
234 | extern int                    dlclose(void *);
235 | extern char *                 dlerror(void);
236 | extern void *                 dlopen(char *, int);
237 | extern void *                 dlsym(void *, char *);
238 | extern void                   dma_access(u_char, u_int, u_int, u_char, u_char);
{% endraw %}

```
### GCC/gcc/config/darwin-crt3.c

```c

{% raw %}
276 |     {
277 |       void *handle;
278 | 
279 |       handle = dlopen ("/usr/lib/libSystem.B.dylib", RTLD_NOLOAD);
280 |       if (!handle)
281 | 	{
{% endraw %}

```