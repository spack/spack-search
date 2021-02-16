---
name: "gridlab-d"
layout: package
next_package: collectd
previous_package: cronie
languages: ['c']
---
## develop
12 / 3604 files match

 - [third_party/dlfcn-win32-read-only/dlfcn.h](#third_partydlfcn-win32-read-onlydlfcnh)
 - [third_party/dlfcn-win32-read-only/test.c](#third_partydlfcn-win32-read-onlytestc)
 - [third_party/dlfcn-win32-read-only/dlfcn.c](#third_partydlfcn-win32-read-onlydlfcnc)
 - [rest/mongoose.c](#restmongoosec)

### third_party/dlfcn-win32-read-only/dlfcn.h

```c

{% raw %}
43 | void *dlopen ( const char *file, int mode );
{% endraw %}

```
### third_party/dlfcn-win32-read-only/test.c

```c

{% raw %}
73 |     library = dlopen( "testdll.dll", RTLD_GLOBAL );
83 |     global = dlopen( 0, RTLD_GLOBAL );
164 |     library = dlopen( "testdll.dll", RTLD_LOCAL );
234 |     library = dlopen( "testdll.dll", RTLD_GLOBAL );
{% endraw %}

```
### third_party/dlfcn-win32-read-only/dlfcn.c

```c

{% raw %}
169 | void *dlopen( const char *file, int mode )
{% endraw %}

```
### rest/mongoose.c

```c

{% raw %}
1630 | static HANDLE dlopen(const char *dll_name, int flags) {
1977 |   if ((dll_handle = dlopen(dll_name, RTLD_LAZY)) == NULL) {
{% endraw %}

```