---
name: "petsc"
layout: package
next_package: kbd
previous_package: rsyslog
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c', 'python']
---
## 3.10.0
7 / 14638 files match, 5 filtered matches.

 - [config/PETSc/Configure.py](#configpetscconfigurepy)
 - [config/BuildSystem/config/libraries.py](#configbuildsystemconfiglibrariespy)
 - [config/BuildSystem/config/setCompilers.py](#configbuildsystemconfigsetcompilerspy)
 - [src/sys/dll/dlimpl.c](#srcsysdlldlimplc)
 - [src/ts/examples/tutorials/advection-diffusion-reaction/ex1.c](#srctsexamplestutorialsadvection-diffusion-reactionex1c)

### config/PETSc/Configure.py

```python

{% raw %}
145 |                  'gettimeofday', 'getwd', 'memalign', 'mkstemp', 'popen', 'PXFGETARG', 'rand', 'getpagesize',
146 |                  'readlink', 'realpath',  'sigaction', 'signal', 'sigset', 'usleep', 'sleep', '_sleep', 'socket',
147 |                  'times', 'gethostbyname', 'uname','snprintf','_snprintf','lseek','_lseek','time','fork','stricmp',
148 |                  'strcasecmp', 'bzero', 'dlopen', 'dlsym', 'dlclose', 'dlerror','get_nprocs','sysctlbyname',
149 |                  '_set_output_format','_mkdir']
150 |     libraries1 = [(['socket', 'nsl'], 'socket'), (['fpe'], 'handle_sigfpes')]
{% endraw %}

```
### config/BuildSystem/config/libraries.py

```python

{% raw %}
436 |     fprintf(stderr, "Could not open lib1.so: %s\\n", dlerror());
437 |     exit(1);
438 |   }
439 |   init = (int (*)(int, char **)) dlsym(lib, "init");
440 |   if (!init) {
441 |     fprintf(stderr, "Could not find initialization function\\n");
450 |     fprintf(stderr, "Could not open lib2.so: %s\\n", dlerror());
451 |     exit(1);
452 |   }
453 |   checkInit = (int (*)(void)) dlsym(lib, "checkInit");
454 |   if (!checkInit) {
455 |     fprintf(stderr, "Could not find initialization check function\\n");
{% endraw %}

```
### config/BuildSystem/config/setCompilers.py

```python

{% raw %}
1503 |       return
1504 |     self.logWrite(self.headers.restoreLog())
1505 |     self.libraries.saveLog()
1506 |     if not self.libraries.add('dl', ['dlopen', 'dlsym', 'dlclose']):
1507 |       if not self.libraries.check('', ['dlopen', 'dlsym', 'dlclose']):
1508 |         self.logWrite(self.libraries.restoreLog())
1509 |         self.logPrint('Dynamic linking disabled since functions dlopen(), dlsym(), and dlclose() were not found')
1510 |         return
1511 |     self.logWrite(self.libraries.restoreLog())
1521 |           oldLib  = self.linkerObj
1522 |           code = '''
1523 | void *handle = dlopen("%s", 0);
1524 | int (*foo)(void) = (int (*)(void)) dlsym(handle, "foo");
1525 | 
1526 | if (!foo) {
{% endraw %}

```
### src/sys/dll/dlimpl.c

```c

{% raw %}
19 | 
20 | #if defined(PETSC_HAVE_WINDOWS_H)
21 | typedef HMODULE dlhandle_t;
22 | typedef FARPROC dlsymbol_t;
23 | #elif defined(PETSC_HAVE_DLFCN_H)
24 | typedef void* dlhandle_t;
25 | typedef void* dlsymbol_t;
26 | #else
27 | typedef void* dlhandle_t;
28 | typedef void* dlsymbol_t;
29 | #endif
30 | 
84 |   */
85 | #elif defined(PETSC_HAVE_DLFCN_H) && defined(PETSC_HAVE_DLOPEN)
86 |   /*
87 |       Mode indicates symbols required by symbol loaded with dlsym()
88 |      are only loaded when required (not all together) also indicates
89 |      symbols required can be contained in other libraries also opened
212 | PetscErrorCode  PetscDLSym(PetscDLHandle handle,const char symbol[],void **value)
213 | {
214 |   PETSC_UNUSED dlhandle_t dlhandle;
215 |   dlsymbol_t              dlsymbol;
216 | 
217 |   PetscValidCharPointer(symbol,2);
218 |   PetscValidPointer(value,3);
219 | 
220 |   dlhandle = (dlhandle_t) 0;
221 |   dlsymbol = (dlsymbol_t) 0;
222 |   *value   = (void*) 0;
223 | 
228 | #if defined(PETSC_HAVE_GETPROCADDRESS)
229 |   if (handle) dlhandle = (dlhandle_t) handle;
230 |   else dlhandle = (dlhandle_t) GetCurrentProcess();
231 |   dlsymbol = (dlsymbol_t) GetProcAddress(dlhandle,symbol);
232 | #if defined(PETSC_HAVE_SETLASTERROR)
233 |   SetLastError((DWORD)0); /* clear any previous error */
235 | #endif /* !PETSC_HAVE_GETPROCADDRESS */
236 | 
237 |   /*
238 |      --- dlsym ---
239 |   */
240 | #elif defined(PETSC_HAVE_DLFCN_H)
284 | #if defined(PETSC_HAVE_DLERROR)
285 |   dlerror(); /* clear any previous error */
286 | #endif
287 |   dlsymbol = (dlsymbol_t) dlsym(dlhandle,symbol);
288 |   /*
289 |      --- unimplemented ---
{% endraw %}

```
### src/ts/examples/tutorials/advection-diffusion-reaction/ex1.c

```c

{% raw %}
270 | 
271 |    test:
272 |      args: -ts_view
273 |      requires: dlsym define(PETSC_HAVE_DYNAMIC_LIBRARIES)
274 | 
275 |    test:
277 |      args: -ts_monitor_lg_error -ts_monitor_lg_solution  -ts_view
278 |      requires: x
279 |      output_file: output/ex1_1.out
280 |      requires: dlsym define(PETSC_HAVE_DYNAMIC_LIBRARIES)
281 | 
282 | TEST*/
{% endraw %}

```