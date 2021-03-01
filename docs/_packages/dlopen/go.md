---
name: "go"
layout: package
next_package: gotcha
previous_package: gnutls
library_name: dlopen
matches: ['dlsym', 'dlopen']
languages: ['go', 'c']
---
## 1.6.4
9 / 5019 files match, 7 filtered matches.

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
70 | 	void *handle;
71 | 
72 | 	// Locate symbol for the system pthread_create function.
73 | 	handle = dlopen("libpthread.so", RTLD_LAZY);
74 | 	if(handle == NULL) {
75 | 		fprintf(stderr, "runtime/cgo: dlopen failed to load libpthread: %s\n", dlerror());
76 | 		abort();
77 | 	}
{% endraw %}

```
### src/runtime/cgo/gcc_openbsd_amd64.c

```c

{% raw %}
70 | 	void *handle;
71 | 
72 | 	// Locate symbol for the system pthread_create function.
73 | 	handle = dlopen("libpthread.so", RTLD_LAZY);
74 | 	if(handle == NULL) {
75 | 		fprintf(stderr, "runtime/cgo: dlopen failed to load libpthread: %s\n", dlerror());
76 | 		abort();
77 | 	}
{% endraw %}

```
### misc/cgo/testcshared/main5.c

```c

{% raw %}
49 | 	}
50 | 
51 | 	if (verbose) {
52 | 		printf("calling dlopen\n");
53 | 	}
54 | 
55 | 	handle = dlopen(argv[1], RTLD_NOW | RTLD_GLOBAL);
56 | 	if (handle == NULL) {
57 | 		fprintf(stderr, "%s\n", dlerror());
{% endraw %}

```
### misc/cgo/testcshared/main1.c

```c

{% raw %}
40 | //   int8_t DidMainRun() // returns true
41 | //   int32_t FromPkg() // returns 1024
42 | int main(int argc, char** argv) {
43 |   void* handle = dlopen(argv[1], RTLD_LAZY | RTLD_GLOBAL);
44 |   if (!handle) {
45 |     fprintf(stderr, "ERROR: failed to open the shared library: %s\n",
{% endraw %}

```
### misc/cgo/testcshared/main3.c

```c

{% raw %}
8 | // Tests "main.main" is exported on android/arm,
9 | // which golang.org/x/mobile/app depends on.
10 | int main(int argc, char** argv) {
11 |   void* handle = dlopen(argv[1], RTLD_LAZY | RTLD_GLOBAL);
12 |   if (!handle) {
13 |     fprintf(stderr, "ERROR: failed to open the shared library: %s\n",
{% endraw %}

```
### misc/cgo/testcshared/main4.c

```c

{% raw %}
105 | 	}
106 | 
107 | 	if (verbose) {
108 | 		printf("calling dlopen\n");
109 | 	}
110 | 
111 | 	handle = dlopen(argv[1], RTLD_NOW | RTLD_GLOBAL);
112 | 	if (handle == NULL) {
113 | 		fprintf(stderr, "%s\n", dlerror());
{% endraw %}

```
### misc/cgo/test/issue4029.go

```go

{% raw %}
50 | }
51 | 
52 | func loadThySelf(t *testing.T, symbol string) {
53 | 	this_process := C.dlopen(nil, C.RTLD_NOW)
54 | 	if this_process == nil {
55 | 		t.Error("dlopen:", C.GoString(C.dlerror()))
56 | 		return
57 | 	}
{% endraw %}

```