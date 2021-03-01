---
name: "procps"
layout: package
next_package: None
previous_package: None
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 3.3.15
2 / 173 files match, 2 filtered matches.

 - [ps/output.c](#psoutputc)
 - [proc/numa.c](#procnumac)

### ps/output.c

```c

{% raw %}
1319 |   if(!ps_getpidcon && !tried_load){
1320 |     void *handle = dlopen("libselinux.so.1", RTLD_NOW);
1321 |     if(handle){
1322 |       ps_freecon = dlsym(handle, "freecon");
1323 |       if(dlerror())
1324 |         ps_freecon = 0;
1325 |       dlerror();
1326 |       ps_getpidcon = dlsym(handle, "getpidcon");
1327 |       if(dlerror())
1328 |         ps_getpidcon = 0;
1329 |       ps_is_selinux_enabled = dlsym(handle, "is_selinux_enabled");
1330 |       if(dlerror())
1331 |         ps_is_selinux_enabled = 0;
{% endraw %}

```
### proc/numa.c

```c

{% raw %}
69 |     // we'll try for the most recent version, then a version we know works...
70 |     if ((libnuma_handle = dlopen("libnuma.so", RTLD_LAZY))
71 |     || (libnuma_handle = dlopen("libnuma.so.1", RTLD_LAZY))) {
72 |         numa_max_node = dlsym(libnuma_handle, "numa_max_node");
73 |         numa_node_of_cpu = dlsym(libnuma_handle, "numa_node_of_cpu");
74 |         if (numa_max_node == NULL
75 |         || (numa_node_of_cpu == NULL)) {
{% endraw %}

```