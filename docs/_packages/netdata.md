---
name: "netdata"
layout: package
next_package: dakota
previous_package: libproxy
languages: ['cpp']
---
## 1.22.1
2 / 1590 files match

 - [configure.ac](#configureac)
 - [collectors/ebpf_process.plugin/ebpf_process.c](#collectorsebpf_processpluginebpf_processc)

### configure.ac

```

{% raw %}
386 |     [dlopen],
{% endraw %}

```
### collectors/ebpf_process.plugin/ebpf_process.c

```cpp

{% raw %}
674 |     libnetdata = dlopen(lpath, RTLD_LAZY);
{% endraw %}

```