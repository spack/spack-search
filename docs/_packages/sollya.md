---
name: "sollya"
layout: package
next_package: r-rcppcctz
previous_package: cbtf
languages: ['c']
---
## 7.0
9 / 1132 files match, 2 filtered matches.

 - [library.c](#libraryc)
 - [external.c](#externalc)

### library.c

```c

{% raw %}
524 |     dlfcnHandle = dlopen(libraryName, RTLD_LOCAL | RTLD_NOW);
{% endraw %}

```
### external.c

```c

{% raw %}
313 |   descr = dlopen(library, RTLD_NOW);
{% endraw %}

```