---
name: "rivet"
layout: package
next_package: rocfft
previous_package: rhash
languages: ['cpp', 'python']
---
## 2.2.0
5 / 1528 files match, 2 filtered matches.

 - [src/Core/AnalysisLoader.cc](#srccoreanalysisloadercc)
 - [pyext/rivet/__init__.py](#pyextrivet__init__py)

### src/Core/AnalysisLoader.cc

```cpp

{% raw %}
101 |     MSG_TRACE("Candidate analysis plugin libs: " << pluginfiles);
102 |     foreach (const string& pf, pluginfiles) {
103 |       MSG_TRACE("Trying to load plugin analyses from file " << pf);
104 |       void* handle = dlopen(pf.c_str(), RTLD_LAZY);
105 |       if (!handle) {
106 |         MSG_WARNING("Cannot open " << pf << ": " << dlerror());
{% endraw %}

```
### pyext/rivet/__init__.py

```python

{% raw %}
1 | try:
2 |     import ctypes
3 |     sys.setdlopenflags(sys.getdlopenflags() | ctypes.RTLD_GLOBAL)
4 |     del ctypes
5 | except:
6 |     import dl
7 |     sys.setdlopenflags(sys.getdlopenflags() | dl.RTLD_GLOBAL)
8 |     del dl
9 | del sys
{% endraw %}

```