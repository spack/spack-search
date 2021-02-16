---
name: "glib"
layout: package
next_package: libxml2
previous_package: py-scipy
languages: ['c']
---
## 2.56.2
14 / 2643 files match

 - [gmodule/gmodule-ar.c](#gmodulegmodule-arc)
 - [gmodule/gmodule-dl.c](#gmodulegmodule-dlc)

### gmodule/gmodule-ar.c

```c

{% raw %}
119 |   handle = dlopen (full_name, 
135 |   handle = dlopen (NULL, RTLD_GLOBAL | RTLD_LAZY);
{% endraw %}

```
### gmodule/gmodule-dl.c

```c

{% raw %}
97 |   handle = dlopen (file_name,
124 |   handle = dlopen (NULL, RTLD_GLOBAL | RTLD_LAZY);
{% endraw %}

```