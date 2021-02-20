---
name: "ferret"
layout: package
next_package: ffmpeg
previous_package: fermisciencetools
languages: ['c']
---
## 7.6.0
2 / 5578 files match, 1 filtered matches.

 - [fer/ccr/EF_InternalUtil.c](#ferccref_internalutilc)

### fer/ccr/EF_InternalUtil.c

```c

{% raw %}
1661 |         }
1662 |         strcpy(libname, fer_dir);
1663 |         strcat(libname, "/libpyefcn.so");
1664 |         pyefcn_handle = dlopen(libname, RTLD_LAZY);
1665 |         if ( pyefcn_handle == NULL ) {
1666 |             sprintf(errstring, "Python-backed external functions not supported \n"
1809 |       strcat(tempText, ef_ptr->name);
1810 |       strcat(tempText, ".so");
1811 | 
1812 |       if ( (ef_ptr->handle = dlopen(tempText, RTLD_LAZY)) == NULL ) {
1813 |          fprintf(stderr, "**ERROR in External Function %s:\n"
1814 |                          "  Dynamic linking call dlopen() returns --\n"
1815 |                          "  \"%s\".\n", ef_ptr->name, dlerror());
1816 |          return -1;
{% endraw %}

```