---
name: "py-cryptography"
layout: package
next_package: py-cyvcf2
previous_package: py-chainer
languages: ['python']
---
## 2.7
1 / 307 files match, 1 filtered matches.

 - [tests/hazmat/backends/test_openssl_memleak.py](#testshazmatbackendstest_openssl_memleakpy)

### tests/hazmat/backends/test_openssl_memleak.py

```python

{% raw %}
35 |             int backtrace(void **, int);
36 |             char **backtrace_symbols(void *const *, int);
37 |         ''')
38 |         backtrace_lib = backtrace_ffi.dlopen(None)
39 | 
40 |         def backtrace():
{% endraw %}

```