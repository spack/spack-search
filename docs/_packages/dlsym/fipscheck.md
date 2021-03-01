---
name: "fipscheck"
layout: package
next_package: flexiblas
previous_package: fio
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 7.0.0.398
1 / 18 files match, 1 filtered matches.

 - [src/library.c](#srclibraryc)

### src/library.c

```c

{% raw %}
76 | 	        return -1;
77 |         }       
78 | 
79 | 	sym = dlsym(dl, symbolname);
80 | 
81 | 	if (sym != NULL && dladdr(sym, &info)) {
{% endraw %}

```