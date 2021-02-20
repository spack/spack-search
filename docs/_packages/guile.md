---
name: "guile"
layout: package
next_package: haproxy
previous_package: guacamole-server
languages: ['c']
---
## 2.2.4
12 / 2069 files match, 2 filtered matches.

 - [libguile/elf.h](#libguileelfh)
 - [libguile/dynl.c](#libguiledynlc)

### libguile/elf.h

```c

{% raw %}
1660 | #define DT_MIPS_RLD_TEXT_RESOLVE_ADDR 0x7000002d /* Address of rld_text_rsolve
1661 | 						    function stored in GOT.  */
1662 | #define DT_MIPS_PERF_SUFFIX  0x7000002e /* Default suffix of dso to be added
1663 | 					   by rld on dlopen() calls.  */
1664 | #define DT_MIPS_COMPACT_SIZE 0x7000002f /* (O32)Size of compact rel section. */
1665 | #define DT_MIPS_GP_VALUE     0x70000030 /* GP value for aux GOTs.  */
{% endraw %}

```
### libguile/dynl.c

```c

{% raw %}
80 | 
81 |   if (fname == NULL)
82 |     /* Return a handle for the program as a whole.  */
83 |     handle = lt_dlopen (NULL);
84 |   else
85 |     {
86 |       handle = lt_dlopenext (fname);
87 | 
88 |       if (handle == NULL
133 |               strcpy (s, fname);
134 | 
135 |               /* Try to load it, and terminate the search if successful */
136 |               handle = lt_dlopenext (fname_attempt);
137 |               if (handle != NULL)
138 |                 break;
187 | 
188 |      'lt_dladdsearchdir' can't be used because it is searched before
189 |      the system-dependent search path, which is the one 'libtool
190 |      --mode=execute -dlopen' fiddles with (info "(libtool) Libltdl
191 |      Interface").  See
192 |      <http://lists.gnu.org/archive/html/guile-devel/2010-11/msg00095.html>.
{% endraw %}

```