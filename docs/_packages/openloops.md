---
name: "openloops"
layout: package
next_package: openmc
previous_package: openldap
languages: ['fortran']
---
## 2.1.1
3 / 730 files match, 2 filtered matches.

 - [lib_src/openloops/src/ol_interface.F90](#lib_srcopenloopssrcol_interfacef90)
 - [lib_src/olcommon/src/common.F90](#lib_srcolcommonsrccommonf90)

### lib_src/openloops/src/ol_interface.F90

```fortran

{% raw %}
347 |     ! [in] amptype: integer to specify BLHA matrix element type
348 |     ! return (integer) process id to be used in OLP_EvalSubProcess
349 |     use KIND_TYPES, only: DREALKIND
350 |     use ol_dlfcn, only: dlopen, RTLD_LAZY
351 |     use ol_loop_parameters_decl_/**/DREALKIND, only: maxpoint, maxrank, do_pole_checks
352 |     implicit none
365 |     type(process_handle) :: prochandle
366 |     type(process_handle), allocatable :: process_handles_bak(:)
367 | 
368 |     lib = dlopen(libname, RTLD_LAZY, 2)
369 |     prochandle = get_process_handle(lib, libname, proc, content, amptype, n_in, perm=perm, pol=pol, &
370 |                                                    & extid=extid, photon_id=photon_id, qcd_powers=qcd_powers)
{% endraw %}

```
### lib_src/olcommon/src/common.F90

```fortran

{% raw %}
811 |   implicit none
812 |   private
813 |   public :: RTLD_LAZY, RTLD_NOW, RTLD_GLOBAL, RTLD_LOCAL
814 |   public :: dlopen, dlsym, dlclose
815 |   ! dlopen modes:
816 |   integer(c_int), bind(c,name="ol_c_rtld_lazy") :: RTLD_LAZY
817 |   integer(c_int), bind(c,name="ol_c_rtld_now") :: RTLD_NOW
819 |   integer(c_int), bind(c,name="ol_c_rtld_local") :: RTLD_LOCAL
820 | 
821 |   interface
822 |     function c_dlopen(file, mode) bind(c,name="dlopen")
823 |       ! void *dlopen(const char *file, int mode);
824 |       use, intrinsic :: iso_c_binding, only: c_char, c_int, c_ptr
825 |       implicit none
826 |       character(kind=c_char), dimension(*), intent(in) :: file
827 |       integer(c_int), value :: mode
828 |       type(c_ptr) :: c_dlopen
829 |     end function c_dlopen
830 |     function c_dlsym(lib, sym) bind(c,name="dlsym")
831 |       ! void *dlsym(void *lib, const char *sym);
859 |     dlerror => c_f_string_ptr(c_dlerror())
860 |   end function
861 | 
862 |   function dlopen(file, mode, fatal)
863 |     ! fatal: 0=silent (default), 1=warning, 2=error
864 |     implicit none
865 |     character(len=*), intent(in) :: file
866 |     integer(c_int), intent(in) :: mode
867 |     integer, intent(in), optional :: fatal
868 |     type(c_ptr) :: dlopen
869 |     dlopen = c_dlopen(trim(file) // c_null_char, mode)
870 |     if (present(fatal)) then
871 |       if (fatal == 1 .and. .not. c_associated(dlopen)) then
872 |         print *, "[OpenLoops] dlopen:", dlerror()
873 |       else if (fatal == 2 .and. .not. c_associated(dlopen)) then
874 |         print *, "[OpenLoops] error in dlopen:", dlerror()
875 |         stop
876 |       end if
877 |     end if
878 |   end function dlopen
879 | 
880 |   function dlsym(lib, sym, fatal) result(f_funp)
{% endraw %}

```