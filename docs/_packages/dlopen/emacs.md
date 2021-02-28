---
name: "emacs"
layout: package
next_package: gotcha
previous_package: fakexrandr
library_name: dlopen
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 25.2
4 / 5054 files match, 1 filtered matches.

 - [src/dynlib.c](#srcdynlibc)

### src/dynlib.c

```c

{% raw %}
272 | dynlib_handle_ptr
273 | dynlib_open (const char *path)
274 | {
275 |   return dlopen (path, RTLD_LAZY);
276 | }
277 | 
{% endraw %}

```