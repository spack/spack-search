---
name: "genometools"
layout: package
next_package: proj
previous_package: g2o
languages: ['c']
---
## 1.6.1
3 / 4299 files match, 2 filtered matches.

 - [src/external/sqlite-3.8.7.1/sqlite3.c](#srcexternalsqlite-3871sqlite3c)
 - [src/external/lua-5.1.5/src/loadlib.c](#srcexternallua-515srcloadlibc)

### src/external/sqlite-3.8.7.1/sqlite3.c

```c

{% raw %}
30841 |   return dlopen(zFilename, RTLD_NOW | RTLD_GLOBAL);
{% endraw %}

```
### src/external/lua-5.1.5/src/loadlib.c

```c

{% raw %}
68 |   void *lib = dlopen(path, RTLD_NOW);
{% endraw %}

```