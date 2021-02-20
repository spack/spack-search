---
name: "plplot"
layout: package
next_package: plumed
previous_package: php
languages: ['c']
---
## 5.14.0
19 / 4022 files match, 4 filtered matches.

 - [src/ltdl_win32.c](#srcltdl_win32c)
 - [src/plcore.c](#srcplcorec)
 - [include/ltdl_win32.h](#includeltdl_win32h)
 - [drivers/test-drv-info.c](#driverstest-drv-infoc)

### src/ltdl_win32.c

```c

{% raw %}
70 | //!
71 | //! @returns A handle to the shared library (if found).
72 | //!
73 | lt_dlhandle lt_dlopenext( char* dllname )
74 | {
75 |     lt_dlhandle dlhandle = (lt_dlhandle) malloc( sizeof ( struct __dlhandle ) );
{% endraw %}

```
### src/plcore.c

```c

{% raw %}
3405 |         pldebug( "plLoadDriver", "Trying to load %s on %s\n",
3406 |             driver->drvnam, drvspec );
3407 | 
3408 |         driver->dlhand = lt_dlopenext( drvspec );
3409 | 
3410 |         // A few of our drivers do not depend on other libraries.  So
3426 | // If it still isn't loaded, then we're doomed.
3427 |     if ( !driver->dlhand )
3428 |     {
3429 |         pldebug( "plLoadDriver", "lt_dlopenext failed because of "
3430 |             "the following reason:\n%s\n", lt_dlerror() );
3431 |         fprintf( stderr, "Unable to load driver: %s.\n", driver->drvnam );
{% endraw %}

```
### include/ltdl_win32.h

```c

{% raw %}
37 | 
38 | PLDLLIMPEXP void lt_dlexit( void );
39 | 
40 | PLDLLIMPEXP lt_dlhandle lt_dlopenext( char* dllname );
41 | 
42 | PLDLLIMPEXP const char* lt_dlerror();
{% endraw %}

```
### drivers/test-drv-info.c

```c

{% raw %}
76 | #else
77 |     snprintf( drvspec, DRVSPEC_LEN, "%s/%s%s", plGetDrvDir(), library_target_prefix, drvnam );
78 | #endif // LTDL_WIN32
79 |     dlhand = lt_dlopenext( drvspec );
80 |     if ( dlhand == NULL )
81 |     {
{% endraw %}

```