---
name: "guile"
layout: package
next_package: libgpuarray
previous_package: kmod
languages: ['c']
---
## 2.2.4
12 / 2069 files match, 2 filtered matches.

 - [libguile/elf.h](#libguileelfh)
 - [libguile/dynl.c](#libguiledynlc)

### libguile/elf.h

```c

{% raw %}
1663 | 					   by rld on dlopen() calls.  */
{% endraw %}

```
### libguile/dynl.c

```c

{% raw %}
83 |     handle = lt_dlopen (NULL);
86 |       handle = lt_dlopenext (fname);
136 |               handle = lt_dlopenext (fname_attempt);
190 |      --mode=execute -dlopen' fiddles with (info "(libtool) Libltdl
{% endraw %}

```