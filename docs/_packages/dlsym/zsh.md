---
name: "zsh"
layout: package
next_package: None
previous_package: zfs
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 5.4.2
4 / 446 files match, 1 filtered matches.

 - [Src/module.c](#srcmodulec)

### Src/module.c

```c

{% raw %}
1522 | 
1523 | static
1524 | void *
1525 | hpux_dlsym(void *handle, char *name)
1526 | {
1527 |     void *sym_addr;
1765 | module_func(Module m, char *name)
1766 | {
1767 | #ifdef DYNAMIC_NAME_CLASH_OK
1768 |     return (Module_generic_func) dlsym(m->u.handle, name);
1769 | #else /* !DYNAMIC_NAME_CLASH_OK */
1770 |     VARARR(char, buf, strlen(name) + strlen(m->node.nam)*2 + 1);
1786 | 	    *q++ = *p;
1787 |     }
1788 |     *q = 0;
1789 |     return (Module_generic_func) dlsym(m->u.handle, buf);
1790 | #endif /* !DYNAMIC_NAME_CLASH_OK */
1791 | }
{% endraw %}

```