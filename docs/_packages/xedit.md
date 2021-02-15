---
name: "xedit"
layout: package
next_package: dmd
previous_package: libxdamage
languages: ['cpp']
---
## 1.2.2
1 / 114 files match

 - [lisp/require.c](#lisprequirec)

### lisp/require.c

```cpp

{% raw %}
121 | 	    if (dlopen(NULL, RTLD_LAZY | RTLD_GLOBAL) == NULL)
127 | 	     dlopen(filename, RTLD_LAZY | RTLD_GLOBAL)) == NULL)
128 | 	    LispDestroy("%s: dlopen: %s", STRFUN(builtin), dlerror());
{% endraw %}

```