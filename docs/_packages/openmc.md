---
name: "openmc"
layout: package
next_package: openmpi
previous_package: openldap
languages: ['python', 'c']
---
## develop
9 / 2160 files match, 4 filtered matches.

 - [include/openmc/source.h](#includeopenmcsourceh)
 - [tests/unit_tests/test_source.py](#testsunit_teststest_sourcepy)
 - [tests/regression_tests/source_parameterized_dlopen/test.py](#testsregression_testssource_parameterized_dlopentestpy)
 - [tests/regression_tests/source_dlopen/test.py](#testsregression_testssource_dlopentestpy)

### include/openmc/source.h

```c

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
### tests/regression_tests/source_dlopen/test.py

```python

{% raw %}
71 | def test_dlopen_source(compile_source, model):
{% endraw %}

```