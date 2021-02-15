---
name: "openscenegraph"
layout: package
next_package: libuser
previous_package: libxxf86misc
languages: []
---
## 3.2.3
2 / 2623 files match

 - [src/osg/GLExtensions.cpp](#srcosgglextensionscpp)
 - [src/osgDB/DynamicLibrary.cpp](#srcosgdbdynamiclibrarycpp)

### src/osg/GLExtensions.cpp

```

{% raw %}
37 |     // Since 10.3 (Panther) OS X has provided the dlopen/dlsym/dlclose
323 |             static void *handle = dlopen("libGLESv1_CM.so", RTLD_NOW);
325 |             static void *handle = dlopen("libGLESv2.so", RTLD_NOW);
364 |             static void *handle = dlopen((const char *)0L, RTLD_LAZY);
370 |         static void *handle = dlopen((const char *)0L, RTLD_LAZY);
375 |         static void *handle = dlopen((const char *)0L, RTLD_LAZY);
{% endraw %}

```
### src/osgDB/DynamicLibrary.cpp

```

{% raw %}
13 | //The dlopen calls were not adding to OS X until 10.3
30 | // Although HP-UX has dlopen() it is broken! We therefore need to stick
115 |     // dlopen will not work with files in the current directory unless
123 |     handle = dlopen( localLibraryName.c_str(), RTLD_LAZY | RTLD_GLOBAL);
{% endraw %}

```