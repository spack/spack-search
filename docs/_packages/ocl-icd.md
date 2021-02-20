---
name: "ocl-icd"
layout: package
next_package: octave
previous_package: oce
languages: ['c']
---
## 2.2.4
3 / 37 files match, 1 filtered matches.

 - [ocl_icd_loader.c](#ocl_icd_loaderc)

### ocl_icd_loader.c

```c

{% raw %}
182 |   unsigned int ret=0;
183 |   debug(D_LOG, "Loading ICD '%s'", lib_path);
184 | 
185 |   _icds[num_icds].dl_handle = dlopen(lib_path, RTLD_LAZY|RTLD_LOCAL);//|RTLD_DEEPBIND);
186 |   if(_icds[num_icds].dl_handle != NULL) {
187 |     debug(D_LOG, "ICD[%i] loaded", num_icds);
188 |     ret=1;
189 |   } else {
190 |     debug(D_WARN, "error while dlopening the IDL: '%s',\n  => skipping ICD", dlerror());
191 |   }
192 |   return ret;
{% endraw %}

```