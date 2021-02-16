---
name: "intel-pin"
layout: package
next_package: mongo-c-driver
previous_package: singularity-legacy
languages: ['c']
---
## 3.14
36 / 4391 files match, 11 filtered matches.

 - [source/tools/MemTranslate/malloc_translation_app.c](#sourcetoolsmemtranslatemalloc_translation_appc)
 - [source/tools/Debugger/dlopen-dlclose.c](#sourcetoolsdebuggerdlopen-dlclosec)
 - [source/tools/ToolUnitTests/dltest.c](#sourcetoolstoolunittestsdltestc)
 - [source/tools/ToolUnitTests/dltest2.c](#sourcetoolstoolunittestsdltest2c)
 - [source/tools/Probes/dltest_unix.c](#sourcetoolsprobesdltest_unixc)
 - [source/tools/Probes/tpss_lin_libc.c](#sourcetoolsprobestpss_lin_libcc)
 - [source/tools/Probes/unloadtest_unix.c](#sourcetoolsprobesunloadtest_unixc)
 - [source/tools/ImageTests/imageUnload_app.c](#sourcetoolsimagetestsimageunload_appc)
 - [extras/crt/include/dlfcn.h](#extrascrtincludedlfcnh)
 - [extras/crt/include/nsswitch.h](#extrascrtincludensswitchh)
 - [extras/crt/include/android/dlext.h](#extrascrtincludeandroiddlexth)

### source/tools/MemTranslate/malloc_translation_app.c

```c

{% raw %}
141 |     void *handle = dlopen(file, RTLD_NOW | RTLD_LOCAL);
{% endraw %}

```
### source/tools/Debugger/dlopen-dlclose.c

```c

{% raw %}
41 |     void *handle = dlopen(file, RTLD_NOW | RTLD_LOCAL);
{% endraw %}

```
### source/tools/ToolUnitTests/dltest.c

```c

{% raw %}
32 |     handle = dlopen(name, RTLD_LAZY);
{% endraw %}

```
### source/tools/ToolUnitTests/dltest2.c

```c

{% raw %}
34 |     handle = dlopen(name, RTLD_LAZY);
{% endraw %}

```
### source/tools/Probes/dltest_unix.c

```c

{% raw %}
25 |     handle = dlopen(name, RTLD_LAZY);
{% endraw %}

```
### source/tools/Probes/tpss_lin_libc.c

```c

{% raw %}
335 | VOID_PTR (*fptr__libc_dlopen_mode)(const CHAR_PTR __name, int __mode);
1389 | VOID_PTR  my__libc_dlopen_mode(const CHAR_PTR __name, int __mode) 
1391 |     printFunctionCalled("my__libc_dlopen_mode");
1392 |     VOID_PTR  res = fptr__libc_dlopen_mode(__name, __mode);
{% endraw %}

```
### source/tools/Probes/unloadtest_unix.c

```c

{% raw %}
25 |     handle = dlopen(name, RTLD_LAZY);
{% endraw %}

```
### source/tools/ImageTests/imageUnload_app.c

```c

{% raw %}
18 |     void* dlh = dlopen(filename, RTLD_LAZY);
{% endraw %}

```
### extras/crt/include/dlfcn.h

```c

{% raw %}
60 | extern void*        dlopen(const char*  filename, int flag);
{% endraw %}

```
### extras/crt/include/nsswitch.h

```c

{% raw %}
203 | 	void		*handle;	/* handle from dlopen() */
{% endraw %}

```
### extras/crt/include/android/dlext.h

```c

{% raw %}
72 | extern void* android_dlopen_ext(const char* filename, int flag, const android_dlextinfo* extinfo);
{% endraw %}

```