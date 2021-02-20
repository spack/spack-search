---
name: "slang"
layout: package
next_package: slurm
previous_package: simgrid
languages: ['c']
---
## 2.3.2
3 / 528 files match, 1 filtered matches.

 - [src/slimport.c](#srcslimportc)

### src/slimport.c

```c

{% raw %}
227 | # define RTLD_GLOBAL 0
228 | #endif
229 | #ifdef RTLD_NOW
230 | 	handle = (VOID_STAR) dlopen (file, RTLD_NOW | RTLD_GLOBAL);
231 | #else
232 | 	handle = (VOID_STAR) dlopen (file, RTLD_LAZY | RTLD_GLOBAL);
233 | #endif
234 | 
{% endraw %}

```