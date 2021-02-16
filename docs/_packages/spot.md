---
name: "spot"
layout: package
next_package: sqlcipher
previous_package: spades
languages: ['cpp', 'c']
---
## 1.2.6
23 / 4036 files match, 7 filtered matches.

 - [iface/dve2/dve2.cc](#ifacedve2dve2cc)
 - [ltdl/ltdl.h](#ltdlltdlh)
 - [ltdl/ltdl.c](#ltdlltdlc)
 - [ltdl/loaders/preopen.c](#ltdlloaderspreopenc)
 - [ltdl/loaders/dlopen.c](#ltdlloadersdlopenc)
 - [ltdl/libltdl/lt__private.h](#ltdllibltdllt__privateh)
 - [ltdl/libltdl/lt_error.h](#ltdllibltdllt_errorh)

### iface/dve2/dve2.cc

```cpp

{% raw %}
1020 |     lt_dlhandle h = lt_dlopen(file.c_str());
{% endraw %}

```
### ltdl/ltdl.h

```c

{% raw %}
76 | LT_SCOPE lt_dlhandle lt_dlopen		(const char *filename);
77 | LT_SCOPE lt_dlhandle lt_dlopenext	(const char *filename);
78 | LT_SCOPE lt_dlhandle lt_dlopenadvise	(const char *filename,
133 |   int		ref_count;	/* number of times lt_dlopened minus
{% endraw %}

```
### ltdl/ltdl.c

```c

{% raw %}
132 | static	int	try_dlopen	      (lt_dlhandle *handle,
135 | static	int	tryall_dlopen	      (lt_dlhandle *handle,
175 |    dlopen an application module.  */
242 | 	 can use _them_ to lt_dlopen its own modules.  */
367 | tryall_dlopen (lt_dlhandle *phandle, const char *filename,
375 |   fprintf (stderr, "tryall_dlopen (%s, %s)\n",
385 |       if ((handle->info.filename == filename) /* dlopen self: 0 == 0 */
485 | tryall_dlopen_module (lt_dlhandle *handle, const char *prefix,
521 |       error += tryall_dlopen_module (handle, (const char *) 0,
524 |   else if (tryall_dlopen (handle, filename, advise, 0) != 0)
539 |      we want the preopened version of it, even if a dlopenable
541 |   if (old_name && tryall_dlopen (handle, old_name,
553 | 	  if (tryall_dlopen_module (handle, (const char *) 0,
561 | 	  if (tryall_dlopen_module (handle, dir, objdir,
568 | 	  if (dir && (tryall_dlopen_module (handle, (const char *) 0,
786 |   if (tryall_dlopen (phandle, filename, advise, 0) != 0)
945 | 	  cur->deplibs[j] = lt_dlopenext(names[depcount-1-i]);
1151 | try_dlopen (lt_dlhandle *phandle, const char *filename, const char *ext,
1168 |   fprintf (stderr, "try_dlopen (%s, %s)\n",
1187 |       if (tryall_dlopen (&newhandle, 0, advise, 0) != 0)
1306 | 	  if (tryall_dlopen (&newhandle, archive_name, advise, vtable) == 0)
1473 | 	  if (tryall_dlopen (&newhandle, attempt, advise, 0) != 0)
1616 | lt_dlopen (const char *filename)
1618 |   return lt_dlopenadvise (filename, NULL);
1627 | lt_dlopenext (const char *filename)
1633 |     handle = lt_dlopenadvise (filename, advise);
1641 | lt_dlopenadvise (const char *filename, lt_dladvise advise)
1663 |       if (try_dlopen (&handle, filename, NULL, advise) != 0)
1672 |       errors += try_dlopen (&handle, filename, archive_ext, advise);
1685 |       errors = try_dlopen (&handle, filename, shlib_ext, advise);
1696 |       errors = try_dlopen (&handle, filename, shared_ext, advise);
1891 |    passing to lt_dlopenext.  The extensions are stripped so that
1894 |    then the same directories that lt_dlopen would search are examined.  */
{% endraw %}

```
### ltdl/loaders/preopen.c

```c

{% raw %}
353 | 		  lt_dlhandle handle = lt_dlopen (symbol->name);
{% endraw %}

```
### ltdl/loaders/dlopen.c

```c

{% raw %}
69 |       vtable->name		= "lt_dlopen";
193 |   module = dlopen (filename, module_flags);
{% endraw %}

```
### ltdl/libltdl/lt__private.h

```c

{% raw %}
111 |   const lt_dlvtable *	vtable;		/* dlopening interface */
{% endraw %}

```
### ltdl/libltdl/lt_error.h

```c

{% raw %}
45 |     LT_ERROR(DLOPEN_NOT_SUPPORTED,  "dlopen support not available\0")	\
{% endraw %}

```