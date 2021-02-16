---
name: "ghostscript"
layout: package
next_package: git
previous_package: gflags
languages: ['c']
---
## 9.27
19 / 4764 files match, 4 filtered matches.

 - [base/gp_unix.c](#basegp_unixc)
 - [base/memento.c](#basemementoc)
 - [jbig2dec/memento.c](#jbig2decmementoc)
 - [contrib/opvp/gdevopvp.c](#contribopvpgdevopvpc)

### base/gp_unix.c

```c

{% raw %}
77 |     if ((handle = dlopen(buff, RTLD_NOW)) != 0) {
{% endraw %}

```
### base/memento.c

```c

{% raw %}
555 |     libbt = dlopen("libbacktrace.so", RTLD_LAZY);
557 |         libbt = dlopen("/opt/lib/libbacktrace.so", RTLD_LAZY);
559 |         libbt = dlopen("/lib/libbacktrace.so", RTLD_LAZY);
561 |         libbt = dlopen("/usr/lib/libbacktrace.so", RTLD_LAZY);
563 |         libbt = dlopen("/usr/local/lib/libbacktrace.so", RTLD_LAZY);
{% endraw %}

```
### jbig2dec/memento.c

```c

{% raw %}
555 |     libbt = dlopen("libbacktrace.so", RTLD_LAZY);
557 |         libbt = dlopen("/opt/lib/libbacktrace.so", RTLD_LAZY);
559 |         libbt = dlopen("/lib/libbacktrace.so", RTLD_LAZY);
561 |         libbt = dlopen("/usr/lib/libbacktrace.so", RTLD_LAZY);
563 |         libbt = dlopen("/usr/local/lib/libbacktrace.so", RTLD_LAZY);
{% endraw %}

```
### contrib/opvp/gdevopvp.c

```c

{% raw %}
1780 |             if ((h = dlopen(list[i],RTLD_NOW))) {
{% endraw %}

```