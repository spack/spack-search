---
name: "pocl"
layout: package
next_package: libpng
previous_package: swipl
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 1.6
3 / 1647 files match, 2 filtered matches.

 - [lib/CL/devices/common.c](#libcldevicescommonc)
 - [lib/CL/devices/devices.c](#libcldevicesdevicesc)

### lib/CL/devices/common.c

```c

{% raw %}
1095 |   snprintf (workgroup_string, WORKGROUP_STRING_LENGTH,
1096 |             "_pocl_kernel_%s_workgroup", run_cmd->kernel->name);
1097 | 
1098 |   ci->wg = dlsym (ci->dlhandle, workgroup_string);
1099 |   dl_error = dlerror ();
1100 | 
1103 |       // Older OSX dyld APIs need the name without the underscore.
1104 |       snprintf (workgroup_string, WORKGROUP_STRING_LENGTH,
1105 |                 "pocl_kernel_%s_workgroup", run_cmd->kernel->name);
1106 |       ci->wg = dlsym (ci->dlhandle, workgroup_string);
1107 |       dl_error = dlerror ();
1108 | 
1109 |       if (ci->wg == NULL || dl_error != NULL)
1110 |         POCL_ABORT ("dlsym(\"%s\", \"%s\") failed with '%s'.\n"
1111 |                     "note: missing symbols in the kernel binary might be"
1112 |                     " reported as 'file not found' errors.\n",
{% endraw %}

```
### lib/CL/devices/devices.c

```c

{% raw %}
592 |           strcat (init_device_ops_name, "_init_device_ops");
593 |           if (pocl_device_handles[i] != NULL)
594 |             {
595 |               pocl_devices_init_ops[i] = (init_device_ops)dlsym (
596 |                   pocl_device_handles[i], init_device_ops_name);
597 |               pocl_devices_init_ops[i](&pocl_device_ops[i]);
{% endraw %}

```