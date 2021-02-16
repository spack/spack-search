---
name: "gnupg"
layout: package
next_package: fcgi
previous_package: py-genders
languages: ['c']
---
## 2.2.15
9 / 1018 files match, 4 filtered matches.

 - [scd/apdu.c](#scdapduc)
 - [common/iobuf.c](#commoniobufc)
 - [common/homedir.c](#commonhomedirc)
 - [common/dynload.h](#commondynloadh)

### scd/apdu.c

```c

{% raw %}
1954 |       handle = dlopen (opt.pcsc_driver, RTLD_LAZY);
{% endraw %}

```
### common/iobuf.c

```c

{% raw %}
2304 | 	handle = dlopen ("kernel32.dll", RTLD_LAZY);
{% endraw %}

```
### common/homedir.c

```c

{% raw %}
138 |           handle = dlopen (dllnames[i], RTLD_LAZY);
{% endraw %}

```
### common/dynload.h

```c

{% raw %}
42 | dlopen (const char *name, int flag)
{% endraw %}

```