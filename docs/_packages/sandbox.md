---
name: "sandbox"
layout: package
next_package: portcullis
previous_package: gmp
languages: ['c']
---
## 2.12
6 / 419 files match

 - [libsbutil/get_sandbox_lib.c](#libsbutilget_sandbox_libc)
 - [libsandbox/wrappers.c](#libsandboxwrappersc)

### libsbutil/get_sandbox_lib.c

```c

{% raw %}
26 | 		void *hndl = dlopen(path, RTLD_LAZY);
{% endraw %}

```
### libsandbox/wrappers.c

```c

{% raw %}
26 | 	libc_handle = dlopen(LIBC_VERSION, RTLD_LAZY);
30 | 		fprintf(stderr, "libsandbox:  Can't dlopen libc: %s\n",
{% endraw %}

```