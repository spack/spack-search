---
name: "openfast"
layout: package
next_package: openfoam
previous_package: opendx
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
56 | !   TYPE DLL_Type
57 | !
58 | !      INTEGER(C_INTPTR_T)       :: FileAddr                                        ! The address of file FileName.         (RETURN value from LoadLibrary ) [Windows]
59 | !      TYPE(C_PTR)               :: FileAddrX                                       ! The address of file FileName.         (RETURN value dlopen ) [Linux]
60 | !      TYPE(C_FUNPTR)            :: ProcAddr                                        ! The address of procedure ProcName.    (RETURN value from GetProcAddress or dlsym)
61 | !
{% endraw %}

```
### modules/nwtc-library/src/SysGnuLinux.f90

```fortran

{% raw %}
412 | !bjj: these are values I found on the web; I have no idea if they actually work...
413 | !bjj: hopefully we can find them pre-defined in a header somewhere
414 |    INTEGER(C_INT), PARAMETER :: RTLD_LAZY=1            ! "Perform lazy binding. Only resolve symbols as the code that references them is executed. If the symbol is never referenced, then it is never resolved. (Lazy binding is only performed for function references; references to variables are always immediately bound when the library is loaded.) "
415 |    INTEGER(C_INT), PARAMETER :: RTLD_NOW=2             ! "If this value is specified, or the environment variable LD_BIND_NOW is set to a nonempty string, all undefined symbols in the library are resolved before dlopen() returns. If this cannot be done, an error is returned."
416 |    INTEGER(C_INT), PARAMETER :: RTLD_GLOBAL=256        ! "The symbols defined by this library will be made available for symbol resolution of subsequently loaded libraries"
417 |    INTEGER(C_INT), PARAMETER :: RTLD_LOCAL=0           ! "This is the converse of RTLD_GLOBAL, and the default if neither flag is specified. Symbols defined in this library are not made available to resolve references in subsequently loaded libraries."
418 | 
419 |    INTERFACE !linux API routines
420 |       !bjj see http://linux.die.net/man/3/dlopen
421 |       !    and https://developer.apple.com/library/mac/documentation/Darwin/Reference/ManPages/man3/dlopen.3.html
422 | 
423 |       FUNCTION dlOpen(filename,mode) BIND(C,NAME="dlopen")
424 |       ! void *dlopen(const char *filename, int mode);
425 |          USE ISO_C_BINDING
426 |          IMPLICIT NONE
{% endraw %}

```
### modules/nwtc-library/src/SysMatlabLinuxIntel.f90

```fortran

{% raw %}
394 | !bjj: these are values I found on the web; I have no idea if they actually work...
395 | !bjj: hopefully we can find them pre-defined in a header somewhere
396 |    INTEGER(C_INT), PARAMETER :: RTLD_LAZY=1            ! "Perform lazy binding. Only resolve symbols as the code that references them is executed. If the symbol is never referenced, then it is never resolved. (Lazy binding is only performed for function references; references to variables are always immediately bound when the library is loaded.) "
397 |    INTEGER(C_INT), PARAMETER :: RTLD_NOW=2             ! "If this value is specified, or the environment variable LD_BIND_NOW is set to a nonempty string, all undefined symbols in the library are resolved before dlopen() returns. If this cannot be done, an error is returned."
398 |    INTEGER(C_INT), PARAMETER :: RTLD_GLOBAL=256        ! "The symbols defined by this library will be made available for symbol resolution of subsequently loaded libraries"
399 |    INTEGER(C_INT), PARAMETER :: RTLD_LOCAL=0           ! "This is the converse of RTLD_GLOBAL, and the default if neither flag is specified. Symbols defined in this library are not made available to resolve references in subsequently loaded libraries."
400 | 
401 |    INTERFACE !linux API routines
402 |       !bjj see http://linux.die.net/man/3/dlopen
403 |       !    and https://developer.apple.com/library/mac/documentation/Darwin/Reference/ManPages/man3/dlopen.3.html
404 | 
405 |       FUNCTION dlOpen(filename,mode) BIND(C,NAME="dlopen")
406 |       ! void *dlopen(const char *filename, int mode);
407 |          USE ISO_C_BINDING
408 |          IMPLICIT NONE
{% endraw %}

```
### modules/nwtc-library/src/SysIFL.f90

```fortran

{% raw %}
390 | !bjj: these are values I found on the web; I have no idea if they actually work...
391 | !bjj: hopefully we can find them pre-defined in a header somewhere
392 |    INTEGER(C_INT), PARAMETER :: RTLD_LAZY=1            ! "Perform lazy binding. Only resolve symbols as the code that references them is executed. If the symbol is never referenced, then it is never resolved. (Lazy binding is only performed for function references; references to variables are always immediately bound when the library is loaded.) "
393 |    INTEGER(C_INT), PARAMETER :: RTLD_NOW=2             ! "If this value is specified, or the environment variable LD_BIND_NOW is set to a nonempty string, all undefined symbols in the library are resolved before dlopen() returns. If this cannot be done, an error is returned."
394 |    INTEGER(C_INT), PARAMETER :: RTLD_GLOBAL=256        ! "The symbols defined by this library will be made available for symbol resolution of subsequently loaded libraries"
395 |    INTEGER(C_INT), PARAMETER :: RTLD_LOCAL=0           ! "This is the converse of RTLD_GLOBAL, and the default if neither flag is specified. Symbols defined in this library are not made available to resolve references in subsequently loaded libraries."
396 | 
397 |    INTERFACE !linux API routines
398 |       !bjj see http://linux.die.net/man/3/dlopen
399 |       !    and https://developer.apple.com/library/mac/documentation/Darwin/Reference/ManPages/man3/dlopen.3.html
400 | 
401 |       FUNCTION dlOpen(filename,mode) BIND(C,NAME="dlopen")
402 |       ! void *dlopen(const char *filename, int mode);
403 |          USE ISO_C_BINDING
404 |          IMPLICIT NONE
{% endraw %}

```
### modules/nwtc-library/src/NWTC_Base.f90

```fortran

{% raw %}
62 |    TYPE DLL_Type 
63 | 
64 |       INTEGER(C_INTPTR_T)       :: FileAddr                                        !< The address of file FileName.         (RETURN value from LoadLibrary ) [Windows]
65 |       TYPE(C_PTR)               :: FileAddrX = C_NULL_PTR                          !< The address of file FileName.         (RETURN value from dlopen ) [Linux]
66 |       TYPE(C_FUNPTR)            :: ProcAddr(NWTC_MAX_DLL_PROC)  = C_NULL_FUNPTR    !< The address of procedure ProcName.    (RETURN value from GetProcAddress or dlsym) [initialized to Null for pack/unpack]
67 | 
{% endraw %}

```
### modules/nwtc-library/src/SysMatlabLinuxGnu.f90

```fortran

{% raw %}
402 | !bjj: these are values I found on the web; I have no idea if they actually work...
403 | !bjj: hopefully we can find them pre-defined in a header somewhere
404 |    INTEGER(C_INT), PARAMETER :: RTLD_LAZY=1            ! "Perform lazy binding. Only resolve symbols as the code that references them is executed. If the symbol is never referenced, then it is never resolved. (Lazy binding is only performed for function references; references to variables are always immediately bound when the library is loaded.) "
405 |    INTEGER(C_INT), PARAMETER :: RTLD_NOW=2             ! "If this value is specified, or the environment variable LD_BIND_NOW is set to a nonempty string, all undefined symbols in the library are resolved before dlopen() returns. If this cannot be done, an error is returned."
406 |    INTEGER(C_INT), PARAMETER :: RTLD_GLOBAL=256        ! "The symbols defined by this library will be made available for symbol resolution of subsequently loaded libraries"
407 |    INTEGER(C_INT), PARAMETER :: RTLD_LOCAL=0           ! "This is the converse of RTLD_GLOBAL, and the default if neither flag is specified. Symbols defined in this library are not made available to resolve references in subsequently loaded libraries."
408 | 
409 |    INTERFACE !linux API routines
410 |       !bjj see http://linux.die.net/man/3/dlopen
411 |       !    and https://developer.apple.com/library/mac/documentation/Darwin/Reference/ManPages/man3/dlopen.3.html
412 | 
413 |       FUNCTION dlOpen(filename,mode) BIND(C,NAME="dlopen")
414 |       ! void *dlopen(const char *filename, int mode);
415 |          USE ISO_C_BINDING
416 |          IMPLICIT NONE
{% endraw %}

```