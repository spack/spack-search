---
name: "q-e-sirius"
layout: package
next_package: xwininfo
previous_package: extrae
languages: ['c']
---
## 6.5-rc3-siriu
1 / 5019 files match, 1 filtered matches.

 - [dev-tools/device_props.c](#dev-toolsdevice_propsc)

### dev-tools/device_props.c

```c

{% raw %}
99 |   cudaRT = dlopen(CUDART_LIBRARY_NAME, RTLD_NOW);
103 |     cudaRT = dlopen(full_library_name, RTLD_NOW);
106 |       cudaRT = dlopen(full_library_name, RTLD_NOW);
{% endraw %}

```