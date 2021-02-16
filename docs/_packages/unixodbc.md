---
name: "unixodbc"
layout: package
next_package: r-nloptr
previous_package: fastjar
languages: ['c']
---
## 2.3.4
44 / 845 files match

 - [exe/dltest.c](#exedltestc)
 - [extras/vms.c](#extrasvmsc)
 - [odbcinst/SQLConfigDataSource.c](#odbcinstsqlconfigdatasourcec)
 - [odbcinst/SQLCreateDataSource.c](#odbcinstsqlcreatedatasourcec)
 - [odbcinst/ODBCINSTConstructProperties.c](#odbcinstodbcinstconstructpropertiesc)
 - [odbcinst/SQLConfigDriver.c](#odbcinstsqlconfigdriverc)
 - [odbcinst/_SQLDriverConnectPrompt.c](#odbcinst_sqldriverconnectpromptc)
 - [odbcinst/SQLManageDataSources.c](#odbcinstsqlmanagedatasourcesc)
 - [DriverManager/SQLConnect.c](#drivermanagersqlconnectc)
 - [libltdl/ltdl.h](#libltdlltdlh)
 - [libltdl/ltdl.c](#libltdlltdlc)
 - [libltdl/loaders/preopen.c](#libltdlloaderspreopenc)
 - [libltdl/loaders/dlopen.c](#libltdlloadersdlopenc)
 - [libltdl/libltdl/lt__private.h](#libltdllibltdllt__privateh)
 - [libltdl/libltdl/lt_error.h](#libltdllibltdllt_errorh)

### exe/dltest.c

```c

{% raw %}
42 | "*      man page for dlopen to create a       *\n" \
78 |     hDLL = lt_dlopen( argv[1] );
81 | 		printf( "[dltest] ERROR dlopen: %s\n", lt_dlerror() );
{% endraw %}

```
### extras/vms.c

```c

{% raw %}
48 | void * lt_dlopen (const char *filename)
{% endraw %}

```
### odbcinst/SQLConfigDataSource.c

```c

{% raw %}
104 | 		if ( (hDLL = lt_dlopen( szDriverSetup ))  )
{% endraw %}

```
### odbcinst/SQLCreateDataSource.c

```c

{% raw %}
203 |     hDLL = lt_dlopen( szNameAndExtension );
217 |         hDLL = lt_dlopen( szPathAndName );
{% endraw %}

```
### odbcinst/ODBCINSTConstructProperties.c

```c

{% raw %}
169 | 	if ( !(hDLL = lt_dlopen( szDriverSetup ))  )
{% endraw %}

```
### odbcinst/SQLConfigDriver.c

```c

{% raw %}
105 | 		if ( (hDLL = lt_dlopen( szDriverSetup ))  )
{% endraw %}

```
### odbcinst/_SQLDriverConnectPrompt.c

```c

{% raw %}
33 |     hDLL = lt_dlopen( szNameAndExtension );
58 |         hDLL = lt_dlopen( szPathAndName );
{% endraw %}

```
### odbcinst/SQLManageDataSources.c

```c

{% raw %}
150 |     hDLL = lt_dlopen( szNameAndExtension );
165 |         hDLL = lt_dlopen( szPathAndName );
{% endraw %}

```
### DriverManager/SQLConnect.c

```c

{% raw %}
810 | static void *odbc_dlopen( char *libname, char **err )
839 |         hand = lt_dlopen( libname );
1129 |     if ( !(connection -> dl_handle = odbc_dlopen( driver_lib, &err )))
2333 |         if ( !(connection -> cl_handle = odbc_dlopen( name, &err )))
2363 |             if ( !(connection -> cl_handle = odbc_dlopen( name, &err )))
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
### libltdl/loaders/preopen.c

```c

{% raw %}
353 | 		  lt_dlhandle handle = lt_dlopen (symbol->name);
{% endraw %}

```
### libltdl/loaders/dlopen.c

```c

{% raw %}
69 |       vtable->name		= "lt_dlopen";
193 |   module = dlopen (filename, module_flags);
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
45 |     LT_ERROR(DLOPEN_NOT_SUPPORTED,  "dlopen support not available\0")	\
{% endraw %}

```