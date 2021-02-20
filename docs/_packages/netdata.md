---
name: "netdata"
layout: package
next_package: netperf
previous_package: nest
languages: ['c']
---
## 1.22.1
2 / 1590 files match, 1 filtered matches.

 - [collectors/ebpf_process.plugin/ebpf_process.c](#collectorsebpf_processpluginebpf_processc)

### collectors/ebpf_process.plugin/ebpf_process.c

```c

{% raw %}
671 |     char lpath[4096];
672 | 
673 |     build_complete_path(lpath, 4096, plugin_dir, "libnetdata_ebpf.so");
674 |     libnetdata = dlopen(lpath, RTLD_LAZY);
675 |     if (!libnetdata) {
676 |         error("[EBPF_PROCESS] Cannot load %s.", lpath);
{% endraw %}

```