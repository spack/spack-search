---
name: "nim"
layout: package
next_package: nix
previous_package: nicstat
languages: ['c']
---
## 0.19.6
9 / 7503 files match, 1 filtered matches.

 - [tests/realtimeGC/cmain.c](#testsrealtimegccmainc)

### tests/realtimeGC/cmain.c

```c

{% raw %}
28 |     count = (pFunc)GetProcAddress((HMODULE) hndl, (char const*)"count");
29 |     checkOccupiedMem = (pFunc)GetProcAddress((HMODULE) hndl, (char const*)"checkOccupiedMem");
30 | #else /* OSX || NIX */
31 |     hndl = (void*) dlopen((char const*)"./tests/realtimeGC/libshared.so", RTLD_LAZY);
32 |     status = (pFunc) dlsym(hndl, (char const*)"status");
33 |     count = (pFunc) dlsym(hndl, (char const*)"count");
{% endraw %}

```