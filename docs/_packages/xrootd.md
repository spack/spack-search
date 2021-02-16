---
name: "xrootd"
layout: package
next_package: neuron
previous_package: py-uwsgi
languages: ['cpp']
---
## 4.8.3
5 / 1257 files match

 - [src/XrdApps/XrdCpy.cc](#srcxrdappsxrdcpycc)
 - [src/XrdSys/XrdSysPlugin.cc](#srcxrdsysxrdsysplugincc)
 - [tests/common/TextRunner.cc](#testscommontextrunnercc)

### src/XrdApps/XrdCpy.cc

```cpp

{% raw %}
1631 |       void *monhandle = dlopen (monlibname.c_str(), RTLD_LAZY);
{% endraw %}

```
### src/XrdSys/XrdSysPlugin.cc

```cpp

{% raw %}
285 |       {if ((myHandle = dlopen(libPath, flags))) libHandle = myHandle;
421 |    if (!(myHandle = dlopen(path, DLflags())))
{% endraw %}

```
### tests/common/TextRunner.cc

```cpp

{% raw %}
102 |   void *libHandle = dlopen( argv[1], RTLD_LAZY );
{% endraw %}

```