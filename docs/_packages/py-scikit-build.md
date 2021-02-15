---
name: "py-scikit-build"
layout: package
next_package: py-soundfile
previous_package: py-matplotlib
languages: ['cmake']
---
## 0.10.0
1 / 224 files match

 - [skbuild/resources/cmake/targetLinkLibrariesWithDynamicLookup.cmake](#skbuildresourcescmaketargetlinklibrarieswithdynamiclookupcmake)

### skbuild/resources/cmake/targetLinkLibrariesWithDynamicLookup.cmake

```cmake

{% raw %}
342 |         counter_module = dlopen(\"./counter.so\", RTLD_LAZY | RTLD_GLOBAL);
{% endraw %}

```