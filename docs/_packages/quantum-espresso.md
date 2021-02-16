---
name: "quantum-espresso"
layout: package
next_package: erfa
previous_package: opari2
languages: ['c']
---
## 6.4
1 / 4877 files match, 1 filtered matches.

 - [dev-tools/device_props.c](#dev-toolsdevice_propsc)

### dev-tools/device_props.c

```c

{% raw %}
99 |   cudaRT = dlopen(CUDART_LIBRARY_NAME, RTLD_NOW);
103 |     cudaRT = dlopen(full_library_name, RTLD_NOW);
106 |       cudaRT = dlopen(full_library_name, RTLD_NOW);
{% endraw %}

```