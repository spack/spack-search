---
name: "fuse-overlayfs"
layout: package
next_package: gatepet2stir
previous_package: frontier-client
languages: ['c']
---
## 1.1.2
2 / 55 files match, 1 filtered matches.

 - [plugin-manager.c](#plugin-managerc)

### plugin-manager.c

```c

{% raw %}
51 |   plugin_name name;
52 |   struct ovl_plugin *p;
53 |   plugin_version version;
54 |   void *handle = dlopen (path, RTLD_NOW|RTLD_LOCAL);
55 |   if (! handle)
56 |     error (EXIT_FAILURE, 0, "cannot load plugin %s: %s", path, dlerror());
{% endraw %}

```