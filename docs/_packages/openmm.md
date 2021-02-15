---
name: "openmm"
layout: package
next_package: llvm-amdgpu
previous_package: m4
languages: ['cpp']
---
## 7.4.1
2 / 1666 files match

 - [libraries/pthreads/include/pthread.h](#librariespthreadsincludepthreadh)
 - [olla/src/Platform.cpp](#ollasrcplatformcpp)

### libraries/pthreads/include/pthread.h

```cpp

{% raw %}
1469 | #define dlopen(...) (pthread_testcancel(), dlopen(__VA_ARGS__))
{% endraw %}

```
### olla/src/Platform.cpp

```

{% raw %}
224 |     void *handle = dlopen(file.c_str(), RTLD_LAZY | RTLD_GLOBAL);
{% endraw %}

```