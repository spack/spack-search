---
name: "libverto"
layout: package
next_package: libwebsockets
previous_package: libuv
languages: ['c']
---
## 0.3.1
2 / 45 files match, 1 filtered matches.

 - [src/module.c](#srcmodulec)

### src/module.c

```c

{% raw %}
102 |     void *mod;
103 |     (void) modname;
104 | 
105 |     mod = dlopen(NULL, RTLD_LAZY | RTLD_LOCAL);
106 |     if (mod) {
107 |         void* sym = dlsym(mod, symbname);
178 |      * more general use of this evil flag. */
179 |     intdll = LoadLibraryEx(filename, NULL, DONT_RESOLVE_DLL_REFERENCES);
180 | #else  /* WIN32 */
181 |     intdll = dlopen(filename, RTLD_LAZY | RTLD_LOCAL);
182 | #endif /* WIN32 */
183 |     if (!intdll)
201 | #ifdef WIN32
202 |     intdll = LoadLibrary(filename);
203 | #else  /* WIN32 */
204 |     intdll = dlopen(filename, RTLD_NOW | RTLD_LOCAL);
205 | #endif /* WIN32 */
206 |     if (!intdll)
{% endraw %}

```