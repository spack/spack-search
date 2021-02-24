---
name: "binutils"
layout: package
next_package: podio
previous_package: ucx
library_name: dlopen
matches: ['dlsym', 'dlopen']
languages: ['c', 'cpp']
---
## 2.32
62 / 22031 files match, 17 filtered matches.

 - [include/aout/sun4.h](#includeaoutsun4h)
 - [bfd/elf32-frv.c](#bfdelf32-frvc)
 - [bfd/elf64-ppc.c](#bfdelf64-ppcc)
 - [bfd/plugin.c](#bfdpluginc)
 - [intl/libgnuintl.h](#intllibgnuintlh)
 - [gold/layout.cc](#goldlayoutcc)
 - [gold/options.h](#goldoptionsh)
 - [gold/plugin.cc](#goldplugincc)
 - [gold/testsuite/ifuncmain3.c](#goldtestsuiteifuncmain3c)
 - [ld/lexsup.c](#ldlexsupc)
 - [ld/plugin.c](#ldpluginc)
 - [ld/testsuite/ld-elf/dl1main.c](#ldtestsuiteld-elfdl1mainc)
 - [ld/testsuite/ld-elf/dl6dmain.c](#ldtestsuiteld-elfdl6dmainc)
 - [ld/testsuite/ld-elf/dl6bmain.c](#ldtestsuiteld-elfdl6bmainc)
 - [ld/testsuite/ld-elf/dl6amain.c](#ldtestsuiteld-elfdl6amainc)
 - [ld/testsuite/ld-elf/dl6cmain.c](#ldtestsuiteld-elfdl6cmainc)
 - [ld/testsuite/ld-elf/pr21964-2c.c](#ldtestsuiteld-elfpr21964-2cc)

### include/aout/sun4.h

```c

{% raw %}
87 | struct internal_sun4_dynamic_link
88 | {
89 |   /* Linked list of loaded objects.  This is filled in at runtime by
90 |      ld.so and probably by dlopen.  */
91 |   unsigned long ld_loaded;
92 | 
{% endraw %}

```
### bfd/elf32-frv.c

```c

{% raw %}
4470 |   entry->relocstlsoff += l;
4471 | 
4472 |   /* If there's any TLSOFF relocation, mark the output file as not
4473 |      suitable for dlopening.  This mark will remain even if we relax
4474 |      all such relocations, but this is not a problem, since we'll only
4475 |      do so for executables, and we definitely don't want anyone
4476 |      dlopening executables.  */
4477 |   if (entry->relocstlsoff)
4478 |     dinfo->info->flags |= DF_STATIC_TLS;
5647 |     return TRUE;
5648 | 
5649 |   /* We can only relax when linking the main executable or a library
5650 |      that can't be dlopened.  */
5651 |   if (! bfd_link_executable (info) && ! (info->flags & DF_STATIC_TLS))
5652 |     return TRUE;
{% endraw %}

```
### bfd/elf64-ppc.c

```c

{% raw %}
7232 |      work than the pthread implementation.  __pthread_condattr_destroy
7233 |      is one such symbol: the libpthread.so implementation is
7234 |      localentry:0 while the libc.so implementation is localentry:8.
7235 |      An app that "cleverly" uses dlopen to only load necessary
7236 |      libraries at runtime may omit loading libpthread.so when not
7237 |      running multi-threaded, which then results in the libc.so
{% endraw %}

```
### bfd/plugin.c

```c

{% raw %}
42 | #define RTLD_NOW 0      /* Dummy value.  */
43 | 
44 | static void *
45 | dlopen (const char *file, int mode ATTRIBUTE_UNUSED)
46 | {
47 |   return LoadLibrary (file);
239 | 
240 |   *has_plugin_p = 0;
241 | 
242 |   plugin_handle = dlopen (pname, RTLD_NOW);
243 |   if (!plugin_handle)
244 |     {
{% endraw %}

```
### intl/libgnuintl.h

```c

{% raw %}
72 |      2. in the shared libraries specified on the link command line, in order,
73 |      3. in the dependencies of the shared libraries specified on the link
74 |         command line,
75 |      4. in the dlopen()ed shared libraries, in the order in which they were
76 |         dlopen()ed.
77 |    The definition in the C library would override the one in libintl.so if
78 |    either
{% endraw %}

```
### gold/layout.cc

```cpp

{% raw %}
5337 |     flags |= elfcpp::DF_1_NODEFLIB;
5338 |   if (parameters->options().nodelete())
5339 |     flags |= elfcpp::DF_1_NODELETE;
5340 |   if (parameters->options().nodlopen())
5341 |     flags |= elfcpp::DF_1_NOOPEN;
5342 |   if (parameters->options().nodump())
{% endraw %}

```
### gold/options.h

```c

{% raw %}
1480 |   DEFINE_bool(nodelete, options::DASH_Z, '\0', false,
1481 | 	      N_("Mark DSO non-deletable at runtime"),
1482 | 	      NULL);
1483 |   DEFINE_bool(nodlopen, options::DASH_Z, '\0', false,
1484 | 	      N_("Mark DSO not available to dlopen"),
1485 | 	      NULL);
1486 |   DEFINE_bool(nodump, options::DASH_Z, '\0', false,
{% endraw %}

```
### gold/plugin.cc

```cpp

{% raw %}
44 | 
45 | #define RTLD_NOW 0      /* Dummy value.  */
46 | static void *
47 | dlopen(const char *file, int mode ATTRIBUTE_UNUSED)
48 | {
49 |   return LoadLibrary(file);
195 | #ifdef ENABLE_PLUGINS
196 |   // Load the plugin library.
197 |   // FIXME: Look for the library in standard locations.
198 |   this->handle_ = dlopen(this->filename_.c_str(), RTLD_NOW);
199 |   if (this->handle_ == NULL)
200 |     {
{% endraw %}

```
### gold/testsuite/ifuncmain3.c

```c

{% raw %}
42 |   foo_p (*f) (void);
43 |   int *ret;
44 | 
45 |   void *h = dlopen ("ifuncmod3.so", RTLD_LAZY);
46 |   if (h == NULL)
47 |     {
{% endraw %}

```
### ld/lexsup.c

```c

{% raw %}
1776 |   fprintf (file, _("\
1777 |   -z nodelete                 Mark DSO non-deletable at runtime\n"));
1778 |   fprintf (file, _("\
1779 |   -z nodlopen                 Mark DSO not available to dlopen\n"));
1780 |   fprintf (file, _("\
1781 |   -z nodump                   Mark DSO not available to dldump\n"));
{% endraw %}

```
### ld/plugin.c

```c

{% raw %}
180 | #define RTLD_NOW 0	/* Dummy value.  */
181 | 
182 | static void *
183 | dlopen (const char *file, int mode ATTRIBUTE_UNUSED)
184 | {
185 |   return LoadLibrary (file);
240 |   newplug = xmalloc (sizeof *newplug);
241 |   memset (newplug, 0, sizeof *newplug);
242 |   newplug->name = plugin;
243 |   newplug->dlhandle = dlopen (plugin, RTLD_NOW);
244 |   if (!newplug->dlhandle)
245 |     einfo (_("%F%P: %s: error loading plugin: %s\n"), plugin, dlerror ());
{% endraw %}

```
### ld/testsuite/ld-elf/dl1main.c

```c

{% raw %}
9 |   void *handle;
10 |   void (*fcn) (void);
11 | 
12 |   handle = dlopen("./tmpdir/libdl1.so", RTLD_GLOBAL|RTLD_LAZY);
13 |   if (!handle)
14 |     {
15 |       printf("dlopen ./tmpdir/libdl1.so: %s\n", dlerror ());
16 |       return 1;
17 |     }
{% endraw %}

```
### ld/testsuite/ld-elf/dl6dmain.c

```c

{% raw %}
9 |   void *handle;
10 |   void (*fcn) (void);
11 | 
12 |   handle = dlopen("./tmpdir/libdl6d.so", RTLD_GLOBAL|RTLD_LAZY);
13 |   if (!handle)
14 |     {
15 |       printf("dlopen ./tmpdir/libdl6d.so: %s\n", dlerror ());
16 |       return 1;
17 |     }
{% endraw %}

```
### ld/testsuite/ld-elf/dl6bmain.c

```c

{% raw %}
9 |   void *handle;
10 |   void (*fcn) (void);
11 | 
12 |   handle = dlopen("./tmpdir/libdl6b.so", RTLD_GLOBAL|RTLD_LAZY);
13 |   if (!handle)
14 |     {
15 |       printf("dlopen ./tmpdir/libdl6b.so: %s\n", dlerror ());
16 |       return 1;
17 |     }
{% endraw %}

```
### ld/testsuite/ld-elf/dl6amain.c

```c

{% raw %}
9 |   void *handle;
10 |   void (*fcn) (void);
11 | 
12 |   handle = dlopen("./tmpdir/libdl6a.so", RTLD_GLOBAL|RTLD_LAZY);
13 |   if (!handle)
14 |     {
15 |       printf("dlopen ./tmpdir/libdl6a.so: %s\n", dlerror ());
16 |       return 1;
17 |     }
{% endraw %}

```
### ld/testsuite/ld-elf/dl6cmain.c

```c

{% raw %}
9 |   void *handle;
10 |   void (*fcn) (void);
11 | 
12 |   handle = dlopen("./tmpdir/libdl6c.so", RTLD_GLOBAL|RTLD_LAZY);
13 |   if (!handle)
14 |     {
15 |       printf("dlopen ./tmpdir/libdl6c.so: %s\n", dlerror ());
16 |       return 1;
17 |     }
{% endraw %}

```
### ld/testsuite/ld-elf/pr21964-2c.c

```c

{% raw %}
11 |   if (foo1 () != 0)
12 |     return 1;
13 | 
14 |   dl = dlopen("pr21964-2b.so", RTLD_LAZY);
15 |   if (!dl)
16 |     return 2;
{% endraw %}

```