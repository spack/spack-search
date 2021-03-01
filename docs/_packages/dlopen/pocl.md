---
name: "pocl"
layout: package
next_package: podio
previous_package: pnmpi
library_name: dlopen
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 1.6
7 / 1647 files match, 2 filtered matches.

 - [lib/CL/devices/common.c](#libcldevicescommonc)
 - [lib/CL/devices/devices.c](#libcldevicesdevicesc)

### lib/CL/devices/common.c

```c

{% raw %}
1083 | 
1084 |   // reset possibly existing error from calls from an ICD loader
1085 |   (void)dlerror();
1086 |   ci->dlhandle = dlopen (module_fn, RTLD_NOW | RTLD_LOCAL);
1087 |   dl_error = dlerror ();
1088 | 
1089 |   if (ci->dlhandle == NULL || dl_error != NULL)
1090 |     POCL_ABORT ("dlopen(\"%s\") failed with '%s'.\n"
1091 |                 "note: missing symbols in the kernel binary might be"
1092 |                 " reported as 'file not found' errors.\n",
{% endraw %}

```
### lib/CL/devices/devices.c

```c

{% raw %}
585 |         {
586 |           char device_library[PATH_MAX] = "";
587 |           get_pocl_device_lib_path (device_library, pocl_device_types[i]);
588 |           pocl_device_handles[i] = dlopen (device_library, RTLD_LAZY);
589 |           char init_device_ops_name[MAX_DEV_NAME_LEN + 21] = "";
590 |           strcat (init_device_ops_name, "pocl_");
{% endraw %}

```