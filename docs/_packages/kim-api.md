---
name: "kim-api"
layout: package
next_package: py-pynacl
previous_package: meme
languages: []
---
## 2.1.0
2 / 341 files match

 - [utils/shared-library-test.cpp](#utilsshared-library-testcpp)
 - [cpp/src/KIM_SharedLibrary.cpp](#cppsrckim_sharedlibrarycpp)

### utils/shared-library-test.cpp

```

{% raw %}
77 |     void * sharedLibraryHandle = dlopen(libFilePath.c_str(), RTLD_NOW);
{% endraw %}

```
### cpp/src/KIM_SharedLibrary.cpp

```

{% raw %}
114 |   sharedLibraryHandle_ = dlopen(sharedLibraryName_.c_str(), RTLD_NOW);
{% endraw %}

```