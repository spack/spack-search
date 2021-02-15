---
name: "tulip"
layout: package
next_package: ppl
previous_package: libsodium
languages: ['python']
---
## 5.4.0
12 / 5173 files match

 - [bundlers/linux/make_appimage_bundle.sh.in](#bundlerslinuxmake_appimage_bundleshin)
 - [library/tulip-core/src/TlpTools.cpp](#librarytulip-coresrctlptoolscpp)
 - [library/tulip-core/src/PluginLibraryLoader.cpp](#librarytulip-coresrcpluginlibraryloadercpp)
 - [library/tulip-python/src/PythonInterpreter.cpp](#librarytulip-pythonsrcpythoninterpretercpp)
 - [library/tulip-python/bindings/tulip-core/__init__.py](#librarytulip-pythonbindingstulip-core__init__py)
 - [library/tulip-python/bindings/tulip-gui/__init__.py](#librarytulip-pythonbindingstulip-gui__init__py)
 - [library/tulip-python/api/Python-3.5.api](#librarytulip-pythonapipython-35api)
 - [library/tulip-python/api/Python-3.8.api](#librarytulip-pythonapipython-38api)
 - [library/tulip-python/api/Python-2.7.api](#librarytulip-pythonapipython-27api)
 - [library/tulip-python/api/Python-3.7.api](#librarytulip-pythonapipython-37api)
 - [library/tulip-python/api/Python-3.6.api](#librarytulip-pythonapipython-36api)
 - [library/tulip-python/api/Python-3.4.api](#librarytulip-pythonapipython-34api)

### bundlers/linux/make_appimage_bundle.sh.in

```

{% raw %}
162 | # performs a dlopen on libpythonX.Y.so when it is loaded
{% endraw %}

```
### library/tulip-core/src/TlpTools.cpp

```

{% raw %}
128 |   void *ptr = dlopen(libTulipName.c_str(), RTLD_LAZY);
{% endraw %}

```
### library/tulip-core/src/PluginLibraryLoader.cpp

```

{% raw %}
157 |   void *handle = dlopen(filename.c_str(), RTLD_NOW);
{% endraw %}

```
### library/tulip-python/src/PythonInterpreter.cpp

```

{% raw %}
299 |     if (!dlopen(QStringToTlpString(libPythonName).c_str(), RTLD_LAZY | RTLD_GLOBAL)) {
309 |       if (!dlopen(QStringToTlpString(libPythonName).c_str(), RTLD_LAZY | RTLD_GLOBAL)) {
317 |         dlopen(QStringToTlpString(libPythonName).c_str(), RTLD_LAZY | RTLD_GLOBAL);
{% endraw %}

```
### library/tulip-python/bindings/tulip-core/__init__.py

```python

{% raw %}
163 |     dlOpenFlagsBackup = sys.getdlopenflags()
166 |         dlOpenFlags = DLFCN.RTLD_NOW | DLFCN.RTLD_GLOBAL
168 |         dlOpenFlags = os.RTLD_NOW | os.RTLD_GLOBAL
169 |     sys.setdlopenflags(dlOpenFlags)
180 |     sys.setdlopenflags(dlOpenFlagsBackup)
{% endraw %}

```
### library/tulip-python/bindings/tulip-gui/__init__.py

```python

{% raw %}
75 |     dlOpenFlagsBackup = sys.getdlopenflags()
78 |         dlOpenFlags = DLFCN.RTLD_NOW | DLFCN.RTLD_GLOBAL
80 |         dlOpenFlags = os.RTLD_NOW | os.RTLD_GLOBAL
81 |     sys.setdlopenflags(dlOpenFlags)
87 |     sys.setdlopenflags(dlOpenFlagsBackup)
{% endraw %}

```
### library/tulip-python/api/Python-3.5.api

```

{% raw %}
6843 | sys.getdlopenflags() -> int
6868 | sys.setdlopenflags(n) -> None
{% endraw %}

```
### library/tulip-python/api/Python-3.8.api

```

{% raw %}
6709 | sys.getdlopenflags(??)
6737 | sys.setdlopenflags(??)
{% endraw %}

```
### library/tulip-python/api/Python-2.7.api

```

{% raw %}
6318 | sys.getdlopenflags() -> int
6340 | sys.setdlopenflags(n) -> None
{% endraw %}

```
### library/tulip-python/api/Python-3.7.api

```

{% raw %}
6497 | sys.getdlopenflags() -> int
6525 | sys.setdlopenflags(n) -> None
{% endraw %}

```
### library/tulip-python/api/Python-3.6.api

```

{% raw %}
6459 | sys.getdlopenflags() -> int
6486 | sys.setdlopenflags(n) -> None
{% endraw %}

```
### library/tulip-python/api/Python-3.4.api

```

{% raw %}
6942 | sys.getdlopenflags() -> int
6965 | sys.setdlopenflags(n) -> None
{% endraw %}

```