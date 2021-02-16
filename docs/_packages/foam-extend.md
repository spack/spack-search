---
name: "foam-extend"
layout: package
next_package: nnvm
previous_package: libxprintapputil
languages: ['c']
---
## 4.0
2 / 9931 files match, 2 filtered matches.

 - [src/OSspecific/MSWindows/MSwindows.C](#srcosspecificmswindowsmswindowsc)
 - [src/foam/db/dlLibraryTable/dlLibraryTable.C](#srcfoamdbdllibrarytabledllibrarytablec)

### src/OSspecific/MSWindows/MSwindows.C

```c

{% raw %}
1303 |             << "dlopen error : " << MSwindows::getLastError()
{% endraw %}

```
### src/foam/db/dlLibraryTable/dlLibraryTable.C

```c

{% raw %}
71 |             dlopen(functionLibName.c_str(), RTLD_LAZY|RTLD_GLOBAL);
83 |                 dlopen(osxFileName.c_str(), RTLD_LAZY|RTLD_GLOBAL);
95 |                 dlopen(l_LIBBIN_Name.c_str(), RTLD_LAZY|RTLD_GLOBAL);
102 |                 dlopen(l_SITE_LIBBIN_Name.c_str(), RTLD_LAZY|RTLD_GLOBAL);
109 |                 dlopen(l_USER_LIBBIN_Name.c_str(), RTLD_LAZY|RTLD_GLOBAL);
115 |                 dlopen(lName.c_str(), RTLD_LAZY|RTLD_GLOBAL);
{% endraw %}

```