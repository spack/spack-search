---
name: "sandbox"
layout: package
next_package: scorep
previous_package: rust
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 2.12
9 / 419 files match, 5 filtered matches.

 - [libsandbox/libsandbox.h](#libsandboxlibsandboxh)
 - [libsandbox/wrappers.c](#libsandboxwrappersc)
 - [libsandbox/memory.c](#libsandboxmemoryc)
 - [libsandbox/wrapper-funcs/__wrapper_simple.c](#libsandboxwrapper-funcs__wrapper_simplec)
 - [libsandbox/wrapper-funcs/__wrapper_exec.c](#libsandboxwrapper-funcs__wrapper_execc)

### libsandbox/libsandbox.h

```c

{% raw %}
51 | bool before_syscall_open_int(int, int, const char *, const char *, int);
52 | bool before_syscall_open_char(int, int, const char *, const char *, const char *);
53 | 
54 | void *get_dlsym(const char *symname, const char *symver);
55 | 
56 | extern char sandbox_lib[SB_PATH_MAX];
{% endraw %}

```
### libsandbox/wrappers.c

```c

{% raw %}
33 | 	}
34 | }
35 | 
36 | void *get_dlsym(const char *symname, const char *symver)
37 | {
38 | 	void *symaddr;
47 | 	}
48 | 
49 | 	if (NULL == symver)
50 | 		symaddr = dlsym(libc_handle, symname);
51 | 	else
52 | 		symaddr = dlvsym(libc_handle, symname, symver);
78 | #define check_dlsym(_name, _symname, _symver) \
79 | { \
80 | 	if (NULL == _name) \
81 | 		_name = get_dlsym(_symname, _symver); \
82 | }
83 | 
{% endraw %}

```
### libsandbox/memory.c

```c

{% raw %}
24 | static void *sb_mmap(void *addr, size_t length, int prot, int flags, int fd, off_t offset)
25 | {
26 | 	if (!_sb_mmap)
27 | 		_sb_mmap = get_dlsym("mmap", NULL);
28 | 	return _sb_mmap(addr, length, prot, flags, fd, offset);
29 | }
32 | static int sb_munmap(void *addr, size_t length)
33 | {
34 | 	if (!_sb_munmap)
35 | 		_sb_munmap = get_dlsym("munmap", NULL);
36 | 	return _sb_munmap(addr, length);
37 | }
{% endraw %}

```
### libsandbox/wrapper-funcs/__wrapper_simple.c

```c

{% raw %}
39 | attribute_hidden
40 | WRAPPER_RET_TYPE SB_HIDDEN_FUNC(WRAPPER_NAME)(WRAPPER_ARGS_PROTO_FULL)
41 | {
42 | 	check_dlsym(WRAPPER_TRUE_NAME, WRAPPER_SYMNAME, WRAPPER_SYMVER);
43 | 	return WRAPPER_TRUE_NAME(WRAPPER_ARGS_FULL);
44 | }
{% endraw %}

```
### libsandbox/wrapper-funcs/__wrapper_exec.c

```c

{% raw %}
214 | attribute_hidden
215 | WRAPPER_RET_TYPE SB_HIDDEN_FUNC(WRAPPER_NAME)(WRAPPER_ARGS_PROTO_FULL)
216 | {
217 | 	check_dlsym(WRAPPER_TRUE_NAME, WRAPPER_SYMNAME, WRAPPER_SYMVER);
218 | 	return WRAPPER_TRUE_NAME(WRAPPER_ARGS_FULL);
219 | }
{% endraw %}

```