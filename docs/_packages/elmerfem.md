---
name: "elmerfem"
layout: package
next_package: emacs
previous_package: elfutils
languages: ['c']
---
## devel
5 / 9371 files match, 2 filtered matches.

 - [fem/src/Load.c](#femsrcloadc)
 - [contrib/lua-5.1.5/src/loadlib.c](#contriblua-515srcloadlibc)

### fem/src/Load.c

```c

{% raw %}
265 | }
266 | 
267 | /*--------------------------------------------------------------------------
268 |   INTERNAL: Tries to open library with dlopen, first without
269 |             any extensions and then with SHL_EXTENSION.
270 |   Args: Libname - name of the library file
271 |         Handle - handle to the dl, NULL if fails
272 |         error_buf - string buffer for error messages
273 |  -------------------------------------------------------------------------*/
274 | static void STDCALLBULL try_dlopen(char *LibName, void **Handle, char *errorBuf)
275 | {
276 |     static char dl_names[2][2*MAX_PATH_LEN];
284 | 
285 |     for (i = 0; i < 2; i++) {
286 | #ifdef HAVE_DLOPEN_API
287 |         if ((*Handle = dlopen(dl_names[i], RTLD_NOW)) == NULL) {
288 |             strncat(errorBuf, dlerror(), MAX_PATH_LEN);
289 |             strncat(errorBuf, "\n", MAX_PATH_LEN);
316 |     char *tok;
317 | 
318 |     /* Try to open first without any prefixes */
319 |     try_dlopen(Library, Handle, errorBuf);
320 | 
321 |     /* and then using the provided paths */
326 |             strncpy(CurrentLib, tok, 2*MAX_PATH_LEN);
327 |             append_path(CurrentLib, Library);
328 | 
329 |             try_dlopen(CurrentLib, Handle, errorBuf);
330 |             if (*Handle != NULL)
331 |                 break;
{% endraw %}

```
### contrib/lua-5.1.5/src/loadlib.c

```c

{% raw %}
65 | 
66 | 
67 | static void *ll_load (lua_State *L, const char *path) {
68 |   void *lib = dlopen(path, RTLD_NOW);
69 |   if (lib == NULL) lua_pushstring(L, dlerror());
70 |   return lib;
{% endraw %}

```