---
name: "openfast"
layout: package
next_package: exmcutils
previous_package: mpfi
languages: ['fortran']
---
## develop
8 / 777 files match, 6 filtered matches.

 - [modules/icefloe/src/interfaces/Console/NWTC_Base_reduced.f90](#modulesicefloesrcinterfacesconsolenwtc_base_reducedf90)
 - [modules/nwtc-library/src/SysGnuLinux.f90](#modulesnwtc-librarysrcsysgnulinuxf90)
 - [modules/nwtc-library/src/SysMatlabLinuxIntel.f90](#modulesnwtc-librarysrcsysmatlablinuxintelf90)
 - [modules/nwtc-library/src/SysIFL.f90](#modulesnwtc-librarysrcsysiflf90)
 - [modules/nwtc-library/src/NWTC_Base.f90](#modulesnwtc-librarysrcnwtc_basef90)
 - [modules/nwtc-library/src/SysMatlabLinuxGnu.f90](#modulesnwtc-librarysrcsysmatlablinuxgnuf90)

### modules/icefloe/src/interfaces/Console/NWTC_Base_reduced.f90

```fortran

{% raw %}
59 | !      TYPE(C_PTR)               :: FileAddrX                                       ! The address of file FileName.         (RETURN value dlopen ) [Linux]
{% endraw %}

```
### modules/nwtc-library/src/SysGnuLinux.f90

```fortran

{% raw %}
415 |    INTEGER(C_INT), PARAMETER :: RTLD_NOW=2             ! "If this value is specified, or the environment variable LD_BIND_NOW is set to a nonempty string, all undefined symbols in the library are resolved before dlopen() returns. If this cannot be done, an error is returned."
420 |       !bjj see http://linux.die.net/man/3/dlopen
421 |       !    and https://developer.apple.com/library/mac/documentation/Darwin/Reference/ManPages/man3/dlopen.3.html
423 |       FUNCTION dlOpen(filename,mode) BIND(C,NAME="dlopen")
424 |       ! void *dlopen(const char *filename, int mode);
{% endraw %}

```
### modules/nwtc-library/src/SysMatlabLinuxIntel.f90

```fortran

{% raw %}
397 |    INTEGER(C_INT), PARAMETER :: RTLD_NOW=2             ! "If this value is specified, or the environment variable LD_BIND_NOW is set to a nonempty string, all undefined symbols in the library are resolved before dlopen() returns. If this cannot be done, an error is returned."
402 |       !bjj see http://linux.die.net/man/3/dlopen
403 |       !    and https://developer.apple.com/library/mac/documentation/Darwin/Reference/ManPages/man3/dlopen.3.html
405 |       FUNCTION dlOpen(filename,mode) BIND(C,NAME="dlopen")
406 |       ! void *dlopen(const char *filename, int mode);
{% endraw %}

```
### modules/nwtc-library/src/SysIFL.f90

```fortran

{% raw %}
393 |    INTEGER(C_INT), PARAMETER :: RTLD_NOW=2             ! "If this value is specified, or the environment variable LD_BIND_NOW is set to a nonempty string, all undefined symbols in the library are resolved before dlopen() returns. If this cannot be done, an error is returned."
398 |       !bjj see http://linux.die.net/man/3/dlopen
399 |       !    and https://developer.apple.com/library/mac/documentation/Darwin/Reference/ManPages/man3/dlopen.3.html
401 |       FUNCTION dlOpen(filename,mode) BIND(C,NAME="dlopen")
402 |       ! void *dlopen(const char *filename, int mode);
{% endraw %}

```
### modules/nwtc-library/src/NWTC_Base.f90

```fortran

{% raw %}
65 |       TYPE(C_PTR)               :: FileAddrX = C_NULL_PTR                          !< The address of file FileName.         (RETURN value from dlopen ) [Linux]
{% endraw %}

```
### modules/nwtc-library/src/SysMatlabLinuxGnu.f90

```fortran

{% raw %}
405 |    INTEGER(C_INT), PARAMETER :: RTLD_NOW=2             ! "If this value is specified, or the environment variable LD_BIND_NOW is set to a nonempty string, all undefined symbols in the library are resolved before dlopen() returns. If this cannot be done, an error is returned."
410 |       !bjj see http://linux.die.net/man/3/dlopen
411 |       !    and https://developer.apple.com/library/mac/documentation/Darwin/Reference/ManPages/man3/dlopen.3.html
413 |       FUNCTION dlOpen(filename,mode) BIND(C,NAME="dlopen")
414 |       ! void *dlopen(const char *filename, int mode);
{% endraw %}

```