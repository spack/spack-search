---
name: "rivet"
layout: package
next_package: rocfft
previous_package: redis
languages: ['cpp', 'python']
---
## 2.2.0
5 / 1528 files match, 2 filtered matches.

 - [src/Core/AnalysisLoader.cc](#srccoreanalysisloadercc)
 - [pyext/rivet/__init__.py](#pyextrivet__init__py)

### src/Core/AnalysisLoader.cc

```cpp

{% raw %}
104 |       void* handle = dlopen(pf.c_str(), RTLD_LAZY);
{% endraw %}

```
### pyext/rivet/__init__.py

```python

{% raw %}
3 |     sys.setdlopenflags(sys.getdlopenflags() | ctypes.RTLD_GLOBAL)
7 |     sys.setdlopenflags(sys.getdlopenflags() | dl.RTLD_GLOBAL)
{% endraw %}

```