---
name: "xrootd"
layout: package
next_package: yasm
previous_package: xdm
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['cpp']
---
## 4.8.3
3 / 1257 files match, 3 filtered matches.

 - [src/XrdApps/XrdCpy.cc](#srcxrdappsxrdcpycc)
 - [src/XrdSys/XrdSysPlugin.cc](#srcxrdsysxrdsysplugincc)
 - [src/XrdPosix/XrdPosixLinkage.cc](#srcxrdposixxrdposixlinkagecc)

### src/XrdApps/XrdCpy.cc

```cpp

{% raw %}
1631 |       void *monhandle = dlopen (monlibname.c_str(), RTLD_LAZY);
1632 | 
1633 |       if (monhandle) {
1634 | 	XrdClientMonIntfHook monlibhook = (XrdClientMonIntfHook)dlsym(monhandle, "XrdClientgetMonIntf");
1635 | 
1636 | 	const char *err = 0;
{% endraw %}

```
### src/XrdSys/XrdSysPlugin.cc

```cpp

{% raw %}
145 | 
146 | // Find the version number
147 | //
148 |    if (!(vP = dlsym(lHandle, vName)))
149 |       {if (vinP->vProcess != XrdVERSIONPLUGIN_Required) return cvMissing;
150 |        return libMsg(dlerror()," required version information for %s in ",pname);
289 | // Get the symbol. In the environment we have defined, null values are not
290 | // allowed and we will issue an error.
291 | //
292 |    if (!(ep = dlsym(myHandle, pname)))
293 |       {if (optional < 2) libMsg(dlerror(), " plugin %s in ", pname);
294 |        return 0;
{% endraw %}

```
### src/XrdPosix/XrdPosixLinkage.cc

```cpp

{% raw %}
59 | /******************************************************************************/
60 |   
61 | #define LOOKUP_UNIX(symb) symb = (Retv_ ## symb (*)(Args_ ## symb)) \
62 |                                  dlsym(RTLD_NEXT, Symb_ ## symb); \
63 |                           if (!symb) {symb = Xrd_U_ ## symb; \
64 |                                       Missing(Symb_ ## symb);}
{% endraw %}

```