---
name: "gettext"
layout: package
next_package: gflags
previous_package: geopm
library_name: dlopen
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 0.20.1
22 / 5109 files match, 4 filtered matches.

 - [gettext-runtime/intl/libgnuintl.in.h](#gettext-runtimeintllibgnuintlinh)
 - [gettext-tools/gnulib-lib/libxml/xmlmodule.c](#gettext-toolsgnulib-liblibxmlxmlmodulec)
 - [gnulib-local/lib/libxml/xmlmodule.c](#gnulib-localliblibxmlxmlmodulec)
 - [libtextstyle/lib/libxml/xmlmodule.c](#libtextstyleliblibxmlxmlmodulec)

### gettext-runtime/intl/libgnuintl.in.h

```c

{% raw %}
68 |      2. in the shared libraries specified on the link command line, in order,
69 |      3. in the dependencies of the shared libraries specified on the link
70 |         command line,
71 |      4. in the dlopen()ed shared libraries, in the order in which they were
72 |         dlopen()ed.
73 |    The definition in the C library would override the one in libintl.so if
74 |    either
{% endraw %}

```
### gettext-tools/gnulib-lib/libxml/xmlmodule.c

```c

{% raw %}
221 | static void *
222 | xmlModulePlatformOpen(const char *name)
223 | {
224 |     return dlopen(name, RTLD_GLOBAL | RTLD_NOW);
225 | }
226 | 
{% endraw %}

```
### gnulib-local/lib/libxml/xmlmodule.c

```c

{% raw %}
221 | static void *
222 | xmlModulePlatformOpen(const char *name)
223 | {
224 |     return dlopen(name, RTLD_GLOBAL | RTLD_NOW);
225 | }
226 | 
{% endraw %}

```
### libtextstyle/lib/libxml/xmlmodule.c

```c

{% raw %}
221 | static void *
222 | xmlModulePlatformOpen(const char *name)
223 | {
224 |     return dlopen(name, RTLD_GLOBAL | RTLD_NOW);
225 | }
226 | 
{% endraw %}

```