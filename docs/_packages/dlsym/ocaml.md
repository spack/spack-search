---
name: "ocaml"
layout: package
next_package: octave
previous_package: numamma
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 4.03.0
5 / 2293 files match, 5 filtered matches.

 - [byterun/unix.c](#byterununixc)
 - [byterun/win32.c](#byterunwin32c)
 - [byterun/dynlink.c](#byterundynlinkc)
 - [byterun/caml/osdeps.h](#byteruncamlosdepsh)
 - [asmrun/natdynlink.c](#asmrunnatdynlinkc)

### byterun/unix.c

```c

{% raw %}
224 |   flexdll_dlclose(handle);
225 | }
226 | 
227 | void * caml_dlsym(void * handle, char * name)
228 | {
229 |   return flexdll_dlsym(handle, name);
230 | }
231 | 
232 | void * caml_globalsym(char * name)
233 | {
234 |   return flexdll_dlsym(flexdll_dlopen(NULL,0), name);
235 | }
236 | 
264 |   dlclose(handle);
265 | }
266 | 
267 | void * caml_dlsym(void * handle, char * name)
268 | {
269 | #ifdef DL_NEEDS_UNDERSCORE
271 |   strncat (_name, name, 998);
272 |   name = _name;
273 | #endif
274 |   return dlsym(handle, name);
275 | }
276 | 
277 | void * caml_globalsym(char * name)
278 | {
279 | #ifdef RTLD_DEFAULT
280 |   return caml_dlsym(RTLD_DEFAULT, name);
281 | #else
282 |   return NULL;
300 | {
301 | }
302 | 
303 | void * caml_dlsym(void * handle, char * name)
304 | {
305 |   return NULL;
{% endraw %}

```
### byterun/win32.c

```c

{% raw %}
213 |   flexdll_dlclose(handle);
214 | }
215 | 
216 | void * caml_dlsym(void * handle, char * name)
217 | {
218 |   return flexdll_dlsym(handle, name);
219 | }
220 | 
221 | void * caml_globalsym(char * name)
222 | {
223 |   return flexdll_dlsym(flexdll_dlopen(NULL,0), name);
224 | }
225 | 
239 | {
240 | }
241 | 
242 | void * caml_dlsym(void * handle, char * name)
243 | {
244 |   return NULL;
{% endraw %}

```
### byterun/dynlink.c

```c

{% raw %}
61 |       return caml_builtin_cprim[i];
62 |   }
63 |   for (i = 0; i < shared_libs.size; i++) {
64 |     res = caml_dlsym(shared_libs.contents[i], name);
65 |     if (res != NULL) return (c_primitive) res;
66 |   }
232 | {
233 |   void * symb;
234 |   value result;
235 |   symb = caml_dlsym(Handle_val(handle), String_val(symbolname));
236 |   /* printf("%s = 0x%lx\n", String_val(symbolname), symb);
237 |      fflush(stdout); */
{% endraw %}

```
### byterun/caml/osdeps.h

```c

{% raw %}
66 | 
67 | /* Look up the given symbol in the given shared library.
68 |    Return [NULL] if not found, or symbol value if found. */
69 | extern void * caml_dlsym(void * handle, char * name);
70 | 
71 | extern void * caml_globalsym(char * name);
{% endraw %}

```
### asmrun/natdynlink.c

```c

{% raw %}
29 | static void *getsym(void *handle, char *module, char *name){
30 |   char *fullname = caml_strconcat(3, "caml", module, name);
31 |   void *sym;
32 |   sym = caml_dlsym (handle, fullname);
33 |   /*  printf("%s => %lx\n", fullname, (uintnat) sym); */
34 |   caml_stat_free(fullname);
66 |   if (NULL == handle)
67 |     CAMLreturn(caml_copy_string(caml_dlerror()));
68 | 
69 |   sym = caml_dlsym(handle, "caml_plugin_header");
70 |   if (NULL == sym)
71 |     CAMLreturn(caml_copy_string("not an OCaml plugin"));
{% endraw %}

```