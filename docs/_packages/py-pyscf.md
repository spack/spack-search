---
name: "py-pyscf"
layout: package
next_package: sqlcipher
previous_package: meshkit
languages: ['bash']
---
## 1.7.3
2 / 2625 files match

 - [doc_legacy/source/install.rst](#doc_legacysourceinstallrst)
 - [pyscf/lib/_runme_to_fix_dylib_osx10.11.sh](#pyscflib_runme_to_fix_dylib_osx1011sh)

### doc_legacy/source/install.rst

```

{% raw %}
104 |     OSError: dlopen(xxx/pyscf/pyscf/lib/libcgto.dylib, 6): Library not loaded: libcint.3.0.dylib
{% endraw %}

```
### pyscf/lib/_runme_to_fix_dylib_osx10.11.sh

```bash

{% raw %}
8 | #  OSError: dlopen(xxx/pyscf/lib/libcgto.dylib, 6): Library not loaded: libcint.3.0.dylib
{% endraw %}

```