---
name: "fio"
layout: package
next_package: fakechroot
previous_package: arrow
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 3.19
4 / 446 files match, 3 filtered matches.

 - [ioengines.c](#ioenginesc)
 - [os/windows/posix.c](#oswindowsposixc)
 - [os/windows/posix/include/dlfcn.h](#oswindowsposixincludedlfcnh)

### ioengines.c

```c

{% raw %}
93 | 	 * Unlike the included modules, external engines should have a
94 | 	 * non-static ioengine structure that we can reference.
95 | 	 */
96 | 	ops = dlsym(dlhandle, engine_lib);
97 | 	if (!ops)
98 | 		ops = dlsym(dlhandle, "ioengine");
99 | 
100 | 	/*
104 | 	 * structure.
105 | 	 */
106 | 	if (!ops) {
107 | 		get_ioengine_t get_ioengine = dlsym(dlhandle, "get_ioengine");
108 | 
109 | 		if (get_ioengine)
111 | 	}
112 | 
113 | 	if (!ops) {
114 | 		td_vmsg(td, -1, dlerror(), "dlsym");
115 | 		dlclose(dlhandle);
116 | 		return NULL;
{% endraw %}

```
### os/windows/posix.c

```c

{% raw %}
262 | 	return hMod;
263 | }
264 | 
265 | void *dlsym(void *handle, const char *name)
266 | {
267 | 	FARPROC fnPtr;
{% endraw %}

```
### os/windows/posix/include/dlfcn.h

```c

{% raw %}
4 | 
5 | void *dlopen(const char *file, int mode);
6 | int dlclose(void *handle);
7 | void *dlsym(void *restrict handle, const char *restrict name);
8 | char *dlerror(void);
9 | 
{% endraw %}

```