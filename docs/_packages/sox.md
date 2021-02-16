---
name: "sox"
layout: package
next_package: qscintilla
previous_package: kylin
languages: ['c']
---
## 14.4.2
13 / 361 files match

 - [src/formats.c](#srcformatsc)
 - [src/win32-ltdl.h](#srcwin32-ltdlh)
 - [src/ladspa.c](#srcladspac)
 - [src/ladspa.h](#srcladspah)
 - [src/util.c](#srcutilc)
 - [src/win32-ltdl.c](#srcwin32-ltdlc)
 - [src/sox_i.h](#srcsox_ih)

### src/formats.c

```c

{% raw %}
1193 |     lt_dlhandle lth = lt_dlopenext(file);
{% endraw %}

```
### src/win32-ltdl.h

```c

{% raw %}
47 | lt_dlopen(
51 | lt_dlopenext(
{% endraw %}

```
### src/ladspa.c

```c

{% raw %}
133 |       || (l_st->lth = lt_dlopenext(l_st->name)) == NULL) {
{% endraw %}

```
### src/ladspa.h

```c

{% raw %}
66 |    linking by dlopen() and family. The file will provide a number of
{% endraw %}

```
### src/util.c

```c

{% raw %}
180 |       dl = lt_dlopenext(*libname);
{% endraw %}

```
### src/win32-ltdl.c

```c

{% raw %}
322 | lt_dlopen(
331 | lt_dlopenext(
{% endraw %}

```
### src/sox_i.h

```c

{% raw %}
404 |      be used). If using DL_LAME, the func may be loaded via dlopen/dlsym, but
{% endraw %}

```