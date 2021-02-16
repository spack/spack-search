---
name: "plplot"
layout: package
next_package: llvm-doe
previous_package: libnbc
languages: ['c']
---
## 5.14.0
19 / 4022 files match

 - [src/ltdl_win32.c](#srcltdl_win32c)
 - [src/plcore.c](#srcplcorec)
 - [include/ltdl_win32.h](#includeltdl_win32h)
 - [drivers/test-drv-info.c](#driverstest-drv-infoc)

### src/ltdl_win32.c

```c

{% raw %}
73 | lt_dlhandle lt_dlopenext( char* dllname )
{% endraw %}

```
### src/plcore.c

```c

{% raw %}
3408 |         driver->dlhand = lt_dlopenext( drvspec );
3429 |         pldebug( "plLoadDriver", "lt_dlopenext failed because of "
{% endraw %}

```
### include/ltdl_win32.h

```c

{% raw %}
40 | PLDLLIMPEXP lt_dlhandle lt_dlopenext( char* dllname );
{% endraw %}

```
### drivers/test-drv-info.c

```c

{% raw %}
79 |     dlhand = lt_dlopenext( drvspec );
{% endraw %}

```