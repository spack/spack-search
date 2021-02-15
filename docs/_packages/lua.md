---
name: "lua"
layout: package
next_package: pnmpi
previous_package: pixman
languages: ['cpp']
---
## 5.3.2
1 / 152 files match

 - [src/loadlib.c](#srcloadlibc)

### src/loadlib.c

```cpp

{% raw %}
126 | #if defined(LUA_USE_DLOPEN)	/* { */
156 |   void *lib = dlopen(path, RTLD_NOW | (seeglb ? RTLD_GLOBAL : RTLD_LOCAL));
{% endraw %}

```