---
name: "openmolcas"
layout: package
next_package: openmpi
previous_package: openmc
languages: ['fortran']
---
## 19.11
2 / 7244 files match, 2 filtered matches.

 - [src/delayed_util/dlfcn.f90](#srcdelayed_utildlfcnf90)
 - [src/delayed_util/link_blas.f90](#srcdelayed_utillink_blasf90)

### src/delayed_util/dlfcn.f90

```fortran

{% raw %}
60 |    END TYPE DL_info
61 | 
62 |    INTERFACE ! All we need is interfaces for the prototypes in <dlfcn.h>
63 |       FUNCTION DLOpen(file,mode) RESULT(handle) BIND(C,NAME="dlopen")
64 |          ! void *dlopen(const char *file, int mode);
65 |          USE ISO_C_BINDING
66 |          CHARACTER(C_CHAR), DIMENSION(*), INTENT(IN) :: file
{% endraw %}

```
### src/delayed_util/link_blas.f90

```fortran

{% raw %}
61 |       do i=1,size(libs)
62 |         libname=libs(i)
63 |         if (len_trim(libs(i)) > 0) then
64 |           handles(i)=dlopen(trim(libname)//c_null_char, int(ior(rtld_global,rtld_lazy),kind=c_int))
65 |           loaded=(loaded .or. c_associated(handles(i)))
66 |           if (prlev > 0) then
{% endraw %}

```