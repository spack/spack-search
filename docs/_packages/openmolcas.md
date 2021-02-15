---
name: "openmolcas"
layout: package
next_package: photos
previous_package: plumed
languages: ['fortran']
---
## 19.11
2 / 7244 files match

 - [src/delayed_util/dlfcn.f90](#srcdelayed_utildlfcnf90)
 - [src/delayed_util/link_blas.f90](#srcdelayed_utillink_blasf90)

### src/delayed_util/dlfcn.f90

```fortran

{% raw %}
48 |    PUBLIC :: DLOpen, DLSym, DLClose, DLError, DLAddr ! DL API
50 |    ! Valid modes for mode in DLOpen:
63 |       FUNCTION DLOpen(file,mode) RESULT(handle) BIND(C,NAME="dlopen")
64 |          ! void *dlopen(const char *file, int mode);
{% endraw %}

```
### src/delayed_util/link_blas.f90

```fortran

{% raw %}
64 |           handles(i)=dlopen(trim(libname)//c_null_char, int(ior(rtld_global,rtld_lazy),kind=c_int))
{% endraw %}

```