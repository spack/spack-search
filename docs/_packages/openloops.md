---
name: "openloops"
layout: package
next_package: freebayes
previous_package: opensubdiv
languages: ['fortran']
---
## 2.1.1
3 / 730 files match, 2 filtered matches.

 - [lib_src/openloops/src/ol_interface.F90](#lib_srcopenloopssrcol_interfacef90)
 - [lib_src/olcommon/src/common.F90](#lib_srcolcommonsrccommonf90)

### lib_src/openloops/src/ol_interface.F90

```fortran

{% raw %}
350 |     use ol_dlfcn, only: dlopen, RTLD_LAZY
368 |     lib = dlopen(libname, RTLD_LAZY, 2)
{% endraw %}

```
### lib_src/olcommon/src/common.F90

```fortran

{% raw %}
814 |   public :: dlopen, dlsym, dlclose
815 |   ! dlopen modes:
822 |     function c_dlopen(file, mode) bind(c,name="dlopen")
823 |       ! void *dlopen(const char *file, int mode);
828 |       type(c_ptr) :: c_dlopen
829 |     end function c_dlopen
862 |   function dlopen(file, mode, fatal)
868 |     type(c_ptr) :: dlopen
869 |     dlopen = c_dlopen(trim(file) // c_null_char, mode)
871 |       if (fatal == 1 .and. .not. c_associated(dlopen)) then
872 |         print *, "[OpenLoops] dlopen:", dlerror()
873 |       else if (fatal == 2 .and. .not. c_associated(dlopen)) then
874 |         print *, "[OpenLoops] error in dlopen:", dlerror()
878 |   end function dlopen
{% endraw %}

```