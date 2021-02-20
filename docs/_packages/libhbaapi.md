---
name: "libhbaapi"
layout: package
next_package: libhio
previous_package: libgssglue
languages: ['c']
---
## 3.10
1 / 13 files match, 1 filtered matches.

 - [hbaapilib.c](#hbaapilibc)

### hbaapilib.c

```c

{% raw %}
541 | 	_hbaapi_librarylist = lib_infop;
542 | 
543 | 	/* Load the DLL now */
544 | 	if((lib_infop->hLibrary = dlopen(librarypath,RTLD_LAZY)) == NULL) {
545 | 	    /*printf("unable to load library %s\n", librarypath); */
546 | 	    continue;
1010 |     memset(attributes, 0, sizeof(HBA_LIBRARYATTRIBUTES));
1011 | 
1012 | #if defined(SOLARIS)
1013 |     if((handle = dlopen("libHBAAPI.so", RTLD_NOW)) != NULL) {
1014 | 	if(dlinfo(handle, RTLD_DI_LINKMAP, &map) >= 0) {
1015 | 	    for(mp = map; mp != NULL; mp = mp->l_next) {
{% endraw %}

```