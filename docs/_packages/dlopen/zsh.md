---
name: "zsh"
layout: package
next_package: fipscheck
previous_package: libkcapi
library_name: dlopen
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 5.4.2
4 / 446 files match, 1 filtered matches.

 - [Src/module.c](#srcmodulec)

### Src/module.c

```c

{% raw %}
1588 | 	    continue;
1589 | 	sprintf(buf, "%s/%s.%s", **pp ? *pp : ".", name, DL_EXT);
1590 | 	unmetafy(buf, NULL);
1591 | 	if (*buf) /* dlopen(NULL) returns a handle to the main binary */
1592 | 	    ret = dlopen(buf, RTLD_LAZY | RTLD_GLOBAL);
1593 |     }
1594 | 
{% endraw %}

```