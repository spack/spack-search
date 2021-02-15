---
name: "automake"
layout: package
next_package: libexif
previous_package: arbor
languages: ['bash']
---
## 1.16.1
11 / 1488 files match

 - [bin/automake.in](#binautomakein)
 - [doc/automake.texi](#docautomaketexi)
 - [doc/automake.info-1](#docautomakeinfo-1)
 - [old/ChangeLog.03](#oldchangelog03)
 - [old/ChangeLog.00](#oldchangelog00)
 - [t/cond14.sh](#tcond14sh)
 - [t/libtool9.sh](#tlibtool9sh)
 - [t/cond31.sh](#tcond31sh)
 - [t/cond15.sh](#tcond15sh)
 - [t/ltinit.sh](#tltinitsh)
 - [t/libtool7.sh](#tlibtool7sh)

### bin/automake.in

```

{% raw %}
2282 | 	       # Skip -dlopen and -dlpreopen; these are explicitly allowed
2285 | 	       # libraries or programs, for which -dlopen and -dlopreopen
{% endraw %}

```
### doc/automake.texi

```

{% raw %}
4828 | linker flags (except for @option{-l}, @option{-L}, @option{-dlopen} and
4853 | @option{-L}, @option{-dlopen} and @option{-dlpreopen} options removed.  The
5158 | modules, should look into @file{libltdl}: libtool's dlopening library
5160 | This offers a portable dlopening facility to load libtool libraries
5429 | These are libtool libraries meant to be dlopened.  They are
5714 | @option{-dlopen} and @option{-dlpreopen}).  Use the @code{_LDFLAGS} variable
5762 | @option{-dlopen} and @option{-dlpreopen} options removed.  The configure
13175 | @c  LocalWords:  pkglib libexecdir prog libcpio cpio's dlopen dlpreopen linux
13208 | @c  LocalWords:  LTLIBOBJ Libtool's libtool's libltdl dlopening itutions libbar
13209 | @c  LocalWords:  WANTEDLIBS libhello sublibraries libtop libsub dlopened Ratfor
{% endraw %}

```
### doc/automake.info-1

```

{% raw %}
4041 | flags (except for ‘-l’, ‘-L’, ‘-dlopen’ and ‘-dlpreopen’).  So, use the
4060 | most configure substitutions, ‘-l’, ‘-L’, ‘-dlopen’ and ‘-dlpreopen’
4321 | modules, should look into ‘libltdl’: libtool’s dlopening library (*note
4323 | dlopening facility to load libtool libraries dynamically, and can also
4553 | These are libtool libraries meant to be dlopened.  They are indicated to
4806 |      program-specific linker flags (except for ‘-l’, ‘-L’, ‘-dlopen’ and
4852 |      ‘_LIBADD’, with most configure substitutions, ‘-l’, ‘-L’, ‘-dlopen’
{% endraw %}

```
### old/ChangeLog.03

```

{% raw %}
2683 | 	* automake.in (handle_lib_objects_cond): Ignore -dlopen and
{% endraw %}

```
### old/ChangeLog.00

```

{% raw %}
1939 | 	* automake.in (LDADD): accept -dlopen and -dlpreopen here
{% endraw %}

```
### t/cond14.sh

```bash

{% raw %}
37 | 	echo '-dlopen is unsupported' >> $@
{% endraw %}

```
### t/libtool9.sh

```bash

{% raw %}
27 | AC_LIBTOOL_DLOPEN
37 | libmod1_la_LIBADD = -dlopen mod2.la
42 | prg_LDADD = -dlopen libmod1.la -dlpreopen mod2.la
{% endraw %}

```
### t/cond31.sh

```bash

{% raw %}
35 | a_LDADD += c2.o -dlopen c3.la
{% endraw %}

```
### t/cond15.sh

```bash

{% raw %}
33 | 	echo '-dlopen is unsupported' >> $@
43 | 	echo '-dlopen is unsupported' >> $@
{% endraw %}

```
### t/ltinit.sh

```bash

{% raw %}
30 | LT_INIT([dlopen])
59 | grep '^checking.*dlfcn\.h.* no$' stdout || grep '^checking.*dlopen' stdout
{% endraw %}

```
### t/libtool7.sh

```bash

{% raw %}
16 | # Make sure we allow Libtool's -dlopen/-dlpreopen
25 | AC_LIBTOOL_DLOPEN
36 | libmod1_la_LIBADD = -dlopen mod2.la
43 | prg_LDADD = -dlopen libmod1.la -dlpreopen mod2.la
{% endraw %}

```