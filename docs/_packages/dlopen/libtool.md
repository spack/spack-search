---
name: "libtool"
layout: package
next_package: nest
previous_package: ffmpeg
library_name: dlopen
matches: ['dlsym', 'dlopen', 'dlmopen']
languages: ['c']
---
## 2.4.6
49 / 327 files match, 6 filtered matches.

 - [libltdl/ltdl.h](#libltdlltdlh)
 - [libltdl/ltdl.c](#libltdlltdlc)
 - [libltdl/loaders/preopen.c](#libltdlloaderspreopenc)
 - [libltdl/loaders/dlopen.c](#libltdlloadersdlopenc)
 - [libltdl/libltdl/lt__private.h](#libltdllibltdllt__privateh)
 - [libltdl/libltdl/lt_error.h](#libltdllibltdllt_errorh)

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
387 | 	      && STREQ (handle->info.filename, filename)))
489 | 
490 | 
491 | static int
492 | tryall_dlopen_module (lt_dlhandle *handle, const char *prefix,
493 | 		      const char *dirname, const char *dlname,
494 | 		      lt_dladvise advise)
525 |      shuffled.  Otherwise, attempt to open FILENAME as a module.  */
526 |   if (prefix)
527 |     {
528 |       error += tryall_dlopen_module (handle, (const char *) 0,
529 | 				     prefix, filename, advise);
530 |     }
531 |   else if (tryall_dlopen (handle, filename, advise, 0) != 0)
532 |     {
533 |       ++error;
543 | 	     lt_dladvise advise)
544 | {
545 |   /* Try to open the old library first; if it was dlpreopened,
546 |      we want the preopened version of it, even if a dlopenable
547 |      module is available.  */
548 |   if (old_name && tryall_dlopen (handle, old_name,
549 | 			  advise, lt_dlloader_find ("lt_preopen") ) == 0)
550 |     {
557 |       /* try to open the installed module */
558 |       if (installed && libdir)
559 | 	{
560 | 	  if (tryall_dlopen_module (handle, (const char *) 0,
561 | 				    libdir, dlname, advise) == 0)
562 | 	    return 0;
565 |       /* try to open the not-installed module */
566 |       if (!installed)
567 | 	{
568 | 	  if (tryall_dlopen_module (handle, dir, objdir,
569 | 				    dlname, advise) == 0)
570 | 	    return 0;
572 | 
573 |       /* maybe it was moved to another directory */
574 |       {
575 | 	  if (dir && (tryall_dlopen_module (handle, (const char *) 0,
576 | 					    dir, dlname, advise) == 0))
577 | 	    return 0;
790 | 
791 |   /* Try to dlopen the file, but do not continue searching in any
792 |      case.  */
793 |   if (tryall_dlopen (phandle, filename, advise, 0) != 0)
794 |     *phandle = 0;
795 | 
949 | 
950 |       for (i = 0; i < depcount; ++i)
951 | 	{
952 | 	  cur->deplibs[j] = lt_dlopenext(names[depcount-1-i]);
953 | 	  if (cur->deplibs[j])
954 | 	    {
1155 | 
1156 | /* Try to open FILENAME as a module. */
1157 | static int
1158 | try_dlopen (lt_dlhandle *phandle, const char *filename, const char *ext,
1159 | 	    lt_dladvise advise)
1160 | {
1172 |   assert (*phandle == 0);
1173 | 
1174 | #ifdef LT_DEBUG_LOADERS
1175 |   fprintf (stderr, "try_dlopen (%s, %s)\n",
1176 | 	   filename ? filename : "(null)",
1177 | 	   ext ? ext : "(null)");
1191 |       /* lt_dlclose()ing yourself is very bad!  Disallow it.  */
1192 |       newhandle->info.is_resident = 1;
1193 | 
1194 |       if (tryall_dlopen (&newhandle, 0, advise, 0) != 0)
1195 | 	{
1196 | 	  FREE (*phandle);
1310 | 	      sprintf (archive_name, "%s.%s", name, libext);
1311 | 	    }
1312 | 
1313 | 	  if (tryall_dlopen (&newhandle, archive_name, advise, vtable) == 0)
1314 | 	    {
1315 | 	      goto register_handle;
1477 | #endif
1478 | 		   )))
1479 | 	{
1480 | 	  if (tryall_dlopen (&newhandle, attempt, advise, 0) != 0)
1481 | 	    {
1482 | 	      newhandle = NULL;
1620 | 
1621 | /* Libtool-1.5.x interface for loading a new module named FILENAME.  */
1622 | lt_dlhandle
1623 | lt_dlopen (const char *filename)
1624 | {
1625 |   return lt_dlopenadvise (filename, NULL);
1626 | }
1627 | 
1631 |    and if a file is still not found try again with MODULE_EXT appended
1632 |    instead.  */
1633 | lt_dlhandle
1634 | lt_dlopenext (const char *filename)
1635 | {
1636 |   lt_dlhandle	handle	= 0;
1637 |   lt_dladvise	advise;
1638 | 
1639 |   if (!lt_dladvise_init (&advise) && !lt_dladvise_ext (&advise))
1640 |     handle = lt_dlopenadvise (filename, advise);
1641 | 
1642 |   lt_dladvise_destroy (&advise);
1645 | 
1646 | 
1647 | lt_dlhandle
1648 | lt_dlopenadvise (const char *filename, lt_dladvise advise)
1649 | {
1650 |   lt_dlhandle	handle	= 0;
1667 |     {
1668 |       /* Just incase we missed a code path in try_dlopen() that reports
1669 | 	 an error, but forgot to reset handle... */
1670 |       if (try_dlopen (&handle, filename, NULL, advise) != 0)
1671 | 	return 0;
1672 | 
1676 |     {
1677 | 
1678 |       /* First try appending ARCHIVE_EXT.  */
1679 |       errors += try_dlopen (&handle, filename, archive_ext, advise);
1680 | 
1681 |       /* If we found FILENAME, stop searching -- whether we were able to
1689 | #if defined LT_MODULE_EXT
1690 |       /* Try appending SHLIB_EXT.   */
1691 |       LT__SETERRORSTR (saved_error);
1692 |       errors = try_dlopen (&handle, filename, shlib_ext, advise);
1693 | 
1694 |       /* As before, if the file was found but loading failed, return now
1700 | #if defined LT_SHARED_EXT
1701 |       /* Try appending SHARED_EXT.   */
1702 |       LT__SETERRORSTR (saved_error);
1703 |       errors = try_dlopen (&handle, filename, shared_ext, advise);
1704 | 
1705 |       /* As before, if the file was found but loading failed, return now
1895 | 
1896 | /* Call FUNC for each unique extensionless file in SEARCH_PATH, along
1897 |    with DATA.  The filenames passed to FUNC would be suitable for
1898 |    passing to lt_dlopenext.  The extensions are stripped so that
1899 |    individual modules do not generate several entries (e.g. libfoo.la,
1900 |    libfoo.so, libfoo.so.1, libfoo.so.1.0.0).  If SEARCH_PATH is NULL,
1901 |    then the same directories that lt_dlopen would search are examined.  */
1902 | int
1903 | lt_dlforeachfile (const char *search_path,
{% endraw %}

```
### libltdl/loaders/preopen.c

```c

{% raw %}
362 | 	      if ((symbol->address == 0)
363 | 		  && (STRNEQ (symbol->name, "@PROGRAM@")))
364 | 		{
365 | 		  lt_dlhandle handle = lt_dlopen (symbol->name);
366 | 		  if (handle == 0)
367 | 		    {
{% endraw %}

```
### libltdl/loaders/dlopen.c

```c

{% raw %}
66 | 
67 |   if (vtable && !vtable->name)
68 |     {
69 |       vtable->name		= "lt_dlopen";
70 | #if defined DLSYM_USCORE
71 |       vtable->sym_prefix	= "_";
207 |     }
208 | #endif
209 | 
210 |   module = dlopen (filename, module_flags);
211 | 
212 | #if defined RTLD_MEMBER && defined LT_SHARED_LIB_MEMBER
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
43 |    expilicitely initialize the string terminator. */
44 | #define lt_dlerror_table						\
45 |     LT_ERROR(UNKNOWN,		    "unknown error\0")			\
46 |     LT_ERROR(DLOPEN_NOT_SUPPORTED,  "dlopen support not available\0")	\
47 |     LT_ERROR(INVALID_LOADER,	    "invalid loader\0")			\
48 |     LT_ERROR(INIT_LOADER,	    "loader initialization failed\0")	\
{% endraw %}

```