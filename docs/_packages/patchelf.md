---
name: "patchelf"
layout: package
next_package: pax-utils
previous_package: parsec
languages: ['c']
---
## 0.10
1 / 30 files match, 1 filtered matches.

 - [src/elf.h](#srcelfh)

### src/elf.h

```c

{% raw %}
1629 | #define DT_MIPS_RLD_TEXT_RESOLVE_ADDR 0x7000002d /* Address of rld_text_rsolve
1630 | 						    function stored in GOT.  */
1631 | #define DT_MIPS_PERF_SUFFIX  0x7000002e /* Default suffix of dso to be added
1632 | 					   by rld on dlopen() calls.  */
1633 | #define DT_MIPS_COMPACT_SIZE 0x7000002f /* (O32)Size of compact rel section. */
1634 | #define DT_MIPS_GP_VALUE     0x70000030 /* GP value for aux GOTs.  */
{% endraw %}

```