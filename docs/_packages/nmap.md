---
name: "nmap"
layout: package
next_package: py-quast
previous_package: fenics-dolfinx
languages: ['c']
---
## 7.70
11 / 2242 files match

 - [liblua/loadlib.c](#liblualoadlibc)

### liblua/loadlib.c

```c

{% raw %}
156 |   void *lib = dlopen(path, RTLD_NOW | (seeglb ? RTLD_GLOBAL : RTLD_LOCAL));
{% endraw %}

```