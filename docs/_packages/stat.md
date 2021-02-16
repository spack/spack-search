---
name: "stat"
layout: package
next_package: sblim-sfcc
previous_package: openldap
languages: ['python', 'c']
---
## 4.0.2
7 / 275 files match

 - [src/dysect/DysectAPI/DysectAPI.C](#srcdysectdysectapidysectapic)
 - [examples/scripts/script_test.py](#examplesscriptsscript_testpy)
 - [scripts/STATview.py](#scriptsstatviewpy)
 - [scripts/STATGUI.py](#scriptsstatguipy)

### src/dysect/DysectAPI/DysectAPI.C

```c

{% raw %}
23 |   libraryHandle = dlopen(path, RTLD_LAZY);
{% endraw %}

```
### examples/scripts/script_test.py

```python

{% raw %}
4 | sys.setdlopenflags(DLFCN.RTLD_NOW | DLFCN.RTLD_GLOBAL)
{% endraw %}

```
### scripts/STATview.py

```python

{% raw %}
39 | dlopenflags_set = False
42 |     sys.setdlopenflags(DLFCN.RTLD_NOW | DLFCN.RTLD_GLOBAL)
43 |     dlopenflags_set = True
46 | if dlopenflags_set == False:
47 |     sys.setdlopenflags(os.RTLD_NOW | os.RTLD_GLOBAL)
{% endraw %}

```
### scripts/STATGUI.py

```python

{% raw %}
41 | dlopenflags_set = False
44 |     sys.setdlopenflags(DLFCN.RTLD_NOW | DLFCN.RTLD_GLOBAL)
45 |     dlopenflags_set = True
48 | if dlopenflags_set == False:
49 |     sys.setdlopenflags(os.RTLD_NOW | os.RTLD_GLOBAL)
{% endraw %}

```