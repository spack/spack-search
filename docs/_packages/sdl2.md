---
name: "sdl2"
layout: package
next_package: prrte
previous_package: pcre2
languages: ['c']
---
## 2.0.5
16 / 1065 files match, 2 filtered matches.

 - [src/loadso/dlopen/SDL_sysloadso.c](#srcloadsodlopensdl_sysloadsoc)
 - [src/dynapi/SDL_dynapi.c](#srcdynapisdl_dynapic)

### src/loadso/dlopen/SDL_sysloadso.c

```c

{% raw %}
49 |     handle = dlopen(sofile, RTLD_NOW|RTLD_LOCAL);
{% endraw %}

```
### src/dynapi/SDL_dynapi.c

```c

{% raw %}
236 |     void *lib = dlopen(fname, RTLD_NOW | RTLD_LOCAL);
{% endraw %}

```