---
name: "guile"
layout: package
next_package: bcftools
previous_package: vim
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 2.2.4
3 / 2069 files match, 1 filtered matches.

 - [libguile/dynl.c](#libguiledynlc)

### libguile/dynl.c

```c

{% raw %}
167 | {
168 |   void *fptr;
169 | 
170 |   fptr = lt_dlsym ((lt_dlhandle) handle, symb);
171 |   if (!fptr)
172 |     scm_misc_error (subr, "Symbol not found: ~a",
{% endraw %}

```