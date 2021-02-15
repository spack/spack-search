---
name: "py-setuptools"
layout: package
next_package: bind9
previous_package: py-billiard
languages: ['python']
---
## 49.6.0
3 / 310 files match

 - [setuptools/_vendor/packaging/tags.py](#setuptools_vendorpackagingtagspy)
 - [setuptools/command/build_ext.py](#setuptoolscommandbuild_extpy)
 - [pkg_resources/_vendor/packaging/tags.py](#pkg_resources_vendorpackagingtagspy)

### setuptools/_vendor/packaging/tags.py

```python

{% raw %}
471 |     # ctypes.CDLL(None) internally calls dlopen(NULL), and as the dlopen
{% endraw %}

```
### setuptools/command/build_ext.py

```python

{% raw %}
264 |                     if_dl("   old_flags = sys.getdlopenflags()"),
268 |                     if_dl("     sys.setdlopenflags(dl.RTLD_NOW)"),
274 |                     if_dl("     sys.setdlopenflags(old_flags)"),
{% endraw %}

```
### pkg_resources/_vendor/packaging/tags.py

```python

{% raw %}
471 |     # ctypes.CDLL(None) internally calls dlopen(NULL), and as the dlopen
{% endraw %}

```