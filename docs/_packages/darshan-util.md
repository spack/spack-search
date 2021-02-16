---
name: "darshan-util"
layout: package
next_package: libvorbis
previous_package: icedtea
languages: ['python']
---
## develop
2 / 409 files match, 1 filtered matches.

 - [darshan-util/pydarshan/darshan/discover_darshan.py](#darshan-utilpydarshandarshandiscover_darshanpy)

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