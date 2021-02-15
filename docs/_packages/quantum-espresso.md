---
name: "quantum-espresso"
layout: package
next_package: erfa
previous_package: opari2
languages: ['cpp']
---
## 6.4
1 / 4877 files match

 - [dev-tools/device_props.c](#dev-toolsdevice_propsc)

### dev-tools/device_props.c

```cpp

{% raw %}
99 |   cudaRT = dlopen(CUDART_LIBRARY_NAME, RTLD_NOW);
103 |     cudaRT = dlopen(full_library_name, RTLD_NOW);
106 |       cudaRT = dlopen(full_library_name, RTLD_NOW);
{% endraw %}

```