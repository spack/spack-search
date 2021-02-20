---
name: "neovim"
layout: package
next_package: nest
previous_package: ncurses
languages: ['c']
---
## 0.2.1
2 / 2259 files match, 1 filtered matches.

 - [src/nvim/os/dl.c](#srcnvimosdlc)

### src/nvim/os/dl.c

```c

{% raw %}
50 |   uv_lib_t lib;
51 | 
52 |   // open the dynamic loadable library
53 |   if (uv_dlopen(libname, &lib)) {
54 |       EMSG2(_("dlerror = \"%s\""), uv_dlerror(&lib));
55 |       return false;
{% endraw %}

```