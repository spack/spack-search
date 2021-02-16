---
name: "pocl"
layout: package
next_package: podio
previous_package: pmix
languages: ['c']
---
## 1.6
7 / 1647 files match, 2 filtered matches.

 - [lib/CL/devices/common.c](#libcldevicescommonc)
 - [lib/CL/devices/devices.c](#libcldevicesdevicesc)

### lib/CL/devices/common.c

```c

{% raw %}
1086 |   ci->dlhandle = dlopen (module_fn, RTLD_NOW | RTLD_LOCAL);
1090 |     POCL_ABORT ("dlopen(\"%s\") failed with '%s'.\n"
{% endraw %}

```
### lib/CL/devices/devices.c

```c

{% raw %}
588 |           pocl_device_handles[i] = dlopen (device_library, RTLD_LAZY);
{% endraw %}

```