---
name: "py-jpype1"
layout: package
next_package: launchmon
previous_package: py-networkit
languages: ['cpp']
---
## 0.6.0
2 / 193 files match

 - [native/common/include/jp_platform_linux.h](#nativecommonincludejp_platform_linuxh)
 - [examples/linux/README.TXT](#exampleslinuxreadmetxt)

### native/common/include/jp_platform_linux.h

```cpp

{% raw %}
37 | 		jvmLibrary = dlopen(path, RTLD_LAZY|RTLD_GLOBAL);
{% endraw %}

```
### examples/linux/README.TXT

```

{% raw %}
4 | Unfortunately, dlopen() will ignore any changes made to the LD_LIBRARY_PATH in the current process.
13 | To learn more about the dlopen problem, you can look at :
{% endraw %}

```