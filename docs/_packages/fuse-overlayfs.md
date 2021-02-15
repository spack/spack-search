---
name: "fuse-overlayfs"
layout: package
next_package: cosma
previous_package: gtkorvo-atl
languages: ['cpp']
---
## 1.1.2
2 / 55 files match

 - [plugin-manager.c](#plugin-managerc)
 - [configure.ac](#configureac)

### plugin-manager.c

```cpp

{% raw %}
54 |   void *handle = dlopen (path, RTLD_NOW|RTLD_LOCAL);
{% endraw %}

```
### configure.ac

```

{% raw %}
74 | AC_SEARCH_LIBS([dlopen], [dl], [], [AC_MSG_ERROR([unable to find dlopen()])])
{% endraw %}

```