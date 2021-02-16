---
name: "swipl"
layout: package
next_package: libluv
previous_package: scalpel
languages: ['pl', 'c']
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
942 | PL_EXPORT(void *)	PL_dlopen(const char *file, int flags);
{% endraw %}

```
### src/pl-nt.c

```c

{% raw %}
734 | PL_dlopen(const char *file, int flags)	/* file is in UTF-8, POSIX path */
{% endraw %}

```
### src/pl-global.h

```c

{% raw %}
565 |     status_t	dl_error;		/* dlopen() emulation in pl-beos.c */
{% endraw %}

```
### src/pl-load.c

```c

{% raw %}
44 | dlopen()) and HPUX (based on slh_load()).   Despite, this covers a large
141 | PL_dlopen(const char *file, int flags)
142 | { return dlopen(file, flags);
218 |   if ( !(dlhandle = PL_dlopen(fn, dlflags)) )
364 | BeginPredDefs(dlopen)
{% endraw %}

```
### src/pl-ext.c

```c

{% raw %}
376 | DECL_PLIST(dlopen);
432 |   REG_PLIST(dlopen);
{% endraw %}

```
### src/pl-beos.c

```c

{% raw %}
56 | PL_dlopen(const char *file, int flags)
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
### boot/syspred.pl

```pl

{% raw %}
1259 | dlopen_flag(now,        2'01).          % see pl-load.c for these constants
1260 | dlopen_flag(global,     2'10).          % Solaris only
1265 |     (   dlopen_flag(F, I)
1267 |     ;   throw(error(domain_error(dlopen_flag, F), _))
{% endraw %}

```
### packages/xpce/src/x11/x11-compat.c

```c

{% raw %}
52 | dlopen(char *path, int mode)
53 | { Cprintf("dlopen(%s, %d)\n", path, mode);
{% endraw %}

```