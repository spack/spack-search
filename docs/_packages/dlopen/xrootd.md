---
name: "xrootd"
layout: package
next_package: openmpi
previous_package: ocaml
library_name: dlopen
matches: ['dlsym', 'dlopen']
languages: ['cpp']
---
## 4.8.3
5 / 1257 files match, 3 filtered matches.

 - [src/XrdApps/XrdCpy.cc](#srcxrdappsxrdcpycc)
 - [src/XrdSys/XrdSysPlugin.cc](#srcxrdsysxrdsysplugincc)
 - [tests/common/TextRunner.cc](#testscommontextrunnercc)

### src/XrdApps/XrdCpy.cc

```cpp

{% raw %}
1628 |       // Initialize monitoring client, if a plugin is present
1629 |       cpnfo.mon = 0;
1630 | #ifndef WIN32
1631 |       void *monhandle = dlopen (monlibname.c_str(), RTLD_LAZY);
1632 | 
1633 |       if (monhandle) {
{% endraw %}

```
### src/XrdSys/XrdSysPlugin.cc

```cpp

{% raw %}
282 | // Open whatever it is we need to open
283 | //
284 |    if (!myHandle)
285 |       {if ((myHandle = dlopen(libPath, flags))) libHandle = myHandle;
286 |           else {if (optional < 2) libMsg(dlerror(), " loading "); return 0;}
287 |       }
418 | 
419 | // Try to open the library
420 | //
421 |    if (!(myHandle = dlopen(path, DLflags())))
422 |       {if (ebuff && eblen > 0)
423 |           {const char *dlMsg = dlerror();
{% endraw %}

```
### tests/common/TextRunner.cc

```cpp

{% raw %}
99 |     std::cerr << "Usage: " << argv[0] << " libname.so testname" << std::endl;
100 |     return 1;
101 |   }
102 |   void *libHandle = dlopen( argv[1], RTLD_LAZY );
103 |   if( libHandle == 0 )
104 |   {
{% endraw %}

```