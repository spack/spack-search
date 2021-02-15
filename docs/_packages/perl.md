---
name: "perl"
layout: package
next_package: xorg-server
previous_package: hsakmt
languages: ['cpp', 'bash', 'pl']
---
## 5.20.3
69 / 5092 files match

 - [config_h.SH](#config_hsh)
 - [uconfig.sh](#uconfigsh)
 - [README.os2](#readmeos2)
 - [configure.com](#configurecom)
 - [makedef.pl](#makedefpl)
 - [uconfig64.sh](#uconfig64sh)
 - [README.solaris](#readmesolaris)
 - [uconfig.h](#uconfigh)
 - [cygwin/cygwin.c](#cygwincygwinc)
 - [ext/DynaLoader/dl_dlopen.xs](#extdynaloaderdl_dlopenxs)
 - [ext/DynaLoader/dl_next.xs](#extdynaloaderdl_nextxs)
 - [ext/DynaLoader/dl_dyld.xs](#extdynaloaderdl_dyldxs)
 - [ext/DynaLoader/dl_dllload.xs](#extdynaloaderdl_dllloadxs)
 - [ext/DynaLoader/dl_aix.xs](#extdynaloaderdl_aixxs)
 - [ext/DynaLoader/dl_win32.xs](#extdynaloaderdl_win32xs)
 - [ext/DynaLoader/DynaLoader_pm.PL](#extdynaloaderdynaloader_pmpl)
 - [ext/DynaLoader/dl_symbian.xs](#extdynaloaderdl_symbianxs)
 - [ext/DynaLoader/dlutils.c](#extdynaloaderdlutilsc)
 - [ext/DynaLoader/hints/netbsd.pl](#extdynaloaderhintsnetbsdpl)
 - [ext/DynaLoader/hints/android.pl](#extdynaloaderhintsandroidpl)
 - [ext/DynaLoader/hints/openbsd.pl](#extdynaloaderhintsopenbsdpl)
 - [cpan/Config-Perl-V/t/22_plv510.t](#cpanconfig-perl-vt22_plv510t)
 - [cpan/Config-Perl-V/t/25_plv516.t](#cpanconfig-perl-vt25_plv516t)
 - [cpan/Config-Perl-V/t/26_plv5182.t](#cpanconfig-perl-vt26_plv5182t)
 - [cpan/Config-Perl-V/t/21_plv58.t](#cpanconfig-perl-vt21_plv58t)
 - [cpan/Config-Perl-V/t/27_plv5200.t](#cpanconfig-perl-vt27_plv5200t)
 - [cpan/Config-Perl-V/t/25_plv5162.t](#cpanconfig-perl-vt25_plv5162t)
 - [cpan/Config-Perl-V/t/20_plv56.t](#cpanconfig-perl-vt20_plv56t)
 - [cpan/Config-Perl-V/t/26_plv518.t](#cpanconfig-perl-vt26_plv518t)
 - [os2/dlfcn.h](#os2dlfcnh)
 - [os2/os2.sym](#os2os2sym)
 - [os2/dl_os2.c](#os2dl_os2c)
 - [os2/os2add.sym](#os2os2addsym)
 - [os2/os2.c](#os2os2c)
 - [symbian/config.sh](#symbianconfigsh)
 - [pod/perl58delta.pod](#podperl58deltapod)
 - [hints/svr5.sh](#hintssvr5sh)
 - [hints/unicos.sh](#hintsunicossh)
 - [hints/linux-android.sh](#hintslinux-androidsh)
 - [hints/aix_4.sh](#hintsaix_4sh)
 - [hints/aix_3.sh](#hintsaix_3sh)
 - [hints/aix.sh](#hintsaixsh)
 - [hints/solaris_2.sh](#hintssolaris_2sh)
 - [hints/linux.sh](#hintslinuxsh)
 - [hints/netbsd.sh](#hintsnetbsdsh)
 - [hints/dec_osf.sh](#hintsdec_osfsh)
 - [hints/vos.sh](#hintsvossh)
 - [hints/sco.sh](#hintsscosh)
 - [hints/bitrig.sh](#hintsbitrigsh)
 - [hints/darwin.sh](#hintsdarwinsh)
 - [hints/os2.sh](#hintsos2sh)
 - [hints/openbsd.sh](#hintsopenbsdsh)
 - [hints/mirbsd.sh](#hintsmirbsdsh)
 - [Cross/config.sh-arm-linux](#crossconfigsh-arm-linux)
 - [Cross/config.sh-arm-linux-n770](#crossconfigsh-arm-linux-n770)
 - [plan9/config.plan9](#plan9configplan9)
 - [plan9/config_h.sample](#plan9config_hsample)
 - [plan9/config_sh.sample](#plan9config_shsample)
 - [Porting/bisect-runner.pl](#portingbisect-runnerpl)
 - [Porting/config.sh](#portingconfigsh)
 - [NetWare/config_H.wc](#netwareconfig_hwc)
 - [NetWare/config.wc](#netwareconfigwc)
 - [win32/config_H.vc](#win32config_hvc)
 - [win32/config_H.ce](#win32config_hce)
 - [win32/config.ce](#win32configce)
 - [win32/config.vc](#win32configvc)
 - [win32/config.gc](#win32configgc)
 - [win32/config_H.gc](#win32config_hgc)
 - [t/perl.supp](#tperlsupp)

### config_h.SH

```bash

{% raw %}
136 |  *	occurred from a call to dlopen(), dlclose() or dlsym().
3473 |  *	case if you're using dl_dlopen.xs.
{% endraw %}

```
### uconfig.sh

```bash

{% raw %}
99 | d_dlopen='undef'
{% endraw %}

```
### README.os2

```

{% raw %}
1920 | The other hack is to restore FP flags after a call to dlopen().  This helps
{% endraw %}

```
### configure.com

```

{% raw %}
5972 | $   WC "d_dlopen='define'"
5975 | $   WC "d_dlopen='undef'"
{% endraw %}

```
### makedef.pl

```pl

{% raw %}
1151 | 		      dlopen
{% endraw %}

```
### uconfig64.sh

```bash

{% raw %}
100 | d_dlopen='undef'
{% endraw %}

```
### README.solaris

```

{% raw %}
309 |  dlopen: stub interception failed
494 | =item dlopen: stub interception failed
496 | The primary cause of the 'dlopen: stub interception failed' message is
{% endraw %}

```
### uconfig.h

```cpp

{% raw %}
101 |  *	occurred from a call to dlopen(), dlclose() or dlsym().
3438 |  *	case if you're using dl_dlopen.xs.
{% endraw %}

```
### cygwin/cygwin.c

```cpp

{% raw %}
559 |     handle = dlopen(NULL, RTLD_LAZY);
{% endraw %}

```
### ext/DynaLoader/dl_dlopen.xs

```

{% raw %}
0 | /* dl_dlopen.xs
2 |  * Platform:	SunOS/Solaris, possibly others which use dlopen.
12 |  * 29th February 2000 - Alan Burlison: Added functionality to close dlopen'd
26 |    dlopen
29 |      dlopen(path, mode)
48 |      dlopen and closes the associated dynamic object file.  It returns zero
59 |      Takes the handle returned from dlopen and the name of a symbol to
70 |      that occurred with either dlopen or dlsym. After each call to
106 |    linker functions dlopen & dlsym both return NULL on error every call 
109 | 	RETVAL = dlopen(filename, 1) ;
168 | #if defined(DLOPEN_WONT_DO_RELATIVE_PATHS)
192 |     handle = dlopen(filename, mode) ;
{% endraw %}

```
### ext/DynaLoader/dl_next.xs

```

{% raw %}
4 |  * Based on:	dl_dlopen.xs by Paul Marquess
20 | dl_next.xs is itself a port from dl_dlopen.xs by Paul Marquess.  It
22 | as an example for how dl_dlopen.xs can be ported to other platforms.
24 | The method used here is just to supply the sun style dlopen etc.
115 | static char *dlopen(char *path, int mode /* mode is ignored */)
178 | static char *dlopen(char *path, int mode /* mode is ignored */)
233 | /* ----- code from dl_dlopen.xs below here ----- */
264 |     retv = dlopen(filename, mode) ;
{% endraw %}

```
### ext/DynaLoader/dl_dyld.xs

```

{% raw %}
5 |  * Based on:	dl_dlopen.xs by Anno Siegel
23 | dl_next.xs is in turn a port from dl_dlopen.xs by Paul Marquess.  It
25 | as an example for how dl_dlopen.xs can be ported to other platforms.
27 | The method used here is just to supply the sun style dlopen etc.
104 | static char *dlopen(char *path, int mode /* mode is ignored */)
139 | /* ----- code from dl_dlopen.xs below here ----- */
165 |     RETVAL = dlopen(filename, mode) ;
{% endraw %}

```
### ext/DynaLoader/dl_dllload.xs

```

{% raw %}
6 |  * 16 January 2001 - based loosely on dl_dlopen.xs.
60 |    dlopen() && dlsym() style dynamic linker calls return (void *).
83 |    Other comments within the dl_dlopen.xs file may be helpful as well.
{% endraw %}

```
### ext/DynaLoader/dl_aix.xs

```

{% raw %}
5 |  *  AIX and merged it with the dl_dlopen.xs file to create a dynamic library
18 |  * which is supposed to use the native dlopen conflicts arise.
21 | #ifdef USE_NATIVE_DLOPEN
121 |  * We simulate dlopen() et al. through a call to load. Because AIX has
133 |  * The void * handle returned from dlopen is actually a ModulePtr.
147 |      * duplicate dlopen's.
208 | void *dlopen(char *path, int mode)
261 | 		strcpy(dl_errbuf, "dlopen: ");
286 | 	 * Assume anonymous exports come from the module this dlopen
287 | 	 * is linked into, that holds true as long as dlopen and all
293 | 	if (loadbind(0, (void *)dlopen, mp->entry) == -1 ||
655 | #endif /* USE_NATIVE_DLOPEN */
657 | /* dl_dlopen.xs
659 |  * Platform:	SunOS/Solaris, possibly others which use dlopen.
674 | 	see dl_dlopen.xs
700 | 	retv = dlopen(filename, RTLD_GLOBAL|RTLD_LAZY) ;
{% endraw %}

```
### ext/DynaLoader/dl_win32.xs

```

{% raw %}
13 | I merely took Paul's dl_dlopen.xs, took out extraneous stuff and
{% endraw %}

```
### ext/DynaLoader/DynaLoader_pm.PL

```pl

{% raw %}
98 | #         (only known to work on Solaris 2 using dlopen(RTLD_GLOBAL))
784 |        (only known to work on Solaris 2 using dlopen(RTLD_GLOBAL))
795 |     SunOS: dlopen($filename)
801 | (The dlopen() function is also used by Solaris and some versions of
{% endraw %}

```
### ext/DynaLoader/dl_symbian.xs

```

{% raw %}
35 | void *dlopen(const char *filename, int flag);
68 | void* dlopen(const char *filename, int flags) {
160 |     h = (PerlSymbianLibHandle*)dlopen(filename, flags);
{% endraw %}

```
### ext/DynaLoader/dlutils.c

```cpp

{% raw %}
6 |  * 29th Feburary 2000 - Alan Burlison: Added functionality to close dlopen'd
63 | /* Close all dlopen'd files */
{% endraw %}

```
### ext/DynaLoader/hints/netbsd.pl

```pl

{% raw %}
1 | # Some NetBSDs seem to have a dlopen() that won't accept relative paths
2 | $self->{CCFLAGS} = $Config{ccflags} . ' -DDLOPEN_WONT_DO_RELATIVE_PATHS';
{% endraw %}

```
### ext/DynaLoader/hints/android.pl

```pl

{% raw %}
6 | # use My::Module::In::Foo; # calls dlopen() with foo/My/Module/...
9 | $self->{CCFLAGS} = $Config{ccflags} . ' -DDLOPEN_WONT_DO_RELATIVE_PATHS';
{% endraw %}

```
### ext/DynaLoader/hints/openbsd.pl

```pl

{% raw %}
1 | # Some OpenBSDs seem to have a dlopen() that won't accept relative paths
2 | $self->{CCFLAGS} = $Config{ccflags} . ' -DDLOPEN_WONT_DO_RELATIVE_PATHS';
{% endraw %}

```
### cpan/Config-Perl-V/t/22_plv510.t

```

{% raw %}
59 |     dlsrc=dl_dlopen.xs, dlext=so, d_dlsymun=undef, ccdlflags='-Wl,-E'
{% endraw %}

```
### cpan/Config-Perl-V/t/25_plv516.t

```

{% raw %}
71 |     dlsrc=dl_dlopen.xs, dlext=so, d_dlsymun=undef, ccdlflags='-Wl,-E'
{% endraw %}

```
### cpan/Config-Perl-V/t/26_plv5182.t

```

{% raw %}
96 |     dlsrc=dl_dlopen.xs, dlext=so, d_dlsymun=undef, ccdlflags='-Wl,-E'
{% endraw %}

```
### cpan/Config-Perl-V/t/21_plv58.t

```

{% raw %}
69 |     dlsrc=dl_dlopen.xs, dlext=so, d_dlsymun=undef, ccdlflags='-Wl,-E'
{% endraw %}

```
### cpan/Config-Perl-V/t/27_plv5200.t

```

{% raw %}
98 |     dlsrc=dl_dlopen.xs, dlext=so, d_dlsymun=undef, ccdlflags='-Wl,-E'
{% endraw %}

```
### cpan/Config-Perl-V/t/25_plv5162.t

```

{% raw %}
110 |     dlsrc           => "dl_dlopen.xs",
145 |     dlsrc=dl_dlopen.xs, dlext=bundle, d_dlsymun=undef, ccdlflags=' '
{% endraw %}

```
### cpan/Config-Perl-V/t/20_plv56.t

```

{% raw %}
64 |     dlsrc=dl_dlopen.xs, dlext=so, d_dlsymun=undef, ccdlflags='-rdynamic'
{% endraw %}

```
### cpan/Config-Perl-V/t/26_plv518.t

```

{% raw %}
96 |     dlsrc=dl_dlopen.xs, dlext=so, d_dlsymun=undef, ccdlflags='-Wl,-E'
{% endraw %}

```
### os2/dlfcn.h

```cpp

{% raw %}
0 | void *dlopen(const char *path, int mode);
{% endraw %}

```
### os2/os2.sym

```

{% raw %}
4 | dlopen
{% endraw %}

```
### os2/dl_os2.c

```cpp

{% raw %}
26 | #ifdef DLOPEN_INITTERM
61 |   doscalls_h = (HMODULE)dlopen("DOSCALLS",0);
68 |   rc = pDosQueryModFromEIP(&mod, &obj, sizeof(buf), buf, &offset, (ULONG)dlopen);
78 | dlopen(const char *path, int mode)
109 |             strcpy(fail, "can't load from myself: compiled without -DDLOPEN_INITTERM");
{% endraw %}

```
### os2/os2add.sym

```

{% raw %}
0 | dlopen
{% endraw %}

```
### os2/os2.c

```cpp

{% raw %}
645 |     HMODULE h = (HMODULE)dlopen(modname, 0);
{% endraw %}

```
### symbian/config.sh

```bash

{% raw %}
105 | d_dlopen='undef'
{% endraw %}

```
### pod/perl58delta.pod

```

{% raw %}
92 | dlopen interface of AIX instead of the old emulated interface.  This
{% endraw %}

```
### hints/svr5.sh

```bash

{% raw %}
155 | # dlsrc='dl_dlopen.xs'
{% endraw %}

```
### hints/unicos.sh

```bash

{% raw %}
54 | d_dlopen='undef'
{% endraw %}

```
### hints/linux-android.sh

```bash

{% raw %}
8 | # path is passed in to dlopen(), it'll only use the path's
12 | # So if you load List::Util and then Hash::Util, the dlopen() for
{% endraw %}

```
### hints/aix_4.sh

```bash

{% raw %}
61 | 	case "$usenativedlopen" in
62 | 	    '') usenativedlopen='false' ;;
66 | 	case "$usenativedlopen" in
67 | 	    '') usenativedlopen='true' ;;
231 | if test $usenativedlopen = 'true' ; then
548 | if test $usenativedlopen = 'true' ; then
549 |     ccflags="$ccflags -DUSE_NATIVE_DLOPEN"
{% endraw %}

```
### hints/aix_3.sh

```bash

{% raw %}
327 | if test $usenativedlopen = 'true' ; then
328 |     ccflags="$ccflags -DUSE_NATIVE_DLOPEN"
{% endraw %}

```
### hints/aix.sh

```bash

{% raw %}
49 | case "$usenativedlopen" in
50 |     '') usenativedlopen='true' ;;
165 | if test $usenativedlopen = 'true' ; then
469 | if test $usenativedlopen = 'true' ; then
470 |     ccflags="$ccflags -DUSE_NATIVE_DLOPEN"
{% endraw %}

```
### hints/solaris_2.sh

```bash

{% raw %}
712 | # If using C++, the Configure scan for dlopen() will fail in Solaris
715 | # is needed for the &dlopen.  Adding any of these would require changing
720 |   d_dlopen='define'
{% endraw %}

```
### hints/linux.sh

```bash

{% raw %}
476 | # If using g++, the Configure scan for dlopen() and (especially)
480 |   d_dlopen='define'
{% endraw %}

```
### hints/netbsd.sh

```bash

{% raw %}
27 | 			d_dlopen=$undef
34 | 		d_dlopen=$define
66 | 		d_dlopen=$define
72 | 		d_dlopen=$undef
{% endraw %}

```
### hints/dec_osf.sh

```bash

{% raw %}
310 | # dlopen() is in libc
684 | #	  Because the dlopen, dlclose,... calls are in the
{% endraw %}

```
### hints/vos.sh

```bash

{% raw %}
98 | # Use dlopen() to open shared libraries.
99 | dlsrc="dl_dlopen.xs"
{% endraw %}

```
### hints/sco.sh

```bash

{% raw %}
160 |         dlsrc='dl_dlopen.xs'
165 |         d_dlopen='define'
{% endraw %}

```
### hints/bitrig.sh

```bash

{% raw %}
40 | 	# Without this, dlopen() is crippled.
{% endraw %}

```
### hints/darwin.sh

```bash

{% raw %}
151 | # 10.4 can use dlopen.
158 |     dlsrc='dl_dlopen.xs';
{% endraw %}

```
### hints/os2.sh

```bash

{% raw %}
227 | dlsrc='dl_dlopen.xs'
{% endraw %}

```
### hints/openbsd.sh

```bash

{% raw %}
70 | 	# Without this, dlopen() is crippled.
{% endraw %}

```
### hints/mirbsd.sh

```bash

{% raw %}
28 | # Without this, dlopen() is crippled. All platforms are ELF.
{% endraw %}

```
### Cross/config.sh-arm-linux

```

{% raw %}
161 | d_dlopen='define'
554 | dlsrc='dl_dlopen.xs'
{% endraw %}

```
### Cross/config.sh-arm-linux-n770

```

{% raw %}
155 | d_dlopen='define'
527 | dlsrc='dl_dlopen.xs'
{% endraw %}

```
### plan9/config.plan9

```

{% raw %}
164 |  *	occurred from a call to dlopen(), dlclose() or dlsym().
1287 |  *	case if you're using dl_dlopen.xs.
{% endraw %}

```
### plan9/config_h.sample

```

{% raw %}
122 |  *	occurred from a call to dlopen(), dlclose() or dlsym().
1240 |  *	case if you're using dl_dlopen.xs.
{% endraw %}

```
### plan9/config_sh.sample

```

{% raw %}
161 | d_dlopen='undef'
{% endraw %}

```
### Porting/bisect-runner.pl

```pl

{% raw %}
2087 | 		d_dlopen=$define
2094 | 		d_dlopen=$undef
2096 | 		d_dlopen=$define
2104 | 		d_dlopen=$undef
2151 | +	# Without this, dlopen() is crippled.
2185 | +	# Without this, dlopen() is crippled.
2207 | +	# Without this, dlopen() is crippled.
3338 |      RETVAL = dlopen(filename, mode) ;
{% endraw %}

```
### Porting/config.sh

```bash

{% raw %}
170 | d_dlopen='define'
565 | dlsrc='dl_dlopen.xs'
{% endraw %}

```
### NetWare/config_H.wc

```

{% raw %}
128 |  *	occurred from a call to dlopen(), dlclose() or dlsym().
1236 |  *	case if you're using dl_dlopen.xs.
{% endraw %}

```
### NetWare/config.wc

```

{% raw %}
148 | d_dlopen='define'
{% endraw %}

```
### win32/config_H.vc

```

{% raw %}
101 |  *	occurred from a call to dlopen(), dlclose() or dlsym().
3438 |  *	case if you're using dl_dlopen.xs.
{% endraw %}

```
### win32/config_H.ce

```

{% raw %}
104 |  *	occurred from a call to dlopen(), dlclose() or dlsym().
1224 |  *	case if you're using dl_dlopen.xs.
{% endraw %}

```
### win32/config.ce

```

{% raw %}
146 | d_dlopen='define'
{% endraw %}

```
### win32/config.vc

```

{% raw %}
148 | d_dlopen='define'
{% endraw %}

```
### win32/config.gc

```

{% raw %}
148 | d_dlopen='define'
{% endraw %}

```
### win32/config_H.gc

```

{% raw %}
101 |  *	occurred from a call to dlopen(), dlclose() or dlsym().
3446 |  *	case if you're using dl_dlopen.xs.
{% endraw %}

```
### t/perl.supp

```

{% raw %}
0 | ## Catch various leaks during dlopen...
40 |    dlopen
{% endraw %}

```