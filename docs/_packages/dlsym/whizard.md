---
name: "whizard"
layout: package
next_package: lvm2
previous_package: folly
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['fortran']
---
## 2.8.3
6 / 3957 files match, 2 filtered matches.

 - [src/system/os_interface.f90_mpi](#srcsystemos_interfacef90_mpi)
 - [src/system/os_interface.f90_serial](#srcsystemos_interfacef90_serial)

### src/system/os_interface.f90_mpi

```fortran

{% raw %}
186 |   end interface
187 | 
188 |   interface
189 |      function dlsym (handle, symbol) result (fptr) bind(C)
190 |        import
191 |        type(c_ptr), value :: handle
192 |        character(c_char), dimension(*) :: symbol
193 |        type(c_funptr) :: fptr
194 |      end function dlsym
195 |   end interface
196 | 
589 |     type(c_funptr) :: fptr
590 |     type(dlaccess_t), intent(inout) :: dlaccess
591 |     type(string_t), intent(in) :: fname
592 |     fptr = dlsym (dlaccess%handle, char (fname) // c_null_char)
593 |     call read_dlerror (dlaccess%has_error, dlaccess%error)
594 |   end function dlaccess_get_c_funptr
{% endraw %}

```
### src/system/os_interface.f90_serial

```fortran

{% raw %}
186 |   end interface
187 | 
188 |   interface
189 |      function dlsym (handle, symbol) result (fptr) bind(C)
190 |        import
191 |        type(c_ptr), value :: handle
192 |        character(c_char), dimension(*) :: symbol
193 |        type(c_funptr) :: fptr
194 |      end function dlsym
195 |   end interface
196 | 
589 |     type(c_funptr) :: fptr
590 |     type(dlaccess_t), intent(inout) :: dlaccess
591 |     type(string_t), intent(in) :: fname
592 |     fptr = dlsym (dlaccess%handle, char (fname) // c_null_char)
593 |     call read_dlerror (dlaccess%has_error, dlaccess%error)
594 |   end function dlaccess_get_c_funptr
{% endraw %}

```