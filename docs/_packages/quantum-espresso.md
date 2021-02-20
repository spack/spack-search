---
name: "quantum-espresso"
layout: package
next_package: r
previous_package: qt-creator
languages: ['c']
---
## 6.4
1 / 4877 files match, 1 filtered matches.

 - [dev-tools/device_props.c](#dev-toolsdevice_propsc)

### dev-tools/device_props.c

```c

{% raw %}
96 |   unsigned int sort;
97 |   simCudaDevice *devices;
98 | 
99 |   cudaRT = dlopen(CUDART_LIBRARY_NAME, RTLD_NOW);
100 |   if(!cudaRT) {
101 |     char full_library_name[PATH_MAX];
102 |     sprintf(full_library_name, "/usr/local/cuda/lib64/%s", CUDART_LIBRARY_NAME);
103 |     cudaRT = dlopen(full_library_name, RTLD_NOW);
104 |     if(!cudaRT) {
105 |       sprintf(full_library_name, "/usr/local/cuda/lib/%s", CUDART_LIBRARY_NAME);
106 |       cudaRT = dlopen(full_library_name, RTLD_NOW);
107 |       if(!cudaRT) {
108 | 	snprintf(error_message, BUFFER_LENGTH,
{% endraw %}

```