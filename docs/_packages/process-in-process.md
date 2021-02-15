---
name: "process-in-process"
layout: package
next_package: iperf3
previous_package: itk
languages: ['cpp']
---
## 2
6 / 584 files match

 - [PiP-Testsuite/PiP-Testsuite/compat/compat-v3.list](#pip-testsuitepip-testsuitecompatcompat-v3list)
 - [PiP-Testsuite/PiP-Testsuite/compat/pip_dlopen.c](#pip-testsuitepip-testsuitecompatpip_dlopenc)
 - [PiP-Testsuite/PiP-Testsuite/compat/compat-v2.list](#pip-testsuitepip-testsuitecompatcompat-v2list)
 - [lib/pip_dlfcn.c](#libpip_dlfcnc)
 - [lib/pip.c](#libpipc)
 - [include/pip/pip_dlfcn.h](#includepippip_dlfcnh)

### PiP-Testsuite/PiP-Testsuite/compat/compat-v3.list

```

{% raw %}
20 | skip T UNSUPPORTED timer 1 pip_blt 1 1 ./pip_dlopen
21 | skip T UNSUPPORTED timer 1 pip_blt 8 8 ./pip_dlopen
{% endraw %}

```
### PiP-Testsuite/PiP-Testsuite/compat/pip_dlopen.c

```cpp

{% raw %}
39 | void *pip_dlopen( const char*, int );
48 |   CHECK( handle = pip_dlopen( LIBNAME, RTLD_LAZY ),
{% endraw %}

```
### PiP-Testsuite/PiP-Testsuite/compat/compat-v2.list

```

{% raw %}
4 | skip T UNSUPPORTED timer 1 pip_task 1 ./pip_dlopen
5 | skip T UNSUPPORTED timer 1 pip_task 8 ./pip_dlopen
{% endraw %}

```
### lib/pip_dlfcn.c

```cpp

{% raw %}
41 | void *pip_dlopen( const char *filename, int flag ) {
44 |   handle = dlopen( filename, flag );
{% endraw %}

```
### lib/pip.c

```cpp

{% raw %}
503 |     pip_root->task_root->loaded = dlopen( NULL, RTLD_NOW );
{% endraw %}

```
### include/pip/pip_dlfcn.h

```cpp

{% raw %}
43 |   void *pip_dlopen( const char *filename, int flag );
{% endraw %}

```