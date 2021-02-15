---
name: "fio"
layout: package
next_package: protobuf-c
previous_package: libwebp
languages: ['cpp']
---
## 3.19
3 / 446 files match

 - [ioengines.c](#ioenginesc)
 - [os/windows/posix.c](#oswindowsposixc)
 - [os/windows/posix/include/dlfcn.h](#oswindowsposixincludedlfcnh)

### ioengines.c

```cpp

{% raw %}
77 | static struct ioengine_ops *dlopen_ioengine(struct thread_data *td,
86 | 	dlhandle = dlopen(engine_lib, RTLD_LAZY);
88 | 		td_vmsg(td, -1, dlerror(), "dlopen");
151 | 	 * Try to load ->ioengine first, and if failed try to dlopen(3) either
159 | 		ops = dlopen_ioengine(td, name);
163 | 	 * dlopen(3) either ->ioengine or ->ioengine_so_path as a path.
{% endraw %}

```
### os/windows/posix.c

```cpp

{% raw %}
252 | void *dlopen(const char *file, int mode)
{% endraw %}

```
### os/windows/posix/include/dlfcn.h

```cpp

{% raw %}
5 | void *dlopen(const char *file, int mode);
{% endraw %}

```