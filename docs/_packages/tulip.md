---
name: "tulip"
layout: package
next_package: turbine
previous_package: trilinos
languages: ['python']
---
## 5.4.0
12 / 5173 files match, 2 filtered matches.

 - [library/tulip-python/bindings/tulip-core/__init__.py](#librarytulip-pythonbindingstulip-core__init__py)
 - [library/tulip-python/bindings/tulip-gui/__init__.py](#librarytulip-pythonbindingstulip-gui__init__py)

### library/tulip-python/bindings/tulip-core/__init__.py

```python

{% raw %}
160 | # fix loading of Tulip plugins when the tulip module has been
161 | # installed with the pip tool
162 | if platform.system() == 'Linux' and os.path.exists(_tulipNativePluginsPath):
163 |     dlOpenFlagsBackup = sys.getdlopenflags()
164 |     if sys.version_info < (3, 6):
165 |         import DLFCN
166 |         dlOpenFlags = DLFCN.RTLD_NOW | DLFCN.RTLD_GLOBAL
167 |     else:
168 |         dlOpenFlags = os.RTLD_NOW | os.RTLD_GLOBAL
169 |     sys.setdlopenflags(dlOpenFlags)
170 | 
171 | tlp.loadTulipPluginsFromDir(_tulipNativePluginsPath)
177 |         os.path.join(os.path.dirname(__file__), 'plugins'))
178 | 
179 | if platform.system() == 'Linux' and os.path.exists(_tulipNativePluginsPath):
180 |     sys.setdlopenflags(dlOpenFlagsBackup)
181 | 
182 | __all__ = ['tlp']
{% endraw %}

```
### library/tulip-python/bindings/tulip-gui/__init__.py

```python

{% raw %}
72 | # fix loading of Tulip plugins when the tulipgui module has been installed
73 | # with the pip tool
74 | if platform.system() == 'Linux' and os.path.exists(_tulipGuiNativePluginsPath):
75 |     dlOpenFlagsBackup = sys.getdlopenflags()
76 |     if sys.version_info < (3, 6):
77 |         import DLFCN
78 |         dlOpenFlags = DLFCN.RTLD_NOW | DLFCN.RTLD_GLOBAL
79 |     else:
80 |         dlOpenFlags = os.RTLD_NOW | os.RTLD_GLOBAL
81 |     sys.setdlopenflags(dlOpenFlags)
82 | 
83 | tlp.loadTulipPluginsFromDir(_tulipGuiPluginsPath)
84 | 
85 | if (platform.system() == 'Linux'
86 |         and os.path.exists(_tulipGuiNativePluginsPath)):
87 |     sys.setdlopenflags(dlOpenFlagsBackup)
88 | 
89 | # Check if we are in script execution mode
{% endraw %}

```