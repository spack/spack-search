---
name: "dcap"
layout: package
next_package: dimemas
previous_package: darshan-util
languages: ['c']
---
## 2.47.12
7 / 166 files match, 4 filtered matches.

 - [src/win32_libdl.c](#srcwin32_libdlc)
 - [src/tunnelManager.c](#srctunnelmanagerc)
 - [src/win32_libdl.h](#srcwin32_libdlh)
 - [src/system_io.c](#srcsystem_ioc)

### src/win32_libdl.c

```c

{% raw %}
9 | 
10 | static char errbuf[512];
11 | 
12 | void *dlopen(const char *name, int mode)
13 | {
14 |   HINSTANCE hdll;
{% endraw %}

```
### src/tunnelManager.c

```c

{% raw %}
98 | 		return NULL;
99 | 	}
100 | 
101 | 	handle = dlopen( libname, RTLD_NOW);
102 | 		
103 | 	if(handle == NULL) {
105 | 		strcpy(fullpath, TUNNELLIBDIR);
106 | 		strcat(fullpath, "/");
107 | 		strcat(fullpath, libname);
108 | 		handle = dlopen(fullpath, RTLD_NOW);
109 | 		free(fullpath);
110 | 	}
{% endraw %}

```
### src/win32_libdl.h

```c

{% raw %}
20 | #define RTLD_LAZY 1
21 | #define RTLD_NOW  2
22 | 
23 | extern void  *dlopen(const char *, int);
24 | extern void  *dlsym(void *, const char *);
25 | extern int   dlclose(void *);
{% endraw %}

```
### src/system_io.c

```c

{% raw %}
234 | 		libname = getenv("DCACHE_IOLIB");
235 | 	}
236 | 	if( libname != NULL ) {
237 | 		handle = dlopen( libname, RTLD_NOW | RTLD_GLOBAL);
238 | 		if(handle == NULL) {
239 | 			m_unlock(&gLock);
{% endraw %}

```