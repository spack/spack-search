---
name: "kubernetes"
layout: package
next_package: lammps
previous_package: kripke
languages: ['go']
---
## 1.18.0
6 / 17660 files match, 4 filtered matches.

 - [vendor/github.com/coreos/pkg/dlopen/dlopen_example.go](#vendorgithubcomcoreospkgdlopendlopen_examplego)
 - [vendor/github.com/coreos/pkg/dlopen/dlopen.go](#vendorgithubcomcoreospkgdlopendlopengo)
 - [vendor/github.com/coreos/go-systemd/util/util_cgo.go](#vendorgithubcomcoreosgo-systemdutilutil_cgogo)
 - [vendor/github.com/mindprince/gonvml/bindings.go](#vendorgithubcommindprincegonvmlbindingsgo)

### vendor/github.com/coreos/pkg/dlopen/dlopen_example.go

```go

{% raw %}
13 | //
14 | // +build linux
15 | 
16 | package dlopen
17 | 
18 | // #include <string.h>
{% endraw %}

```
### vendor/github.com/coreos/pkg/dlopen/dlopen.go

```go

{% raw %}
13 | 
14 | // Package dlopen provides some convenience functions to dlopen a library and
15 | // get its symbols.
16 | package dlopen
17 | 
18 | // #cgo LDFLAGS: -ldl
41 | 	for _, name := range libs {
42 | 		libname := C.CString(name)
43 | 		defer C.free(unsafe.Pointer(libname))
44 | 		handle := C.dlopen(libname, C.RTLD_LAZY)
45 | 		if handle != nil {
46 | 			h := &LibHandle{
{% endraw %}

```
### vendor/github.com/coreos/go-systemd/util/util_cgo.go

```go

{% raw %}
57 | 	"syscall"
58 | 	"unsafe"
59 | 
60 | 	"github.com/coreos/pkg/dlopen"
61 | )
62 | 
71 | }
72 | 
73 | func getRunningSlice() (slice string, err error) {
74 | 	var h *dlopen.LibHandle
75 | 	h, err = dlopen.GetHandle(libsystemdNames)
76 | 	if err != nil {
77 | 		return
101 | }
102 | 
103 | func runningFromSystemService() (ret bool, err error) {
104 | 	var h *dlopen.LibHandle
105 | 	h, err = dlopen.GetHandle(libsystemdNames)
106 | 	if err != nil {
107 | 		return
143 | }
144 | 
145 | func currentUnitName() (unit string, err error) {
146 | 	var h *dlopen.LibHandle
147 | 	h, err = dlopen.GetHandle(libsystemdNames)
148 | 	if err != nil {
149 | 		return
{% endraw %}

```
### vendor/github.com/mindprince/gonvml/bindings.go

```go

{% raw %}
148 | // Loads all symbols needed and initializes NVML.
149 | // Call this before calling any other methods.
150 | nvmlReturn_t nvmlInit_dl(void) {
151 |   nvmlHandle = dlopen("libnvidia-ml.so.1", RTLD_LAZY);
152 |   if (nvmlHandle == NULL) {
153 |     return NVML_ERROR_LIBRARY_NOT_FOUND;
{% endraw %}

```