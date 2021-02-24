---
name: "perl"
layout: package
next_package: openloops
previous_package: mono
library_name: dlopen
matches: ['dlsym', 'dlopen']
languages: ['c', 'pl']
---
## 5.20.3
69 / 5092 files match, 7 filtered matches.

 - [makedef.pl](#makedefpl)
 - [cygwin/cygwin.c](#cygwincygwinc)
 - [ext/DynaLoader/DynaLoader_pm.PL](#extdynaloaderdynaloader_pmpl)
 - [os2/dlfcn.h](#os2dlfcnh)
 - [os2/dl_os2.c](#os2dl_os2c)
 - [os2/os2.c](#os2os2c)
 - [Porting/bisect-runner.pl](#portingbisect-runnerpl)

### makedef.pl

```pl

{% raw %}
1148 | 		      Perl_OS2_init3
1149 | 		      Perl_OS2_term
1150 | 		      OS2_Perl_data
1151 | 		      dlopen
1152 | 		      dlsym
1153 | 		      dlerror
{% endraw %}

```
### cygwin/cygwin.c

```c

{% raw %}
556 |     newXS("Cygwin::sync_winenv", XS_Cygwin_sync_winenv, file);
557 | 
558 |     /* Initialize Win32CORE if it has been statically linked. */
559 |     handle = dlopen(NULL, RTLD_LAZY);
560 |     if (handle) {
561 |         void (*pfn_init)(pTHX);
{% endraw %}

```
### ext/DynaLoader/DynaLoader_pm.PL

```pl

{% raw %}
781 | Assigned bits:
782 | 
783 |  0x01  make symbols available for linking later dl_load_file's.
784 |        (only known to work on Solaris 2 using dlopen(RTLD_GLOBAL))
785 |        (ignored under VMS; this is a normal part of image linking)
786 | 
792 | This is the function that does the real work.  It should use the
793 | current values of @dl_require_symbols and @dl_resolve_using if required.
794 | 
795 |     SunOS: dlopen($filename)
796 |     HP-UX: shl_load($filename)
797 |     Linux: dld_create_reference(@dl_require_symbols); dld_link($filename)
798 |     NeXT:  rld_load($filename, @dl_resolve_using)
799 |     VMS:   lib$find_image_symbol($filename,$dl_require_symbols[0])
800 | 
801 | (The dlopen() function is also used by Solaris and some versions of
802 | Linux, and is a common choice when providing a "wrapper" on other
803 | mechanisms as is done in the OS/2 port.)
{% endraw %}

```
### os2/dlfcn.h

```c

{% raw %}
1 | void *dlsym(void *handle, const char *symbol);
2 | char *dlerror(void);
{% endraw %}

```
### os2/dl_os2.c

```c

{% raw %}
58 |   if (failed)
59 | 	return 0;
60 |   failed = 1;
61 |   doscalls_h = (HMODULE)dlopen("DOSCALLS",0);
62 |   if (!doscalls_h)
63 | 	return 0;
65 |   rc = DosQueryProcAddr(doscalls_h, 360, 0, (PFN*)&pDosQueryModFromEIP);
66 |   if (rc)
67 | 	return 0;
68 |   rc = pDosQueryModFromEIP(&mod, &obj, sizeof(buf), buf, &offset, (ULONG)dlopen);
69 |   if (rc)
70 | 	return 0;
75 | }
76 | 
77 | void *
78 | dlopen(const char *path, int mode)
79 | {
80 | 	HMODULE handle;
{% endraw %}

```
### os2/os2.c

```c

{% raw %}
642 | HMODULE
643 | loadModule(const char *modname, int fail)
644 | {
645 |     HMODULE h = (HMODULE)dlopen(modname, 0);
646 | 
647 |     if (!h && fail)
{% endraw %}

```
### Porting/bisect-runner.pl

```pl

{% raw %}
2084 | 	;;
2085 | *)
2086 | 	if [ -f /usr/libexec/ld.elf_so ]; then
2087 | 		d_dlopen=$define
2088 | 		d_dlerror=$define
2089 | 		ccdlflags="-Wl,-E -Wl,-R${PREFIX}/lib $ccdlflags"
2091 | 		lddlflags="--whole-archive -shared $lddlflags"
2092 | 	elif [ "`uname -m`" = "pmax" ]; then
2093 | # NetBSD 1.3 and 1.3.1 on pmax shipped an 'old' ld.so, which will not work.
2094 | 		d_dlopen=$undef
2095 | 	elif [ -f /usr/libexec/ld.so ]; then
2096 | 		d_dlopen=$define
2097 | 		d_dlerror=$define
2098 | 		ccdlflags="-Wl,-R${PREFIX}/lib $ccdlflags"
2101 | 		cccdlflags="-DPIC -fPIC $cccdlflags"
2102 | 		lddlflags="-Bforcearchive -Bshareable $lddlflags"
2103 | 	else
2104 | 		d_dlopen=$undef
2105 | 	fi
2106 | 	;;
2148 | +	esac
2149 | +
2150 | +	# We need to force ld to export symbols on ELF platforms.
2151 | +	# Without this, dlopen() is crippled.
2152 | +	ELF=`${cc:-cc} -dM -E - </dev/null | grep __ELF__`
2153 | +	test -n "$ELF" && ldflags="-Wl,-E $ldflags"
2182 |  	esac
2183 | +
2184 | +	# We need to force ld to export symbols on ELF platforms.
2185 | +	# Without this, dlopen() is crippled.
2186 | +	ELF=`${cc:-cc} -dM -E - </dev/null | grep __ELF__`
2187 | +	test -n "$ELF" && ldflags="-Wl,-E $ldflags"
2204 |  	esac
2205 | +
2206 | +	# We need to force ld to export symbols on ELF platforms.
2207 | +	# Without this, dlopen() is crippled.
2208 | +	ELF=`${cc:-cc} -dM -E - </dev/null | grep __ELF__`
2209 | +	test -n "$ELF" && ldflags="-Wl,-E $ldflags"
3335 |      if (flags & 0x01)
3336 | -	Perl_warn(aTHX_ "Can't make loaded symbols global on this platform while loading %s",filename);
3337 | +	Perl_warn_nocontext("Can't make loaded symbols global on this platform while loading %s",filename);
3338 |      RETVAL = dlopen(filename, mode) ;
3339 |      DLDEBUG(2,PerlIO_printf(Perl_debug_log, " libref=%x\n", RETVAL));
3340 |      ST(0) = sv_newmortal() ;
{% endraw %}

```