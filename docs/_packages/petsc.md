---
name: "petsc"
layout: package
next_package: apex
previous_package: fipscheck
languages: ['html', 'cpp', 'python']
---
## 3.10.0
6 / 14638 files match

 - [config/PETSc/Configure.py](#configpetscconfigurepy)
 - [config/BuildSystem/config/compilers.py](#configbuildsystemconfigcompilerspy)
 - [config/BuildSystem/config/libraries.py](#configbuildsystemconfiglibrariespy)
 - [config/BuildSystem/config/setCompilers.py](#configbuildsystemconfigsetcompilerspy)
 - [src/sys/dll/dlimpl.c.html](#srcsysdlldlimplchtml)
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
### src/sys/dll/dlimpl.c.html

```html

{% raw %}
45 | <a name="line33"> 33: </a><font color="#B22222">   <a href="../../../docs/manualpages/Sys/PetscDLOpen.html#PetscDLOpen">PetscDLOpen</a> - opens dynamic library</font>
59 | <a name="line47"> 47: </a><strong><font color="#4169E1"><a name="PetscDLOpen"></a><a href="../../../docs/manualpages/Sys/PetscErrorCode.html#PetscErrorCode">PetscErrorCode</a>  <a href="../../../docs/manualpages/Sys/PetscDLOpen.html#PetscDLOpen">PetscDLOpen</a>(const char name[],PetscDLMode mode,PetscDLHandle *handle)</font></strong>
92 | <a name="line84"> 84: </a><font color="#B22222">     --- dlopen ---</font>
94 | <a name="line86"> 86: </a><font color="#A020F0">#elif defined(PETSC_HAVE_DLFCN_H) &amp;&amp; defined(PETSC_HAVE_DLOPEN)</font>
99 | <a name="line91"> 91: </a><font color="#B22222">     with dlopen()</font>
116 | <a name="line108">108: </a>  dlhandle = dlopen(name,dlflags1|dlflags2);
123 | <a name="line115">115: </a>    <a href="../../../docs/manualpages/Sys/SETERRQ2.html#SETERRQ2">SETERRQ2</a>(<a href="../../../docs/manualpages/Sys/PETSC_COMM_SELF.html#PETSC_COMM_SELF">PETSC_COMM_SELF</a>,PETSC_ERR_FILE_OPEN,<font color="#666666">"Unable to open dynamic library:\n  %s\n  Error message from dlopen() %s\n"</font>,name,errmsg);
144 | <a name="line136">136: </a><font color="#B22222">.   handle - the handle for the library obtained with <a href="../../../docs/manualpages/Sys/PetscDLOpen.html#PetscDLOpen">PetscDLOpen</a>()</font>
205 | <a name="line199">199: </a><font color="#B22222">+   handle - obtained with <a href="../../../docs/manualpages/Sys/PetscDLOpen.html#PetscDLOpen">PetscDLOpen</a>() or NULL</font>
250 | <a name="line246">246: </a><font color="#A020F0">#if defined(PETSC_HAVE_DLOPEN) &amp;&amp; defined(PETSC_HAVE_DYNAMIC_LIBRARIES)</font>
278 | <a name="line274">274: </a>      dlhandle = dlopen(0, dlflags1|dlflags2);
281 | <a name="line277">277: </a>        <font color="#4169E1">if</font> (e) <a href="../../../docs/manualpages/Sys/SETERRQ1.html#SETERRQ1">SETERRQ1</a>(<a href="../../../docs/manualpages/Sys/PETSC_COMM_SELF.html#PETSC_COMM_SELF">PETSC_COMM_SELF</a>, PETSC_ERR_ARG_WRONG, <font color="#666666">"Error opening main executable as a dynamic library:\n  Error message from dlopen(): '%s'\n"</font>, e);
287 | <a name="line283">283: </a><font color="#A020F0">#endif </font><font color="#B22222">/* PETSC_HAVE_DLOPEN &amp;&amp; PETSC_HAVE_DYNAMIC_LIBRARIES */</font><font color="#A020F0"></font>
{% endraw %}

```
### src/sys/dll/dlimpl.c

```cpp

{% raw %}
32 |    PetscDLOpen - opens dynamic library
46 | PetscErrorCode  PetscDLOpen(const char name[],PetscDLMode mode,PetscDLHandle *handle)
83 |      --- dlopen ---
85 | #elif defined(PETSC_HAVE_DLFCN_H) && defined(PETSC_HAVE_DLOPEN)
90 |      with dlopen()
107 |   dlhandle = dlopen(name,dlflags1|dlflags2);
114 |     SETERRQ2(PETSC_COMM_SELF,PETSC_ERR_FILE_OPEN,"Unable to open dynamic library:\n  %s\n  Error message from dlopen() %s\n",name,errmsg);
135 | .   handle - the handle for the library obtained with PetscDLOpen()
198 | +   handle - obtained with PetscDLOpen() or NULL
245 | #if defined(PETSC_HAVE_DLOPEN) && defined(PETSC_HAVE_DYNAMIC_LIBRARIES)
273 |       dlhandle = dlopen(0, dlflags1|dlflags2);
276 |         if (e) SETERRQ1(PETSC_COMM_SELF, PETSC_ERR_ARG_WRONG, "Error opening main executable as a dynamic library:\n  Error message from dlopen(): '%s'\n", e);
282 | #endif /* PETSC_HAVE_DLOPEN && PETSC_HAVE_DYNAMIC_LIBRARIES */
{% endraw %}

```