---
name: "intel-pin"
layout: package
next_package: intel-tbb
previous_package: intel-llvm
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
138 |     const char* file = argv[1];
139 |     printf("Loading shared object %s\n", file);
140 |     fflush(stdout);
141 |     void *handle = dlopen(file, RTLD_NOW | RTLD_LOCAL);
142 |     if (NULL == handle)
143 |     {
{% endraw %}

```
### source/tools/Debugger/dlopen-dlclose.c

```c

{% raw %}
38 |     const char* file = argv[1];
39 |     printf("Loading shared object %s\n", file);
40 |     fflush(stdout);
41 |     void *handle = dlopen(file, RTLD_NOW | RTLD_LOCAL);
42 |     if (NULL == handle)
43 |     {
{% endraw %}

```
### source/tools/ToolUnitTests/dltest.c

```c

{% raw %}
29 |     void * handle;
30 |     int (*sym)();
31 |     
32 |     handle = dlopen(name, RTLD_LAZY);
33 |     if (handle == 0)
34 |     {
{% endraw %}

```
### source/tools/ToolUnitTests/dltest2.c

```c

{% raw %}
31 |     int (*sym)();
32 |     double (*fsin)(double);
33 |     
34 |     handle = dlopen(name, RTLD_LAZY);
35 |     if (handle == 0)
36 |     {
{% endraw %}

```
### source/tools/Probes/dltest_unix.c

```c

{% raw %}
22 |     void * handle;
23 |     int (*sym)();
24 |     
25 |     handle = dlopen(name, RTLD_LAZY);
26 |     if (handle == 0)
27 |     {
{% endraw %}

```
### source/tools/Probes/tpss_lin_libc.c

```c

{% raw %}
332 | 
333 | int (*fptrfcntl)(int __fd, int __cmd, VOID_PTR  __argp);
334 | 
335 | VOID_PTR (*fptr__libc_dlopen_mode)(const CHAR_PTR __name, int __mode);
336 | 
337 | INT_PTR  (*fptr__errno_location)(void);
1386 |     return res;
1387 | }
1388 | 
1389 | VOID_PTR  my__libc_dlopen_mode(const CHAR_PTR __name, int __mode) 
1390 | {
1391 |     printFunctionCalled("my__libc_dlopen_mode");
1392 |     VOID_PTR  res = fptr__libc_dlopen_mode(__name, __mode);
1393 | 
1394 |     return res;
{% endraw %}

```
### source/tools/Probes/unloadtest_unix.c

```c

{% raw %}
22 |     void * handle;
23 |     int (*sym)();
24 |     
25 |     handle = dlopen(name, RTLD_LAZY);
26 |     if (handle == 0)
27 |     {
{% endraw %}

```
### source/tools/ImageTests/imageUnload_app.c

```c

{% raw %}
15 | 
16 | void Open(char* filename)
17 | {
18 |     void* dlh = dlopen(filename, RTLD_LAZY);
19 |     if( !dlh )
20 |     {
{% endraw %}

```
### extras/crt/include/dlfcn.h

```c

{% raw %}
57 |                                in dli_sname */
58 | } Dl_info;
59 | 
60 | extern void*        dlopen(const char*  filename, int flag);
61 | extern int          dlclose(void*  handle);
62 | extern const char*  dlerror(void);
{% endraw %}

```
### extras/crt/include/nsswitch.h

```c

{% raw %}
200 |  */
201 | typedef struct {
202 | 	const char	*name;		/* module name */
203 | 	void		*handle;	/* handle from dlopen() */
204 | 	ns_mtab		*mtab;		/* method table */
205 | 	u_int		 mtabsize;	/* size of mtab */
{% endraw %}

```
### extras/crt/include/android/dlext.h

```c

{% raw %}
69 |   int     library_fd;
70 | } android_dlextinfo;
71 | 
72 | extern void* android_dlopen_ext(const char* filename, int flag, const android_dlextinfo* extinfo);
73 | 
74 | __END_DECLS
{% endraw %}

```