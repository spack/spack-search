---
name: "mivisionx"
layout: package
next_package: mono
previous_package: meson
library_name: dlopen
matches: ['dlsym', 'dlopen']
languages: ['python']
---
## 3.8.0
4 / 1738 files match, 1 filtered matches.

 - [model_compiler/python/nnir_to_clib.py](#model_compilerpythonnnir_to_clibpy)

### model_compiler/python/nnir_to_clib.py

```python

{% raw %}
1206 | 
1207 | mvDeployAPI::mvDeployAPI(const char *library_name)
1208 | {
1209 |     libHandle = dlopen(library_name, RTLD_NOW | RTLD_LOCAL);
1210 |     if (!libHandle)
1211 |     {
{% endraw %}

```