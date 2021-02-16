---
name: "ncurses"
layout: package
next_package: spindle
previous_package: pnfft
languages: ['c']
---
## 5.9
3 / 1026 files match, 2 filtered matches.

 - [ncurses/curses.priv.h](#ncursescursesprivh)
 - [ncurses/base/lib_mouse.c](#ncursesbaselib_mousec)

### ncurses/curses.priv.h

```c

{% raw %}
1066 | 	void		*_dlopen_gpm;
{% endraw %}

```
### ncurses/base/lib_mouse.c

```c

{% raw %}
410 |     if (sp->_dlopen_gpm != 0) {
414 | 	dlclose(sp->_dlopen_gpm);
415 | 	sp->_dlopen_gpm = 0;
423 |     if ((sp->_dlopen_gpm = dlopen(LIBGPM_SONAME, my_RTLD)) != 0) {
{% endraw %}

```