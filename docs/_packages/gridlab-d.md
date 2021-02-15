---
name: "gridlab-d"
layout: package
next_package: collectd
previous_package: cronie
languages: ['cpp']
---
## develop
12 / 3604 files match

 - [configure.ac](#configureac)
 - [gldcore/gridlabd.h](#gldcoregridlabdh)
 - [gldcore/class.c](#gldcoreclassc)
 - [gldcore/module.c](#gldcoremodulec)
 - [gldcore/link.cpp](#gldcorelinkcpp)
 - [third_party/dlfcn-win32-read-only/dlfcn.h](#third_partydlfcn-win32-read-onlydlfcnh)
 - [third_party/dlfcn-win32-read-only/test.c](#third_partydlfcn-win32-read-onlytestc)
 - [third_party/dlfcn-win32-read-only/dlfcn.c](#third_partydlfcn-win32-read-onlydlfcnc)
 - [rest/mongoose.c](#restmongoosec)
 - [plc/main.cpp](#plcmaincpp)
 - [powerflow/node.cpp](#powerflownodecpp)
 - [tape/tape.c](#tapetapec)

### configure.ac

```

{% raw %}
586 | LT_INIT([dlopen win32-dll shared disable-static])
{% endraw %}

```
### gldcore/gridlabd.h

```cpp

{% raw %}
2480 | 	#define DLLOAD(P) dlopen(P,RTLD_LAZY)
2483 | 	#define DLLOAD(P) dlopen(P,RTLD_LAZY)
{% endraw %}

```
### gldcore/class.c

```cpp

{% raw %}
39 | #define DLLOAD(P) dlopen(P,RTLD_LAZY)
{% endraw %}

```
### gldcore/module.c

```cpp

{% raw %}
56 | #define DLLOAD(P) dlopen(P,RTLD_LAZY)
{% endraw %}

```
### gldcore/link.cpp

```

{% raw %}
34 | 	#define DLLOAD(P) dlopen(P,RTLD_LAZY)
37 | 	#define DLLOAD(P) dlopen(P,RTLD_LAZY)
{% endraw %}

```
### third_party/dlfcn-win32-read-only/dlfcn.h

```cpp

{% raw %}
43 | void *dlopen ( const char *file, int mode );
{% endraw %}

```
### third_party/dlfcn-win32-read-only/test.c

```cpp

{% raw %}
73 |     library = dlopen( "testdll.dll", RTLD_GLOBAL );
83 |     global = dlopen( 0, RTLD_GLOBAL );
164 |     library = dlopen( "testdll.dll", RTLD_LOCAL );
234 |     library = dlopen( "testdll.dll", RTLD_GLOBAL );
{% endraw %}

```
### third_party/dlfcn-win32-read-only/dlfcn.c

```cpp

{% raw %}
71 |      * dlopen?
169 | void *dlopen( const char *file, int mode )
{% endraw %}

```
### rest/mongoose.c

```cpp

{% raw %}
1630 | static HANDLE dlopen(const char *dll_name, int flags) {
1977 |   if ((dll_handle = dlopen(dll_name, RTLD_LAZY)) == NULL) {
{% endraw %}

```
### plc/main.cpp

```

{% raw %}
30 | 	void *hLib = dlopen(name, RTLD_LAZY);
{% endraw %}

```
### powerflow/node.cpp

```

{% raw %}
77 | #define DLLOAD(P) dlopen(P,RTLD_LAZY)
{% endraw %}

```
### tape/tape.c

```cpp

{% raw %}
68 | #define DLLOAD(P) dlopen(P,RTLD_LAZY)
{% endraw %}

```