---
name: "emacs"
layout: package
next_package: kaldi
previous_package: llvm
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 25.2
3 / 5054 files match, 1 filtered matches.

 - [src/dynlib.c](#srcdynlibc)

### src/dynlib.c

```c

{% raw %}
278 | void *
279 | dynlib_sym (dynlib_handle_ptr h, const char *sym)
280 | {
281 |   return dlsym (h, sym);
282 | }
283 | 
{% endraw %}

```