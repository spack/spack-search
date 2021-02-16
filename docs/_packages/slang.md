---
name: "slang"
layout: package
next_package: stacks
previous_package: tix
languages: ['c']
---
## 2.3.2
3 / 528 files match, 1 filtered matches.

 - [src/slimport.c](#srcslimportc)

### src/slimport.c

```c

{% raw %}
230 | 	handle = (VOID_STAR) dlopen (file, RTLD_NOW | RTLD_GLOBAL);
232 | 	handle = (VOID_STAR) dlopen (file, RTLD_LAZY | RTLD_GLOBAL);
{% endraw %}

```