---
name: "parsec"
layout: package
next_package: papi
previous_package: file
library_name: dlopen
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 1.1.0
1 / 618 files match, 1 filtered matches.

 - [dplasma/cores/cuda_zgemm.c](#dplasmacorescuda_zgemmc)

### dplasma/cores/cuda_zgemm.c

```c

{% raw %}
113 |             snprintf(library_name,  FILENAME_MAX, "%s", env);
114 |         }
115 | 
116 |         dlh = dlopen(library_name, RTLD_NOW | RTLD_NODELETE );
117 |         if(NULL == dlh) {
118 |             if(env) ERROR(("Could not find %s library: %s\n"
131 |         /* Couldn't load from dynamic libs, try static */
132 |         if(NULL == fn) {
133 |             DEBUG3(("No dynamic function %s found, loading from statically linked\n", function_name));
134 |             dlh = dlopen(NULL, RTLD_NOW | RTLD_NODELETE);
135 |             if(NULL == dlh) ERROR(("Error parsing static libs: %s\n", dlerror()));
136 |             fn = dlsym(dlh, function_name);
{% endraw %}

```