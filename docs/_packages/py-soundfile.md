---
name: "py-soundfile"
layout: package
next_package: py-tables
previous_package: py-shiboken
languages: ['python']
---
## 0.10.3.post1
2 / 22 files match, 2 filtered matches.

 - [soundfile.py](#soundfilepy)
 - [doc/fake__soundfile.py](#docfake__soundfilepy)

### soundfile.py

```python

{% raw %}
139 |     _libname = _find_library('sndfile')
140 |     if _libname is None:
141 |         raise OSError('sndfile library not found')
142 |     _snd = _ffi.dlopen(_libname)
143 | except OSError:
144 |     if _sys.platform == 'darwin':
158 |     while not _os.path.isdir(_path):
159 |         _path = _os.path.abspath(_os.path.join(_path, '..'))
160 | 
161 |     _snd = _ffi.dlopen(_os.path.join(
162 |         _path, '_soundfile_data', _libname))
163 | 
{% endraw %}

```
### doc/fake__soundfile.py

```python

{% raw %}
7 | 
8 | class ffi(object):
9 | 
10 |     def dlopen(self, _):
11 |         return self
12 | 
{% endraw %}

```