---
name: "hunspell"
layout: package
next_package: perl-dbd-sqlite
previous_package: rhash
languages: ['cpp', 'bash']
---
## 1.6.0
3 / 768 files match

 - [tests/test.sh](#teststestsh)
 - [intl/libgnuintl.in.h](#intllibgnuintlinh)
 - [m4/lib-link.m4](#m4lib-linkm4)

### tests/test.sh

```bash

{% raw %}
75 | alias hunspell='../libtool --mode=execute -dlopen ../src/hunspell/.libs/libhunspell*.la ../src/tools/hunspell'
76 | alias analyze='../libtool --mode=execute -dlopen ../src/hunspell/.libs/libhunspell*.la ../src/tools/analyze'
84 |   alias hunspell='../libtool --mode=execute -dlopen ../src/hunspell/.libs/libhunspell*.la valgrind --tool=$VALGRIND --leak-check=yes --show-reachable=yes --log-file=$TEMPDIR/test.pid ../src/tools/hunspell'
85 |   alias analyze='../libtool --mode=execute -dlopen ../src/hunspell/.libs/libhunspell*.la valgrind --tool=$VALGRIND --leak-check=yes --show-reachable=yes --log-file=$TEMPDIR/test.pid ../src/tools/analyze'
{% endraw %}

```
### intl/libgnuintl.in.h

```cpp

{% raw %}
72 |      4. in the dlopen()ed shared libraries, in the order in which they were
73 |         dlopen()ed.
78 |      * libintl.so is a dependency of a dlopen()ed shared library but not
{% endraw %}

```
### m4/lib-link.m4

```

{% raw %}
518 |               dnl age, revision, installed, dlopen, dlpreopen, libdir.
{% endraw %}

```