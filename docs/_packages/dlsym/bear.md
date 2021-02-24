---
name: "bear"
layout: package
next_package: nginx
previous_package: imagemagick
library_name: dlsym
matches: ['dlsym']
languages: ['c']
---
## 2.2.0
1 / 51 files match, 1 filtered matches.

 - [libear/ear.c](#libearearc)

### libear/ear.c

```c

{% raw %}
67 |         void *from;                                                            \
68 |         TYPE_ to;                                                              \
69 |     } cast;                                                                    \
70 |     if (0 == (cast.from = dlsym(RTLD_NEXT, SYMBOL_))) {                        \
71 |         perror("bear: dlsym");                                                 \
72 |         exit(EXIT_FAILURE);                                                    \
73 |     }                                                                          \
{% endraw %}

```