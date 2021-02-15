---
name: "py-pyjnius"
layout: package
next_package: mpip
previous_package: liblbxutil
languages: ['python']
---
## 1.3.0.0
4 / 32 files match

 - [setup.py](#setuppy)
 - [jnius/jnius_jvm_dlopen.pxi](#jniusjnius_jvm_dlopenpxi)
 - [jnius/jnius.pyx](#jniusjniuspyx)
 - [pyjnius.egg-info/SOURCES.txt](#pyjniusegg-infosourcestxt)

### setup.py

```python

{% raw %}
52 |     'jnius_jvm_dlopen.pxi',
{% endraw %}

```
### jnius/jnius_jvm_dlopen.pxi

```

{% raw %}
11 |     void* dlopen(const char *filename, int flag)
97 |     handle = dlopen(lib_path, RTLD_NOW | RTLD_GLOBAL)
100 |         raise SystemError("Error calling dlopen({0}: {1}".format(lib_path, dlerror()))
{% endraw %}

```
### jnius/jnius.pyx

```

{% raw %}
106 |     include "jnius_jvm_dlopen.pxi"
{% endraw %}

```
### pyjnius.egg-info/SOURCES.txt

```

{% raw %}
18 | jnius/jnius_jvm_dlopen.pxi
{% endraw %}

```