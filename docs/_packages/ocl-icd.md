---
name: "ocl-icd"
layout: package
next_package: isc-dhcp
previous_package: py-uvloop
languages: ['c']
---
## 2.2.4
3 / 37 files match

 - [ocl_icd_loader.c](#ocl_icd_loaderc)

### ocl_icd_loader.c

```c

{% raw %}
185 |   _icds[num_icds].dl_handle = dlopen(lib_path, RTLD_LAZY|RTLD_LOCAL);//|RTLD_DEEPBIND);
190 |     debug(D_WARN, "error while dlopening the IDL: '%s',\n  => skipping ICD", dlerror());
{% endraw %}

```