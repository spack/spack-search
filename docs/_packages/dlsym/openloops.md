---
name: "openloops"
layout: package
next_package: binutils
previous_package: casacore
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['fortran']
---
## 2.1.1
2 / 730 files match, 2 filtered matches.

 - [lib_src/openloops/src/ol_interface.F90](#lib_srcopenloopssrcol_interfacef90)
 - [lib_src/olcommon/src/common.F90](#lib_srcolcommonsrccommonf90)

### lib_src/openloops/src/ol_interface.F90

```fortran

{% raw %}
214 |     ! [in] content: integer with binary tags for tree, loop, loop2, pt
215 |     ! [in] amptype: integer to specify BLHA matrix element type
216 |     ! return process handle of type process_handle
217 |     ! note: error handling is done in dlsym
218 |     use KIND_TYPES, only: DREALKIND
219 |     use ol_dlfcn, only: dlsym
220 |     use ol_loop_parameters_decl_/**/DREALKIND, only: &
221 |          & stability_mode,a_switch,a_switch_rescue,redlib_qp,hel_mem_opt_switch
234 |     procedure(), pointer :: tmp_fun
235 | 
236 |     ! number of external particles
237 |     tmp_fun => dlsym(lib, "ol_f_n_external_" // trim(proc))
238 | 
239 |     call tmp_fun(get_process_handle%n_particles)
251 |       get_process_handle%permutation = [(k, k=1, get_process_handle%n_particles)]
252 |     end if
253 |     get_process_handle%library_handle = lib
254 |     get_process_handle%set_permutation => dlsym(lib, "ol_f_set_permutation_" // trim(proc))
255 |     get_process_handle%rambo => dlsym(lib, "ol_f_rambo_" // trim(proc))
256 |     get_process_handle%amplitude_type = amptype
257 |     get_process_handle%tree => dlsym(lib, "ol_f_amp2_" // trim(proc))
258 |     get_process_handle%loop => dlsym(lib, "ol_f_vamp2_" // trim(proc))
259 |     get_process_handle%ct => dlsym(lib, "ol_f_ctamp2_" // trim(proc))
260 |     get_process_handle%pt => dlsym(lib, "ol_f_ptamp2_" // trim(proc))
261 |     get_process_handle%schsf => dlsym(lib, "ol_f_schsfamp2_" // trim(proc))
262 |     get_process_handle%content = content
263 |     get_process_handle%n_in = n_in
264 |     get_process_handle%qcd_powers = qcd_powers
265 |     ! loop correlators
266 |     get_process_handle%loopcr => dlsym(lib, "ol_f_vampcr2_" // trim(proc))
267 |     allocate(get_process_handle%last_psp(4,get_process_handle%n_particles))
268 |     get_process_handle%last_psp=0
272 |     get_process_handle%last_pol=0
273 |     get_process_handle%loop_parameters_status = -1
274 |     ! external masses and highest tensor rank
275 |     tmp_fun => dlsym(lib, "ol_f_get_masses_" // trim(proc))
276 |     allocate(get_process_handle%masses(get_process_handle%n_particles))
277 |     call tmp_fun(get_process_handle%masses)
278 |     allocate(get_process_handle%pol(get_process_handle%n_particles))
279 |     get_process_handle%pol_init => dlsym(lib, "ol_f_pol_init_" // trim(proc))
280 |     if (present(pol)) then
281 |       ! check correct size of the polarization vector
309 |     else
310 |       get_process_handle%photon_id = 0
311 |     end if
312 |     get_process_handle%set_photons => dlsym(lib, "ol_f_set_photons_" // trim(proc))
313 |     if (btest(content, 1)) then
314 |       tmp_fun => dlsym(lib, "ol_f_max_point_" // trim(proc))
315 |       call tmp_fun(get_process_handle%max_point)
316 |       tmp_fun => dlsym(lib, "ol_f_tensor_rank_" // trim(proc))
317 |       call tmp_fun(get_process_handle%tensor_rank)
318 |     end if
319 |     ! colour basis
320 |     get_process_handle%tree_colbasis_dim => dlsym(lib, "ol_tree_colbasis_dim_" // trim(proc))
321 |     get_process_handle%tree_colbasis => dlsym(lib, "ol_tree_colbasis_" // trim(proc))
322 |     get_process_handle%tree_colvect => dlsym(lib, "ol_tree_colvect_" // trim(proc))
323 |     ! stability settings
324 |     get_process_handle%a_switch=a_switch
326 |     get_process_handle%redlib_qp=redlib_qp
327 |     get_process_handle%stability_mode=stability_mode
328 |     ! optimized helicity bookkeeping
329 |     tmp_fun => dlsym(lib, "ol_hel_mem_opt_" // trim(proc))
330 |     if (associated(tmp_fun)) then
331 |       call tmp_fun(hel_mem_opt_switch)
332 |     else
333 | !      call ol_fatal_update()
334 |     end if
335 |     tmp_fun => dlsym(lib, "ol_f_iopamp2_" // trim(proc))
336 |     if (associated(tmp_fun)) then
337 |       get_process_handle%iop => tmp_fun
338 |     end if
339 |     get_process_handle%loopcc => dlsym(lib, "ol_loopcc_" // trim(proc))
340 |   end function get_process_handle
341 | 
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
827 |       integer(c_int), value :: mode
828 |       type(c_ptr) :: c_dlopen
829 |     end function c_dlopen
830 |     function c_dlsym(lib, sym) bind(c,name="dlsym")
831 |       ! void *dlsym(void *lib, const char *sym);
832 |       use, intrinsic :: iso_c_binding, only: c_ptr, c_char, c_funptr
833 |       implicit none
834 |       type(c_ptr), value :: lib
835 |       character(kind=c_char), dimension(*), intent(in) :: sym
836 |       type(c_funptr) :: c_dlsym
837 |     end function c_dlsym
838 |     function c_dlclose(lib) bind(c,name="dlclose")
839 |       ! int dlclose(void *lib);
877 |     end if
878 |   end function dlopen
879 | 
880 |   function dlsym(lib, sym, fatal) result(f_funp)
881 |     ! fatal: 0=silent (default), 1=warning, 2=error
882 |     implicit none
885 |     integer, intent(in), optional :: fatal
886 |     type(c_funptr) :: c_funp
887 |     procedure(), pointer :: f_funp
888 |     c_funp = c_dlsym(lib, trim(sym) // c_null_char)
889 |     if (present(fatal)) then
890 |       if (fatal == 1 .and. .not. c_associated(c_funp)) then
891 |         print *, "[OpenLoops] dlsym:", dlerror()
892 |       else if (fatal == 2 .and. .not. c_associated(c_funp)) then
893 |         print *, "[OpenLoops] error in dlsym:", dlerror()
894 |         stop
895 |       end if
899 |     else
900 |       f_funp => null()
901 |     end if
902 |   end function dlsym
903 | 
904 |   subroutine dlclose(lib, fatal)
{% endraw %}

```