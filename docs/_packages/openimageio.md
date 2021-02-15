---
name: "openimageio"
layout: package
next_package: nfft
previous_package: assimp
languages: []
---
## 2.2.7.0
2 / 1143 files match

 - [CHANGES.md](#changesmd)
 - [src/libutil/plugin.cpp](#srclibutilplugincpp)

### CHANGES.md

```

{% raw %}
1904 | * Fixes for Windows when making Unicode builds, and fix Plugin::dlopen
{% endraw %}

```
### src/libutil/plugin.cpp

```

{% raw %}
48 | dlopen(const char* plugin_filename, int)
97 |     Handle h = dlopen(plugin_filename, mode);
{% endraw %}

```