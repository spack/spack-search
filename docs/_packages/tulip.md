---
name: "tulip"
layout: package
next_package: ppl
previous_package: libsodium
languages: ['python']
---
## 5.4.0
12 / 5173 files match

 - [library/tulip-python/bindings/tulip-core/__init__.py](#librarytulip-pythonbindingstulip-core__init__py)
 - [library/tulip-python/bindings/tulip-gui/__init__.py](#librarytulip-pythonbindingstulip-gui__init__py)

### library/tulip-python/bindings/tulip-core/__init__.py

```python

{% raw %}
163 |     dlOpenFlagsBackup = sys.getdlopenflags()
169 |     sys.setdlopenflags(dlOpenFlags)
180 |     sys.setdlopenflags(dlOpenFlagsBackup)
{% endraw %}

```
### library/tulip-python/bindings/tulip-gui/__init__.py

```python

{% raw %}
75 |     dlOpenFlagsBackup = sys.getdlopenflags()
81 |     sys.setdlopenflags(dlOpenFlags)
87 |     sys.setdlopenflags(dlOpenFlagsBackup)
{% endraw %}

```