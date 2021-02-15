---
name: "dimemas"
layout: package
next_package: libffs
previous_package: libbeagle
languages: ['cpp']
---
## 5.4.1
3 / 244 files match

 - [configure.ac](#configureac)
 - [Simulator/model/communic.c](#simulatormodelcommunicc)
 - [m4/ltoptions.m4](#m4ltoptionsm4)

### configure.ac

```

{% raw %}
248 | AC_CHECK_LIB([dl],[dlopen])
{% endraw %}

```
### Simulator/model/communic.c

```cpp

{% raw %}
322 |         external_comm_library = dlopen(external_comm_library_name, RTLD_LAZY);
{% endraw %}

```
### m4/ltoptions.m4

```

{% raw %}
70 |   _LT_UNLESS_OPTIONS([LT_INIT], [dlopen], [enable_dlopen=no
107 | # dlopen
109 | LT_OPTION_DEFINE([LT_INIT], [dlopen], [enable_dlopen=yes
112 | AU_DEFUN([AC_LIBTOOL_DLOPEN],
113 | [_LT_SET_OPTION([LT_INIT], [dlopen])
116 | put the 'dlopen' option into LT_INIT's first parameter.])
120 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN], [])
{% endraw %}

```