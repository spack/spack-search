---
name: "libiberty"
layout: package
next_package: lesstif
previous_package: atk
languages: ['cpp', 'c']
---
## 2.31.1
60 / 21078 files match

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
90 |      ld.so and probably by dlopen.  */
{% endraw %}

```
### bfd/elf32-frv.c

```c

{% raw %}
4473 |      suitable for dlopening.  This mark will remain even if we relax
4476 |      dlopening executables.  */
5650 |      that can't be dlopened.  */
{% endraw %}

```
### bfd/elf64-ppc.c

```c

{% raw %}
8478 |      An app that "cleverly" uses dlopen to only load necessary
{% endraw %}

```
### bfd/plugin.c

```c

{% raw %}
45 | dlopen (const char *file, int mode ATTRIBUTE_UNUSED)
227 |   plugin_handle = dlopen (pname, RTLD_NOW);
{% endraw %}

```
### intl/libgnuintl.h

```c

{% raw %}
75 |      4. in the dlopen()ed shared libraries, in the order in which they were
76 |         dlopen()ed.
{% endraw %}

```
### gold/layout.cc

```cpp

{% raw %}
5340 |   if (parameters->options().nodlopen())
{% endraw %}

```
### gold/options.h

```c

{% raw %}
1479 |   DEFINE_bool(nodlopen, options::DASH_Z, '\0', false,
1480 | 	      N_("Mark DSO not available to dlopen"),
{% endraw %}

```
### gold/plugin.cc

```cpp

{% raw %}
47 | dlopen(const char *file, int mode ATTRIBUTE_UNUSED)
198 |   this->handle_ = dlopen(this->filename_.c_str(), RTLD_NOW);
{% endraw %}

```
### gold/testsuite/ifuncmain3.c

```c

{% raw %}
45 |   void *h = dlopen ("ifuncmod3.so", RTLD_LAZY);
{% endraw %}

```
### ld/lexsup.c

```c

{% raw %}
1779 |   -z nodlopen                 Mark DSO not available to dlopen\n"));
{% endraw %}

```
### ld/plugin.c

```c

{% raw %}
183 | dlopen (const char *file, int mode ATTRIBUTE_UNUSED)
243 |   newplug->dlhandle = dlopen (plugin, RTLD_NOW);
{% endraw %}

```
### ld/testsuite/ld-elf/dl1main.c

```c

{% raw %}
12 |   handle = dlopen("./tmpdir/libdl1.so", RTLD_GLOBAL|RTLD_LAZY);
15 |       printf("dlopen ./tmpdir/libdl1.so: %s\n", dlerror ());
{% endraw %}

```
### ld/testsuite/ld-elf/dl6dmain.c

```c

{% raw %}
12 |   handle = dlopen("./tmpdir/libdl6d.so", RTLD_GLOBAL|RTLD_LAZY);
15 |       printf("dlopen ./tmpdir/libdl6d.so: %s\n", dlerror ());
{% endraw %}

```
### ld/testsuite/ld-elf/dl6bmain.c

```c

{% raw %}
12 |   handle = dlopen("./tmpdir/libdl6b.so", RTLD_GLOBAL|RTLD_LAZY);
15 |       printf("dlopen ./tmpdir/libdl6b.so: %s\n", dlerror ());
{% endraw %}

```
### ld/testsuite/ld-elf/dl6amain.c

```c

{% raw %}
12 |   handle = dlopen("./tmpdir/libdl6a.so", RTLD_GLOBAL|RTLD_LAZY);
15 |       printf("dlopen ./tmpdir/libdl6a.so: %s\n", dlerror ());
{% endraw %}

```
### ld/testsuite/ld-elf/dl6cmain.c

```c

{% raw %}
12 |   handle = dlopen("./tmpdir/libdl6c.so", RTLD_GLOBAL|RTLD_LAZY);
15 |       printf("dlopen ./tmpdir/libdl6c.so: %s\n", dlerror ());
{% endraw %}

```
### ld/testsuite/ld-elf/pr21964-2c.c

```c

{% raw %}
14 |   dl = dlopen("pr21964-2b.so", RTLD_LAZY);
{% endraw %}

```