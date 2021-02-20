---
name: "openfoam"
layout: package
next_package: openfoam-org
previous_package: openfast
languages: ['c']
---
## 1806
3 / 11471 files match, 2 filtered matches.

 - [src/OSspecific/POSIX/POSIX.C](#srcosspecificposixposixc)
 - [src/OpenFOAM/db/dynamicLibrary/dynamicCode/dynamicCode.C](#srcopenfoamdbdynamiclibrarydynamiccodedynamiccodec)

### src/OSspecific/POSIX/POSIX.C

```c

{% raw %}
1497 |     if (POSIX::debug)
1498 |     {
1499 |         std::cout<< "dlOpen(const fileName&)"
1500 |             << " : dlopen of " << lib << std::endl;
1501 |     }
1502 |     void* handle = ::dlopen(lib.c_str(), RTLD_LAZY|RTLD_GLOBAL);
1503 | 
1504 |     #ifdef darwin
1506 |     if (!handle && lib.hasExt("so"))
1507 |     {
1508 |         const fileName dylib(lib.lessExt().ext("dylib"));
1509 |         handle = ::dlopen(dylib.c_str(), RTLD_LAZY|RTLD_GLOBAL);
1510 |     }
1511 |     #endif
1513 |     if (!handle && check)
1514 |     {
1515 |         WarningInFunction
1516 |             << "dlopen error : " << ::dlerror()
1517 |             << endl;
1518 |     }
1521 |     {
1522 |         std::cout
1523 |             << "dlOpen(const fileName&)"
1524 |             << " : dlopen of " << lib
1525 |             << " handle " << handle << std::endl;
1526 |     }
{% endraw %}

```
### src/OpenFOAM/db/dynamicLibrary/dynamicCode/dynamicCode.C

```c

{% raw %}
65 |             << "This code should not be executed by someone with administrator"
66 |             << " rights due to security reasons." << nl
67 |             << "(it writes a shared library which then gets loaded "
68 |             << "using dlopen)"
69 |             << exit(FatalIOError);
70 |     }
{% endraw %}

```