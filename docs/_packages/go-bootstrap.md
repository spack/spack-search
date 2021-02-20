---
name: "go-bootstrap"
layout: package
next_package: gobject-introspection
previous_package: go
languages: ['go', 'c']
---
## 1.4-bootstrap-20161024
9 / 4257 files match, 5 filtered matches.

 - [src/runtime/syscall_solaris.go](#srcruntimesyscall_solarisgo)
 - [src/runtime/cgo/gcc_openbsd_386.c](#srcruntimecgogcc_openbsd_386c)
 - [src/runtime/cgo/gcc_openbsd_amd64.c](#srcruntimecgogcc_openbsd_amd64c)
 - [src/syscall/so_solaris.go](#srcsyscallso_solarisgo)
 - [misc/cgo/test/issue4029.go](#misccgotestissue4029go)

### src/runtime/syscall_solaris.go

```go

{% raw %}
9 | 	libc_chdir,
10 | 	libc_chroot,
11 | 	libc_close,
12 | 	libc_dlopen,
13 | 	libc_dlclose,
14 | 	libc_dlsym,
86 | 	return int32(sysvicall1(&libc_close, uintptr(fd)))
87 | }
88 | 
89 | func syscall_dlopen(name *byte, mode uintptr) (handle uintptr, err uintptr) {
90 | 	call := libcall{
91 | 		fn:   uintptr(unsafe.Pointer(&libc_dlopen)),
92 | 		n:    2,
93 | 		args: uintptr(unsafe.Pointer(&name)),
{% endraw %}

```
### src/runtime/cgo/gcc_openbsd_386.c

```c

{% raw %}
68 | 	void *handle;
69 | 
70 | 	// Locate symbol for the system pthread_create function.
71 | 	handle = dlopen("libpthread.so", RTLD_LAZY);
72 | 	if(handle == NULL) {
73 | 		fprintf(stderr, "runtime/cgo: dlopen failed to load libpthread: %s\n", dlerror());
74 | 		abort();
75 | 	}
{% endraw %}

```
### src/runtime/cgo/gcc_openbsd_amd64.c

```c

{% raw %}
68 | 	void *handle;
69 | 
70 | 	// Locate symbol for the system pthread_create function.
71 | 	handle = dlopen("libpthread.so", RTLD_LAZY);
72 | 	if(handle == NULL) {
73 | 		fprintf(stderr, "runtime/cgo: dlopen failed to load libpthread: %s\n", dlerror());
74 | 		abort();
75 | 	}
{% endraw %}

```
### src/syscall/so_solaris.go

```go

{% raw %}
22 | func rawSysvicall6(trap, nargs, a1, a2, a3, a4, a5, a6 uintptr) (r1, r2 uintptr, err Errno)
23 | func sysvicall6(trap, nargs, a1, a2, a3, a4, a5, a6 uintptr) (r1, r2 uintptr, err Errno)
24 | func dlclose(handle uintptr) (err Errno)
25 | func dlopen(name *uint8, mode uintptr) (handle uintptr, err Errno)
26 | func dlsym(handle uintptr, name *uint8) (proc uintptr, err Errno)
27 | 
37 | 	if err != nil {
38 | 		return nil, err
39 | 	}
40 | 	h, e := dlopen(namep, 1) // RTLD_LAZY
41 | 	use(unsafe.Pointer(namep))
42 | 	if e != 0 {
{% endraw %}

```
### misc/cgo/test/issue4029.go

```go

{% raw %}
44 | }
45 | 
46 | func loadThySelf(t *testing.T, symbol string) {
47 | 	this_process := C.dlopen(nil, C.RTLD_NOW)
48 | 	if this_process == nil {
49 | 		t.Error("dlopen:", C.GoString(C.dlerror()))
50 | 		return
51 | 	}
{% endraw %}

```