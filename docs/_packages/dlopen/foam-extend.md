---
name: "foam-extend"
layout: package
next_package: kitty
previous_package: autogen
library_name: dlopen
matches: ['dlopen']
languages: ['c']
---
## 4.0
2 / 9931 files match, 2 filtered matches.

 - [src/OSspecific/MSWindows/MSwindows.C](#srcosspecificmswindowsmswindowsc)
 - [src/foam/db/dlLibraryTable/dlLibraryTable.C](#srcfoamdbdllibrarytabledllibrarytablec)

### src/OSspecific/MSWindows/MSwindows.C

```c

{% raw %}
1300 |     else if (check)
1301 |     {
1302 |         WarningIn("dlOpen(const fileName&, const bool)")
1303 |             << "dlopen error : " << MSwindows::getLastError()
1304 |             << endl;
1305 |     }
{% endraw %}

```
### src/foam/db/dlLibraryTable/dlLibraryTable.C

```c

{% raw %}
68 |     if (functionLibName.size())
69 |     {
70 |         void* functionLibPtr =
71 |             dlopen(functionLibName.c_str(), RTLD_LAZY|RTLD_GLOBAL);
72 | 
73 | #ifdef darwin
80 |             osxFileName=functionLibName.lessExt()+".dylib";
81 | 
82 |             functionLibPtr =
83 |                 dlopen(osxFileName.c_str(), RTLD_LAZY|RTLD_GLOBAL);
84 |         }
85 | 
92 |             fileName l_LIBBIN_Name =
93 |                 getEnv("FOAM_LIBBIN")/osxFileName;
94 |             functionLibPtr =
95 |                 dlopen(l_LIBBIN_Name.c_str(), RTLD_LAZY|RTLD_GLOBAL);
96 |         }
97 |         if (!functionLibPtr)
99 |             fileName l_SITE_LIBBIN_Name =
100 |                 getEnv("FOAM_SITE_LIBBIN")/osxFileName;
101 |             functionLibPtr =
102 |                 dlopen(l_SITE_LIBBIN_Name.c_str(), RTLD_LAZY|RTLD_GLOBAL);
103 |         }
104 |         if (!functionLibPtr)
106 |             fileName l_USER_LIBBIN_Name =
107 |                 getEnv("FOAM_USER_LIBBIN")/osxFileName;
108 |             functionLibPtr =
109 |                 dlopen(l_USER_LIBBIN_Name.c_str(), RTLD_LAZY|RTLD_GLOBAL);
110 |         }
111 | #elif defined mingw
112 |         if(!functionLibPtr && functionLibName.ext()=="so") {
113 |             fileName lName=functionLibName.lessExt()+".dll";
114 |             functionLibPtr =
115 |                 dlopen(lName.c_str(), RTLD_LAZY|RTLD_GLOBAL);
116 |         }
117 | #endif
{% endraw %}

```