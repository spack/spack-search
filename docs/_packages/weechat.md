---
name: "weechat"
layout: package
next_package: lksctp-tools
previous_package: llvm-openmp-ompt
languages: ['cpp']
---
## 2.9
4 / 761 files match

 - [configure.ac](#configureac)
 - [src/plugins/weechat-plugin.h](#srcpluginsweechat-pluginh)
 - [src/plugins/plugin.c](#srcpluginspluginc)
 - [tests/tests.cpp](#teststestscpp)

### configure.ac

```

{% raw %}
211 | AC_CHECK_FUNCS(dlopen, LIBDL_FOUND=yes, LIBDL_FOUND=no)
213 |     AC_CHECK_LIB(dl, dlopen, [LIBDL_FOUND=yes; PLUGINS_LFLAGS=-ldl], LIBDL_FOUND=no)
{% endraw %}

```
### src/plugins/weechat-plugin.h

```cpp

{% raw %}
253 |     void *handle;                      /* handle of plugin (given by dlopen)*/
{% endraw %}

```
### src/plugins/plugin.c

```cpp

{% raw %}
414 |     handle = dlopen (filename, RTLD_GLOBAL | RTLD_NOW);
{% endraw %}

```
### tests/tests.cpp

```

{% raw %}
245 |     handle = dlopen (ptr_path, RTLD_GLOBAL | RTLD_NOW);
{% endraw %}

```