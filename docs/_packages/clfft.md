---
name: "clfft"
layout: package
next_package: cmake
previous_package: clamr
languages: ['c']
---
## 2.12.2
3 / 159 files match, 1 filtered matches.

 - [src/include/sharedLibrary.h](#srcincludesharedlibraryh)

### src/include/sharedLibrary.h

```c

{% raw %}
38 | #elif defined(__linux__)
39 |         tstring linuxName = unixPrefix;
40 | 	linuxName += libraryName += ".so";
41 | 	void* fileHandle = ::dlopen( linuxName.c_str( ), RTLD_NOW );
42 | 	if( !quiet && !fileHandle )
43 | 	{
46 | #elif defined(__APPLE__)
47 |   tstring appleName = unixPrefix;
48 |   appleName += libraryName += ".dylib";
49 |   void* fileHandle = ::dlopen( appleName.c_str( ), RTLD_NOW );
50 |   if( !quiet && !fileHandle )
51 |   {
54 | #elif defined(__FreeBSD_kernel__)
55 |         tstring freebsdName = unixPrefix;
56 |         freebsdName += libraryName += ".so";
57 |         void* fileHandle = ::dlopen( freebsdName.c_str( ), RTLD_NOW );
58 |         if( !quiet && !fileHandle )
59 |         {
{% endraw %}

```