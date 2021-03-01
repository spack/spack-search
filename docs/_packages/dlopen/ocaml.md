---
name: "ocaml"
layout: package
next_package: octave
previous_package: nspr
library_name: dlopen
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 4.03.0
6 / 2293 files match, 6 filtered matches.

 - [byterun/unix.c](#byterununixc)
 - [byterun/win32.c](#byterunwin32c)
 - [byterun/dynlink.c](#byterundynlinkc)
 - [byterun/caml/osdeps.h](#byteruncamlosdepsh)
 - [config/s-templ.h](#configs-templh)
 - [asmrun/natdynlink.c](#asmrunnatdynlinkc)

### byterun/unix.c

```c

{% raw %}
212 | #ifdef __CYGWIN__
213 | /* Use flexdll */
214 | 
215 | void * caml_dlopen(char * libname, int for_execution, int global)
216 | {
217 |   int flags = (global ? FLEXDLL_RTLD_GLOBAL : 0);
218 |   if (!for_execution) flags |= FLEXDLL_RTLD_NOEXEC;
219 |   return flexdll_dlopen(libname, flags);
220 | }
221 | 
231 | 
232 | void * caml_globalsym(char * name)
233 | {
234 |   return flexdll_dlsym(flexdll_dlopen(NULL,0), name);
235 | }
236 | 
252 | #define RTLD_NODELETE 0
253 | #endif
254 | 
255 | void * caml_dlopen(char * libname, int for_execution, int global)
256 | {
257 |   return dlopen(libname, RTLD_NOW | (global ? RTLD_GLOBAL : RTLD_LOCAL)
258 |                          | RTLD_NODELETE);
259 |   /* Could use RTLD_LAZY if for_execution == 0, but needs testing */
291 | #endif
292 | #else
293 | 
294 | void * caml_dlopen(char * libname, int for_execution, int global)
295 | {
296 |   return NULL;
{% endraw %}

```
### byterun/win32.c

```c

{% raw %}
195 | 
196 | #ifdef SUPPORT_DYNAMIC_LINKING
197 | 
198 | void * caml_dlopen(char * libname, int for_execution, int global)
199 | {
200 |   void *handle;
201 |   int flags = (global ? FLEXDLL_RTLD_GLOBAL : 0);
202 |   if (!for_execution) flags |= FLEXDLL_RTLD_NOEXEC;
203 |   handle = flexdll_dlopen(libname, flags);
204 |   if ((handle != NULL) && ((caml_verb_gc & 0x100) != 0)) {
205 |     flexdll_dump_exports(handle);
220 | 
221 | void * caml_globalsym(char * name)
222 | {
223 |   return flexdll_dlsym(flexdll_dlopen(NULL,0), name);
224 | }
225 | 
230 | 
231 | #else
232 | 
233 | void * caml_dlopen(char * libname, int for_execution, int global)
234 | {
235 |   return NULL;
{% endraw %}

```
### byterun/dynlink.c

```c

{% raw %}
122 |   caml_gc_message(0x100, "Loading shared library %s\n",
123 |                   (uintnat) realname);
124 |   caml_enter_blocking_section();
125 |   handle = caml_dlopen(realname, 1, 1);
126 |   caml_leave_blocking_section();
127 |   if (handle == NULL)
212 |                   (uintnat) String_val(filename));
213 |   p = caml_strdup(String_val(filename));
214 |   caml_enter_blocking_section();
215 |   handle = caml_dlopen(p, Int_val(mode), 1);
216 |   caml_leave_blocking_section();
217 |   caml_stat_free(p);
{% endraw %}

```
### byterun/caml/osdeps.h

```c

{% raw %}
59 |    If [global] is true, symbols from the shared library can be used
60 |    to resolve for other libraries to be opened later on.
61 |    Return [NULL] on error. */
62 | extern void * caml_dlopen(char * libname, int for_execution, int global);
63 | 
64 | /* Close a shared library handle */
{% endraw %}

```
### config/s-templ.h

```c

{% raw %}
49 | #define SUPPORT_DYNAMIC_LINKING
50 | 
51 | /* Define SUPPORT_DYNAMIC_LINKING if dynamic loading of C stub code
52 |    via dlopen() is available. */
53 | 
54 | #define HAS_C99_FLOAT_OPS
{% endraw %}

```
### asmrun/natdynlink.c

```c

{% raw %}
59 | 
60 |   p = caml_strdup(String_val(filename));
61 |   caml_enter_blocking_section();
62 |   handle = caml_dlopen(p, 1, Int_val(global));
63 |   caml_leave_blocking_section();
64 |   caml_stat_free(p);
130 | 
131 |   p = caml_strdup(String_val(filename));
132 |   caml_enter_blocking_section();
133 |   handle = caml_dlopen(p, 1, 1);
134 |   caml_leave_blocking_section();
135 |   caml_stat_free(p);
{% endraw %}

```