---
name: "py-setuptools"
layout: package
next_package: py-shiboken
previous_package: py-scipy
languages: ['python']
---
## 49.6.0
3 / 310 files match, 1 filtered matches.

 - [setuptools/command/build_ext.py](#setuptoolscommandbuild_extpy)

### setuptools/command/build_ext.py

```python

{% raw %}
261 |                     "   del __bootstrap__",
262 |                     "   if '__loader__' in globals():",
263 |                     "       del __loader__",
264 |                     if_dl("   old_flags = sys.getdlopenflags()"),
265 |                     "   old_dir = os.getcwd()",
266 |                     "   try:",
267 |                     "     os.chdir(os.path.dirname(__file__))",
268 |                     if_dl("     sys.setdlopenflags(dl.RTLD_NOW)"),
269 |                     "     spec = importlib.util.spec_from_file_location(",
270 |                     "                __name__, __file__)",
271 |                     "     mod = importlib.util.module_from_spec(spec)",
272 |                     "     spec.loader.exec_module(mod)",
273 |                     "   finally:",
274 |                     if_dl("     sys.setdlopenflags(old_flags)"),
275 |                     "     os.chdir(old_dir)",
276 |                     "__bootstrap__()",
{% endraw %}

```