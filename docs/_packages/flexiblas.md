---
name: "flexiblas"
layout: package
next_package: mpe2
previous_package: sosflow
languages: ['c']
---
## 3.0.3
9 / 16005 files match

 - [src/hooks.c](#srchooksc)
 - [src/sh_utils.c](#srcsh_utilsc)
 - [src/helper.h](#srchelperh)
 - [src/flexiblas.c](#srcflexiblasc)
 - [src/tool/hookhandling.c](#srctoolhookhandlingc)
 - [libcscutils/contrib/lua/src/loadlib.c](#libcscutilscontribluasrcloadlibc)
 - [tools/lapack_checks/lapack-check.c](#toolslapack_checkslapack-checkc)

### src/hooks.c

```c

{% raw %}
103 |             handle  = __flexiblas_dlopen(curfn, RTLD_LAZY | RTLD_LOCAL , NULL);
186 |             handle  = __flexiblas_dlopen(curfn, RTLD_LAZY | RTLD_LOCAL , NULL);
216 |     handle  = __flexiblas_dlopen(path, RTLD_LAZY | RTLD_LOCAL , NULL);
{% endraw %}

```
### src/sh_utils.c

```c

{% raw %}
118 | HIDDEN void * __flexiblas_dlopen( const char *libname, int flags, char ** sofile ){
207 | 			handle = dlopen(filepath, RTLD_LAZY | RTLD_LOCAL);
262 | 		handle = dlopen(filepath, flags);
271 | 			DPRINTF_ERROR(0, "dlopen: %s\n", dlerror());
364 |         handle = dlopen(filepath, RTLD_LAZY | RTLD_LOCAL);
{% endraw %}

```
### src/helper.h

```c

{% raw %}
60 |     HIDDEN void * __flexiblas_dlopen( const char *libname, int flags, char **soname );
{% endraw %}

```
### src/flexiblas.c

```c

{% raw %}
266 |         library = __flexiblas_dlopen(clibrary, DLOPEN_FLAGS_FROM_FILE , NULL);
274 |         library = __flexiblas_dlopen(env_FLEXIBLAS, DLOPEN_FLAGS_FROM_FILE, NULL);
311 |             library  = __flexiblas_dlopen(clibrary, DLOPEN_FLAGS_FROM_FILE , NULL);
327 |             library = __flexiblas_dlopen(clibrary,DLOPEN_FLAGS_FROM_FILE , NULL);
404 |     library = __flexiblas_dlopen(clibrary, DLOPEN_FLAGS_FROM_FILE, (char **) NULL);
497 |     library = __flexiblas_dlopen(blas_sofile, DLOPEN_FLAGS_FROM_FILE, (char **) NULL);
679 |             __flexiblas_blas_fallback = __flexiblas_dlopen(blas_name, RTLD_LAZY | RTLD_GLOBAL , NULL);
698 |             __flexiblas_lapack_fallback = __flexiblas_dlopen(lapack_name, RTLD_LAZY | RTLD_DEEPBIND |  RTLD_GLOBAL , NULL);
700 |             __flexiblas_lapack_fallback = __flexiblas_dlopen(lapack_name, RTLD_LAZY | RTLD_GLOBAL , NULL);
784 |             handle  = __flexiblas_dlopen(sofile, RTLD_LAZY | RTLD_LOCAL , NULL);
{% endraw %}

```
### src/tool/hookhandling.c

```c

{% raw %}
177 |     handle = __flexiblas_dlopen(sofile, RTLD_LAZY | RTLD_LOCAL, NULL);
389 |     handle = __flexiblas_dlopen(sofile, RTLD_LAZY | RTLD_LOCAL, NULL);
{% endraw %}

```
### libcscutils/contrib/lua/src/loadlib.c

```c

{% raw %}
126 |   void *lib = dlopen(path, RTLD_NOW | (seeglb ? RTLD_GLOBAL : RTLD_LOCAL));
{% endraw %}

```
### tools/lapack_checks/lapack-check.c

```c

{% raw %}
187 |     ptr = dlopen(argv[1], RTLD_LOCAL | RTLD_LAZY);
{% endraw %}

```