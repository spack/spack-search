---
name: "openfoam"
layout: package
next_package: adlbx
previous_package: id3lib
languages: ['cpp']
---
## 1806
3 / 11471 files match

 - [src/OSspecific/POSIX/POSIX.C](#srcosspecificposixposixc)
 - [src/OpenFOAM/include/OSspecific.H](#srcopenfoamincludeosspecifich)
 - [src/OpenFOAM/db/dynamicLibrary/dynamicCode/dynamicCode.C](#srcopenfoamdbdynamiclibrarydynamiccodedynamiccodec)

### src/OSspecific/POSIX/POSIX.C

```cpp

{% raw %}
1495 | void* Foam::dlOpen(const fileName& lib, const bool check)
1499 |         std::cout<< "dlOpen(const fileName&)"
1500 |             << " : dlopen of " << lib << std::endl;
1502 |     void* handle = ::dlopen(lib.c_str(), RTLD_LAZY|RTLD_GLOBAL);
1509 |         handle = ::dlopen(dylib.c_str(), RTLD_LAZY|RTLD_GLOBAL);
1516 |             << "dlopen error : " << ::dlerror()
1523 |             << "dlOpen(const fileName&)"
1524 |             << " : dlopen of " << lib
1552 |     // clear any old errors - see manpage dlopen
1583 |         // clear any old errors - see manpage dlopen
{% endraw %}

```
### src/OpenFOAM/include/OSspecific.H

```cpp

{% raw %}
246 | void* dlOpen(const fileName& lib, const bool check = true);
248 | //- Close a dlopened library using handle. Return true if successful
251 | //- Lookup a symbol in a dlopened library using handle to library
254 | //- Report if symbol in a dlopened library could be found.
{% endraw %}

```
### src/OpenFOAM/db/dynamicLibrary/dynamicCode/dynamicCode.C

```cpp

{% raw %}
68 |             << "using dlopen)"
{% endraw %}

```