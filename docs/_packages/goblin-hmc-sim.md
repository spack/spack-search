---
name: "goblin-hmc-sim"
layout: package
next_package: gotcha
previous_package: gobject-introspection
languages: ['c']
---
## 8.0.0
17 / 280 files match, 1 filtered matches.

 - [src/hmc_cmc.c](#srchmc_cmcc)

### src/hmc_cmc.c

```c

{% raw %}
224 | #ifdef HMC_DEBUG
225 |   HMCSIM_PRINT_TRACE( "LOADING CMC LIBRARY" );
226 | #endif
227 |   handle = dlopen( cmc_lib, RTLD_NOW );
228 | 
229 |   if( handle == NULL ){
{% endraw %}

```