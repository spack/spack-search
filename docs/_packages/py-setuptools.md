---
name: "py-setuptools"
layout: package
next_package: bind9
previous_package: py-billiard
languages: ['python']
---
## 49.6.0
3 / 310 files match, 1 filtered matches.

 - [setuptools/command/build_ext.py](#setuptoolscommandbuild_extpy)

### setuptools/command/build_ext.py

```python

{% raw %}
264 |                     if_dl("   old_flags = sys.getdlopenflags()"),
268 |                     if_dl("     sys.setdlopenflags(dl.RTLD_NOW)"),
274 |                     if_dl("     sys.setdlopenflags(old_flags)"),
{% endraw %}

```