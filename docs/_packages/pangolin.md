---
name: "pangolin"
layout: package
next_package: bcftools
previous_package: libxevie
languages: ['cmake']
---
## master
2 / 429 files match

 - [src/display/device/display_android.cpp](#srcdisplaydevicedisplay_androidcpp)
 - [CMakeModules/AndroidUtils.cmake](#cmakemodulesandroidutilscmake)

### src/display/device/display_android.cpp

```

{% raw %}
686 |     *(void **) (&main) = dlsym( dlopen(android_app->application_so, RTLD_NOW), "main");
{% endraw %}

```
### CMakeModules/AndroidUtils.cmake

```cmake

{% raw %}
77 |     void * handle = dlopen(l, RTLD_NOW | RTLD_GLOBAL);
78 |     if (!handle) LOGE( \"dlopen('%s'): %s\", l, strerror(errno) );
{% endraw %}

```