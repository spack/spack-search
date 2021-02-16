---
name: "pdsh"
layout: package
next_package: npm
previous_package: mysql
languages: ['c']
---
## 2.31
9 / 162 files match

 - [src/qsnet/qswutil.c](#srcqsnetqswutilc)
 - [src/pdsh/ltdl.h](#srcpdshltdlh)
 - [src/pdsh/ltdl.c](#srcpdshltdlc)
 - [src/pdsh/mod.c](#srcpdshmodc)

### src/qsnet/qswutil.c

```c

{% raw %}
268 |     if (!(elan3h = dlopen ("libelan3.so", RTLD_LAZY))) {
{% endraw %}

```
### src/pdsh/ltdl.h

```c

{% raw %}
170 | LT_SCOPE	lt_dlhandle lt_dlopen		LT_PARAMS((const char *filename));
171 | LT_SCOPE	lt_dlhandle lt_dlopenext	LT_PARAMS((const char *filename));
244 |   int	ref_count;		/* number of times lt_dlopened minus
314 |     LT_ERROR(DLOPEN_NOT_SUPPORTED,  "dlopen support not available")	\
{% endraw %}

```
### src/pdsh/ltdl.c

```c

{% raw %}
842 |   lt_dlloader	       *loader;		/* dlopening interface */
1109 |   lt_module   module   = dlopen (filename, LT_GLOBAL | LT_LAZY_OR_NOW);
2182 | static	int	try_dlopen	      LT_PARAMS((lt_dlhandle *handle,
2184 | static	int	tryall_dlopen	      LT_PARAMS((lt_dlhandle *handle,
2227 |       errors += lt_dlloader_add (lt_dlloader_next (0), &sys_dl, "dlopen");
2230 |       errors += lt_dlloader_add (lt_dlloader_next (0), &sys_shl, "dlopen");
2233 |       errors += lt_dlloader_add (lt_dlloader_next (0), &sys_wll, "dlopen");
2236 |       errors += lt_dlloader_add (lt_dlloader_next (0), &sys_bedl, "dlopen");
2372 | tryall_dlopen (handle, filename, useloader)
2475 | tryall_dlopen_module (handle, prefix, dirname, dlname)
2513 |       error += tryall_dlopen_module (handle,
2516 |   else if (tryall_dlopen (handle, filename, NULL) != 0)
2535 |      we want the preopened version of it, even if a dlopenable
2537 |   if (old_name && tryall_dlopen (handle, old_name, "dlpreload") == 0)
2548 | 	  if (tryall_dlopen_module (handle,
2556 | 	  if (tryall_dlopen_module (handle, dir, objdir, dlname) == 0)
2562 | 	  if (dir && (tryall_dlopen_module (handle,
2801 |   if (tryall_dlopen (handle, filename,NULL) != 0)
2957 | 	  handle->deplibs[j] = lt_dlopenext(names[depcount-1-i]);
3059 | try_dlopen (phandle, filename)
3090 |       if (tryall_dlopen (&newhandle, 0, NULL) != 0)
3396 |           if (tryall_dlopen (&newhandle, filename, NULL) != 0)
3435 | lt_dlopen (filename)
3442 |   if (try_dlopen (&handle, filename) != 0)
3467 | lt_dlopenext (filename)
3478 |       return lt_dlopen (filename);
3494 |       return lt_dlopen (filename);
3504 |   errors = try_dlopen (&handle, tmp);
3534 |   errors = try_dlopen (&handle, tmp);
3748 |    passing to lt_dlopenext.  The extensions are stripped so that
3751 |    then the same directories that lt_dlopen would search are examined.  */
{% endraw %}

```
### src/pdsh/mod.c

```c

{% raw %}
814 |     if (!(mod->handle = lt_dlopen(fq_path)))
{% endraw %}

```