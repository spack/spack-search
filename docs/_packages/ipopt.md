---
name: "ipopt"
layout: package
next_package: iproute2
previous_package: ipcalc
languages: ['c']
---
## 3.12.1
12 / 690 files match, 1 filtered matches.

 - [Ipopt/src/contrib/LinearSolverLoader/LibraryHandler.c](#ipoptsrccontriblinearsolverloaderlibraryhandlerc)

### Ipopt/src/contrib/LinearSolverLoader/LibraryHandler.c

```c

{% raw %}
45 |     mysnprintf(msgBuf, msgLen, "Windows error while loading dynamic library %s, error = %d.\n(see http://msdn.microsoft.com/en-us/library/ms681381%%28v=vs.85%%29.aspx)\n", libName, GetLastError());
46 |   }
47 | # else
48 |   h = dlopen (libName, RTLD_NOW);
49 |   if (NULL == h) {
50 |     strncpy(msgBuf, dlerror(), msgLen);
{% endraw %}

```