---
name: "fio"
layout: package
next_package: protobuf-c
previous_package: libwebp
languages: ['c']
---
## 3.19
3 / 446 files match, 3 filtered matches.

 - [ioengines.c](#ioenginesc)
 - [os/windows/posix.c](#oswindowsposixc)
 - [os/windows/posix/include/dlfcn.h](#oswindowsposixincludedlfcnh)

### ioengines.c

```c

{% raw %}
77 | static struct ioengine_ops *dlopen_ioengine(struct thread_data *td,
86 | 	dlhandle = dlopen(engine_lib, RTLD_LAZY);
88 | 		td_vmsg(td, -1, dlerror(), "dlopen");
159 | 		ops = dlopen_ioengine(td, name);
{% endraw %}

```
### os/windows/posix.c

```c

{% raw %}
252 | void *dlopen(const char *file, int mode)
{% endraw %}

```
### os/windows/posix/include/dlfcn.h

```c

{% raw %}
5 | void *dlopen(const char *file, int mode);
{% endraw %}

```