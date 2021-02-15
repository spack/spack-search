---
name: "kubernetes"
layout: package
next_package: httpd
previous_package: tpm2-tss
languages: ['go']
---
## 1.18.0
6 / 17660 files match

 - [vendor/modules.txt](#vendormodulestxt)
 - [vendor/github.com/coreos/pkg/dlopen/dlopen_example.go](#vendorgithubcomcoreospkgdlopendlopen_examplego)
 - [vendor/github.com/coreos/pkg/dlopen/dlopen.go](#vendorgithubcomcoreospkgdlopendlopengo)
 - [vendor/github.com/coreos/go-systemd/util/util_cgo.go](#vendorgithubcomcoreosgo-systemdutilutil_cgogo)
 - [vendor/github.com/mindprince/gonvml/README.md](#vendorgithubcommindprincegonvmlreadmemd)
 - [vendor/github.com/mindprince/gonvml/bindings.go](#vendorgithubcommindprincegonvmlbindingsgo)

### vendor/modules.txt

```

{% raw %}
202 | github.com/coreos/pkg/dlopen
{% endraw %}

```
### vendor/github.com/coreos/pkg/dlopen/dlopen_example.go

```go

{% raw %}
16 | package dlopen
{% endraw %}

```
### vendor/github.com/coreos/pkg/dlopen/dlopen.go

```go

{% raw %}
14 | // Package dlopen provides some convenience functions to dlopen a library and
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
### vendor/github.com/mindprince/gonvml/README.md

```

{% raw %}
17 | cgo preamble in `bindings.go` uses `dlopen` to dynamically load NVML and makes
{% endraw %}

```
### vendor/github.com/mindprince/gonvml/bindings.go

```go

{% raw %}
151 |   nvmlHandle = dlopen("libnvidia-ml.so.1", RTLD_LAZY);
{% endraw %}

```