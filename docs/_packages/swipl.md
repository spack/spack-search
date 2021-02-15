---
name: "swipl"
layout: package
next_package: libluv
previous_package: scalpel
languages: ['cmake', 'cpp', 'pl']
---
## 8.0.3
13 / 3902 files match

 - [src/pl-incl.h](#srcpl-inclh)
 - [src/SWI-Prolog.h](#srcswi-prologh)
 - [src/pl-nt.c](#srcpl-ntc)
 - [src/pl-global.h](#srcpl-globalh)
 - [src/pl-load.c](#srcpl-loadc)
 - [src/pl-ext.c](#srcpl-extc)
 - [src/pl-beos.c](#srcpl-beosc)
 - [src/config/wincfg.h](#srcconfigwincfgh)
 - [library/shlib.pl](#libraryshlibpl)
 - [man/foreign.doc](#manforeigndoc)
 - [boot/syspred.pl](#bootsyspredpl)
 - [packages/xpce/src/x11/x11-compat.c](#packagesxpcesrcx11x11-compatc)
 - [cmake/Config.cmake](#cmakeconfigcmake)

### src/pl-incl.h

```cpp

{% raw %}
343 | #define EMULATE_DLOPEN 1		/* Emulated dlopen() in pl-beos.c */
{% endraw %}

```
### src/SWI-Prolog.h

```cpp

{% raw %}
942 | PL_EXPORT(void *)	PL_dlopen(const char *file, int flags);
{% endraw %}

```
### src/pl-nt.c

```cpp

{% raw %}
636 | 		 *	DLOPEN AND FRIENDS	*
639 | #ifdef EMULATE_DLOPEN
734 | PL_dlopen(const char *file, int flags)	/* file is in UTF-8, POSIX path */
790 | #endif /*EMULATE_DLOPEN*/
{% endraw %}

```
### src/pl-global.h

```cpp

{% raw %}
565 |     status_t	dl_error;		/* dlopen() emulation in pl-beos.c */
{% endraw %}

```
### src/pl-load.c

```cpp

{% raw %}
44 | dlopen()) and HPUX (based on slh_load()).   Despite, this covers a large
49 | EMULATE_DLOPEN. You find examples in pl-nt.c   (for Win32) and pl-beos.c
70 | 		 *     DLOPEN() AND FRIENDS	*
73 | #ifndef EMULATE_DLOPEN
74 | #ifdef HAVE_DLOPEN			/* sysvr4, elf binaries */
80 | #else /*HAVE_DLOPEN*/
85 | #define dlopen(path, flags) shl_load((path), (flags), 0L)
106 | #endif /*HAVE_DLOPEN*/
107 | #endif /*EMULATE_DLOPEN*/
109 | #if defined(HAVE_DLOPEN) || defined(HAVE_SHL_LOAD) || defined(EMULATE_DLOPEN)
139 | #ifndef EMULATE_DLOPEN
141 | PL_dlopen(const char *file, int flags)
142 | { return dlopen(file, flags);
160 | #endif /*EMULATE_DLOPEN*/
218 |   if ( !(dlhandle = PL_dlopen(fn, dlflags)) )
346 | #else /*HAVE_DLOPEN*/
358 | #endif /*HAVE_DLOPEN*/
364 | BeginPredDefs(dlopen)
{% endraw %}

```
### src/pl-ext.c

```cpp

{% raw %}
376 | DECL_PLIST(dlopen);
432 |   REG_PLIST(dlopen);
{% endraw %}

```
### src/pl-beos.c

```cpp

{% raw %}
44 | 		 *	DLOPEN AND FRIENDS	*
47 | #ifdef EMULATE_DLOPEN
56 | PL_dlopen(const char *file, int flags)
95 | #endif	/* EMULATE_DLOPEN */
{% endraw %}

```
### src/config/wincfg.h

```cpp

{% raw %}
52 | /* Define for emulating dlopen(), etc. using LoadLibrary */
53 | #define EMULATE_DLOPEN 1
{% endraw %}

```
### library/shlib.pl

```pl

{% raw %}
180 | %   regular file because dlopen()  and   Windows  LoadLibrary() expect a
185 | %       memory and than fdlopen() to link this.
187 | %       make dlopen() work on non-files.  This is highly non-portably
{% endraw %}

```
### man/foreign.doc

```

{% raw %}
99 | machines providing \manref{dlopen}{2} (Solaris, Linux, FreeBSD, Irix and
120 | supported by your operating system. Check the documentation of dlopen()
4148 | valgrind can deal with code loaded through dlopen().
{% endraw %}

```
### boot/syspred.pl

```pl

{% raw %}
1233 |                  *            DLOPEN            *
1259 | dlopen_flag(now,        2'01).          % see pl-load.c for these constants
1260 | dlopen_flag(global,     2'10).          % Solaris only
1265 |     (   dlopen_flag(F, I)
1267 |     ;   throw(error(domain_error(dlopen_flag, F), _))
{% endraw %}

```
### packages/xpce/src/x11/x11-compat.c

```cpp

{% raw %}
52 | dlopen(char *path, int mode)
53 | { Cprintf("dlopen(%s, %d)\n", path, mode);
{% endraw %}

```
### cmake/Config.cmake

```cmake

{% raw %}
52 | check_library_exists(dl dlopen	      "" HAVE_LIBDL)
156 | check_function_exists(dlopen HAVE_DLOPEN)
{% endraw %}

```