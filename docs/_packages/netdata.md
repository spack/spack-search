---
name: "netdata"
layout: package
next_package: dakota
previous_package: libproxy
languages: ['c']
---
## 1.22.1
2 / 1590 files match, 1 filtered matches.

 - [collectors/ebpf_process.plugin/ebpf_process.c](#collectorsebpf_processpluginebpf_processc)

### collectors/ebpf_process.plugin/ebpf_process.c

```c

{% raw %}
674 |     libnetdata = dlopen(lpath, RTLD_LAZY);
{% endraw %}

```