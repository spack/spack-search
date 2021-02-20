---
name: "sdl2"
layout: package
next_package: seacas
previous_package: scorep
languages: ['c']
---
## 2.0.5
16 / 1065 files match, 2 filtered matches.

 - [src/loadso/dlopen/SDL_sysloadso.c](#srcloadsodlopensdl_sysloadsoc)
 - [src/dynapi/SDL_dynapi.c](#srcdynapisdl_dynapic)

### src/loadso/dlopen/SDL_sysloadso.c

```c

{% raw %}
46 |     }
47 | #endif
48 | 
49 |     handle = dlopen(sofile, RTLD_NOW|RTLD_LOCAL);
50 |     loaderror = (char *) dlerror();
51 |     if (handle == NULL) {
{% endraw %}

```
### src/dynapi/SDL_dynapi.c

```c

{% raw %}
233 | #include <dlfcn.h>
234 | static SDL_INLINE void *get_sdlapi_entry(const char *fname, const char *sym)
235 | {
236 |     void *lib = dlopen(fname, RTLD_NOW | RTLD_LOCAL);
237 |     void *retval = NULL;
238 |     if (lib != NULL) {
{% endraw %}

```