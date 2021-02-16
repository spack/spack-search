---
name: "r-lpsolve"
layout: package
next_package: pcre2
previous_package: libpipeline
languages: ['c']
---
## 5.6.13.2
3 / 91 files match

 - [src/lp_lib.c](#srclp_libc)
 - [src/lp_explicit.h](#srclp_explicith)

### src/lp_lib.c

```c

{% raw %}
5180 |     lp->hBFP = dlopen(bfpname, RTLD_LAZY);
5442 |     lp->hXLI = dlopen(xliname, RTLD_LAZY);
{% endraw %}

```
### src/lp_explicit.h

```c

{% raw %}
508 |   lpsolve = dlopen("liblpsolve55.so", RTLD_LAZY);;
{% endraw %}

```