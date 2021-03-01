---
name: "vtable-dumper"
layout: package
next_package: vtk
previous_package: vim
library_name: dlopen
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 1.0
1 / 2 files match, 1 filtered matches.

 - [dump-vtable.c](#dump-vtablec)

### dump-vtable.c

```c

{% raw %}
318 |         return ERR;
319 |     }
320 |     
321 |     dlhndl = dlopen(file, RTLD_LAZY);
322 |     if (dlhndl == NULL)
323 |     {
324 |         printf("Failed to dlopen %s\n", file);
325 |         if ((error = dlerror()) != NULL)
326 |         {
{% endraw %}

```