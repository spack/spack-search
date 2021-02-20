---
name: "fio"
layout: package
next_package: fipscheck
previous_package: ffmpeg
languages: ['c']
---
## 3.19
3 / 446 files match, 3 filtered matches.

 - [ioengines.c](#ioenginesc)
 - [os/windows/posix.c](#oswindowsposixc)
 - [os/windows/posix/include/dlfcn.h](#oswindowsposixincludedlfcnh)

### ioengines.c

```c

{% raw %}
74 | 	return NULL;
75 | }
76 | 
77 | static struct ioengine_ops *dlopen_ioengine(struct thread_data *td,
78 | 					    const char *engine_lib)
79 | {
83 | 	dprint(FD_IO, "dload engine %s\n", engine_lib);
84 | 
85 | 	dlerror();
86 | 	dlhandle = dlopen(engine_lib, RTLD_LAZY);
87 | 	if (!dlhandle) {
88 | 		td_vmsg(td, -1, dlerror(), "dlopen");
89 | 		return NULL;
90 | 	}
156 | 	 */
157 | 	ops = __load_ioengine(td->o.ioengine);
158 | 	if (!ops)
159 | 		ops = dlopen_ioengine(td, name);
160 | 
161 | 	/*
{% endraw %}

```
### os/windows/posix.c

```c

{% raw %}
249 | 	return !FreeLibrary((HMODULE)handle);
250 | }
251 | 
252 | void *dlopen(const char *file, int mode)
253 | {
254 | 	HMODULE hMod;
{% endraw %}

```
### os/windows/posix/include/dlfcn.h

```c

{% raw %}
2 | 
3 | #define RTLD_LAZY 1
4 | 
5 | void *dlopen(const char *file, int mode);
6 | int dlclose(void *handle);
7 | void *dlsym(void *restrict handle, const char *restrict name);
{% endraw %}

```