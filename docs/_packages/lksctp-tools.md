---
name: "lksctp-tools"
layout: package
next_package: llvm
previous_package: linux-pam
languages: ['c']
---
## 1.0.18
2 / 128 files match, 1 filtered matches.

 - [src/withsctp/sctp_load_libs.c](#srcwithsctpsctp_load_libsc)

### src/withsctp/sctp_load_libs.c

```c

{% raw %}
42 | {
43 |     if (NULL != lib_handle) return; /* Only init once.  */
44 | 
45 |     if (!(lib_handle = dlopen("libc.so", RTLD_LAZY))) {
46 | 	if (!(lib_handle = dlopen("libc.so.6", RTLD_LAZY))) {
47 | 	    fprintf(stderr, "error loading libc!\n");
48 | 	    exit (1);
{% endraw %}

```