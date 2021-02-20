---
name: "pnmpi"
layout: package
next_package: pocl
previous_package: pmix
languages: ['c']
---
## 1.7
2 / 294 files match, 1 filtered matches.

 - [src/pnmpi/core.c](#srcpnmpicorec)

### src/pnmpi/core.c

```c

{% raw %}
598 |                   else
599 |                     {
600 |                       /* we could open the module - hence we are good to go */
601 |                       DBGPRINT2("dlopen successful");
602 | 
603 |                       modules.module[modules.num]->stack_delimiter = 0;
{% endraw %}

```