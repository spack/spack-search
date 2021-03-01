---
name: "parsec"
layout: package
next_package: pdsh
previous_package: papi
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 1.1.0
1 / 618 files match, 1 filtered matches.

 - [dplasma/cores/cuda_zgemm.c](#dplasmacorescuda_zgemmc)

### dplasma/cores/cuda_zgemm.c

```c

{% raw %}
124 |             DEBUG3(("Could not find %s dynamic library (%s)\n", library_name, dlerror()));
125 |         }
126 |         else {
127 |             fn = dlsym(dlh, function_name);
128 |             dlclose(dlh);
129 |         }
133 |             DEBUG3(("No dynamic function %s found, loading from statically linked\n", function_name));
134 |             dlh = dlopen(NULL, RTLD_NOW | RTLD_NODELETE);
135 |             if(NULL == dlh) ERROR(("Error parsing static libs: %s\n", dlerror()));
136 |             fn = dlsym(dlh, function_name);
137 |             if(env && fn) WARNING(("Internal static function %s used (because library %s didn't loaded correctly)\n", function_name, library_name));
138 |             dlclose(dlh);
{% endraw %}

```