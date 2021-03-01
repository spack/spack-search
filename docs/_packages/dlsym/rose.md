---
name: "rose"
layout: package
next_package: rr
previous_package: root
library_name: dlsym
matches: ['dlsym', 'dlopen', 'dlmopen']
languages: ['c']
---
## develop
26 / 31213 files match, 9 filtered matches.

 - [src/frontend/Experimental_Csharp_ROSE_Connection/csharp_support.C](#srcfrontendexperimental_csharp_rose_connectioncsharp_supportc)
 - [tests/nonsmoke/functional/roseTests/astOutliningTests/reference/autotuning_lib.c](#testsnonsmokefunctionalrosetestsastoutliningtestsreferenceautotuning_libc)
 - [tests/nonsmoke/functional/CompileTests/C_tests/test2012_19.c](#testsnonsmokefunctionalcompiletestsc_teststest2012_19c)
 - [tests/nonsmoke/functional/CompileTests/C_tests/test2012_102.c](#testsnonsmokefunctionalcompiletestsc_teststest2012_102c)
 - [tests/nonsmoke/functional/CompileTests/C_tests/test2012_28.c](#testsnonsmokefunctionalcompiletestsc_teststest2012_28c)
 - [projects/interpreter/interp_extcall.C](#projectsinterpreterinterp_extcallc)
 - [projects/autoTuning/autotuning_lib.c](#projectsautotuningautotuning_libc)
 - [projects/autoTuning/doc/smg2000_harmony.c](#projectsautotuningdocsmg2000_harmonyc)
 - [projects/autoTuning/doc/smg2000_dlopen.c](#projectsautotuningdocsmg2000_dlopenc)

### src/frontend/Experimental_Csharp_ROSE_Connection/csharp_support.C

```c

{% raw %}
31 |           return false;
32 |         }
33 | 
34 |      printf ("In C++ process(): calling dlsym() function = %s \n",function.c_str());
35 | 
36 |      process = (void (*)(char*,char*)) dlsym(handle, function.c_str());
37 | 
38 |      printf ("In C++ process(): after call to dlsym(): process = %p \n",process);
39 | 
40 |   // if ((error = dlerror()) != nullptr)
{% endraw %}

```
### tests/nonsmoke/functional/roseTests/astOutliningTests/reference/autotuning_lib.c

```c

{% raw %}
36 |     exit(1);
37 |   }
38 |   // find the function
39 |   result = dlsym( functionLib, function_name);
40 |   dlError = dlerror();
41 |   if( dlError )
{% endraw %}

```
### tests/nonsmoke/functional/CompileTests/C_tests/test2012_19.c

```c

{% raw %}
5044 | 
5045 | 
5046 | 
5047 | extern void *dlsym (void *__restrict __handle,
5048 |       __const char *__restrict __name) __attribute__ ((__nothrow__)) __attribute__ ((__nonnull__ (2)));
5049 | 
{% endraw %}

```
### tests/nonsmoke/functional/CompileTests/C_tests/test2012_102.c

```c

{% raw %}
12718 | 
12719 | 
12720 | 
12721 | extern void *dlsym (void *__restrict __handle,
12722 |       __const char *__restrict __name) __attribute__ ((__nothrow__)) __attribute__ ((__nonnull__ (2)));
12723 | 
12937 | module_func(Module m, char *name)
12938 | {
12939 | 
12940 |     return (Module_generic_func) dlsym(m->u.handle, name);
12941 | // # 1778 "module.c"
12942 | }
{% endraw %}

```
### tests/nonsmoke/functional/CompileTests/C_tests/test2012_28.c

```c

{% raw %}
5044 | 
5045 | 
5046 | 
5047 | extern void *dlsym (void *__restrict __handle,
5048 |       __const char *__restrict __name) __attribute__ ((__nothrow__)) __attribute__ ((__nonnull__ (2)));
5049 | 
{% endraw %}

```
### projects/interpreter/interp_extcall.C

```c

{% raw %}
231 |      string symName = sym->get_name().getString();
232 |      for (vector<void *>::const_iterator sharedLib = sharedLibraries.begin(); sharedLib != sharedLibraries.end(); ++sharedLib)
233 |         {
234 |           void (*fnPtr)() = reinterpret_cast<void(*)()>(dlsym(*sharedLib, symName.c_str()));
235 |           if (fnPtr != NULL)
236 |              {
{% endraw %}

```
### projects/autoTuning/autotuning_lib.c

```c

{% raw %}
36 |     exit(1);
37 |   }
38 |   // find the function
39 |   result = dlsym( functionLib, function_name);
40 |   dlError = dlerror();
41 |   if( dlError )
{% endraw %}

```
### projects/autoTuning/doc/smg2000_harmony.c

```c

{% raw %}
34 |   //Use the value provided Harmony to find a kernel variant
35 |   sprintf(nextUnroll, "OUT__1__6755__%d",*unroll);
36 |   printf("Trying to find: %s ...\n",nextUnroll);
37 |   OUT__1__6755__ = (void (*)(void**)) dlsym( FunctionLib, nextUnroll);
38 | 
39 |   // timing the execution of a variant
{% endraw %}

```
### projects/autoTuning/doc/smg2000_dlopen.c

```c

{% raw %}
26 |   }
27 | 
28 |   /* Find the first loaded function */
29 |   OUT__1__6755__ = dlsym (FunctionLib, "OUT__1__6755__");
30 |   dlError = dlerror ();
31 |   if (dlError)
{% endraw %}

```