---
name: "blast-legacy"
layout: package
next_package: bloaty
previous_package: bison
languages: ['c']
---
## 2.2.26
1 / 3030 files match, 1 filtered matches.

 - [network/medarch/server/ma_intfc.c](#networkmedarchserverma_intfcc)

### network/medarch/server/ma_intfc.c

```c

{% raw %}
310 |     /* Open the library */
311 | 
312 |     if( handler->load_path != NULL ) {
313 | 	handler->handle = dlopen( handler->load_path, RTLD_LAZY );
314 | 	if( handler->handle == NULL ) goto err;
315 | 
{% endraw %}

```