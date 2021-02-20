---
name: "arrayfire"
layout: package
next_package: arrow
previous_package: apr
languages: ['c']
---
## 3.7.0
3 / 4691 files match, 2 filtered matches.

 - [extern/forge/extern/glad/src/glad.c](#externforgeexterngladsrcgladc)
 - [extern/glad/src/glad.c](#externgladsrcgladc)

### extern/forge/extern/glad/src/glad.c

```c

{% raw %}
893 | 
894 |     unsigned int index = 0;
895 |     for(index = 0; index < (sizeof(NAMES) / sizeof(NAMES[0])); index++) {
896 |         libGL = dlopen(NAMES[index], RTLD_NOW | RTLD_GLOBAL);
897 | 
898 |         if(libGL != NULL) {
{% endraw %}

```
### extern/glad/src/glad.c

```c

{% raw %}
893 | 
894 |     unsigned int index = 0;
895 |     for(index = 0; index < (sizeof(NAMES) / sizeof(NAMES[0])); index++) {
896 |         libGL = dlopen(NAMES[index], RTLD_NOW | RTLD_GLOBAL);
897 | 
898 |         if(libGL != NULL) {
{% endraw %}

```