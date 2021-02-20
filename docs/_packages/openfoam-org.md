---
name: "openfoam-org"
layout: package
next_package: openfst
previous_package: openfoam
languages: ['c']
---
## 5.0
3 / 9349 files match, 2 filtered matches.

 - [src/OSspecific/POSIX/POSIX.C](#srcosspecificposixposixc)
 - [src/OpenFOAM/db/dynamicLibrary/dynamicCode/dynamicCode.C](#srcopenfoamdbdynamiclibrarydynamiccodedynamiccodec)

### src/OSspecific/POSIX/POSIX.C

```c

{% raw %}
1200 |     if (POSIX::debug)
1201 |     {
1202 |         std::cout<< "dlOpen(const fileName&)"
1203 |             << " : dlopen of " << lib << std::endl;
1204 |     }
1205 |     void* handle = ::dlopen(lib.c_str(), RTLD_LAZY|RTLD_GLOBAL);
1206 | 
1207 |     if (!handle && check)
1208 |     {
1209 |         WarningInFunction
1210 |             << "dlopen error : " << ::dlerror()
1211 |             << endl;
1212 |     }
1215 |     {
1216 |         std::cout
1217 |             << "dlOpen(const fileName&)"
1218 |             << " : dlopen of " << lib
1219 |             << " handle " << handle << std::endl;
1220 |     }
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