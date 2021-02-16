---
name: "petsc"
layout: package
next_package: apex
previous_package: fipscheck
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
148 |                  'strcasecmp', 'bzero', 'dlopen', 'dlsym', 'dlclose', 'dlerror','get_nprocs','sysctlbyname',
{% endraw %}

```
### config/BuildSystem/config/compilers.py

```python

{% raw %}
402 |     '''Checks that dlopen() takes RTLD_XXX, and defines PETSC_HAVE_RTLD_XXX if it does'''
404 |       if self.checkLink('#include <dlfcn.h>\nchar *libname;\n', 'dlopen(libname, RTLD_LAZY);\n'):
406 |       if self.checkLink('#include <dlfcn.h>\nchar *libname;\n', 'dlopen(libname, RTLD_NOW);\n'):
408 |       if self.checkLink('#include <dlfcn.h>\nchar *libname;\n', 'dlopen(libname, RTLD_LOCAL);\n'):
410 |       if self.checkLink('#include <dlfcn.h>\nchar *libname;\n', 'dlopen(libname, RTLD_GLOBAL);\n'):
{% endraw %}

```
### config/BuildSystem/config/libraries.py

```python

{% raw %}
337 |     self.check(['dl'], 'dlopen')
434 |   lib = dlopen("'''+lib1Name+'''", RTLD_LAZY);
448 |   lib = dlopen("'''+lib2Name+'''", RTLD_LAZY);
{% endraw %}

```
### config/BuildSystem/config/setCompilers.py

```python

{% raw %}
1506 |     if not self.libraries.add('dl', ['dlopen', 'dlsym', 'dlclose']):
1507 |       if not self.libraries.check('', ['dlopen', 'dlsym', 'dlclose']):
1509 |         self.logPrint('Dynamic linking disabled since functions dlopen(), dlsym(), and dlclose() were not found')
1523 | void *handle = dlopen("%s", 0);
{% endraw %}

```
### src/sys/dll/dlimpl.c

```c

{% raw %}
83 |      --- dlopen ---
90 |      with dlopen()
107 |   dlhandle = dlopen(name,dlflags1|dlflags2);
114 |     SETERRQ2(PETSC_COMM_SELF,PETSC_ERR_FILE_OPEN,"Unable to open dynamic library:\n  %s\n  Error message from dlopen() %s\n",name,errmsg);
273 |       dlhandle = dlopen(0, dlflags1|dlflags2);
276 |         if (e) SETERRQ1(PETSC_COMM_SELF, PETSC_ERR_ARG_WRONG, "Error opening main executable as a dynamic library:\n  Error message from dlopen(): '%s'\n", e);
{% endraw %}

```