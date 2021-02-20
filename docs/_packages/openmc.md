---
name: "openmc"
layout: package
next_package: openmolcas
previous_package: openloops
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
107 | 
108 |   double strength() const override { return custom_source_->strength(); }
109 | private:
110 |   void* shared_library_; //!< library from dlopen
111 |   std::unique_ptr<Source> custom_source_;
112 | };
{% endraw %}

```
### tests/unit_tests/test_source.py

```python

{% raw %}
34 |     assert 'strength' in elem.attrib
35 |     assert 'file' in elem.attrib
36 | 
37 | def test_source_dlopen():
38 |     library = './libsource.so'
39 |     src = openmc.Source(library=library)
{% endraw %}

```
### tests/regression_tests/source_parameterized_dlopen/test.py

```python

{% raw %}
69 |     return model
70 | 
71 | 
72 | def test_dlopen_source(compile_source, model):
73 |     harness = PyAPITestHarness('statepoint.10.h5', model)
74 |     harness.main()
{% endraw %}

```
### tests/regression_tests/source_dlopen/test.py

```python

{% raw %}
68 |     return model
69 | 
70 | 
71 | def test_dlopen_source(compile_source, model):
72 |     harness = PyAPITestHarness('statepoint.10.h5', model)
73 |     harness.main()
{% endraw %}

```