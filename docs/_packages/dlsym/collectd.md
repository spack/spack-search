---
name: "collectd"
layout: package
next_package: cpuinfo
previous_package: clinfo
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 5.10.0
2 / 489 files match, 2 filtered matches.

 - [src/daemon/plugin.c](#srcdaemonpluginc)
 - [contrib/docker/rootfs_prefix/rootfs_prefix.c](#contribdockerrootfs_prefixrootfs_prefixc)

### src/daemon/plugin.c

```c

{% raw %}
434 |     return ENOENT;
435 |   }
436 | 
437 |   void (*reg_handle)(void) = dlsym(dlh, "module_register");
438 |   if (reg_handle == NULL) {
439 |     ERROR("Couldn't find symbol \"module_register\" in \"%s\": %s\n", file,
{% endraw %}

```
### contrib/docker/rootfs_prefix/rootfs_prefix.c

```c

{% raw %}
63 |   char filename[BUFSIZE] = "\0";
64 | 
65 |   FILE *(*original_fopen)(const char *, const char *);
66 |   original_fopen = dlsym(RTLD_NEXT, "fopen");
67 | 
68 |   return (*original_fopen)(add_prefix(path, filename), mode);
72 |   char filename[BUFSIZE] = "\0";
73 | 
74 |   DIR *(*original_opendir)(const char *);
75 |   original_opendir = dlsym(RTLD_NEXT, "opendir");
76 | 
77 |   return (*original_opendir)(add_prefix(name, filename));
81 |   char filename[BUFSIZE] = "\0";
82 | 
83 |   int *(*original_open)(const char *, int);
84 |   original_open = dlsym(RTLD_NEXT, "open");
85 | 
86 |   return (*original_open)(add_prefix(pathname, filename), flags);
{% endraw %}

```