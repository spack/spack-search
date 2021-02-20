---
name: "graphicsmagick"
layout: package
next_package: graphviz
previous_package: grafana
languages: ['c']
---
## 1.3.31
16 / 1293 files match, 2 filtered matches.

 - [magick/module.c](#magickmodulec)
 - [magick/nt_base.c](#magicknt_basec)

### magick/module.c

```c

{% raw %}
374 |       return(MagickFail);
375 | 
376 |     /* Open the module */
377 |     handle=lt_dlopen(module_path);
378 |     if (handle == (ModuleHandle) NULL)
379 |       {
1404 |     (void) LogMagickEvent(ConfigureEvent,GetMagickModule(),
1405 |       "Opening module at path \"%s\" ...", path);
1406 | 
1407 |     handle=lt_dlopen(path);
1408 |     if (handle == (ModuleHandle) NULL)
1409 |       {
{% endraw %}

```
### magick/nt_base.c

```c

{% raw %}
765 | %                                                                             %
766 | %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
767 | %
768 | %   Method NTdlopen loads a dynamic module into memory and returns a handle
769 | %   that can be used to access the various procedures in the module.
770 | %
771 | %  The format of the NTdlopen method is:
772 | %
773 | %      void *NTdlopen(const char *filename)
774 | %
775 | %  A description of each parameter follows:
778 | %            is to be loaded.
779 | %
780 | */
781 | MagickExport void *NTdlopen(const char *filename)
782 | {
783 | #define MaxPathElements  31
1741 |   if (!NTGhostscriptDLL(dll_path,sizeof(dll_path)))
1742 |     return False;
1743 | 
1744 |   gs_dll_handle = lt_dlopen(dll_path);
1745 |   if (gs_dll_handle == (void *) NULL)
1746 |     return False;
{% endraw %}

```