---
name: "unixodbc"
layout: package
next_package: numamma
previous_package: global
library_name: dlopen
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 2.3.4
44 / 845 files match, 15 filtered matches.

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
39 | "*      unresolved symbol in the lib. This is *\n" \
40 | "*      not caught since dltest started using *\n" \
41 | "*      libtool. Linux users can refer to the *\n" \
42 | "*      man page for dlopen to create a       *\n" \
43 | "*      better test.                          *\n" \
44 | "*                                            *\n" \
75 | 		exit( 1 );
76 | 	}
77 | 
78 |     hDLL = lt_dlopen( argv[1] );
79 | 	if ( !hDLL )
80 | 	{
81 | 		printf( "[dltest] ERROR dlopen: %s\n", lt_dlerror() );
82 | 		exit( 1 );
83 | 	}
{% endraw %}

```
### extras/vms.c

```c

{% raw %}
45 | 	return 1;
46 | }
47 | 
48 | void * lt_dlopen (const char *filename)
49 | {
50 | 
{% endraw %}

```
### odbcinst/SQLConfigDataSource.c

```c

{% raw %}
101 | 		}
102 | 
103 | 		nReturn = FALSE;
104 | 		if ( (hDLL = lt_dlopen( szDriverSetup ))  )
105 | 		{
106 | 			pFunc = (BOOL (*)(HWND, WORD, LPCSTR, LPCSTR )) lt_dlsym( hDLL, "ConfigDSN" );
{% endraw %}

```
### odbcinst/SQLCreateDataSource.c

```c

{% raw %}
200 |     _appendUIPluginExtension( szNameAndExtension, _getUIPluginName( szName, hODBCInstWnd->szUI ) );
201 | 
202 |     /* lets try loading the plugin using an implicit path */
203 |     hDLL = lt_dlopen( szNameAndExtension );
204 |     if ( hDLL )
205 |     {
214 |     {
215 |         /* try with explicit path */
216 |         _prependUIPluginPath( szPathAndName, szNameAndExtension );
217 |         hDLL = lt_dlopen( szPathAndName );
218 |         if ( hDLL )
219 |         {
{% endraw %}

```
### odbcinst/ODBCINSTConstructProperties.c

```c

{% raw %}
166 |     lt_dlinit();
167 | 
168 | 	/* TRY GET FUNC FROM DRIVER SETUP */
169 | 	if ( !(hDLL = lt_dlopen( szDriverSetup ))  )
170 | 	{
171 | 		inst_logPushMsg( __FILE__, __FILE__, __LINE__, LOG_CRITICAL, ODBC_ERROR_GENERAL_ERR, "Could not load library" );
{% endraw %}

```
### odbcinst/SQLConfigDriver.c

```c

{% raw %}
102 | 	case ODBC_REMOVE_DRIVER:
103 | 	default :						/* DRIVER SEPCIFIC are default; HANDLE AS PER INSTALL & REMOVE */
104 | 		/* errors in here are ignored, according to the spec; perhaps I should ret error and let app ignore? */
105 | 		if ( (hDLL = lt_dlopen( szDriverSetup ))  )
106 | 		{
107 | 			pConfigDriver = (BOOL (*)(HWND, WORD, LPCSTR, LPCSTR, LPCSTR, WORD, WORD * )) lt_dlsym( hDLL, "ConfigDriver" );
{% endraw %}

```
### odbcinst/_SQLDriverConnectPrompt.c

```c

{% raw %}
30 | 	}
31 | 
32 |     /* lets try loading the plugin using an implicit path */
33 |     hDLL = lt_dlopen( szNameAndExtension );
34 |     if ( hDLL )
35 |     {
55 |     {
56 |         /* try with explicit path */
57 |         _prependUIPluginPath( szPathAndName, szNameAndExtension );
58 |         hDLL = lt_dlopen( szPathAndName );
59 |         if ( hDLL )
60 |         {
{% endraw %}

```
### odbcinst/SQLManageDataSources.c

```c

{% raw %}
147 |     _appendUIPluginExtension( szNameAndExtension, _getUIPluginName( szName, hODBCInstWnd->szUI ) );
148 | 
149 |     /* lets try loading the plugin using an implicit path */
150 |     hDLL = lt_dlopen( szNameAndExtension );
151 |     if ( hDLL )
152 |     {
162 |         inst_logPushMsg( __FILE__, __FILE__, __LINE__, LOG_WARNING, ODBC_ERROR_GENERAL_ERR, (char*)lt_dlerror() );
163 |         /* try with explicit path */
164 |         _prependUIPluginPath( szPathAndName, szNameAndExtension );
165 |         hDLL = lt_dlopen( szPathAndName );
166 |         if ( hDLL )
167 |         {
{% endraw %}

```
### DriverManager/SQLConnect.c

```c

{% raw %}
807 | static struct lib_count single_lib_count;
808 | static char single_lib_name[ INI_MAX_PROPERTY_VALUE + 1 ];
809 | 
810 | static void *odbc_dlopen( char *libname, char **err )
811 | {
812 |     void *hand;
836 |     }
837 |     else
838 |     {
839 |         hand = lt_dlopen( libname );
840 | 
841 |         if ( hand )
1126 |     connection -> functions = NULL;
1127 |     connection -> dl_handle = NULL;
1128 | 
1129 |     if ( !(connection -> dl_handle = odbc_dlopen( driver_lib, &err )))
1130 |     {
1131 |         char txt[ 2048 ];
2330 |             sprintf( name, "%s%s", CURSOR_LIB, ext );
2331 | #endif
2332 | 
2333 |         if ( !(connection -> cl_handle = odbc_dlopen( name, &err )))
2334 |         {
2335 |             char b1[ ODBC_FILENAME_MAX + 1 ];
2360 | #endif
2361 | #endif
2362 | #endif
2363 |             if ( !(connection -> cl_handle = odbc_dlopen( name, &err )))
2364 |             {
2365 |                 char txt[ 256 ];
{% endraw %}

```
### libltdl/ltdl.h

```c

{% raw %}
73 | LT_SCOPE int	    lt_dladvise_preload	 (lt_dladvise *advise);
74 | 
75 | /* Portable libltdl versions of the system dlopen() API. */
76 | LT_SCOPE lt_dlhandle lt_dlopen		(const char *filename);
77 | LT_SCOPE lt_dlhandle lt_dlopenext	(const char *filename);
78 | LT_SCOPE lt_dlhandle lt_dlopenadvise	(const char *filename,
79 | 					 lt_dladvise advise);
80 | LT_SCOPE void *	    lt_dlsym		(lt_dlhandle handle, const char *name);
130 | typedef	struct {
131 |   char *	filename;	/* file name */
132 |   char *	name;		/* module name */
133 |   int		ref_count;	/* number of times lt_dlopened minus
134 | 				   number of times lt_dlclosed. */
135 |   unsigned int	is_resident:1;	/* module can't be unloaded. */
{% endraw %}

```
### libltdl/ltdl.c

```c

{% raw %}
129 | static  int     has_library_ext       (const char *filename);
130 | static	int	load_deplibs	      (lt_dlhandle handle,  char *deplibs);
131 | static	int	trim		      (char **dest, const char *str);
132 | static	int	try_dlopen	      (lt_dlhandle *handle,
133 | 				       const char *filename, const char *ext,
134 | 				       lt_dladvise advise);
135 | static	int	tryall_dlopen	      (lt_dlhandle *handle,
136 | 				       const char *filename,
137 | 				       lt_dladvise padvise,
172 | #ifdef HAVE_LIBDLLOADER
173 | /* This function is called to initialise each preloaded module loader,
174 |    and hook it into the list of loaders to be used when attempting to
175 |    dlopen an application module.  */
176 | static int
177 | loader_init_callback (lt_dlhandle handle)
239 |       errors += loader_init (get_vtable, 0);
240 | 
241 |       /* Now open all the preloaded module loaders, so the application
242 | 	 can use _them_ to lt_dlopen its own modules.  */
243 | #ifdef HAVE_LIBDLLOADER
244 |       if (!errors)
364 |    If the library is not successfully loaded, return non-zero.  Otherwise,
365 |    the dlhandle is stored at the address given in PHANDLE.  */
366 | static int
367 | tryall_dlopen (lt_dlhandle *phandle, const char *filename,
368 | 	       lt_dladvise advise, const lt_dlvtable *vtable)
369 | {
372 |   int		errors		= 0;
373 | 
374 | #ifdef LT_DEBUG_LOADERS
375 |   fprintf (stderr, "tryall_dlopen (%s, %s)\n",
376 | 	   filename ? filename : "(null)",
377 | 	   vtable ? vtable->name : "(ALL)");
382 |   /* check whether the module was already opened */
383 |   for (;handle; handle = handle->next)
384 |     {
385 |       if ((handle->info.filename == filename) /* dlopen self: 0 == 0 */
386 | 	  || (handle->info.filename && filename
387 | 	      && streq (handle->info.filename, filename)))
482 | 
483 | 
484 | static int
485 | tryall_dlopen_module (lt_dlhandle *handle, const char *prefix,
486 | 		      const char *dirname, const char *dlname,
487 | 		      lt_dladvise advise)
518 |      shuffled.  Otherwise, attempt to open FILENAME as a module.  */
519 |   if (prefix)
520 |     {
521 |       error += tryall_dlopen_module (handle, (const char *) 0,
522 | 				     prefix, filename, advise);
523 |     }
524 |   else if (tryall_dlopen (handle, filename, advise, 0) != 0)
525 |     {
526 |       ++error;
536 | 	     lt_dladvise advise)
537 | {
538 |   /* Try to open the old library first; if it was dlpreopened,
539 |      we want the preopened version of it, even if a dlopenable
540 |      module is available.  */
541 |   if (old_name && tryall_dlopen (handle, old_name,
542 | 			  advise, lt_dlloader_find ("lt_preopen") ) == 0)
543 |     {
550 |       /* try to open the installed module */
551 |       if (installed && libdir)
552 | 	{
553 | 	  if (tryall_dlopen_module (handle, (const char *) 0,
554 | 				    libdir, dlname, advise) == 0)
555 | 	    return 0;
558 |       /* try to open the not-installed module */
559 |       if (!installed)
560 | 	{
561 | 	  if (tryall_dlopen_module (handle, dir, objdir,
562 | 				    dlname, advise) == 0)
563 | 	    return 0;
565 | 
566 |       /* maybe it was moved to another directory */
567 |       {
568 | 	  if (dir && (tryall_dlopen_module (handle, (const char *) 0,
569 | 					    dir, dlname, advise) == 0))
570 | 	    return 0;
783 | 
784 |   /* Try to dlopen the file, but do not continue searching in any
785 |      case.  */
786 |   if (tryall_dlopen (phandle, filename, advise, 0) != 0)
787 |     *phandle = 0;
788 | 
942 | 
943 |       for (i = 0; i < depcount; ++i)
944 | 	{
945 | 	  cur->deplibs[j] = lt_dlopenext(names[depcount-1-i]);
946 | 	  if (cur->deplibs[j])
947 | 	    {
1148 | 
1149 | /* Try to open FILENAME as a module. */
1150 | static int
1151 | try_dlopen (lt_dlhandle *phandle, const char *filename, const char *ext,
1152 | 	    lt_dladvise advise)
1153 | {
1165 |   assert (*phandle == 0);
1166 | 
1167 | #ifdef LT_DEBUG_LOADERS
1168 |   fprintf (stderr, "try_dlopen (%s, %s)\n",
1169 | 	   filename ? filename : "(null)",
1170 | 	   ext ? ext : "(null)");
1184 |       /* lt_dlclose()ing yourself is very bad!  Disallow it.  */
1185 |       newhandle->info.is_resident = 1;
1186 | 
1187 |       if (tryall_dlopen (&newhandle, 0, advise, 0) != 0)
1188 | 	{
1189 | 	  FREE (*phandle);
1303 | 	      sprintf (archive_name, "%s.%s", name, libext);
1304 | 	    }
1305 | 
1306 | 	  if (tryall_dlopen (&newhandle, archive_name, advise, vtable) == 0)
1307 | 	    {
1308 | 	      goto register_handle;
1470 | #endif
1471 | 		   )))
1472 | 	{
1473 | 	  if (tryall_dlopen (&newhandle, attempt, advise, 0) != 0)
1474 | 	    {
1475 | 	      newhandle = NULL;
1613 | 
1614 | /* Libtool-1.5.x interface for loading a new module named FILENAME.  */
1615 | lt_dlhandle
1616 | lt_dlopen (const char *filename)
1617 | {
1618 |   return lt_dlopenadvise (filename, NULL);
1619 | }
1620 | 
1624 |    and if a file is still not found try again with MODULE_EXT appended
1625 |    instead.  */
1626 | lt_dlhandle
1627 | lt_dlopenext (const char *filename)
1628 | {
1629 |   lt_dlhandle	handle	= 0;
1630 |   lt_dladvise	advise;
1631 | 
1632 |   if (!lt_dladvise_init (&advise) && !lt_dladvise_ext (&advise))
1633 |     handle = lt_dlopenadvise (filename, advise);
1634 | 
1635 |   lt_dladvise_destroy (&advise);
1638 | 
1639 | 
1640 | lt_dlhandle
1641 | lt_dlopenadvise (const char *filename, lt_dladvise advise)
1642 | {
1643 |   lt_dlhandle	handle	= 0;
1660 |     {
1661 |       /* Just incase we missed a code path in try_dlopen() that reports
1662 | 	 an error, but forgot to reset handle... */
1663 |       if (try_dlopen (&handle, filename, NULL, advise) != 0)
1664 | 	return 0;
1665 | 
1669 |     {
1670 | 
1671 |       /* First try appending ARCHIVE_EXT.  */
1672 |       errors += try_dlopen (&handle, filename, archive_ext, advise);
1673 | 
1674 |       /* If we found FILENAME, stop searching -- whether we were able to
1682 | #if defined(LT_MODULE_EXT)
1683 |       /* Try appending SHLIB_EXT.   */
1684 |       LT__SETERRORSTR (saved_error);
1685 |       errors = try_dlopen (&handle, filename, shlib_ext, advise);
1686 | 
1687 |       /* As before, if the file was found but loading failed, return now
1693 | #if defined(LT_SHARED_EXT)
1694 |       /* Try appending SHARED_EXT.   */
1695 |       LT__SETERRORSTR (saved_error);
1696 |       errors = try_dlopen (&handle, filename, shared_ext, advise);
1697 | 
1698 |       /* As before, if the file was found but loading failed, return now
1888 | 
1889 | /* Call FUNC for each unique extensionless file in SEARCH_PATH, along
1890 |    with DATA.  The filenames passed to FUNC would be suitable for
1891 |    passing to lt_dlopenext.  The extensions are stripped so that
1892 |    individual modules do not generate several entries (e.g. libfoo.la,
1893 |    libfoo.so, libfoo.so.1, libfoo.so.1.0.0).  If SEARCH_PATH is NULL,
1894 |    then the same directories that lt_dlopen would search are examined.  */
1895 | int
1896 | lt_dlforeachfile (const char *search_path,
{% endraw %}

```
### libltdl/loaders/preopen.c

```c

{% raw %}
350 | 	      if ((symbol->address == 0)
351 | 		  && (strneq (symbol->name, "@PROGRAM@")))
352 | 		{
353 | 		  lt_dlhandle handle = lt_dlopen (symbol->name);
354 | 		  if (handle == 0)
355 | 		    {
{% endraw %}

```
### libltdl/loaders/dlopen.c

```c

{% raw %}
66 | 
67 |   if (vtable && !vtable->name)
68 |     {
69 |       vtable->name		= "lt_dlopen";
70 | #if defined(DLSYM_USCORE)
71 |       vtable->sym_prefix	= "_";
190 | #endif
191 |     }
192 | 
193 |   module = dlopen (filename, module_flags);
194 | 
195 |   if (!module)
{% endraw %}

```
### libltdl/libltdl/lt__private.h

```c

{% raw %}
108 | 
109 | struct lt__handle {
110 |   lt_dlhandle		next;
111 |   const lt_dlvtable *	vtable;		/* dlopening interface */
112 |   lt_dlinfo		info;		/* user visible fields */
113 |   int			depcount;	/* number of dependencies */
{% endraw %}

```
### libltdl/libltdl/lt_error.h

```c

{% raw %}
42 |    expilicitely initialize the string terminator. */
43 | #define lt_dlerror_table						\
44 |     LT_ERROR(UNKNOWN,		    "unknown error\0")			\
45 |     LT_ERROR(DLOPEN_NOT_SUPPORTED,  "dlopen support not available\0")	\
46 |     LT_ERROR(INVALID_LOADER,	    "invalid loader\0")			\
47 |     LT_ERROR(INIT_LOADER,	    "loader initialization failed\0")	\
{% endraw %}

```