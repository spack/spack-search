---
name: "openfoam"
layout: package
next_package: openfoam-org
previous_package: opencv
languages: ['c']
---
## 1806
3 / 11471 files match, 2 filtered matches.

 - [src/OSspecific/POSIX/POSIX.C](#srcosspecificposixposixc)
 - [src/OpenFOAM/db/dynamicLibrary/dynamicCode/dynamicCode.C](#srcopenfoamdbdynamiclibrarydynamiccodedynamiccodec)

### src/OSspecific/POSIX/POSIX.C

```c

{% raw %}
1500 |             << " : dlopen of " << lib << std::endl;
1502 |     void* handle = ::dlopen(lib.c_str(), RTLD_LAZY|RTLD_GLOBAL);
1509 |         handle = ::dlopen(dylib.c_str(), RTLD_LAZY|RTLD_GLOBAL);
1516 |             << "dlopen error : " << ::dlerror()
1524 |             << " : dlopen of " << lib
{% endraw %}

```
### src/OpenFOAM/db/dynamicLibrary/dynamicCode/dynamicCode.C

```c

{% raw %}
68 |             << "using dlopen)"
{% endraw %}

```