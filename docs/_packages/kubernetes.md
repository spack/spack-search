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
16 | package dlopen
{% endraw %}

```
### vendor/github.com/coreos/pkg/dlopen/dlopen.go

```go

{% raw %}
16 | package dlopen
44 | 		handle := C.dlopen(libname, C.RTLD_LAZY)
{% endraw %}

```
### vendor/github.com/coreos/go-systemd/util/util_cgo.go

```go

{% raw %}
60 | 	"github.com/coreos/pkg/dlopen"
74 | 	var h *dlopen.LibHandle
75 | 	h, err = dlopen.GetHandle(libsystemdNames)
104 | 	var h *dlopen.LibHandle
105 | 	h, err = dlopen.GetHandle(libsystemdNames)
146 | 	var h *dlopen.LibHandle
147 | 	h, err = dlopen.GetHandle(libsystemdNames)
{% endraw %}

```
### vendor/github.com/mindprince/gonvml/bindings.go

```go

{% raw %}
151 |   nvmlHandle = dlopen("libnvidia-ml.so.1", RTLD_LAZY);
{% endraw %}

```