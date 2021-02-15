---
name: "lksctp-tools"
layout: package
next_package: cgm
previous_package: weechat
languages: ['cpp']
---
## 1.0.18
2 / 128 files match

 - [src/withsctp/sctp_socket.h](#srcwithsctpsctp_socketh)
 - [src/withsctp/sctp_load_libs.c](#srcwithsctpsctp_load_libsc)

### src/withsctp/sctp_socket.h

```cpp

{% raw %}
57 | #include <dlfcn.h> /* for dlopen() and company */
{% endraw %}

```
### src/withsctp/sctp_load_libs.c

```cpp

{% raw %}
45 |     if (!(lib_handle = dlopen("libc.so", RTLD_LAZY))) {
46 | 	if (!(lib_handle = dlopen("libc.so.6", RTLD_LAZY))) {
{% endraw %}

```