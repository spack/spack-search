---
name: "gridlab-d"
layout: package
next_package: gromacs
previous_package: grass
languages: ['c']
---
## develop
12 / 3604 files match, 4 filtered matches.

 - [third_party/dlfcn-win32-read-only/dlfcn.h](#third_partydlfcn-win32-read-onlydlfcnh)
 - [third_party/dlfcn-win32-read-only/test.c](#third_partydlfcn-win32-read-onlytestc)
 - [third_party/dlfcn-win32-read-only/dlfcn.c](#third_partydlfcn-win32-read-onlydlfcnc)
 - [rest/mongoose.c](#restmongoosec)

### third_party/dlfcn-win32-read-only/dlfcn.h

```c

{% raw %}
40 | #define RTLD_DEFAULT    0
41 | #define RTLD_NEXT       0
42 | 
43 | void *dlopen ( const char *file, int mode );
44 | int   dlclose( void *handle );
45 | void *dlsym  ( void *handle, const char *name );
{% endraw %}

```
### third_party/dlfcn-win32-read-only/test.c

```c

{% raw %}
70 |     int (*nonexistentfunction)( void );
71 |     int ret;
72 | 
73 |     library = dlopen( "testdll.dll", RTLD_GLOBAL );
74 |     if( !library )
75 |     {
80 |     else
81 |         printf( "SUCCESS\tOpened library globally: %p\n", library );
82 | 
83 |     global = dlopen( 0, RTLD_GLOBAL );
84 |     if( !global )
85 |     {
161 |     else
162 |         printf( "SUCCESS\tClosed library.\n" );
163 | 
164 |     library = dlopen( "testdll.dll", RTLD_LOCAL );
165 |     if( !library )
166 |     {
231 |                 error ? error : "" );
232 |     }
233 | 
234 |     library = dlopen( "testdll.dll", RTLD_GLOBAL );
235 |     if( !library )
236 |     {
{% endraw %}

```
### third_party/dlfcn-win32-read-only/dlfcn.c

```c

{% raw %}
166 |     save_err_str( ptr_buf );
167 | }
168 | 
169 | void *dlopen( const char *file, int mode )
170 | {
171 |     HMODULE hModule;
{% endraw %}

```
### rest/mongoose.c

```c

{% raw %}
1627 |   return (long)_beginthread((void (__cdecl *)(void *)) f, 0, p) == -1L ? -1 : 0;
1628 | }
1629 | 
1630 | static HANDLE dlopen(const char *dll_name, int flags) {
1631 |   wchar_t wbuf[PATH_MAX];
1632 |   (void) flags;
1974 |   void  *dll_handle;
1975 |   struct ssl_func *fp;
1976 | 
1977 |   if ((dll_handle = dlopen(dll_name, RTLD_LAZY)) == NULL) {
1978 |     cry(fc(ctx), "%s: cannot load %s", __func__, dll_name);
1979 |     return 0;
{% endraw %}

```