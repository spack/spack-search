---
name: "go"
layout: package
next_package: libbsd
previous_package: lammps
languages: ['cpp', 'go']
---
## 1.6.4
9 / 5019 files match

 - [src/runtime/rt0_linux_arm.s](#srcruntimert0_linux_arms)
 - [src/runtime/cgo/gcc_openbsd_386.c](#srcruntimecgogcc_openbsd_386c)
 - [src/runtime/cgo/gcc_openbsd_amd64.c](#srcruntimecgogcc_openbsd_amd64c)
 - [src/cmd/link/internal/ld/lib.go](#srccmdlinkinternalldlibgo)
 - [misc/cgo/testcshared/main5.c](#misccgotestcsharedmain5c)
 - [misc/cgo/testcshared/main1.c](#misccgotestcsharedmain1c)
 - [misc/cgo/testcshared/main3.c](#misccgotestcsharedmain3c)
 - [misc/cgo/testcshared/main4.c](#misccgotestcsharedmain4c)
 - [misc/cgo/test/issue4029.go](#misccgotestissue4029go)

### src/runtime/rt0_linux_arm.s

```

{% raw %}
15 | 	// Preserve callee-save registers.  Raspberry Pi's dlopen(), for example,
{% endraw %}

```
### src/runtime/cgo/gcc_openbsd_386.c

```cpp

{% raw %}
73 | 	handle = dlopen("libpthread.so", RTLD_LAZY);
75 | 		fprintf(stderr, "runtime/cgo: dlopen failed to load libpthread: %s\n", dlerror());
{% endraw %}

```
### src/runtime/cgo/gcc_openbsd_amd64.c

```cpp

{% raw %}
73 | 	handle = dlopen("libpthread.so", RTLD_LAZY);
75 | 		fprintf(stderr, "runtime/cgo: dlopen failed to load libpthread: %s\n", dlerror());
{% endraw %}

```
### src/cmd/link/internal/ld/lib.go

```go

{% raw %}
1128 | 	// Force global symbols to be exported for dlopen, etc.
{% endraw %}

```
### misc/cgo/testcshared/main5.c

```cpp

{% raw %}
52 | 		printf("calling dlopen\n");
55 | 	handle = dlopen(argv[1], RTLD_NOW | RTLD_GLOBAL);
{% endraw %}

```
### misc/cgo/testcshared/main1.c

```cpp

{% raw %}
43 |   void* handle = dlopen(argv[1], RTLD_LAZY | RTLD_GLOBAL);
{% endraw %}

```
### misc/cgo/testcshared/main3.c

```cpp

{% raw %}
11 |   void* handle = dlopen(argv[1], RTLD_LAZY | RTLD_GLOBAL);
{% endraw %}

```
### misc/cgo/testcshared/main4.c

```cpp

{% raw %}
108 | 		printf("calling dlopen\n");
111 | 	handle = dlopen(argv[1], RTLD_NOW | RTLD_GLOBAL);
{% endraw %}

```
### misc/cgo/test/issue4029.go

```go

{% raw %}
53 | 	this_process := C.dlopen(nil, C.RTLD_NOW)
55 | 		t.Error("dlopen:", C.GoString(C.dlerror()))
{% endraw %}

```