---
name: "autogen"
layout: package
next_package: foam-extend
previous_package: vtk
library_name: dlopen
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 5.18.12
8 / 411 files match, 1 filtered matches.

 - [agen5/opts.c](#agen5optsc)

### agen5/opts.c

```c

{% raw %}
67 | # ifdef HAVE_DLFCN_H
68 | #  include <dlfcn.h>
69 | # else
70 |    extern void * dlopen(char const *,int);
71 | # endif
72 | 
{% endraw %}

```