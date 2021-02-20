---
name: "petsc"
layout: package
next_package: php
previous_package: perl-dbd-sqlite
languages: ['python', 'c']
---
## 3.10.0
6 / 14638 files match, 5 filtered matches.

 - [config/PETSc/Configure.py](#configpetscconfigurepy)
 - [config/BuildSystem/config/compilers.py](#configbuildsystemconfigcompilerspy)
 - [config/BuildSystem/config/libraries.py](#configbuildsystemconfiglibrariespy)
 - [config/BuildSystem/config/setCompilers.py](#configbuildsystemconfigsetcompilerspy)
 - [src/sys/dll/dlimpl.c](#srcsysdlldlimplc)

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
### config/BuildSystem/config/compilers.py

```python

{% raw %}
399 |     return
400 | 
401 |   def checkDynamicLoadFlag(self):
402 |     '''Checks that dlopen() takes RTLD_XXX, and defines PETSC_HAVE_RTLD_XXX if it does'''
403 |     if self.setCompilers.dynamicLibraries:
404 |       if self.checkLink('#include <dlfcn.h>\nchar *libname;\n', 'dlopen(libname, RTLD_LAZY);\n'):
405 |         self.addDefine('HAVE_RTLD_LAZY', 1)
406 |       if self.checkLink('#include <dlfcn.h>\nchar *libname;\n', 'dlopen(libname, RTLD_NOW);\n'):
407 |         self.addDefine('HAVE_RTLD_NOW', 1)
408 |       if self.checkLink('#include <dlfcn.h>\nchar *libname;\n', 'dlopen(libname, RTLD_LOCAL);\n'):
409 |         self.addDefine('HAVE_RTLD_LOCAL', 1)
410 |       if self.checkLink('#include <dlfcn.h>\nchar *libname;\n', 'dlopen(libname, RTLD_GLOBAL);\n'):
411 |         self.addDefine('HAVE_RTLD_GLOBAL', 1)
412 |     return
{% endraw %}

```
### config/BuildSystem/config/libraries.py

```python

{% raw %}
334 |   def checkDynamic(self):
335 |     '''Check for the header and libraries necessary for dynamic library manipulation'''
336 |     if 'with-dynamic-loading' in self.argDB and not self.argDB['with-dynamic-loading']: return
337 |     self.check(['dl'], 'dlopen')
338 |     self.headers.check('dlfcn.h')
339 |     return
431 |   int (*init)(int, char **);
432 |   int (*checkInit)(void);
433 | 
434 |   lib = dlopen("'''+lib1Name+'''", RTLD_LAZY);
435 |   if (!lib) {
436 |     fprintf(stderr, "Could not open lib1.so: %s\\n", dlerror());
445 |     fprintf(stderr, "Could not initialize library\\n");
446 |     exit(1);
447 |   }
448 |   lib = dlopen("'''+lib2Name+'''", RTLD_LAZY);
449 |   if (!lib) {
450 |     fprintf(stderr, "Could not open lib2.so: %s\\n", dlerror());
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
1520 |         if self.checkLink(includes = '#include <stdio.h>\nint '+testMethod+'(void) {printf("test");return 0;}\n', codeBegin = '', codeEnd = '', cleanup = 0, shared = 'dynamic'):
1521 |           oldLib  = self.linkerObj
1522 |           code = '''
1523 | void *handle = dlopen("%s", 0);
1524 | int (*foo)(void) = (int (*)(void)) dlsym(handle, "foo");
1525 | 
{% endraw %}

```
### src/sys/dll/dlimpl.c

```c

{% raw %}
80 |   }
81 | 
82 |   /*
83 |      --- dlopen ---
84 |   */
85 | #elif defined(PETSC_HAVE_DLFCN_H) && defined(PETSC_HAVE_DLOPEN)
87 |       Mode indicates symbols required by symbol loaded with dlsym()
88 |      are only loaded when required (not all together) also indicates
89 |      symbols required can be contained in other libraries also opened
90 |      with dlopen()
91 |   */
92 | #if defined(PETSC_HAVE_RTLD_LAZY)
104 | #if defined(PETSC_HAVE_DLERROR)
105 |   dlerror(); /* clear any previous error */
106 | #endif
107 |   dlhandle = dlopen(name,dlflags1|dlflags2);
108 |   if (!dlhandle) {
109 | #if defined(PETSC_HAVE_DLERROR)
111 | #else
112 |     const char *errmsg = "unavailable";
113 | #endif
114 |     SETERRQ2(PETSC_COMM_SELF,PETSC_ERR_FILE_OPEN,"Unable to open dynamic library:\n  %s\n  Error message from dlopen() %s\n",name,errmsg);
115 |   }
116 | 
270 | #if defined(PETSC_HAVE_RTDL_DEFAULT)
271 |       dlhandle = RTLD_DEFAULT;
272 | #else
273 |       dlhandle = dlopen(0, dlflags1|dlflags2);
274 | #if defined(PETSC_HAVE_DLERROR)
275 |       { const char *e = (const char*) dlerror();
276 |         if (e) SETERRQ1(PETSC_COMM_SELF, PETSC_ERR_ARG_WRONG, "Error opening main executable as a dynamic library:\n  Error message from dlopen(): '%s'\n", e);
277 |       }
278 | #endif
{% endraw %}

```