---
name: "pax-utils"
layout: package
next_package: pdsh
previous_package: patchelf
languages: ['c']
---
## 1.2.2
8 / 385 files match, 1 filtered matches.

 - [elf.h](#elfh)

### elf.h

```c

{% raw %}
1704 | #define DT_MIPS_RLD_TEXT_RESOLVE_ADDR 0x7000002d /* Address of rld_text_rsolve
1705 | 						    function stored in GOT.  */
1706 | #define DT_MIPS_PERF_SUFFIX  0x7000002e /* Default suffix of dso to be added
1707 | 					   by rld on dlopen() calls.  */
1708 | #define DT_MIPS_COMPACT_SIZE 0x7000002f /* (O32)Size of compact rel section. */
1709 | #define DT_MIPS_GP_VALUE     0x70000030 /* GP value for aux GOTs.  */
{% endraw %}

```