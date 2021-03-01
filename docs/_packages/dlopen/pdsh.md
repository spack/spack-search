---
name: "pdsh"
layout: package
next_package: perl
previous_package: parsec
library_name: dlopen
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 2.31
9 / 162 files match, 4 filtered matches.

 - [src/qsnet/qswutil.c](#srcqsnetqswutilc)
 - [src/pdsh/ltdl.h](#srcpdshltdlh)
 - [src/pdsh/ltdl.c](#srcpdshltdlc)
 - [src/pdsh/mod.c](#srcpdshmodc)

### src/qsnet/qswutil.c

```c

{% raw %}
265 | {	
266 |     struct neterr_args *args = arg;
267 | 
268 |     if (!(elan3h = dlopen ("libelan3.so", RTLD_LAZY))) {
269 |         syslog(LOG_ERR, "unable to open libelan3.so: %s", dlerror());
270 |         goto fail;
{% endraw %}

```
### src/pdsh/ltdl.h

```c

{% raw %}
167 | 			lt_ptr data));
168 | 
169 | /* Portable libltdl versions of the system dlopen() API. */
170 | LT_SCOPE	lt_dlhandle lt_dlopen		LT_PARAMS((const char *filename));
171 | LT_SCOPE	lt_dlhandle lt_dlopenext	LT_PARAMS((const char *filename));
172 | LT_SCOPE	lt_ptr	    lt_dlsym		LT_PARAMS((lt_dlhandle handle,
173 | 						     const char *name));
241 | typedef	struct {
242 |   char	*filename;		/* file name */
243 |   char	*name;			/* module name */
244 |   int	ref_count;		/* number of times lt_dlopened minus
245 | 				   number of times lt_dlclosed. */
246 | } lt_dlinfo;
311 |    onto the table of error strings.  */
312 | #define lt_dlerror_table						\
313 |     LT_ERROR(UNKNOWN,		    "unknown error")			\
314 |     LT_ERROR(DLOPEN_NOT_SUPPORTED,  "dlopen support not available")	\
315 |     LT_ERROR(INVALID_LOADER,	    "invalid loader")			\
316 |     LT_ERROR(INIT_LOADER,	    "loader initialization failed")	\
{% endraw %}

```
### src/pdsh/ltdl.c

```c

{% raw %}
839 | 
840 | struct lt_dlhandle_struct {
841 |   struct lt_dlhandle_struct   *next;
842 |   lt_dlloader	       *loader;		/* dlopening interface */
843 |   lt_dlinfo		info;
844 |   int			depcount;	/* number of dependencies */
1106 |      lt_user_data loader_data;
1107 |      const char *filename;
1108 | {
1109 |   lt_module   module   = dlopen (filename, LT_GLOBAL | LT_LAZY_OR_NOW);
1110 | 
1111 |   if (!module)
2179 | 						 char *deplibs));
2180 | static	int	trim		      LT_PARAMS((char **dest,
2181 | 						 const char *str));
2182 | static	int	try_dlopen	      LT_PARAMS((lt_dlhandle *handle,
2183 | 						 const char *filename));
2184 | static	int	tryall_dlopen	      LT_PARAMS((lt_dlhandle *handle,
2185 | 						 const char *filename,
2186 | 						 const char * useloader));
2224 |       user_search_path = 0; /* empty search path */
2225 | 
2226 | #if HAVE_LIBDL
2227 |       errors += lt_dlloader_add (lt_dlloader_next (0), &sys_dl, "dlopen");
2228 | #endif
2229 | #if HAVE_SHL_LOAD
2230 |       errors += lt_dlloader_add (lt_dlloader_next (0), &sys_shl, "dlopen");
2231 | #endif
2232 | #ifdef __WINDOWS__
2233 |       errors += lt_dlloader_add (lt_dlloader_next (0), &sys_wll, "dlopen");
2234 | #endif
2235 | #ifdef __BEOS__
2236 |       errors += lt_dlloader_add (lt_dlloader_next (0), &sys_bedl, "dlopen");
2237 | #endif
2238 | #if HAVE_DLD
2369 | }
2370 | 
2371 | static int
2372 | tryall_dlopen (handle, filename, useloader)
2373 |      lt_dlhandle *handle;
2374 |      const char *filename;
2472 | }
2473 | 
2474 | static int
2475 | tryall_dlopen_module (handle, prefix, dirname, dlname)
2476 |      lt_dlhandle *handle;
2477 |      const char *prefix;
2510 |      shuffled.  Otherwise, attempt to open FILENAME as a module.  */
2511 |   if (prefix)
2512 |     {
2513 |       error += tryall_dlopen_module (handle,
2514 | 				     (const char *) 0, prefix, filename);
2515 |     }
2516 |   else if (tryall_dlopen (handle, filename, NULL) != 0)
2517 |     {
2518 |       ++error;
2532 |      int installed;
2533 | {
2534 |   /* Try to open the old library first; if it was dlpreopened,
2535 |      we want the preopened version of it, even if a dlopenable
2536 |      module is available.  */
2537 |   if (old_name && tryall_dlopen (handle, old_name, "dlpreload") == 0)
2538 |     {
2539 |       return 0;
2545 |       /* try to open the installed module */
2546 |       if (installed && libdir)
2547 | 	{
2548 | 	  if (tryall_dlopen_module (handle,
2549 | 				    (const char *) 0, libdir, dlname) == 0)
2550 | 	    return 0;
2553 |       /* try to open the not-installed module */
2554 |       if (!installed)
2555 | 	{
2556 | 	  if (tryall_dlopen_module (handle, dir, objdir, dlname) == 0)
2557 | 	    return 0;
2558 | 	}
2559 | 
2560 |       /* maybe it was moved to another directory */
2561 |       {
2562 | 	  if (dir && (tryall_dlopen_module (handle,
2563 | 				    (const char *) 0, dir, dlname) == 0))
2564 | 	    return 0;
2798 | 
2799 |   /* Try to dlopen the file, but do not continue searching in any
2800 |      case.  */
2801 |   if (tryall_dlopen (handle, filename,NULL) != 0)
2802 |     *handle = 0;
2803 | 
2954 | 
2955 |       for (i = 0; i < depcount; ++i)
2956 | 	{
2957 | 	  handle->deplibs[j] = lt_dlopenext(names[depcount-1-i]);
2958 | 	  if (handle->deplibs[j])
2959 | 	    {
3056 | }
3057 | 
3058 | static int
3059 | try_dlopen (phandle, filename)
3060 |      lt_dlhandle *phandle;
3061 |      const char *filename;
3087 |       /* lt_dlclose()ing yourself is very bad!  Disallow it.  */
3088 |       LT_DLSET_FLAG (*phandle, LT_DLRESIDENT_FLAG);
3089 | 
3090 |       if (tryall_dlopen (&newhandle, 0, NULL) != 0)
3091 | 	{
3092 | 	  LT_DLFREE (*phandle);
3393 | #endif
3394 | 		   )))
3395 | 	{
3396 |           if (tryall_dlopen (&newhandle, filename, NULL) != 0)
3397 |             {
3398 |               newhandle = NULL;
3432 | }
3433 | 
3434 | lt_dlhandle
3435 | lt_dlopen (filename)
3436 |      const char *filename;
3437 | {
3439 | 
3440 |   /* Just incase we missed a code path in try_dlopen() that reports
3441 |      an error, but forgets to reset handle... */
3442 |   if (try_dlopen (&handle, filename) != 0)
3443 |     return 0;
3444 | 
3464 |    and if a file is still not found try again with SHLIB_EXT appended
3465 |    instead.  */
3466 | lt_dlhandle
3467 | lt_dlopenext (filename)
3468 |      const char *filename;
3469 | {
3475 | 
3476 |   if (!filename)
3477 |     {
3478 |       return lt_dlopen (filename);
3479 |     }
3480 | 
3491 | #endif
3492 |       ))
3493 |     {
3494 |       return lt_dlopen (filename);
3495 |     }
3496 | 
3501 | 
3502 |   strcpy (tmp, filename);
3503 |   strcat (tmp, archive_ext);
3504 |   errors = try_dlopen (&handle, tmp);
3505 | 
3506 |   /* If we found FILENAME, stop searching -- whether we were able to
3531 |     }
3532 | 
3533 |   strcat(tmp, shlib_ext);
3534 |   errors = try_dlopen (&handle, tmp);
3535 | 
3536 |   /* As before, if the file was found but loading failed, return now
3745 | 
3746 | /* Call FUNC for each unique extensionless file in SEARCH_PATH, along
3747 |    with DATA.  The filenames passed to FUNC would be suitable for
3748 |    passing to lt_dlopenext.  The extensions are stripped so that
3749 |    individual modules do not generate several entries (e.g. libfoo.la,
3750 |    libfoo.so, libfoo.so.1, libfoo.so.1.0.0).  If SEARCH_PATH is NULL,
3751 |    then the same directories that lt_dlopen would search are examined.  */
3752 | int
3753 | lt_dlforeachfile (search_path, func, data)
{% endraw %}

```
### src/pdsh/mod.c

```c

{% raw %}
811 | 
812 |     mod = mod_create();
813 | 
814 |     if (!(mod->handle = lt_dlopen(fq_path)))
815 |         goto fail;
816 | 
{% endraw %}

```