---
name: "procps-ng"
layout: package
next_package: udunits
previous_package: r-rsqlite
languages: ['c']
---
## 3.3.16
9 / 269 files match

 - [ps/output.c](#psoutputc)
 - [proc/numa.c](#procnumac)
 - [top/top.c](#toptopc)

### ps/output.c

```c

{% raw %}
1320 |     void *handle = dlopen("libselinux.so.1", RTLD_NOW);
{% endraw %}

```
### proc/numa.c

```c

{% raw %}
70 |     if ((libnuma_handle = dlopen("libnuma.so", RTLD_LAZY))
71 |     || (libnuma_handle = dlopen("libnuma.so.1", RTLD_LAZY))) {
{% endraw %}

```
### top/top.c

```c

{% raw %}
4650 |       ld route to symbol resolution (we use that dlopen() guy instead)! */
{% endraw %}

```