---
name: "foam-extend"
layout: package
next_package: nnvm
previous_package: libxprintapputil
languages: ['cpp']
---
## 4.0
2 / 9931 files match

 - [src/OSspecific/MSWindows/MSwindows.C](#srcosspecificmswindowsmswindowsc)
 - [src/foam/db/dlLibraryTable/dlLibraryTable.C](#srcfoamdbdllibrarytabledllibrarytablec)

### src/OSspecific/MSWindows/MSwindows.C

```cpp

{% raw %}
1271 | void* dlOpen(const fileName& libName, const bool check)
1275 |         Info<< "dlOpen(const fileName&)"
1302 |         WarningIn("dlOpen(const fileName&, const bool)")
1303 |             << "dlopen error : " << MSwindows::getLastError()
1309 |         Info<< "dlOpen(const fileName&)"
{% endraw %}

```
### src/foam/db/dlLibraryTable/dlLibraryTable.C

```cpp

{% raw %}
71 |             dlopen(functionLibName.c_str(), RTLD_LAZY|RTLD_GLOBAL);
83 |                 dlopen(osxFileName.c_str(), RTLD_LAZY|RTLD_GLOBAL);
95 |                 dlopen(l_LIBBIN_Name.c_str(), RTLD_LAZY|RTLD_GLOBAL);
102 |                 dlopen(l_SITE_LIBBIN_Name.c_str(), RTLD_LAZY|RTLD_GLOBAL);
109 |                 dlopen(l_USER_LIBBIN_Name.c_str(), RTLD_LAZY|RTLD_GLOBAL);
115 |                 dlopen(lName.c_str(), RTLD_LAZY|RTLD_GLOBAL);
{% endraw %}

```