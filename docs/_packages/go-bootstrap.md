---
name: "go-bootstrap"
layout: package
next_package: octave
previous_package: fontconfig
languages: ['go', 'c']
---
## 1.4-bootstrap-20161024
9 / 4257 files match

 - [src/runtime/syscall_solaris.go](#srcruntimesyscall_solarisgo)
 - [src/runtime/cgo/gcc_openbsd_386.c](#srcruntimecgogcc_openbsd_386c)
 - [src/runtime/cgo/gcc_openbsd_amd64.c](#srcruntimecgogcc_openbsd_amd64c)
 - [src/syscall/so_solaris.go](#srcsyscallso_solarisgo)
 - [misc/cgo/test/issue4029.go](#misccgotestissue4029go)

### src/runtime/syscall_solaris.go

```go

{% raw %}
12 | 	libc_dlopen,
89 | func syscall_dlopen(name *byte, mode uintptr) (handle uintptr, err uintptr) {
91 | 		fn:   uintptr(unsafe.Pointer(&libc_dlopen)),
{% endraw %}

```
### src/runtime/cgo/gcc_openbsd_386.c

```c

{% raw %}
71 | 	handle = dlopen("libpthread.so", RTLD_LAZY);
73 | 		fprintf(stderr, "runtime/cgo: dlopen failed to load libpthread: %s\n", dlerror());
{% endraw %}

```
### src/runtime/cgo/gcc_openbsd_amd64.c

```c

{% raw %}
71 | 	handle = dlopen("libpthread.so", RTLD_LAZY);
73 | 		fprintf(stderr, "runtime/cgo: dlopen failed to load libpthread: %s\n", dlerror());
{% endraw %}

```
### src/syscall/so_solaris.go

```go

{% raw %}
25 | func dlopen(name *uint8, mode uintptr) (handle uintptr, err Errno)
40 | 	h, e := dlopen(namep, 1) // RTLD_LAZY
{% endraw %}

```
### misc/cgo/test/issue4029.go

```go

{% raw %}
47 | 	this_process := C.dlopen(nil, C.RTLD_NOW)
49 | 		t.Error("dlopen:", C.GoString(C.dlerror()))
{% endraw %}

```