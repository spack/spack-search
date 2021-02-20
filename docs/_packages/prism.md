---
name: "prism"
layout: package
next_package: process-in-process
previous_package: premake-core
languages: ['c']
---
## 4.5
5 / 2725 files match, 4 filtered matches.

 - [prism/ext/lpsolve55/src/lp_solve_5.5/lp_lib.c](#prismextlpsolve55srclp_solve_55lp_libc)
 - [prism/ext/lpsolve55/src/lp_solve_5.5/lp_explicit.h](#prismextlpsolve55srclp_solve_55lp_explicith)
 - [prism/ext/lpsolve55/src/lp_solve_5.5/shared/myblas.c](#prismextlpsolve55srclp_solve_55sharedmyblasc)
 - [prism/ext/lpsolve55/include/lp_explicit.h](#prismextlpsolve55includelp_explicith)

### prism/ext/lpsolve55/src/lp_solve_5.5/lp_lib.c

```c

{% raw %}
5370 |       strcat(bfpname, ".so");
5371 | 
5372 |    /* Get a handle to the module. */
5373 |     lp->hBFP = dlopen(bfpname, RTLD_LAZY);
5374 | 
5375 |    /* If the handle is valid, try to get the function addresses. */
5630 |       strcat(xliname, ".so");
5631 | 
5632 |    /* Get a handle to the module. */
5633 |     lp->hXLI = dlopen(xliname, RTLD_LAZY);
5634 | 
5635 |    /* If the handle is valid, try to get the function addresses. */
{% endraw %}

```
### prism/ext/lpsolve55/src/lp_solve_5.5/lp_explicit.h

```c

{% raw %}
529 |   /* Get a handle to the Windows DLL module. */
530 |   lpsolve = LoadLibrary("lpsolve55.dll");
531 | # else
532 |   lpsolve = dlopen("liblpsolve55.so", RTLD_LAZY);;
533 | # endif
534 |   return(lpsolve);
{% endraw %}

```
### prism/ext/lpsolve55/src/lp_solve_5.5/shared/myblas.c

```c

{% raw %}
120 |       strcat(blasname, ".so");
121 | 
122 |    /* Get a handle to the module. */
123 |     hBLAS = dlopen(blasname, RTLD_LAZY);
124 | 
125 |    /* If the handle is valid, try to get the function addresses. */
{% endraw %}

```
### prism/ext/lpsolve55/include/lp_explicit.h

```c

{% raw %}
529 |   /* Get a handle to the Windows DLL module. */
530 |   lpsolve = LoadLibrary("lpsolve55.dll");
531 | # else
532 |   lpsolve = dlopen("liblpsolve55.so", RTLD_LAZY);;
533 | # endif
534 |   return(lpsolve);
{% endraw %}

```