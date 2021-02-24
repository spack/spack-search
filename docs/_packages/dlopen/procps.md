---
name: "procps"
layout: package
next_package: rsync
previous_package: openssl
library_name: dlopen
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 3.3.15
5 / 173 files match, 3 filtered matches.

 - [ps/output.c](#psoutputc)
 - [proc/numa.c](#procnumac)
 - [top/top.c](#toptopc)

### ps/output.c

```c

{% raw %}
1317 |   static int tried_load = 0;
1318 | 
1319 |   if(!ps_getpidcon && !tried_load){
1320 |     void *handle = dlopen("libselinux.so.1", RTLD_NOW);
1321 |     if(handle){
1322 |       ps_freecon = dlsym(handle, "freecon");
{% endraw %}

```
### proc/numa.c

```c

{% raw %}
67 | #ifndef NUMA_DISABLE
68 |  #ifndef PRETEND_NUMA
69 |     // we'll try for the most recent version, then a version we know works...
70 |     if ((libnuma_handle = dlopen("libnuma.so", RTLD_LAZY))
71 |     || (libnuma_handle = dlopen("libnuma.so.1", RTLD_LAZY))) {
72 |         numa_max_node = dlsym(libnuma_handle, "numa_max_node");
73 |         numa_node_of_cpu = dlsym(libnuma_handle, "numa_node_of_cpu");
{% endraw %}

```
### top/top.c

```c

{% raw %}
4493 |       make sure he does not corrupt poor ol' top's first output screen!
4494 |       Yes, he provides some overridable 'weak' functions to change such
4495 |       behavior but we can't exploit that since we don't follow a normal
4496 |       ld route to symbol resolution (we use that dlopen() guy instead)! */
4497 |    Stderr_save = dup(fileno(stderr));
4498 |    if (-1 < Stderr_save && freopen("/dev/null", "w", stderr))
{% endraw %}

```