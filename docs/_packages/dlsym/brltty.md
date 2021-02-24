---
name: "brltty"
layout: package
next_package: imagemagick
previous_package: gawk
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 5.5
2 / 1334 files match, 1 filtered matches.

 - [Programs/brltty_jni.c](#programsbrltty_jnic)

### Programs/brltty_jni.c

```c

{% raw %}
213 |     while (symbol->name) {
214 |       const void **pointer = symbol->pointer;
215 | 
216 |       if ((*pointer = dlsym(coreHandle, symbol->name))) {
217 |         LOG("core symbol: %s -> %p", symbol->name, *pointer);
218 |       } else {
{% endraw %}

```