---
name: "procps"
layout: package
next_package: prrte
previous_package: process-in-process
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
4496 |       ld route to symbol resolution (we use that dlopen() guy instead)! */
{% endraw %}

```