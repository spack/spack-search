---
name: "whizard"
layout: package
next_package: wireshark
previous_package: watch
languages: ['fortran']
---
## 2.8.3
11 / 3957 files match, 2 filtered matches.

 - [src/system/os_interface.f90_mpi](#srcsystemos_interfacef90_mpi)
 - [src/system/os_interface.f90_serial](#srcsystemos_interfacef90_serial)

### src/system/os_interface.f90_mpi

```fortran

{% raw %}
165 |      function dlopen (filename, flag) result (handle) bind(C)
170 |      end function dlopen
560 |     dlaccess%handle = dlopen (char (filename) // c_null_char, ior ( &
{% endraw %}

```
### src/system/os_interface.f90_serial

```fortran

{% raw %}
165 |      function dlopen (filename, flag) result (handle) bind(C)
170 |      end function dlopen
560 |     dlaccess%handle = dlopen (char (filename) // c_null_char, ior ( &
{% endraw %}

```