---
name: "zsh"
layout: package
next_package: raft
previous_package: jq
languages: ['cpp']
---
## 5.4.2
4 / 446 files match

 - [config.h.in](#confighin)
 - [configure.ac](#configureac)
 - [aczsh.m4](#aczshm4)
 - [Src/module.c](#srcmodulec)

### config.h.in

```

{% raw %}
183 | /* Define to 1 if you have the `dlopen' function. */
184 | #undef HAVE_DLOPEN
{% endraw %}

```
### configure.ac

```

{% raw %}
869 |   AC_CHECK_LIB(dl, dlopen)
1435 |   AC_CHECK_FUNCS(dlopen dlerror dlsym dlclose load loadquery loadbind unload \
2745 | elif test "$ac_cv_func_dlopen"  != yes ||
2946 |       # also, dlopen() at least in Zeta respects $LIBRARY_PATH, so needs %A added to it.
2980 | #define dlopen(file,mode) (void *)shl_load((file), (mode), (long) 0)
3005 |     handle = dlopen("./conftest.$DL_EXT", RTLD_LAZY) ;
3007 |         fprintf (f, "dlopen failed") ;
{% endraw %}

```
### aczsh.m4

```

{% raw %}
127 | #define dlopen(file,mode) (void *)shl_load((file), (mode), (long) 0)
152 |     handle1 = dlopen("./conftest1.$DL_EXT", RTLD_LAZY | RTLD_GLOBAL);
154 |     handle2 = dlopen("./conftest2.$DL_EXT", RTLD_LAZY | RTLD_GLOBAL);
163 |     handle1 = dlopen("./conftest1.$DL_EXT", RTLD_LAZY | RTLD_GLOBAL);
208 | #define dlopen(file,mode) (void *)shl_load((file), (mode), (long) 0)
233 |     handle1 = dlopen("./conftest1.$DL_EXT", RTLD_LAZY | RTLD_GLOBAL);
235 |     handle2 = dlopen("./conftest2.$DL_EXT", RTLD_LAZY | RTLD_GLOBAL);
283 | #define dlopen(file,mode) (void *)shl_load((file), (mode), (long) 0)
307 |     handle = dlopen("./conftest1.$DL_EXT", RTLD_LAZY | RTLD_GLOBAL);
309 |     handle = dlopen("./conftest2.$DL_EXT", RTLD_LAZY | RTLD_GLOBAL);
352 | #define dlopen(file,mode) (void *)shl_load((file), (mode), (long) 0)
376 |     handle = dlopen("./conftest1.$DL_EXT", RTLD_LAZY | RTLD_GLOBAL);
425 | #define dlopen(file,mode) (void *)shl_load((file), (mode), (long) 0)
449 |     handle = dlopen("./conftest1.$DL_EXT", RTLD_LAZY | RTLD_GLOBAL);
492 | #define dlopen(file,mode) (void *)shl_load((file), (mode), (long) 0)
516 |     handle = dlopen("./conftest1.$DL_EXT", RTLD_LAZY | RTLD_GLOBAL);
{% endraw %}

```
### Src/module.c

```cpp

{% raw %}
1490 | #define dlopen(X,Y) load_and_bind(X)
1520 | # define dlopen(file,mode) (void *)shl_load((file), (mode), (long) 0)
1591 | 	if (*buf) /* dlopen(NULL) returns a handle to the main binary */
1592 | 	    ret = dlopen(buf, RTLD_LAZY | RTLD_GLOBAL);
{% endraw %}

```