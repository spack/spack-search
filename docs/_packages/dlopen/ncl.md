---
name: "ncl"
layout: package
next_package: nest
previous_package: nccl
library_name: dlopen
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 6.5.0
3 / 8693 files match, 2 filtered matches.

 - [ni/src/ncl/NclDriver.c](#nisrcnclncldriverc)
 - [ni/src/ncl/NclApi.c](#nisrcnclnclapic)

### ni/src/ncl/NclDriver.c

```c

{% raw %}
320 | #if defined (HPUX)
321 |                     so_handle = shl_load(buffer, BIND_IMMEDIATE, 0L);
322 | #else
323 |                     so_handle = dlopen(buffer, RTLD_NOW);
324 |                     if (so_handle == NULL) {
325 |                         NhlPError(NhlFATAL, NhlEUNKNOWN,
{% endraw %}

```
### ni/src/ncl/NclApi.c

```c

{% raw %}
218 | #if defined(HPUX)
219 | 					so_handle = shl_load(buffer,BIND_IMMEDIATE,0L);
220 | #else
221 | 					so_handle = dlopen(buffer,RTLD_NOW);
222 | 					if(so_handle == NULL) {
223 | 						NhlPError(NhlFATAL,NhlEUNKNOWN," Could not open (%s): %s",buffer,dlerror());
{% endraw %}

```