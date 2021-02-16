---
name: "r-rgraphviz"
layout: package
next_package: fipscheck
previous_package: hipsycl
languages: ['c']
---
## 2.20.0
38 / 778 files match

 - [src/graphviz/lib/gvc/gvplugin.c](#srcgraphvizlibgvcgvpluginc)
 - [src/graphviz/libltdl/ltdl.h](#srcgraphvizlibltdlltdlh)
 - [src/graphviz/libltdl/ltdl.c](#srcgraphvizlibltdlltdlc)
 - [src/graphviz/libltdl/loaders/preopen.c](#srcgraphvizlibltdlloaderspreopenc)
 - [src/graphviz/libltdl/loaders/dlopen.c](#srcgraphvizlibltdlloadersdlopenc)
 - [src/graphviz/libltdl/libltdl/lt__private.h](#srcgraphvizlibltdllibltdllt__privateh)
 - [src/graphviz/libltdl/libltdl/lt_error.h](#srcgraphvizlibltdllibltdllt_errorh)

### src/graphviz/lib/gvc/gvplugin.c

```c

{% raw %}
196 |     hndl = lt_dlopen (p);
{% endraw %}

```
### src/graphviz/libltdl/ltdl.h

```c

{% raw %}
76 | LT_SCOPE lt_dlhandle lt_dlopen		(const char *filename);
77 | LT_SCOPE lt_dlhandle lt_dlopenext	(const char *filename);
78 | LT_SCOPE lt_dlhandle lt_dlopenadvise	(const char *filename,
132 |   int		ref_count;	/* number of times lt_dlopened minus
{% endraw %}

```
### src/graphviz/libltdl/ltdl.c

```c

{% raw %}
122 | static	int	try_dlopen	      (lt_dlhandle *handle,
125 | static	int	tryall_dlopen	      (lt_dlhandle *handle,
165 |    dlopen an application module.  */
232 | 	 can use _them_ to lt_dlopen its own modules.  */
357 | tryall_dlopen (lt_dlhandle *phandle, const char *filename,
365 |   fprintf (stderr, "tryall_dlopen (%s, %s)\n",
375 |       if ((handle->info.filename == filename) /* dlopen self: 0 == 0 */
475 | tryall_dlopen_module (lt_dlhandle *handle, const char *prefix,
511 |       error += tryall_dlopen_module (handle, (const char *) 0,
514 |   else if (tryall_dlopen (handle, filename, advise, 0) != 0)
529 |      we want the preopened version of it, even if a dlopenable
531 |   if (old_name && tryall_dlopen (handle, old_name,
543 | 	  if (tryall_dlopen_module (handle, (const char *) 0,
551 | 	  if (tryall_dlopen_module (handle, dir, objdir,
558 | 	  if (dir && (tryall_dlopen_module (handle, (const char *) 0,
776 |   if (tryall_dlopen (phandle, filename, advise, 0) != 0)
935 | 	  cur->deplibs[j] = lt_dlopenext(names[depcount-1-i]);
1133 | try_dlopen (lt_dlhandle *phandle, const char *filename, const char *ext,
1150 |   fprintf (stderr, "try_dlopen (%s, %s)\n",
1169 |       if (tryall_dlopen (&newhandle, 0, advise, 0) != 0)
1281 | 	  if (tryall_dlopen (&newhandle, archive_name, advise, vtable) == 0)
1448 | 	  if (tryall_dlopen (&newhandle, attempt, advise, 0) != 0)
1588 | lt_dlopen (const char *filename)
1590 |   return lt_dlopenadvise (filename, NULL);
1599 | lt_dlopenext (const char *filename)
1605 |     handle = lt_dlopenadvise (filename, advise);
1613 | lt_dlopenadvise (const char *filename, lt_dladvise advise)
1632 |       if (try_dlopen (&handle, filename, NULL, advise) != 0)
1641 |       errors += try_dlopen (&handle, filename, archive_ext, advise);
1653 |       errors = try_dlopen (&handle, filename, shlib_ext, advise);
1848 |    passing to lt_dlopenext.  The extensions are stripped so that
1851 |    then the same directories that lt_dlopen would search are examined.  */
{% endraw %}

```
### src/graphviz/libltdl/loaders/preopen.c

```c

{% raw %}
353 | 		  lt_dlhandle handle = lt_dlopen (symbol->name);
{% endraw %}

```
### src/graphviz/libltdl/loaders/dlopen.c

```c

{% raw %}
69 |       vtable->name		= "lt_dlopen";
193 |   module = dlopen (filename, module_flags);
{% endraw %}

```
### src/graphviz/libltdl/libltdl/lt__private.h

```c

{% raw %}
111 |   const lt_dlvtable *	vtable;		/* dlopening interface */
{% endraw %}

```
### src/graphviz/libltdl/libltdl/lt_error.h

```c

{% raw %}
45 |     LT_ERROR(DLOPEN_NOT_SUPPORTED,  "dlopen support not available\0")	\
{% endraw %}

```