---
name: "r-rgraphviz"
layout: package
next_package: r-rhtslib
previous_package: r-rcppcctz
languages: ['c']
---
## 2.20.0
38 / 778 files match, 7 filtered matches.

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
193 |         agerr(AGERR, "failed to init libltdl\n");
194 |         return NULL;
195 |     }
196 |     hndl = lt_dlopen (p);
197 |     if (!hndl) {
198 |         agerr(AGWARN, "Could not load \"%s\" - %s\n", p, (char*)lt_dlerror());
{% endraw %}

```
### src/graphviz/libltdl/ltdl.h

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
129 | typedef	struct {
130 |   char *	filename;	/* file name */
131 |   char *	name;		/* module name */
132 |   int		ref_count;	/* number of times lt_dlopened minus
133 | 				   number of times lt_dlclosed. */
134 |   unsigned int	is_resident:1;	/* module can't be unloaded. */
{% endraw %}

```
### src/graphviz/libltdl/ltdl.c

```c

{% raw %}
119 | static  int     has_library_ext       (const char *filename);
120 | static	int	load_deplibs	      (lt_dlhandle handle,  char *deplibs);
121 | static	int	trim		      (char **dest, const char *str);
122 | static	int	try_dlopen	      (lt_dlhandle *handle,
123 | 				       const char *filename, const char *ext,
124 | 				       lt_dladvise advise);
125 | static	int	tryall_dlopen	      (lt_dlhandle *handle,
126 | 				       const char *filename,
127 | 				       lt_dladvise padvise,
162 | #ifdef HAVE_LIBDLLOADER
163 | /* This function is called to initialise each preloaded module loader,
164 |    and hook it into the list of loaders to be used when attempting to
165 |    dlopen an application module.  */
166 | static int
167 | loader_init_callback (lt_dlhandle handle)
229 |       errors += loader_init (get_vtable, 0);
230 | 
231 |       /* Now open all the preloaded module loaders, so the application
232 | 	 can use _them_ to lt_dlopen its own modules.  */
233 | #ifdef HAVE_LIBDLLOADER
234 |       if (!errors)
354 |    If the library is not successfully loaded, return non-zero.  Otherwise,
355 |    the dlhandle is stored at the address given in PHANDLE.  */
356 | static int
357 | tryall_dlopen (lt_dlhandle *phandle, const char *filename,
358 | 	       lt_dladvise advise, const lt_dlvtable *vtable)
359 | {
362 |   int		errors		= 0;
363 | 
364 | #ifdef LT_DEBUG_LOADERS
365 |   fprintf (stderr, "tryall_dlopen (%s, %s)\n",
366 | 	   filename ? filename : "(null)",
367 | 	   vtable ? vtable->name : "(ALL)");
372 |   /* check whether the module was already opened */
373 |   for (;handle; handle = handle->next)
374 |     {
375 |       if ((handle->info.filename == filename) /* dlopen self: 0 == 0 */
376 | 	  || (handle->info.filename && filename
377 | 	      && streq (handle->info.filename, filename)))
472 | 
473 | 
474 | static int
475 | tryall_dlopen_module (lt_dlhandle *handle, const char *prefix,
476 | 		      const char *dirname, const char *dlname,
477 | 		      lt_dladvise advise)
508 |      shuffled.  Otherwise, attempt to open FILENAME as a module.  */
509 |   if (prefix)
510 |     {
511 |       error += tryall_dlopen_module (handle, (const char *) 0,
512 | 				     prefix, filename, advise);
513 |     }
514 |   else if (tryall_dlopen (handle, filename, advise, 0) != 0)
515 |     {
516 |       ++error;
526 | 	     lt_dladvise advise)
527 | {
528 |   /* Try to open the old library first; if it was dlpreopened,
529 |      we want the preopened version of it, even if a dlopenable
530 |      module is available.  */
531 |   if (old_name && tryall_dlopen (handle, old_name,
532 | 			  advise, lt_dlloader_find ("lt_preopen") ) == 0)
533 |     {
540 |       /* try to open the installed module */
541 |       if (installed && libdir)
542 | 	{
543 | 	  if (tryall_dlopen_module (handle, (const char *) 0,
544 | 				    libdir, dlname, advise) == 0)
545 | 	    return 0;
548 |       /* try to open the not-installed module */
549 |       if (!installed)
550 | 	{
551 | 	  if (tryall_dlopen_module (handle, dir, objdir,
552 | 				    dlname, advise) == 0)
553 | 	    return 0;
555 | 
556 |       /* maybe it was moved to another directory */
557 |       {
558 | 	  if (dir && (tryall_dlopen_module (handle, (const char *) 0,
559 | 					    dir, dlname, advise) == 0))
560 | 	    return 0;
773 | 
774 |   /* Try to dlopen the file, but do not continue searching in any
775 |      case.  */
776 |   if (tryall_dlopen (phandle, filename, advise, 0) != 0)
777 |     *phandle = 0;
778 | 
932 | 
933 |       for (i = 0; i < depcount; ++i)
934 | 	{
935 | 	  cur->deplibs[j] = lt_dlopenext(names[depcount-1-i]);
936 | 	  if (cur->deplibs[j])
937 | 	    {
1130 | 
1131 | /* Try to open FILENAME as a module. */
1132 | static int
1133 | try_dlopen (lt_dlhandle *phandle, const char *filename, const char *ext,
1134 | 	    lt_dladvise advise)
1135 | {
1147 |   assert (*phandle == 0);
1148 | 
1149 | #ifdef LT_DEBUG_LOADERS
1150 |   fprintf (stderr, "try_dlopen (%s, %s)\n",
1151 | 	   filename ? filename : "(null)",
1152 | 	   ext ? ext : "(null)");
1166 |       /* lt_dlclose()ing yourself is very bad!  Disallow it.  */
1167 |       newhandle->info.is_resident = 1;
1168 | 
1169 |       if (tryall_dlopen (&newhandle, 0, advise, 0) != 0)
1170 | 	{
1171 | 	  FREE (*phandle);
1278 | 	     archive name.  */
1279 | 	  sprintf (archive_name, "%s.%s", name, libext);
1280 | 
1281 | 	  if (tryall_dlopen (&newhandle, archive_name, advise, vtable) == 0)
1282 | 	    {
1283 | 	      goto register_handle;
1445 | #endif
1446 | 		   )))
1447 | 	{
1448 | 	  if (tryall_dlopen (&newhandle, attempt, advise, 0) != 0)
1449 | 	    {
1450 | 	      newhandle = NULL;
1585 | 
1586 | /* Libtool-1.5.x interface for loading a new module named FILENAME.  */
1587 | lt_dlhandle
1588 | lt_dlopen (const char *filename)
1589 | {
1590 |   return lt_dlopenadvise (filename, NULL);
1591 | }
1592 | 
1596 |    and if a file is still not found try again with MODULE_EXT appended
1597 |    instead.  */
1598 | lt_dlhandle
1599 | lt_dlopenext (const char *filename)
1600 | {
1601 |   lt_dlhandle	handle	= 0;
1602 |   lt_dladvise	advise;
1603 | 
1604 |   if (!lt_dladvise_init (&advise) && !lt_dladvise_ext (&advise))
1605 |     handle = lt_dlopenadvise (filename, advise);
1606 | 
1607 |   lt_dladvise_destroy (&advise);
1610 | 
1611 | 
1612 | lt_dlhandle
1613 | lt_dlopenadvise (const char *filename, lt_dladvise advise)
1614 | {
1615 |   lt_dlhandle	handle	= 0;
1629 |     {
1630 |       /* Just incase we missed a code path in try_dlopen() that reports
1631 | 	 an error, but forgot to reset handle... */
1632 |       if (try_dlopen (&handle, filename, NULL, advise) != 0)
1633 | 	return 0;
1634 | 
1638 |     {
1639 | 
1640 |       /* First try appending ARCHIVE_EXT.  */
1641 |       errors += try_dlopen (&handle, filename, archive_ext, advise);
1642 | 
1643 |       /* If we found FILENAME, stop searching -- whether we were able to
1650 | 
1651 | #if defined(LT_MODULE_EXT)
1652 |       /* Try appending SHLIB_EXT.   */
1653 |       errors = try_dlopen (&handle, filename, shlib_ext, advise);
1654 | 
1655 |       /* As before, if the file was found but loading failed, return now
1845 | 
1846 | /* Call FUNC for each unique extensionless file in SEARCH_PATH, along
1847 |    with DATA.  The filenames passed to FUNC would be suitable for
1848 |    passing to lt_dlopenext.  The extensions are stripped so that
1849 |    individual modules do not generate several entries (e.g. libfoo.la,
1850 |    libfoo.so, libfoo.so.1, libfoo.so.1.0.0).  If SEARCH_PATH is NULL,
1851 |    then the same directories that lt_dlopen would search are examined.  */
1852 | int
1853 | lt_dlforeachfile (const char *search_path,
{% endraw %}

```
### src/graphviz/libltdl/loaders/preopen.c

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
### src/graphviz/libltdl/loaders/dlopen.c

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
### src/graphviz/libltdl/libltdl/lt__private.h

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
### src/graphviz/libltdl/libltdl/lt_error.h

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