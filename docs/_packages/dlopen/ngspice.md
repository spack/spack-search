---
name: "ngspice"
layout: package
next_package: apr
previous_package: kmod
library_name: dlopen
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 33
5 / 3566 files match, 2 filtered matches.

 - [src/spicelib/devices/dev.c](#srcspicelibdevicesdevc)
 - [visualc/ng_shared_xspice_v/src/main_xspice.c](#visualcng_shared_xspice_vsrcmain_xspicec)

### src/spicelib/devices/dev.c

```c

{% raw %}
47 | #undef BOOLEAN
48 | #include <windows.h>
49 | typedef FARPROC funptr_t;
50 | void *dlopen(const char *, int);
51 | funptr_t dlsym(void *, const char *);
52 | char *dlerror(void);
315 |   strcat(libname,name);
316 |   strcat(libname,".so");
317 | 
318 |   lib = dlopen(libname,RTLD_NOW);
319 |   if(!lib){
320 |     msg = dlerror();
415 |     Evt_Udn_Info_t **udns;
416 |     funptr_t fetch;
417 | 
418 |     lib = dlopen(name, RTLD_NOW);
419 |     if (!lib) {
420 |         msg = dlerror();
507 | static char errstr[sizeof errstr_fmt - 3 + 3 * sizeof(unsigned long)];
508 | 
509 | /* Emulations of POSIX dlopen(), dlsym(), and dlerror(). */
510 | void *dlopen(const char *name, int type)
511 | {
512 |     NG_IGNORE(type);
{% endraw %}

```
### visualc/ng_shared_xspice_v/src/main_xspice.c

```c

{% raw %}
40 | #undef BOOLEAN
41 | #include <windows.h>
42 | typedef FARPROC funptr_t;
43 | void *dlopen (const char *, int);
44 | funptr_t dlsym (void *, const char *);
45 | int dlclose (void *);
133 | #else
134 |     loadstring = "libngspice.so";
135 | #endif
136 |     ngdllhandle = dlopen(loadstring, RTLD_NOW);
137 |     errmsg = dlerror();
138 |     if (errmsg)
642 | }
643 | 
644 | /* Unify LINUX and Windows dynamic library handling:
645 |    Add functions dlopen, dlsym, dlerror, dlclose to Windows by
646 |    tranlating to Windows API functions.
647 | */
648 | #if defined(__MINGW32__) ||  defined(_MSC_VER)
649 | 
650 | void *dlopen(const char *name,int type)
651 | {
652 | 	return LoadLibrary((LPCSTR)name);
{% endraw %}

```