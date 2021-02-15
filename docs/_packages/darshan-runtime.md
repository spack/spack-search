---
name: "darshan-runtime"
layout: package
next_package: gccxml
previous_package: xdm
languages: ['python']
---
## develop
2 / 409 files match

 - [darshan-util/pydarshan/examples/99_darshan-low-level-direct-libdarshanutils-interaction.ipynb](#darshan-utilpydarshanexamples99_darshan-low-level-direct-libdarshanutils-interactionipynb)
 - [darshan-util/pydarshan/darshan/discover_darshan.py](#darshan-utilpydarshandarshandiscover_darshanpy)

### darshan-util/pydarshan/examples/99_darshan-low-level-direct-libdarshanutils-interaction.ipynb

```

{% raw %}
76 |     "libdutil = ffi.dlopen(\"libdarshan-util.so\")"
{% endraw %}

```
### darshan-util/pydarshan/darshan/discover_darshan.py

```python

{% raw %}
138 |     1) Try if the current environment allows dlopen to load libdarshan-util
150 |             libdutil = ffi.dlopen("libdarshan-util.so")
158 |             libdutil = ffi.dlopen(library_path + "/lib/libdarshan-util.so")
166 |             libdutil = ffi.dlopen(library_path + "/lib/libdarshan-util.so")
178 |             libdutil = ffi.dlopen(library_path)
191 |             libdutil = ffi.dlopen(library_path)
{% endraw %}

```