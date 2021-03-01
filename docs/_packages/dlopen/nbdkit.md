---
name: "nbdkit"
layout: package
next_package: nccl
previous_package: mysql
library_name: dlopen
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 1.23.7
8 / 763 files match, 3 filtered matches.

 - [server/main.c](#servermainc)
 - [plugins/vddk/vddk.c](#pluginsvddkvddkc)
 - [plugins/cc/cc.c](#pluginsccccc)

### server/main.c

```c

{% raw %}
805 |     free_filename = true;
806 |   }
807 | 
808 |   dl = dlopen (filename, RTLD_NOW|RTLD_GLOBAL);
809 |   if (dl == NULL) {
810 |     fprintf (stderr,
858 |     free_filename = true;
859 |   }
860 | 
861 |   dl = dlopen (filename, RTLD_NOW|RTLD_GLOBAL);
862 |   if (dl == NULL) {
863 |     fprintf (stderr, "%s: error: cannot open filter '%s': %s\n",
{% endraw %}

```
### plugins/vddk/vddk.c

```c

{% raw %}
73 | #define VDDK_MAJOR 5
74 | #define VDDK_MINOR 5
75 | 
76 | static void *dl;                           /* dlopen handle */
77 | static bool init_called;                   /* was InitEx called */
78 | static __thread int error_suppression;     /* threadlocal error suppression */
318 |       exit (EXIT_FAILURE);
319 |     }
320 | 
321 |     dl = dlopen (path, RTLD_NOW);
322 |     if (dl != NULL) {
323 |       /* Now that we found the library, ensure that LD_LIBRARY_PATH
{% endraw %}

```
### plugins/cc/cc.c

```c

{% raw %}
231 |   }
232 | 
233 |   /* Load the subplugin. */
234 |   dl = dlopen (tmpfile, RTLD_NOW);
235 |   unlink (tmpfile);
236 |   if (dl == NULL) {
{% endraw %}

```