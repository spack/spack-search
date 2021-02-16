---
name: "virtualgl"
layout: package
next_package: otf
previous_package: rccl
languages: ['c']
---
## 2.5.2
14 / 497 files match

 - [server/faker-sym.h](#serverfaker-symh)
 - [server/dlfakerut.c](#serverdlfakerutc)
 - [server/dlfaker.c](#serverdlfakerc)
 - [server/faker-mapfile.c](#serverfaker-mapfilec)

### server/faker-sym.h

```c

{% raw %}
621 | typedef	void* (*_dlopenType)(const char *, int);
622 | void *_vgl_dlopen(const char *, int);
623 | SYMDEF(dlopen);
{% endraw %}

```
### server/dlfakerut.c

```c

{% raw %}
67 | 		gldllhnd=dlopen(temps, RTLD_NOW);
69 | 	else gldllhnd=dlopen("libGL.so", RTLD_NOW);
126 | 	fprintf(stderr, "dlopen() name matching test:\n");
127 | 	gldllhnd=dlopen("libGLdlfakerut.so", RTLD_NOW);
156 | 	gldllhnd=dlopen("libdeepbindtest.so", RTLD_NOW|RTLD_DEEPBIND);
200 | 	test("dlopen() test");
{% endraw %}

```
### server/dlfaker.c

```c

{% raw %}
21 | extern void *_vgl_dlopen(const char *, int);
26 |    intercept dlopen() and return a handle to itself rather than a handle to
29 |    NOTE: If the application tries to use dlopen() to obtain a handle to libdl,
34 | void *dlopen(const char *filename, int flag)
48 | 		fprintf(stderr, "[VGL] dlopen (filename=%s flag=%d",
67 | 				"[VGL] NOTICE: Replacing dlopen(\"%s\") with dlopen(\"%s\")\n",
69 | 		retval=_vgl_dlopen(env, flag);
75 | 			fprintf(stderr, "[VGL] NOTICE: Replacing dlopen(\"%s\") with dlopen(\"lib"VGL_DLFAKER_NAME".so\")\n",
77 | 		retval=_vgl_dlopen("lib"VGL_DLFAKER_NAME".so", flag);
79 | 	else retval=_vgl_dlopen(filename, flag);
87 | 			fprintf(stderr, "[VGL] NOTICE: dlopen(\"%s\") failed.\n", filename);
88 | 			fprintf(stderr, "[VGL]    Trying dlopen(\"%s\")\n", temps);
90 | 		retval=_vgl_dlopen(temps, flag);
{% endraw %}

```
### server/faker-mapfile.c

```c

{% raw %}
137 | 		_vgl_dlopen;
{% endraw %}

```