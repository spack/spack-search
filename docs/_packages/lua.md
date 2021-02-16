---
name: "lua"
layout: package
next_package: pnmpi
previous_package: pixman
languages: ['c']
---
## 5.3.2
1 / 152 files match, 1 filtered matches.

 - [src/loadlib.c](#srcloadlibc)

### src/loadlib.c

```c

{% raw %}
156 |   void *lib = dlopen(path, RTLD_NOW | (seeglb ? RTLD_GLOBAL : RTLD_LOCAL));
{% endraw %}

```