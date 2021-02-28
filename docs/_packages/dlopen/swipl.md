---
name: "swipl"
layout: package
next_package: wireshark
previous_package: boost
library_name: dlopen
matches: ['dlsym', 'dlopen']
languages: ['c', 'pl']
---
## 8.0.3
13 / 3902 files match, 9 filtered matches.

 - [src/SWI-Prolog.h](#srcswi-prologh)
 - [src/pl-nt.c](#srcpl-ntc)
 - [src/pl-global.h](#srcpl-globalh)
 - [src/pl-load.c](#srcpl-loadc)
 - [src/pl-ext.c](#srcpl-extc)
 - [src/pl-beos.c](#srcpl-beosc)
 - [library/shlib.pl](#libraryshlibpl)
 - [boot/syspred.pl](#bootsyspredpl)
 - [packages/xpce/src/x11/x11-compat.c](#packagesxpcesrcx11x11-compatc)

### src/SWI-Prolog.h

```c

{% raw %}
939 | 		 *	  DYNAMIC LINKING	*
940 | 		 *******************************/
941 | 
942 | PL_EXPORT(void *)	PL_dlopen(const char *file, int flags);
943 | PL_EXPORT(const char *) PL_dlerror(void);
944 | PL_EXPORT(void *)	PL_dlsym(void *handle, char *symbol);
{% endraw %}

```
### src/pl-nt.c

```c

{% raw %}
731 | }
732 | 
733 | void *
734 | PL_dlopen(const char *file, int flags)	/* file is in UTF-8, POSIX path */
735 | { HINSTANCE h;
736 |   DWORD llflags = 0;
{% endraw %}

```
### src/pl-global.h

```c

{% raw %}
562 |   struct
563 |   {
564 | #ifdef __BEOS__
565 |     status_t	dl_error;		/* dlopen() emulation in pl-beos.c */
566 | #endif
567 |     int		rand_initialised;	/* have we initialised random? */
{% endraw %}

```
### src/pl-load.c

```c

{% raw %}
41 | SWI-Prolog interface for runtime loading of foreign code (plugins).
42 | 
43 | Currently, this interface is implemented only  for ELF systems (based on
44 | dlopen()) and HPUX (based on slh_load()).   Despite, this covers a large
45 | number of modern Unix platforms. To name a few: Solaris, Linux, freeBSD,
46 | IRIX, HPUX, MacOS X.
138 | 
139 | #ifndef EMULATE_DLOPEN
140 | void *
141 | PL_dlopen(const char *file, int flags)
142 | { return dlopen(file, flags);
143 | }
144 | 
215 |   if ( !PL_get_atom_ex(file, &afile) ||
216 |        !PL_get_file_name(file, &fn, 0) )
217 |     fail;
218 |   if ( !(dlhandle = PL_dlopen(fn, dlflags)) )
219 |     return PL_error(NULL, 0, NULL, ERR_SHARED_OBJECT_OP,
220 | 		    ATOM_open, PL_dlerror());
361 | 		 *      PUBLISH PREDICATES	*
362 | 		 *******************************/
363 | 
364 | BeginPredDefs(dlopen)
365 |   PRED_DEF("$open_shared_object", 3, open_shared_object, 0)
366 | #ifdef HAVE_SHARED_OBJECTS
{% endraw %}

```
### src/pl-ext.c

```c

{% raw %}
373 | DECL_PLIST(proc);
374 | DECL_PLIST(srcfile);
375 | DECL_PLIST(write);
376 | DECL_PLIST(dlopen);
377 | DECL_PLIST(system);
378 | DECL_PLIST(op);
429 |   REG_PLIST(proc);
430 |   REG_PLIST(srcfile);
431 |   REG_PLIST(write);
432 |   REG_PLIST(dlopen);
433 |   REG_PLIST(system);
434 |   REG_PLIST(op);
{% endraw %}

```
### src/pl-beos.c

```c

{% raw %}
53 | - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - */
54 | 
55 | void *
56 | PL_dlopen(const char *file, int flags)
57 | { image_id image = load_add_on(file);
58 | 
{% endraw %}

```
### library/shlib.pl

```pl

{% raw %}
177 | %!  lib_to_file(+Lib0, -Lib, -Copy) is det.
178 | %
179 | %   If Lib0 is not a regular file  we   need  to  copy it to a temporary
180 | %   regular file because dlopen()  and   Windows  LoadLibrary() expect a
181 | %   file name. On some systems this can   be  avoided. Roughly using two
182 | %   approaches (after discussion with Peter Ludemann):
183 | %
184 | %     - On FreeBSD there is shm_open() to create an anonymous file in
185 | %       memory and than fdlopen() to link this.
186 | %     - In general, we could redefine the system calls open(), etc. to
187 | %       make dlopen() work on non-files.  This is highly non-portably
188 | %       though.
189 | %     - We can mount the resource zip using e.g., `fuse-zip` on Linux.
{% endraw %}

```
### boot/syspred.pl

```pl

{% raw %}
1256 |     map_dlflags(Flags, Mask),
1257 |     '$open_shared_object'(File, Handle, Mask).
1258 | 
1259 | dlopen_flag(now,        2'01).          % see pl-load.c for these constants
1260 | dlopen_flag(global,     2'10).          % Solaris only
1261 | 
1262 | map_dlflags([], 0).
1263 | map_dlflags([F|T], M) :-
1264 |     map_dlflags(T, M0),
1265 |     (   dlopen_flag(F, I)
1266 |     ->  true
1267 |     ;   throw(error(domain_error(dlopen_flag, F), _))
1268 |     ),
1269 |     M is M0 \/ I.
{% endraw %}

```
### packages/xpce/src/x11/x11-compat.c

```c

{% raw %}
49 | #if !defined(HAVE_LIBDL) && defined(__sun__) && XT_REVISION == 5
50 | 
51 | void *
52 | dlopen(char *path, int mode)
53 | { Cprintf("dlopen(%s, %d)\n", path, mode);
54 | 
55 |   return NULL;
{% endraw %}

```