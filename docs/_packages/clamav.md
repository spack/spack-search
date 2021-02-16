---
name: "clamav"
layout: package
next_package: modern-wheel
previous_package: llvm-doe
languages: ['c']
---
## 0.101.2
55 / 6766 files match

 - [libclamav/others.c](#libclamavothersc)
 - [libltdl/ltdl.h](#libltdlltdlh)
 - [libltdl/ltdl.c](#libltdlltdlc)
 - [libltdl/loaders/preopen.c](#libltdlloaderspreopenc)
 - [libltdl/loaders/dlopen.c](#libltdlloadersdlopenc)
 - [libltdl/libltdl/lt__private.h](#libltdllibltdllt__privateh)
 - [libltdl/libltdl/lt_error.h](#libltdllibltdllt_errorh)
 - [win32/compat/ltdl.h](#win32compatltdlh)
 - [win32/compat/ltdl.c](#win32compatltdlc)
 - [win32/3rdparty/libxml2/xmlmodule.c](#win323rdpartylibxml2xmlmodulec)
 - [win32/3rdparty/libxml2/os400/wrappers.h](#win323rdpartylibxml2os400wrappersh)
 - [win32/3rdparty/libxml2/os400/wrappers.c](#win323rdpartylibxml2os400wrappersc)
 - [win32/3rdparty/libxml2/os400/dlfcn/dlfcn.h](#win323rdpartylibxml2os400dlfcndlfcnh)
 - [win32/3rdparty/libxml2/os400/dlfcn/dlfcn.c](#win323rdpartylibxml2os400dlfcndlfcnc)

### libclamav/others.c

```c

{% raw %}
150 | 	rhandle = lt_dlopen(modulename);
160 |         cli_warnmsg("Cannot dlopen %s: %s - %s support unavailable\n", name, err, featurename);
162 |         cli_dbgmsg("Cannot dlopen %s: %s - %s support unavailable\n", name, err, featurename);
{% endraw %}

```
### libltdl/ltdl.h

```c

{% raw %}
76 | LT_SCOPE lt_dlhandle lt_dlopen		(const char *filename);
77 | LT_SCOPE lt_dlhandle lt_dlopenext	(const char *filename);
78 | LT_SCOPE lt_dlhandle lt_dlopenadvise	(const char *filename,
133 |   int		ref_count;	/* number of times lt_dlopened minus
{% endraw %}

```
### libltdl/ltdl.c

```c

{% raw %}
132 | static	int	try_dlopen	      (lt_dlhandle *handle,
135 | static	int	tryall_dlopen	      (lt_dlhandle *handle,
175 |    dlopen an application module.  */
242 | 	 can use _them_ to lt_dlopen its own modules.  */
367 | tryall_dlopen (lt_dlhandle *phandle, const char *filename,
375 |   fprintf (stderr, "tryall_dlopen (%s, %s)\n",
385 |       if ((handle->info.filename == filename) /* dlopen self: 0 == 0 */
492 | tryall_dlopen_module (lt_dlhandle *handle, const char *prefix,
528 |       error += tryall_dlopen_module (handle, (const char *) 0,
531 |   else if (tryall_dlopen (handle, filename, advise, 0) != 0)
546 |      we want the preopened version of it, even if a dlopenable
548 |   if (old_name && tryall_dlopen (handle, old_name,
560 | 	  if (tryall_dlopen_module (handle, (const char *) 0,
568 | 	  if (tryall_dlopen_module (handle, dir, objdir,
575 | 	  if (dir && (tryall_dlopen_module (handle, (const char *) 0,
793 |   if (tryall_dlopen (phandle, filename, advise, 0) != 0)
952 | 	  cur->deplibs[j] = lt_dlopenext(names[depcount-1-i]);
1158 | try_dlopen (lt_dlhandle *phandle, const char *filename, const char *ext,
1175 |   fprintf (stderr, "try_dlopen (%s, %s)\n",
1194 |       if (tryall_dlopen (&newhandle, 0, advise, 0) != 0)
1313 | 	  if (tryall_dlopen (&newhandle, archive_name, advise, vtable) == 0)
1480 | 	  if (tryall_dlopen (&newhandle, attempt, advise, 0) != 0)
1623 | lt_dlopen (const char *filename)
1625 |   return lt_dlopenadvise (filename, NULL);
1634 | lt_dlopenext (const char *filename)
1640 |     handle = lt_dlopenadvise (filename, advise);
1648 | lt_dlopenadvise (const char *filename, lt_dladvise advise)
1670 |       if (try_dlopen (&handle, filename, NULL, advise) != 0)
1679 |       errors += try_dlopen (&handle, filename, archive_ext, advise);
1692 |       errors = try_dlopen (&handle, filename, shlib_ext, advise);
1703 |       errors = try_dlopen (&handle, filename, shared_ext, advise);
1898 |    passing to lt_dlopenext.  The extensions are stripped so that
1901 |    then the same directories that lt_dlopen would search are examined.  */
{% endraw %}

```
### libltdl/loaders/preopen.c

```c

{% raw %}
365 | 		  lt_dlhandle handle = lt_dlopen (symbol->name);
{% endraw %}

```
### libltdl/loaders/dlopen.c

```c

{% raw %}
69 |       vtable->name		= "lt_dlopen";
210 |   module = dlopen (filename, module_flags);
{% endraw %}

```
### libltdl/libltdl/lt__private.h

```c

{% raw %}
111 |   const lt_dlvtable *	vtable;		/* dlopening interface */
{% endraw %}

```
### libltdl/libltdl/lt_error.h

```c

{% raw %}
46 |     LT_ERROR(DLOPEN_NOT_SUPPORTED,  "dlopen support not available\0")	\
{% endraw %}

```
### win32/compat/ltdl.h

```c

{% raw %}
31 | lt_dlhandle lt_dlopen(const char *filename);
41 |   int		ref_count;	/* number of times lt_dlopened minus
{% endraw %}

```
### win32/compat/ltdl.c

```c

{% raw %}
30 | lt_dlhandle lt_dlopen(const char *filename) {
{% endraw %}

```
### win32/3rdparty/libxml2/xmlmodule.c

```c

{% raw %}
224 |     return dlopen(name, RTLD_GLOBAL | RTLD_NOW);
{% endraw %}

```
### win32/3rdparty/libxml2/os400/wrappers.h

```c

{% raw %}
40 | extern void *   _lx_dlopen(const char * filename, int flag);
{% endraw %}

```
### win32/3rdparty/libxml2/os400/wrappers.c

```c

{% raw %}
70 | _lx_dlopen(const char * filename, int flag)
76 |         result = dlopen(xmlTranscodeResult(filename, NULL, &d, NULL), flag);
{% endraw %}

```
### win32/3rdparty/libxml2/os400/dlfcn/dlfcn.h

```c

{% raw %}
26 | extern void *           dlopen(const char * filename, int flag);
{% endraw %}

```
### win32/3rdparty/libxml2/os400/dlfcn/dlfcn.c

```c

{% raw %}
1046 | dlopenqsys(const Qp0l_QSYS_Info_t * dllinfo)
1155 | dlopen(const char * filename, int flag)
1187 |                 dlhandle = dlopenqsys(&dllinfo);
1190 |                 dlhandle = dlopenqsys(&dllinfo);
1192 |                 dlhandle = dlopenqsys(&dllinfo);
1194 |                 dlhandle = dlopenqsys(&dllinfo);
1197 |                 dlhandle = dlopenqsys(&dllinfo);
1200 |                 dlhandle = dlopenqsys(&dllinfo);
1203 |                 dlhandle = dlopenqsys(&dllinfo);
{% endraw %}

```