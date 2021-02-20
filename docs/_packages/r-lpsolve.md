---
name: "r-lpsolve"
layout: package
next_package: r-lubridate
previous_package: r-igraph
languages: ['c']
---
## 5.6.13.2
3 / 91 files match, 2 filtered matches.

 - [src/lp_lib.c](#srclp_libc)
 - [src/lp_explicit.h](#srclp_explicith)

### src/lp_lib.c

```c

{% raw %}
5177 |       strcat(bfpname, ".so");
5178 | 
5179 |    /* Get a handle to the module. */
5180 |     lp->hBFP = dlopen(bfpname, RTLD_LAZY);
5181 | 
5182 |    /* If the handle is valid, try to get the function addresses. */
5439 |       strcat(xliname, ".so");
5440 | 
5441 |    /* Get a handle to the module. */
5442 |     lp->hXLI = dlopen(xliname, RTLD_LAZY);
5443 | 
5444 |    /* If the handle is valid, try to get the function addresses. */
{% endraw %}

```
### src/lp_explicit.h

```c

{% raw %}
505 |   /* Get a handle to the Windows DLL module. */
506 |   lpsolve = LoadLibrary("lpsolve55.dll");
507 | # else
508 |   lpsolve = dlopen("liblpsolve55.so", RTLD_LAZY);;
509 | # endif
510 |   return(lpsolve);
{% endraw %}

```