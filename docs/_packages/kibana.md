---
name: "kibana"
layout: package
next_package: kitty
previous_package: keepalived
languages: ['c']
---
## 6.4.0
6 / 56280 files match, 1 filtered matches.

 - [node/include/node/uv.h](#nodeincludenodeuvh)

### node/include/node/uv.h

```c

{% raw %}
1457 | 
1458 | UV_EXTERN void uv_disable_stdio_inheritance(void);
1459 | 
1460 | UV_EXTERN int uv_dlopen(const char* filename, uv_lib_t* lib);
1461 | UV_EXTERN void uv_dlclose(uv_lib_t* lib);
1462 | UV_EXTERN int uv_dlsym(uv_lib_t* lib, const char* name, void** ptr);
{% endraw %}

```