---
name: "ncurses"
layout: package
next_package: neovim
previous_package: ncl
languages: ['c']
---
## 5.9
3 / 1026 files match, 2 filtered matches.

 - [ncurses/curses.priv.h](#ncursescursesprivh)
 - [ncurses/base/lib_mouse.c](#ncursesbaselib_mousec)

### ncurses/curses.priv.h

```c

{% raw %}
1063 | 	bool		_mouse_gpm_loaded;
1064 | 	bool		_mouse_gpm_found;
1065 | #ifdef HAVE_LIBDL
1066 | 	void		*_dlopen_gpm;
1067 | 	TYPE_gpm_fd	_mouse_gpm_fd;
1068 | 	TYPE_Gpm_Open	_mouse_Gpm_Open;
{% endraw %}

```
### ncurses/base/lib_mouse.c

```c

{% raw %}
407 | static void
408 | unload_gpm_library(SCREEN *sp)
409 | {
410 |     if (sp->_dlopen_gpm != 0) {
411 | 	T(("unload GPM library"));
412 | 	sp->_mouse_gpm_loaded = FALSE;
413 | 	sp->_mouse_fd = -1;
414 | 	dlclose(sp->_dlopen_gpm);
415 | 	sp->_dlopen_gpm = 0;
416 |     }
417 | }
420 | load_gpm_library(SCREEN *sp)
421 | {
422 |     sp->_mouse_gpm_found = FALSE;
423 |     if ((sp->_dlopen_gpm = dlopen(LIBGPM_SONAME, my_RTLD)) != 0) {
424 | 	if (GET_DLSYM(gpm_fd) == 0 ||
425 | 	    GET_DLSYM(Gpm_Open) == 0 ||
{% endraw %}

```