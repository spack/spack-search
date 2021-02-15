---
name: "gmsh"
layout: package
next_package: rsync
previous_package: sz
languages: []
---
## 4.4.1
1 / 2450 files match

 - [Plugin/PluginManager.cpp](#pluginpluginmanagercpp)

### Plugin/PluginManager.cpp

```

{% raw %}
71 | #undef HAVE_DLOPEN
73 | #if defined(HAVE_DLOPEN)
321 | #if !defined(HAVE_DLOPEN) || !defined(HAVE_FLTK)
325 |   void *hlib = dlopen(fileName.c_str(), RTLD_NOW);
{% endraw %}

```