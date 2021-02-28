---
name: "sandbox"
layout: package
next_package: python
previous_package: rdc
library_name: dlopen
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 2.12
6 / 419 files match, 2 filtered matches.

 - [libsbutil/get_sandbox_lib.c](#libsbutilget_sandbox_libc)
 - [libsandbox/wrappers.c](#libsandboxwrappersc)

### libsbutil/get_sandbox_lib.c

```c

{% raw %}
23 | 	save_errno();
24 | 	strcpy(path, LIB_NAME);
25 | 	if (strncmp("/usr/lib", LIBSANDBOX_PATH, 8)) {
26 | 		void *hndl = dlopen(path, RTLD_LAZY);
27 | 		if (!hndl)
28 | 			snprintf(path, SB_PATH_MAX, "%s/%s", LIBSANDBOX_PATH, LIB_NAME);
{% endraw %}

```
### libsandbox/wrappers.c

```c

{% raw %}
23 | static void load_libc_handle(void)
24 | {
25 | 	save_errno();	/* #260765 */
26 | 	libc_handle = dlopen(LIBC_VERSION, RTLD_LAZY);
27 | 	restore_errno();
28 | 
29 | 	if (!libc_handle) {
30 | 		fprintf(stderr, "libsandbox:  Can't dlopen libc: %s\n",
31 | 			dlerror());
32 | 		exit(EXIT_FAILURE);
{% endraw %}

```