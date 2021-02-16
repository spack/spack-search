---
name: "premake-core"
layout: package
next_package: openpbs
previous_package: cairo
languages: ['c']
---
## 5.0.0-alpha13
2 / 1665 files match, 1 filtered matches.

 - [contrib/lua/src/loadlib.c](#contribluasrcloadlibc)

### contrib/lua/src/loadlib.c

```c

{% raw %}
126 |   void *lib = dlopen(path, RTLD_NOW | (seeglb ? RTLD_GLOBAL : RTLD_LOCAL));
{% endraw %}

```