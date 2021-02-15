---
name: "ocl-icd"
layout: package
next_package: isc-dhcp
previous_package: py-uvloop
languages: ['cpp']
---
## 2.2.4
3 / 37 files match

 - [configure.ac](#configureac)
 - [ocl_icd_loader.c](#ocl_icd_loaderc)
 - [doc/libOpenCL.7.txt](#doclibopencl7txt)

### configure.ac

```

{% raw %}
34 | AC_CHECK_LIB([dl], [dlopen])
{% endraw %}

```
### ocl_icd_loader.c

```cpp

{% raw %}
185 |   _icds[num_icds].dl_handle = dlopen(lib_path, RTLD_LAZY|RTLD_LOCAL);//|RTLD_DEEPBIND);
190 |     debug(D_WARN, "error while dlopening the IDL: '%s',\n  => skipping ICD", dlerror());
{% endraw %}

```
### doc/libOpenCL.7.txt

```

{% raw %}
21 | whose name ends with '`.icd`', the ICD Loader loads with **dlopen**(3) the
49 |   library itself (i.e. to load it directly with **dlopen**(3)).
{% endraw %}

```