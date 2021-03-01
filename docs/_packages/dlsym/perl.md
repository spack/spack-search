---
name: "perl"
layout: package
next_package: petsc
previous_package: perfstubs
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['pl', 'c']
---
## 5.20.3
60 / 5092 files match, 6 filtered matches.

 - [makedef.pl](#makedefpl)
 - [cygwin/cygwin.c](#cygwincygwinc)
 - [ext/SDBM_File/sdbm/Makefile.PL](#extsdbm_filesdbmmakefilepl)
 - [ext/DynaLoader/DynaLoader_pm.PL](#extdynaloaderdynaloader_pmpl)
 - [os2/dlfcn.h](#os2dlfcnh)
 - [os2/dl_os2.c](#os2dl_os2c)

### makedef.pl

```pl

{% raw %}
1149 | 		      Perl_OS2_term
1150 | 		      OS2_Perl_data
1151 | 		      dlopen
1152 | 		      dlsym
1153 | 		      dlerror
1154 | 		      dlclose
{% endraw %}

```
### cygwin/cygwin.c

```c

{% raw %}
559 |     handle = dlopen(NULL, RTLD_LAZY);
560 |     if (handle) {
561 |         void (*pfn_init)(pTHX);
562 |         pfn_init = (void (*)(pTHX))dlsym(handle, "init_Win32CORE");
563 |         if (pfn_init)
564 |             pfn_init(aTHX);
{% endraw %}

```
### ext/SDBM_File/sdbm/Makefile.PL

```pl

{% raw %}
12 | #    LINKTYPE  => 'static',
13 |     DEFINE    => $define,
14 |     INC       => '-I$(PERL_INC)', # force PERL_INC dir ahead of system -I's
15 |     SKIP      => [qw(dynamic dynamic_lib dlsyms)],
16 |     OBJECT    => '$(O_FILES)',
17 |     clean     => {'FILES' => 'dbu libsdbm.a dbd dba dbe x-dbu *.dir *.pag'},
{% endraw %}

```
### ext/DynaLoader/DynaLoader_pm.PL

```pl

{% raw %}
865 | currently defined.  The only initial requirement is that $symref can
866 | be passed to, and understood by, dl_install_xsub().
867 | 
868 |     SunOS: dlsym($libref, $symbol)
869 |     HP-UX: shl_findsym($libref, $symbol)
870 |     Linux: dld_get_func($symbol) and/or dld_get_symbol($symbol)
{% endraw %}

```
### os2/dlfcn.h

```c

{% raw %}
1 | void *dlsym(void *handle, const char *symbol);
2 | char *dlerror(void);
3 | int dlclose(void *handle);
{% endraw %}

```
### os2/dl_os2.c

```c

{% raw %}
142 | #define ERROR_WRONG_PROCTYPE 0xffffffff
143 | 
144 | void *
145 | dlsym(void *handle, const char *symbol)
146 | {
147 | 	ULONG rc, type;
{% endraw %}

```