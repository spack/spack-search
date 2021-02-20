---
name: "process-in-process"
layout: package
next_package: procps
previous_package: prism
languages: ['c']
---
## 2
6 / 584 files match, 4 filtered matches.

 - [PiP-Testsuite/PiP-Testsuite/compat/pip_dlopen.c](#pip-testsuitepip-testsuitecompatpip_dlopenc)
 - [lib/pip_dlfcn.c](#libpip_dlfcnc)
 - [lib/pip.c](#libpipc)
 - [include/pip/pip_dlfcn.h](#includepippip_dlfcnh)

### PiP-Testsuite/PiP-Testsuite/compat/pip_dlopen.c

```c

{% raw %}
36 | 
37 | #define LIBNAME 	"./libnull.so"
38 | 
39 | void *pip_dlopen( const char*, int );
40 | void *pip_dlsym( void*, const char* );
41 | int   pip_dlclose( void* );
45 |   int(*foo)(void);
46 | 
47 |   CHECK( pip_init(NULL,NULL,NULL,0), RV, return(EXIT_FAIL) );
48 |   CHECK( handle = pip_dlopen( LIBNAME, RTLD_LAZY ),
49 | 	 handle==NULL,
50 | 	 return(EXIT_FAIL) );
{% endraw %}

```
### lib/pip_dlfcn.c

```c

{% raw %}
38 | 
39 | /* locked dl* functions */
40 | 
41 | void *pip_dlopen( const char *filename, int flag ) {
42 |   void *handle;
43 |   pip_glibc_lock();
44 |   handle = dlopen( filename, flag );
45 |   pip_glibc_unlock();
46 |   return handle;
{% endraw %}

```
### lib/pip.c

```c

{% raw %}
500 |     }
501 |     pip_root->task_root->pipid  = pipid;
502 |     pip_root->task_root->type   = PIP_TYPE_ROOT;
503 |     pip_root->task_root->loaded = dlopen( NULL, RTLD_NOW );
504 |     pip_root->task_root->thread = pthread_self();
505 |     pip_root->task_root->tid    = pip_gettid();
{% endraw %}

```
### include/pip/pip_dlfcn.h

```c

{% raw %}
40 | #endif
41 | 
42 |   /* locked dl* functions */
43 |   void *pip_dlopen( const char *filename, int flag );
44 |   void *pip_dlmopen( long lmid, const char *path, int flag );
45 |   int   pip_dlinfo( void *handle, int request, void *info );
{% endraw %}

```