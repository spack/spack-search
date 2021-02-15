---
name: "r-lpsolve"
layout: package
next_package: pcre2
previous_package: libpipeline
languages: ['cpp']
---
## 5.6.13.2
3 / 91 files match

 - [src/lp_lib.c](#srclp_libc)
 - [src/commonlib.h](#srccommonlibh)
 - [src/lp_explicit.h](#srclp_explicith)

### src/lp_lib.c

```cpp

{% raw %}
5180 |     lp->hBFP = dlopen(bfpname, RTLD_LAZY);
5442 |     lp->hXLI = dlopen(xliname, RTLD_LAZY);
{% endraw %}

```
### src/commonlib.h

```cpp

{% raw %}
29 |   #define my_LoadLibrary(name)              dlopen(name, RTLD_LAZY)
{% endraw %}

```
### src/lp_explicit.h

```cpp

{% raw %}
508 |   lpsolve = dlopen("liblpsolve55.so", RTLD_LAZY);;
{% endraw %}

```