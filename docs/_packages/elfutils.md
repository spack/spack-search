---
name: "elfutils"
layout: package
next_package: expat
previous_package: fastdb
languages: ['cpp', 'bash']
---
## 0.180
9 / 1398 files match

 - [elfutils.spec](#elfutilsspec)
 - [libelf/elf.h](#libelfelfh)
 - [config/elfutils.spec.in](#configelfutilsspecin)
 - [src/elfclassify.c](#srcelfclassifyc)
 - [tests/run-debuginfod-find.sh](#testsrun-debuginfod-findsh)
 - [po/uk.po](#poukpo)
 - [po/es.po](#poespo)
 - [po/ja.po](#pojapo)
 - [libdwfl/debuginfod-client.c](#libdwfldebuginfod-clientc)

### elfutils.spec

```

{% raw %}
367 |             through dlopen, but are now compiled into libdw.so directly.
{% endraw %}

```
### libelf/elf.h

```cpp

{% raw %}
1958 | 					   by rld on dlopen() calls.  */
{% endraw %}

```
### config/elfutils.spec.in

```

{% raw %}
367 |             through dlopen, but are now compiled into libdw.so directly.
{% endraw %}

```
### src/elfclassify.c

```cpp

{% raw %}
604 |      can dlopen it just fine.  */
{% endraw %}

```
### tests/run-debuginfod-find.sh

```bash

{% raw %}
135 | # Test whether elfutils, via the debuginfod client library dlopen hooks,
{% endraw %}

```
### po/uk.po

```

{% raw %}
7322 | #~ msgid "Mark object as not loadable with 'dlopen'."
7324 | #~ "Позначити об’єкт, як непридатний для завантаження за допомогою «dlopen»."
{% endraw %}

```
### po/es.po

```

{% raw %}
7283 | #~ msgid "Mark object as not loadable with 'dlopen'."
7284 | #~ msgstr "Marcar el objeto como no cargable con 'dlopen'"
{% endraw %}

```
### po/ja.po

```

{% raw %}
6956 | #~ msgid "Mark object as not loadable with 'dlopen'."
6957 | #~ msgstr "'dlopen' でロードできないと記します。"
{% endraw %}

```
### libdwfl/debuginfod-client.c

```cpp

{% raw %}
103 |   void *debuginfod_so = dlopen("libdebuginfod-" VERSION ".so", RTLD_LAZY);
106 |     debuginfod_so = dlopen("libdebuginfod.so", RTLD_LAZY);
{% endraw %}

```