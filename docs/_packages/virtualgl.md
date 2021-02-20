---
name: "virtualgl"
layout: package
next_package: vpic
previous_package: vim
languages: ['c']
---
## 2.5.2
14 / 497 files match, 4 filtered matches.

 - [server/faker-sym.h](#serverfaker-symh)
 - [server/dlfakerut.c](#serverdlfakerutc)
 - [server/dlfaker.c](#serverdlfakerc)
 - [server/faker-mapfile.c](#serverfaker-mapfilec)

### server/faker-sym.h

```c

{% raw %}
618 | 
619 | // From dlfaker
620 | 
621 | typedef	void* (*_dlopenType)(const char *, int);
622 | void *_vgl_dlopen(const char *, int);
623 | SYMDEF(dlopen);
624 | 
625 | 
{% endraw %}

```
### server/dlfakerut.c

```c

{% raw %}
64 | 	{
65 | 		char temps[256];
66 | 		snprintf(temps, 255, "%s/libGL.so", prefix);
67 | 		gldllhnd=dlopen(temps, RTLD_NOW);
68 | 	}
69 | 	else gldllhnd=dlopen("libGL.so", RTLD_NOW);
70 | 	err=dlerror();
71 | 	if(err) _throw(err)
123 | {
124 | 	const char *err=NULL;
125 | 
126 | 	fprintf(stderr, "dlopen() name matching test:\n");
127 | 	gldllhnd=dlopen("libGLdlfakerut.so", RTLD_NOW);
128 | 	err=dlerror();
129 | 	if(err) _throw(err)
153 | {
154 | 	const char *err=NULL;
155 | 
156 | 	gldllhnd=dlopen("libdeepbindtest.so", RTLD_NOW|RTLD_DEEPBIND);
157 | 	err=dlerror();
158 | 	if(err) _throw(err)
197 | 	nameMatchTest();
198 | 
199 | 	loadSymbols1(prefix);
200 | 	test("dlopen() test");
201 | 
202 | 	loadSymbols2();
{% endraw %}

```
### server/dlfaker.c

```c

{% raw %}
18 | #include "vendor.h"
19 | 
20 | 
21 | extern void *_vgl_dlopen(const char *, int);
22 | 
23 | 
24 | /* If an application uses dlopen()/dlsym() to load functions from libGL or
25 |    libX11, this bypasses the LD_PRELOAD mechanism.  Thus, VirtualGL has to
26 |    intercept dlopen() and return a handle to itself rather than a handle to
27 |    libGL or libX11.
28 | 
29 |    NOTE: If the application tries to use dlopen() to obtain a handle to libdl,
30 |    we similarly replace the handle with a handle to libdlfaker.  This works
31 |    around an interaction issue between 180.xx of the nVidia drivers and WINE.
32 | */
33 | 
34 | void *dlopen(const char *filename, int flag)
35 | {
36 | 	char *env=NULL, *env2=NULL;  const char *envname="FAKERLIB32";
45 | 
46 | 	if(trace)
47 | 	{
48 | 		fprintf(stderr, "[VGL] dlopen (filename=%s flag=%d",
49 | 			filename? filename:"NULL", flag);
50 | 	}
64 | 	{
65 | 		if(verbose)
66 | 			fprintf(stderr,
67 | 				"[VGL] NOTICE: Replacing dlopen(\"%s\") with dlopen(\"%s\")\n",
68 | 				filename? filename:"NULL", env? env:"NULL");
69 | 		retval=_vgl_dlopen(env, flag);
70 | 	}
71 | 	else if(filename && (!strncmp(filename, "libdl.", 6)
72 | 		|| strstr(filename, "/libdl.")))
73 | 	{
74 | 		if(verbose)
75 | 			fprintf(stderr, "[VGL] NOTICE: Replacing dlopen(\"%s\") with dlopen(\"lib"VGL_DLFAKER_NAME".so\")\n",
76 | 				filename? filename:"NULL");
77 | 		retval=_vgl_dlopen("lib"VGL_DLFAKER_NAME".so", flag);
78 | 	}
79 | 	else retval=_vgl_dlopen(filename, flag);
80 | 
81 | 	if(!retval && filename && !strncmp(filename, "VBoxOGL", 7))
84 | 		snprintf(temps, 255, "/usr/lib/virtualbox/%s", filename);
85 | 		if(verbose)
86 | 		{
87 | 			fprintf(stderr, "[VGL] NOTICE: dlopen(\"%s\") failed.\n", filename);
88 | 			fprintf(stderr, "[VGL]    Trying dlopen(\"%s\")\n", temps);
89 | 		}
90 | 		retval=_vgl_dlopen(temps, flag);
91 | 	}
92 | 
{% endraw %}

```
### server/faker-mapfile.c

```c

{% raw %}
134 | 
135 | 		XCopyArea_FBX;
136 | 
137 | 		_vgl_dlopen;
138 | 
139 | 		/* XCB */
{% endraw %}

```