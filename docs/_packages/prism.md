---
name: "prism"
layout: package
next_package: yasm
previous_package: code-server
languages: ['cpp']
---
## 4.5
5 / 2725 files match

 - [prism/ext/lpsolve55/src/lp_solve_5.5/lp_lib.c](#prismextlpsolve55srclp_solve_55lp_libc)
 - [prism/ext/lpsolve55/src/lp_solve_5.5/lp_explicit.h](#prismextlpsolve55srclp_solve_55lp_explicith)
 - [prism/ext/lpsolve55/src/lp_solve_5.5/shared/commonlib.h](#prismextlpsolve55srclp_solve_55sharedcommonlibh)
 - [prism/ext/lpsolve55/src/lp_solve_5.5/shared/myblas.c](#prismextlpsolve55srclp_solve_55sharedmyblasc)
 - [prism/ext/lpsolve55/include/lp_explicit.h](#prismextlpsolve55includelp_explicith)

### prism/ext/lpsolve55/src/lp_solve_5.5/lp_lib.c

```cpp

{% raw %}
5373 |     lp->hBFP = dlopen(bfpname, RTLD_LAZY);
5633 |     lp->hXLI = dlopen(xliname, RTLD_LAZY);
{% endraw %}

```
### prism/ext/lpsolve55/src/lp_solve_5.5/lp_explicit.h

```cpp

{% raw %}
532 |   lpsolve = dlopen("liblpsolve55.so", RTLD_LAZY);;
{% endraw %}

```
### prism/ext/lpsolve55/src/lp_solve_5.5/shared/commonlib.h

```cpp

{% raw %}
35 |   #define my_LoadLibrary(name)              dlopen(name, RTLD_LAZY)
{% endraw %}

```
### prism/ext/lpsolve55/src/lp_solve_5.5/shared/myblas.c

```cpp

{% raw %}
123 |     hBLAS = dlopen(blasname, RTLD_LAZY);
{% endraw %}

```
### prism/ext/lpsolve55/include/lp_explicit.h

```cpp

{% raw %}
532 |   lpsolve = dlopen("liblpsolve55.so", RTLD_LAZY);;
{% endraw %}

```