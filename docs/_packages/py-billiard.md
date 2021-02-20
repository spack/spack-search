---
name: "py-billiard"
layout: package
next_package: py-cairocffi
previous_package: pulseaudio
languages: ['python']
---
## 3.6.0.0
1 / 70 files match, 1 filtered matches.

 - [billiard/util.py](#billiardutilpy)

### billiard/util.py

```python

{% raw %}
177 |             ffi = cffi.FFI()
178 |             ffi.cdef("int prctl (int __option, ...);")
179 |             arg = ffi.new("int *")
180 |             C = ffi.dlopen(None)
181 |             C.prctl(PR_GET_PDEATHSIG, arg)
182 |             return arg[0]
204 |         if 'cffi' in sys.modules:
205 |             ffi = cffi.FFI()
206 |             ffi.cdef("int prctl (int __option, ...);")
207 |             C = ffi.dlopen(None)
208 |             C.prctl(PR_SET_PDEATHSIG, ffi.cast("int", sig))
209 |         else:
{% endraw %}

```