---
name: "openfoam-org"
layout: package
next_package: etcd
previous_package: modern-wheel
languages: ['c']
---
## 5.0
3 / 9349 files match, 2 filtered matches.

 - [src/OSspecific/POSIX/POSIX.C](#srcosspecificposixposixc)
 - [src/OpenFOAM/db/dynamicLibrary/dynamicCode/dynamicCode.C](#srcopenfoamdbdynamiclibrarydynamiccodedynamiccodec)

### src/OSspecific/POSIX/POSIX.C

```c

{% raw %}
1203 |             << " : dlopen of " << lib << std::endl;
1205 |     void* handle = ::dlopen(lib.c_str(), RTLD_LAZY|RTLD_GLOBAL);
1210 |             << "dlopen error : " << ::dlerror()
1218 |             << " : dlopen of " << lib
{% endraw %}

```
### src/OpenFOAM/db/dynamicLibrary/dynamicCode/dynamicCode.C

```c

{% raw %}
68 |             << "using dlopen)"
{% endraw %}

```