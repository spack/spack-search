---
name: "whizard"
layout: package
next_package: wireshark
previous_package: weechat
library_name: dlopen
matches: ['dlsym', 'dlopen']
languages: ['fortran']
---
## 2.8.3
11 / 3957 files match, 2 filtered matches.

 - [src/system/os_interface.f90_mpi](#srcsystemos_interfacef90_mpi)
 - [src/system/os_interface.f90_serial](#srcsystemos_interfacef90_serial)

### src/system/os_interface.f90_mpi

```fortran

{% raw %}
162 | 
163 | 
164 |   interface
165 |      function dlopen (filename, flag) result (handle) bind(C)
166 |        import
167 |        character(c_char), dimension(*) :: filename
168 |        integer(c_int), value :: flag
169 |        type(c_ptr) :: handle
170 |      end function dlopen
171 |   end interface
172 | 
557 |           return
558 |        end if
559 |     end if
560 |     dlaccess%handle = dlopen (char (filename) // c_null_char, ior ( &
561 |        RTLD_LAZY, RTLD_LOCAL))
562 |     dlaccess%is_open = c_associated (dlaccess%handle)
{% endraw %}

```
### src/system/os_interface.f90_serial

```fortran

{% raw %}
162 | 
163 | 
164 |   interface
165 |      function dlopen (filename, flag) result (handle) bind(C)
166 |        import
167 |        character(c_char), dimension(*) :: filename
168 |        integer(c_int), value :: flag
169 |        type(c_ptr) :: handle
170 |      end function dlopen
171 |   end interface
172 | 
557 |           return
558 |        end if
559 |     end if
560 |     dlaccess%handle = dlopen (char (filename) // c_null_char, ior ( &
561 |        RTLD_LAZY, RTLD_LOCAL))
562 |     dlaccess%is_open = c_associated (dlaccess%handle)
{% endraw %}

```