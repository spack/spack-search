---
name: "go"
layout: package
next_package: php
previous_package: apr
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c', 'go']
---
## 1.6.4
7 / 5019 files match, 7 filtered matches.

 - [src/runtime/cgo/gcc_openbsd_386.c](#srcruntimecgogcc_openbsd_386c)
 - [src/runtime/cgo/gcc_openbsd_amd64.c](#srcruntimecgogcc_openbsd_amd64c)
 - [misc/cgo/testcshared/main5.c](#misccgotestcsharedmain5c)
 - [misc/cgo/testcshared/main1.c](#misccgotestcsharedmain1c)
 - [misc/cgo/testcshared/main3.c](#misccgotestcsharedmain3c)
 - [misc/cgo/testcshared/main4.c](#misccgotestcsharedmain4c)
 - [misc/cgo/test/issue4029.go](#misccgotestissue4029go)

### src/runtime/cgo/gcc_openbsd_386.c

```c

{% raw %}
75 | 		fprintf(stderr, "runtime/cgo: dlopen failed to load libpthread: %s\n", dlerror());
76 | 		abort();
77 | 	}
78 | 	sys_pthread_create = dlsym(handle, "pthread_create");
79 | 	if(sys_pthread_create == NULL) {
80 | 		fprintf(stderr, "runtime/cgo: dlsym failed to find pthread_create: %s\n", dlerror());
81 | 		abort();
82 | 	}
{% endraw %}

```
### src/runtime/cgo/gcc_openbsd_amd64.c

```c

{% raw %}
75 | 		fprintf(stderr, "runtime/cgo: dlopen failed to load libpthread: %s\n", dlerror());
76 | 		abort();
77 | 	}
78 | 	sys_pthread_create = dlsym(handle, "pthread_create");
79 | 	if(sys_pthread_create == NULL) {
80 | 		fprintf(stderr, "runtime/cgo: dlsym failed to find pthread_create: %s\n", dlerror());
81 | 		abort();
82 | 	}
{% endraw %}

```
### misc/cgo/testcshared/main5.c

```c

{% raw %}
91 | 	// Tell the Go code to catch SIGIO.
92 | 
93 | 	if (verbose) {
94 | 		printf("calling dlsym\n");
95 | 	}
96 | 
97 | 	fn1 = (void(*)(void))dlsym(handle, "CatchSIGIO");
98 | 	if (fn1 == NULL) {
99 | 		fprintf(stderr, "%s\n", dlerror());
115 | 	}
116 | 
117 | 	if (verbose) {
118 | 		printf("calling dlsym\n");
119 | 	}
120 | 
121 | 	// Check that the Go code saw SIGIO.
122 | 	sawSIGIO = (int (*)(void))dlsym(handle, "SawSIGIO");
123 | 	if (sawSIGIO == NULL) {
124 | 		fprintf(stderr, "%s\n", dlerror());
142 | 	// Tell the Go code to stop catching SIGIO.
143 | 
144 | 	if (verbose) {
145 | 		printf("calling dlsym\n");
146 | 	}
147 | 
148 | 	fn1 = (void(*)(void))dlsym(handle, "ResetSIGIO");
149 | 	if (fn1 == NULL) {
150 | 		fprintf(stderr, "%s\n", dlerror());
{% endraw %}

```
### misc/cgo/testcshared/main1.c

```c

{% raw %}
7 | 
8 | int check_int8(void* handle, const char* fname, int8_t want) {
9 |   int8_t (*fn)();
10 |   fn = (int8_t (*)())dlsym(handle, fname);
11 |   if (!fn) {
12 |     fprintf(stderr, "ERROR: missing %s: %s\n", fname, dlerror());
22 | 
23 | int check_int32(void* handle, const char* fname, int32_t want) {
24 |   int32_t (*fn)();
25 |   fn = (int32_t (*)())dlsym(handle, fname);
26 |   if (!fn) {
27 |     fprintf(stderr, "ERROR: missing %s: %s\n", fname, dlerror());
{% endraw %}

```
### misc/cgo/testcshared/main3.c

```c

{% raw %}
15 |     return 2;
16 |   }
17 | 
18 |   uintptr_t main_fn = (uintptr_t)dlsym(handle, "main.main");
19 |   if (!main_fn) {
20 |     fprintf(stderr, "ERROR: missing main.main: %s\n", dlerror());
{% endraw %}

```
### misc/cgo/testcshared/main4.c

```c

{% raw %}
115 | 	}
116 | 
117 | 	if (verbose) {
118 | 		printf("calling dlsym\n");
119 | 	}
120 | 
121 | 	// Start some goroutines.
122 | 	fn = (void(*)(void))dlsym(handle, "RunGoroutines");
123 | 	if (fn == NULL) {
124 | 		fprintf(stderr, "%s\n", dlerror());
192 | 	}
193 | 
194 | 	if (verbose) {
195 | 		printf("calling dlsym\n");
196 | 	}
197 | 
198 | 	// Make sure that a SIGSEGV in Go causes a run-time panic.
199 | 	fn = (void (*)(void))dlsym(handle, "TestSEGV");
200 | 	if (fn == NULL) {
201 | 		fprintf(stderr, "%s\n", dlerror());
{% endraw %}

```
### misc/cgo/test/issue4029.go

```go

{% raw %}
57 | 	}
58 | 	defer C.dlclose(this_process)
59 | 
60 | 	symbol_address := C.dlsym(this_process, C.CString(symbol))
61 | 	if symbol_address == nil {
62 | 		t.Error("dlsym:", C.GoString(C.dlerror()))
63 | 		return
64 | 	}
{% endraw %}

```