---
name: "openmc"
layout: package
next_package: libszip
previous_package: graphicsmagick
languages: ['cpp', 'python']
---
## develop
9 / 2160 files match

 - [src/source.cpp](#srcsourcecpp)
 - [include/openmc/source.h](#includeopenmcsourceh)
 - [tests/unit_tests/test_source.py](#testsunit_teststest_sourcepy)
 - [tests/regression_tests/source_parameterized_dlopen/test.py](#testsregression_testssource_parameterized_dlopentestpy)
 - [tests/regression_tests/source_parameterized_dlopen/parameterized_source_sampling.cpp](#testsregression_testssource_parameterized_dlopenparameterized_source_samplingcpp)
 - [tests/regression_tests/source_dlopen/test.py](#testsregression_testssource_dlopentestpy)
 - [tests/regression_tests/source_dlopen/source_sampling.cpp](#testsregression_testssource_dlopensource_samplingcpp)
 - [examples/custom_source/source_ring.cpp](#examplescustom_sourcesource_ringcpp)
 - [examples/parameterized_custom_source/parameterized_source_ring.cpp](#examplesparameterized_custom_sourceparameterized_source_ringcpp)

### src/source.cpp

```

{% raw %}
10 | #include <dlfcn.h> // for dlopen, dlsym, dlclose, dlerror
279 |   shared_library_ = dlopen(path.c_str(), RTLD_LAZY);
{% endraw %}

```
### include/openmc/source.h

```cpp

{% raw %}
110 |   void* shared_library_; //!< library from dlopen
{% endraw %}

```
### tests/unit_tests/test_source.py

```python

{% raw %}
37 | def test_source_dlopen():
{% endraw %}

```
### tests/regression_tests/source_parameterized_dlopen/test.py

```python

{% raw %}
72 | def test_dlopen_source(compile_source, model):
{% endraw %}

```
### tests/regression_tests/source_parameterized_dlopen/parameterized_source_sampling.cpp

```

{% raw %}
31 | // via a plugin call using dlopen/dlsym.
32 | // You must have external C linkage here otherwise dlopen will not find the file
{% endraw %}

```
### tests/regression_tests/source_dlopen/test.py

```python

{% raw %}
71 | def test_dlopen_source(compile_source, model):
{% endraw %}

```
### tests/regression_tests/source_dlopen/source_sampling.cpp

```

{% raw %}
29 | // via a plugin call using dlopen/dlsym.
30 | // You must have external C linkage here otherwise dlopen will not find the file
{% endraw %}

```
### examples/custom_source/source_ring.cpp

```

{% raw %}
30 | // via a plugin call using dlopen/dlsym.
31 | // You must have external C linkage here otherwise dlopen will not find the file
{% endraw %}

```
### examples/parameterized_custom_source/parameterized_source_ring.cpp

```

{% raw %}
59 | // via a plugin call using dlopen/dlsym.
60 | // You must have external C linkage here otherwise dlopen will not find the file
{% endraw %}

```