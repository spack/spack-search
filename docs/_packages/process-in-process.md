---
name: "process-in-process"
layout: package
next_package: iperf3
previous_package: itk
languages: ['c']
---
## 2
6 / 584 files match, 4 filtered matches.

 - [PiP-Testsuite/PiP-Testsuite/compat/pip_dlopen.c](#pip-testsuitepip-testsuitecompatpip_dlopenc)
 - [lib/pip_dlfcn.c](#libpip_dlfcnc)
 - [lib/pip.c](#libpipc)
 - [include/pip/pip_dlfcn.h](#includepippip_dlfcnh)

### PiP-Testsuite/PiP-Testsuite/compat/pip_dlopen.c

```c

{% raw %}
39 | void *pip_dlopen( const char*, int );
48 |   CHECK( handle = pip_dlopen( LIBNAME, RTLD_LAZY ),
{% endraw %}

```
### lib/pip_dlfcn.c

```c

{% raw %}
41 | void *pip_dlopen( const char *filename, int flag ) {
44 |   handle = dlopen( filename, flag );
{% endraw %}

```
### lib/pip.c

```c

{% raw %}
503 |     pip_root->task_root->loaded = dlopen( NULL, RTLD_NOW );
{% endraw %}

```
### include/pip/pip_dlfcn.h

```c

{% raw %}
43 |   void *pip_dlopen( const char *filename, int flag );
{% endraw %}

```