---
name: "lksctp-tools"
layout: package
next_package: cgm
previous_package: weechat
languages: ['c']
---
## 1.0.18
2 / 128 files match, 1 filtered matches.

 - [src/withsctp/sctp_load_libs.c](#srcwithsctpsctp_load_libsc)

### src/withsctp/sctp_load_libs.c

```c

{% raw %}
45 |     if (!(lib_handle = dlopen("libc.so", RTLD_LAZY))) {
46 | 	if (!(lib_handle = dlopen("libc.so.6", RTLD_LAZY))) {
{% endraw %}

```