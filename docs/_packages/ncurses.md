---
name: "ncurses"
layout: package
next_package: spindle
previous_package: pnfft
languages: ['cpp']
---
## 5.9
3 / 1026 files match

 - [aclocal.m4](#aclocalm4)
 - [ncurses/curses.priv.h](#ncursescursesprivh)
 - [ncurses/base/lib_mouse.c](#ncursesbaselib_mousec)

### aclocal.m4

```

{% raw %}
1329 | 		if ((obj = dlopen("filename", 0)) != 0) {
{% endraw %}

```
### ncurses/curses.priv.h

```cpp

{% raw %}
1066 | 	void		*_dlopen_gpm;
{% endraw %}

```
### ncurses/base/lib_mouse.c

```cpp

{% raw %}
156 | #define GET_DLSYM(name) (my_##name = (TYPE_##name) dlsym(sp->_dlopen_gpm, #name))
410 |     if (sp->_dlopen_gpm != 0) {
414 | 	dlclose(sp->_dlopen_gpm);
415 | 	sp->_dlopen_gpm = 0;
423 |     if ((sp->_dlopen_gpm = dlopen(LIBGPM_SONAME, my_RTLD)) != 0) {
{% endraw %}

```