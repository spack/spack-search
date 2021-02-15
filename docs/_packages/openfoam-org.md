---
name: "openfoam-org"
layout: package
next_package: etcd
previous_package: modern-wheel
languages: ['cpp']
---
## 5.0
3 / 9349 files match

 - [src/OSspecific/POSIX/POSIX.C](#srcosspecificposixposixc)
 - [src/OpenFOAM/include/OSspecific.H](#srcopenfoamincludeosspecifich)
 - [src/OpenFOAM/db/dynamicLibrary/dynamicCode/dynamicCode.C](#srcopenfoamdbdynamiclibrarydynamiccodedynamiccodec)

### src/OSspecific/POSIX/POSIX.C

```cpp

{% raw %}
1198 | void* Foam::dlOpen(const fileName& lib, const bool check)
1202 |         std::cout<< "dlOpen(const fileName&)"
1203 |             << " : dlopen of " << lib << std::endl;
1205 |     void* handle = ::dlopen(lib.c_str(), RTLD_LAZY|RTLD_GLOBAL);
1210 |             << "dlopen error : " << ::dlerror()
1217 |             << "dlOpen(const fileName&)"
1218 |             << " : dlopen of " << lib
1246 |     // clear any old errors - see manpage dlopen
1277 |         // clear any old errors - see manpage dlopen
{% endraw %}

```
### src/OpenFOAM/include/OSspecific.H

```cpp

{% raw %}
187 | void* dlOpen(const fileName& lib, const bool check = true);
189 | //- Close a dlopened library using handle. Return true if successful
192 | //- Lookup a symbol in a dlopened library using handle to library
195 | //- Report if symbol in a dlopened library could be found
{% endraw %}

```
### src/OpenFOAM/db/dynamicLibrary/dynamicCode/dynamicCode.C

```cpp

{% raw %}
68 |             << "using dlopen)"
{% endraw %}

```