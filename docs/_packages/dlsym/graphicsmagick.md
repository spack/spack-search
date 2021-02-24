---
name: "graphicsmagick"
layout: package
next_package: unifyfs
previous_package: mivisionx
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 1.3.31
10 / 1293 files match, 2 filtered matches.

 - [magick/module.c](#magickmodulec)
 - [magick/nt_base.c](#magicknt_basec)

### magick/module.c

```c

{% raw %}
400 |     FormatString(method_name,"%.64sImage",tag);
401 | #endif
402 |     method=(unsigned int (*)(Image **,const int,char **))
403 |       lt_dlsym(handle,method_name);
404 | 
405 |     (void) LogMagickEvent(CoderEvent,GetMagickModule(),
1428 |       Locate and record RegisterFORMATImage function
1429 |     */
1430 |     TagToFunctionName(module_name,"Register%sImage",name);
1431 |     coder_info->register_function=(void (*)(void)) lt_dlsym(handle,name);
1432 |     if (coder_info->register_function == (void (*)(void)) NULL)
1433 |       {
1445 |       Locate and record UnregisterFORMATImage function
1446 |     */
1447 |     TagToFunctionName(module_name,"Unregister%sImage",name);
1448 |     coder_info->unregister_function=(void (*)(void)) lt_dlsym(handle,name);
1449 |     if (coder_info->unregister_function == (void (*)(void)) NULL)
1450 |       {
2038 | %  TagToFunctionName() formats the module tag name to a string using the
2039 | %  upper-case tag name as the input string, and a user-provided format.
2040 | %  This function is used to prepare the RegisterTAGImage and UnregisterTAGImage
2041 | %  function names passed lt_dlsym.
2042 | %
2043 | %  The format of the TagToFunctionName method is:
{% endraw %}

```
### magick/nt_base.c

```c

{% raw %}
889 | %                                                                             %
890 | %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
891 | %
892 | %   Method NTdlsym retrieve the procedure address of the procedure specified
893 | %   by the passed character string.
894 | %
895 | %  The format of the NTdlsym method is:
896 | %
897 | %      void *NTdlsym(void *handle,const char *name)
898 | %
899 | %  A description of each parameter follows:
903 | %    o name: Specifies the procedure entry point to be returned.
904 | %
905 | */
906 | MagickExport void *NTdlsym(void *handle,const char *name)
907 | {
908 |   LPFNDLLFUNC1
1748 |   memset((void*)&gs_vectors, 0, sizeof(GhostscriptVectors));
1749 | 
1750 |   gs_vectors.exit=(int (MagickDLLCall *)(gs_main_instance*))
1751 |     lt_dlsym(gs_dll_handle,"gsapi_exit");
1752 |   gs_vectors.init_with_args=(int (MagickDLLCall *)(gs_main_instance *, int, char **))
1753 |     (lt_dlsym(gs_dll_handle,"gsapi_init_with_args"));
1754 |   gs_vectors.new_instance=(int (MagickDLLCall *)(gs_main_instance **, void *))
1755 |     (lt_dlsym(gs_dll_handle,"gsapi_new_instance"));
1756 |   gs_vectors.run_string=(int (MagickDLLCall *)(gs_main_instance *, const char *, int, int *))
1757 |     (lt_dlsym(gs_dll_handle,"gsapi_run_string"));
1758 |   gs_vectors.delete_instance=(void (MagickDLLCall *)(gs_main_instance *))
1759 |     (lt_dlsym(gs_dll_handle,"gsapi_delete_instance"));
1760 | 
1761 |   if ((gs_vectors.exit==NULL) ||
{% endraw %}

```