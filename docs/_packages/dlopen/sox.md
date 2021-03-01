---
name: "sox"
layout: package
next_package: spindle
previous_package: sollya
library_name: dlopen
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 14.4.2
13 / 361 files match, 7 filtered matches.

 - [src/formats.c](#srcformatsc)
 - [src/win32-ltdl.h](#srcwin32-ltdlh)
 - [src/ladspa.c](#srcladspac)
 - [src/ladspa.h](#srcladspah)
 - [src/util.c](#srcutilc)
 - [src/win32-ltdl.c](#srcwin32-ltdlc)
 - [src/sox_i.h](#srcsox_ih)

### src/formats.c

```c

{% raw %}
1190 | 
1191 |   static int init_format(const char *file, lt_ptr data)
1192 |   {
1193 |     lt_dlhandle lth = lt_dlopenext(file);
1194 |     const char *end = file + strlen(file);
1195 |     const char prefix[] = "sox_fmt_";
{% endraw %}

```
### src/win32-ltdl.h

```c

{% raw %}
44 |   lt_ptr pData);
45 | 
46 | lt_dlhandle
47 | lt_dlopen(
48 |   const char *szFileName);
49 | 
50 | lt_dlhandle
51 | lt_dlopenext(
52 |   const char *szFileName);
53 | 
{% endraw %}

```
### src/ladspa.c

```c

{% raw %}
130 |     path = LADSPA_PATH;
131 | 
132 |   if(lt_dlinit() || lt_dlsetsearchpath(path)
133 |       || (l_st->lth = lt_dlopenext(l_st->name)) == NULL) {
134 |     lsx_fail("could not open LADSPA plugin %s", l_st->name);
135 |     return SOX_EOF;
{% endraw %}

```
### src/ladspa.h

```c

{% raw %}
63 |    `connect_port()' function below) before it is asked to run.
64 | 
65 |    Plugins will reside in shared object files suitable for dynamic
66 |    linking by dlopen() and family. The file will provide a number of
67 |    `plugin types' that can be used to instantiate actual plugins
68 |    (sometimes known as `plugin instances') that can be connected
{% endraw %}

```
### src/util.c

```c

{% raw %}
177 |     for (libname = library_names; *libname; libname++)
178 |     {
179 |       lsx_debug("Attempting to open %s (%s).", library_description, *libname);
180 |       dl = lt_dlopenext(*libname);
181 |       if (dl)
182 |       {
{% endraw %}

```
### src/win32-ltdl.c

```c

{% raw %}
319 | }
320 | 
321 | lt_dlhandle
322 | lt_dlopen(
323 |     const char *szFileName)
324 | {
328 | }
329 | 
330 | lt_dlhandle
331 | lt_dlopenext(
332 |     const char *szFileName)
333 | {
{% endraw %}

```
### src/sox_i.h

```c

{% raw %}
401 | 
402 |   /* LSX_DLENTRY_STUB: For use in creating an ENTRIES macro. func need not
403 |      be available at link time (and if present, the link time version will not
404 |      be used). If using DL_LAME, the func may be loaded via dlopen/dlsym, but
405 |      if not found, the shared library will still be used if all of the
406 |      non-stub functions are found. If the function is not found via dlsym (or
{% endraw %}

```