---
name: "etcd"
layout: package
next_package: python
previous_package: openfoam-org
languages: ['go']
---
## 3.3.20
4 / 2237 files match, 3 filtered matches.

 - [vendor/github.com/coreos/pkg/dlopen/dlopen_example.go](#vendorgithubcomcoreospkgdlopendlopen_examplego)
 - [vendor/github.com/coreos/pkg/dlopen/dlopen.go](#vendorgithubcomcoreospkgdlopendlopengo)
 - [vendor/github.com/coreos/go-systemd/util/util_cgo.go](#vendorgithubcomcoreosgo-systemdutilutil_cgogo)

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