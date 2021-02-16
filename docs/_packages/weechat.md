---
name: "weechat"
layout: package
next_package: lksctp-tools
previous_package: llvm-openmp-ompt
languages: ['c']
---
## 2.9
4 / 761 files match

 - [src/plugins/weechat-plugin.h](#srcpluginsweechat-pluginh)
 - [src/plugins/plugin.c](#srcpluginspluginc)

### src/plugins/weechat-plugin.h

```c

{% raw %}
253 |     void *handle;                      /* handle of plugin (given by dlopen)*/
{% endraw %}

```
### src/plugins/plugin.c

```c

{% raw %}
414 |     handle = dlopen (filename, RTLD_GLOBAL | RTLD_NOW);
{% endraw %}

```