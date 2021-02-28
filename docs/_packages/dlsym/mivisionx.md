---
name: "mivisionx"
layout: package
next_package: vtable-dumper
previous_package: ipcalc
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['python']
---
## 3.8.0
3 / 1738 files match, 1 filtered matches.

 - [model_compiler/python/nnir_to_clib.py](#model_compilerpythonnnir_to_clibpy)

### model_compiler/python/nnir_to_clib.py

```python

{% raw %}
1223 |         mvWaitForCompletion_f       = nullptr;
1224 |         mvReleaseInference_f        = nullptr;
1225 |     } else {
1226 |         mvQueryInference_f          = (mvQueryInference_t) dlsym(libHandle, "mvQueryInference");
1227 |         mvSetLogCallback_f          = (mvSetLogCallback_t) dlsym(libHandle, "mvSetLogCallback");
1228 |         mvSetPreProcessCallback_f   = (mvSetPreProcessCallback_t) dlsym(libHandle, "mvSetPreProcessCallback");
1229 |         mvSetPostProcessCallback_f  = (mvSetPostProcessCallback_t) dlsym(libHandle, "mvSetPostProcessCallback");
1230 |         mvCreateInference_f         = (mvCreateInference_t) dlsym(libHandle, "mvCreateInference");
1231 |         mvCopyToTensorFromMem_f     = (mvCopyToTensorFromMem_t) dlsym(libHandle, "mvCopyToTensorFromMem");
1232 |         mvCopyToTensorFromFile_f    = (mvCopyToTensorFromFile_t) dlsym(libHandle, "mvCopyToTensorFromFile");
1233 |         mvProcessInference_f        = (mvProcessInference_t) dlsym(libHandle, "mvProcessInference");
1234 |         mvGetOutput_f               = (mvGetOutput_t) dlsym(libHandle, "mvGetOutput");
1235 |         mvScheduleInference_f       = (mvScheduleInference_t) dlsym(libHandle, "mvScheduleInference");
1236 |         mvWaitForCompletion_f       = (mvWaitForCompletion_t) dlsym(libHandle, "mvWaitForCompletion");
1237 |         mvReleaseInference_f        = (mvReleaseInference_t) dlsym(libHandle, "mvReleaseInference");
1238 |     }
1239 | 
{% endraw %}

```