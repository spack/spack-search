---
name: "g2o"
layout: package
next_package: genometools
previous_package: qnnpack
languages: ['cpp']
---
## 20200410_git
2 / 695 files match

 - [g2o/core/optimization_algorithm_factory.h](#g2ocoreoptimization_algorithm_factoryh)
 - [g2o/apps/g2o_cli/dl_wrapper.cpp](#g2oappsg2o_clidl_wrappercpp)

### g2o/core/optimization_algorithm_factory.h

```cpp

{% raw %}
154 |  * it via dlopen() (or similar functions) you should indicate
{% endraw %}

```
### g2o/apps/g2o_cli/dl_wrapper.cpp

```

{% raw %}
117 |   void* handle = dlopen(filename.c_str(), RTLD_LAZY);
{% endraw %}

```