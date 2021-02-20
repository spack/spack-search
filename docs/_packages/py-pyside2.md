---
name: "py-pyside2"
layout: package
next_package: py-pyzmq
previous_package: py-pyside
languages: ['c']
---
## 5.13.1
1 / 2624 files match, 1 filtered matches.

 - [sources/patchelf/elf.h](#sourcespatchelfelfh)

### sources/patchelf/elf.h

```c

{% raw %}
1604 | #define DT_MIPS_RLD_TEXT_RESOLVE_ADDR 0x7000002d /* Address of rld_text_rsolve
1605 | 						    function stored in GOT.  */
1606 | #define DT_MIPS_PERF_SUFFIX  0x7000002e /* Default suffix of dso to be added
1607 | 					   by rld on dlopen() calls.  */
1608 | #define DT_MIPS_COMPACT_SIZE 0x7000002f /* (O32)Size of compact rel section. */
1609 | #define DT_MIPS_GP_VALUE     0x70000030 /* GP value for aux GOTs.  */
{% endraw %}

```