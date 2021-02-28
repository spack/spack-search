---
name: "ngspice"
layout: package
next_package: stat
previous_package: dotconf
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 33
4 / 3566 files match, 2 filtered matches.

 - [src/spicelib/devices/dev.c](#srcspicelibdevicesdevc)
 - [visualc/ng_shared_xspice_v/src/main_xspice.c](#visualcng_shared_xspice_vsrcmain_xspicec)

### src/spicelib/devices/dev.c

```c

{% raw %}
48 | #include <windows.h>
49 | typedef FARPROC funptr_t;
50 | void *dlopen(const char *, int);
51 | funptr_t dlsym(void *, const char *);
52 | char *dlerror(void);
53 | #define FREE_DLERR_MSG(msg) free_dlerr_msg(msg)
325 |   strcpy(libname, "get_");
326 |   strcat(libname,name);
327 |   strcat(libname,"_info");
328 |   fetch = dlsym(lib,libname);
329 | 
330 |   if(!fetch){
425 | 
426 | 
427 |     /* Get code models defined by the library */
428 |     if ((fetch = dlsym(lib, "CMdevNum")) != (funptr_t) NULL) {
429 |         num = *(*(int * (*)(void)) fetch)();
430 |         fetch = dlsym(lib, "CMdevs");
431 |         if (fetch != (funptr_t) NULL) {
432 |             devs = (*(SPICEdev ** (*)(void)) fetch)();
454 | 
455 | 
456 |     /* Get user-defined ndes defined by the library */
457 |     if ((fetch = dlsym(lib, "CMudnNum")) != (funptr_t) NULL) {
458 |         num = *(*(int * (*)(void)) fetch)();
459 |         fetch = dlsym(lib, "CMudns");
460 |         if (fetch != (funptr_t) NULL) {
461 |             udns = (*(Evt_Udn_Info_t ** (*)(void)) fetch)();
481 | #endif
482 | 
483 |     /* Give the code model access to facilities provided by ngspice. */
484 |     if ((fetch = dlsym(lib,"CMgetCoreItfPtr")) != (funptr_t) NULL) {
485 |         const struct coreInfo_t ** const core =
486 |                 (const struct coreInfo_t **const)
513 |     return LoadLibrary(name);
514 | }
515 | 
516 | funptr_t dlsym(void *hDll, const char *funcname)
517 | {
518 |     return GetProcAddress(hDll, funcname);
{% endraw %}

```
### visualc/ng_shared_xspice_v/src/main_xspice.c

```c

{% raw %}
41 | #include <windows.h>
42 | typedef FARPROC funptr_t;
43 | void *dlopen (const char *, int);
44 | funptr_t dlsym (void *, const char *);
45 | int dlclose (void *);
46 | char *dlerror (void);
144 | //        exit(1);
145 |     }
146 | 
147 |     ngSpice_Init_handle = dlsym(ngdllhandle, "ngSpice_Init");
148 |     errmsg = dlerror();
149 |     if (errmsg)
150 |         printf(errmsg);
151 |     ngSpice_Command_handle = dlsym(ngdllhandle, "ngSpice_Command");
152 |     errmsg = dlerror();
153 |     if (errmsg)
154 |         printf(errmsg);
155 |     ngSpice_CurPlot_handle = dlsym(ngdllhandle, "ngSpice_CurPlot");
156 |     errmsg = dlerror();
157 |     if (errmsg)
158 |         printf(errmsg);
159 |     ngSpice_AllVecs_handle = dlsym(ngdllhandle, "ngSpice_AllVecs");
160 |     errmsg = dlerror();
161 |     if (errmsg)
162 |         printf(errmsg);
163 |     ngSpice_GVI_handle = dlsym(ngdllhandle, "ngGet_Vec_Info");
164 |     errmsg = dlerror();
165 |     if (errmsg)
166 |         printf(errmsg);
167 |     ngSpice_AllEvtNodes_handle = dlsym(ngdllhandle, "ngSpice_AllEvtNodes");
168 |     errmsg = dlerror();
169 |     if (errmsg)
170 |         printf(errmsg);
171 |     ngSpice_EVT_handle = dlsym(ngdllhandle, "ngGet_Evt_NodeInfo");
172 |     errmsg = dlerror();
173 |     if (errmsg)
174 |         printf(errmsg);
175 |     ngSpice_Init_Evt_handle = dlsym(ngdllhandle, "ngSpice_Init_Evt");
176 |     errmsg = dlerror();
177 |     if (errmsg)
642 | }
643 | 
644 | /* Unify LINUX and Windows dynamic library handling:
645 |    Add functions dlopen, dlsym, dlerror, dlclose to Windows by
646 |    tranlating to Windows API functions.
647 | */
652 | 	return LoadLibrary((LPCSTR)name);
653 | }
654 | 
655 | funptr_t dlsym(void *hDll, const char *funcname)
656 | {
657 | 	return GetProcAddress(hDll, funcname);
{% endraw %}

```