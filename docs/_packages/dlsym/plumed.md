---
name: "plumed"
layout: package
next_package: sollya
previous_package: numamma
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 2.5.1
6 / 5058 files match, 1 filtered matches.

 - [src/wrapper/Plumed.h](#srcwrapperplumedh)

### src/wrapper/Plumed.h

```c

{% raw %}
310 | 
311 |   An important novelty is in the way the runtime loader is implemented.
312 |   In particular, the loader works also if the symbols of the main executable are not exported.
313 |   The proper functions from the kernel are indeed searched explicitly now using `dlsym`.
314 | 
315 |   Some additional features can be enabled using suitable environment variables. In particular:
2083 | */
2084 | #define __PLUMED_SEARCH_FUNCTION(tmpptr,handle,func,name,debug) \
2085 |   if(!func) { \
2086 |     tmpptr=dlsym(handle,name); \
2087 |     if(tmpptr) { \
2088 |       *(void **)(&func)=tmpptr; \
2117 |     unnecessary and might be removed at some point.
2118 |   */
2119 |   debug=__PLUMED_GETENV("PLUMED_LOAD_DEBUG");
2120 |   table_ptr=(plumed_symbol_table_type*) dlsym(handle,"plumed_symbol_table");
2121 |   if(table_ptr) functions=table_ptr->functions;
2122 |   if(debug) {
2232 |   if(functions) *functions=g;
2233 | #else
2234 |   /*
2235 |     On the other hand, for runtime binding, we use dlsym to find the relevant functions.
2236 |   */
2237 |   plumed_plumedmain_function_holder g;
{% endraw %}

```