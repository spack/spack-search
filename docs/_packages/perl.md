---
name: "perl"
layout: package
next_package: xorg-server
previous_package: hsakmt
languages: ['pl', 'c']
---
## 5.20.3
69 / 5092 files match

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
1151 | 		      dlopen
{% endraw %}

```
### cygwin/cygwin.c

```c

{% raw %}
559 |     handle = dlopen(NULL, RTLD_LAZY);
{% endraw %}

```
### ext/DynaLoader/DynaLoader_pm.PL

```pl

{% raw %}
784 |        (only known to work on Solaris 2 using dlopen(RTLD_GLOBAL))
795 |     SunOS: dlopen($filename)
801 | (The dlopen() function is also used by Solaris and some versions of
{% endraw %}

```
### os2/dlfcn.h

```c

{% raw %}
0 | void *dlopen(const char *path, int mode);
{% endraw %}

```
### os2/dl_os2.c

```c

{% raw %}
61 |   doscalls_h = (HMODULE)dlopen("DOSCALLS",0);
68 |   rc = pDosQueryModFromEIP(&mod, &obj, sizeof(buf), buf, &offset, (ULONG)dlopen);
78 | dlopen(const char *path, int mode)
{% endraw %}

```
### os2/os2.c

```c

{% raw %}
645 |     HMODULE h = (HMODULE)dlopen(modname, 0);
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