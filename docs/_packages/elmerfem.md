---
name: "elmerfem"
layout: package
next_package: emacs
previous_package: elfutils
languages: ['c']
---
## devel
5 / 9371 files match, 2 filtered matches.

 - [fem/src/Load.c](#femsrcloadc)
 - [contrib/lua-5.1.5/src/loadlib.c](#contriblua-515srcloadlibc)

### fem/src/Load.c

```c

{% raw %}
268 |   INTERNAL: Tries to open library with dlopen, first without
274 | static void STDCALLBULL try_dlopen(char *LibName, void **Handle, char *errorBuf)
287 |         if ((*Handle = dlopen(dl_names[i], RTLD_NOW)) == NULL) {
319 |     try_dlopen(Library, Handle, errorBuf);
329 |             try_dlopen(CurrentLib, Handle, errorBuf);
{% endraw %}

```
### contrib/lua-5.1.5/src/loadlib.c

```c

{% raw %}
68 |   void *lib = dlopen(path, RTLD_NOW);
{% endraw %}

```