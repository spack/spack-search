---
name: "gmt"
layout: package
next_package: gnupg
previous_package: gmake
library_name: dlopen
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 6.1.0
4 / 3639 files match, 2 filtered matches.

 - [src/gmt_api.c](#srcgmt_apic)
 - [src/gmt_sharedlibs.c](#srcgmt_sharedlibsc)

### src/gmt_api.c

```c

{% raw %}
1002 | 	else {	/* The handling of the core library is only special when gmt.c is used. */
1003 | 		API->lib[0].path = strdup (GMT_CORE_LIB_NAME);
1004 | 		GMT_Report (API, GMT_MSG_DEBUG, "Loading core GMT shared library: %s\n", API->lib[0].path);
1005 | 		if ((API->lib[0].handle = dlopen_special (API->lib[0].path)) == NULL) {
1006 | 			GMT_Report (API, GMT_MSG_ERROR, "Failure while loading core GMT shared library: %s\n", dlerror());
1007 | 			gmtapi_exit (API, GMT_RUNTIME_ERROR); return GMT_RUNTIME_ERROR;
10634 | 	/* Function that returns a pointer to the function named module in specified shared library lib_no, or NULL if not found  */
10635 | 	void *p_func = NULL;       /* function pointer */
10636 | 	if (API->lib[lib_no].skip) return (NULL);	/* Tried to open this shared library before and it was not available */
10637 | 	if (API->lib[lib_no].handle == NULL && (API->lib[lib_no].handle = dlopen (API->lib[lib_no].path, RTLD_LAZY)) == NULL) {	/* Not opened this shared library yet */
10638 | 		GMT_Report (API, GMT_MSG_ERROR, "Unable to open GMT shared %s library: %s\n", API->lib[lib_no].name, dlerror());
10639 | 		API->lib[lib_no].skip = true;	/* Not bother the next time... */
10727 | 	const char *keys = NULL;       /* char pointer to module keys */
10728 | 	const char * (*func)(void*, char*) = NULL;       /* function pointer */
10729 | 	if (API->lib[lib_no].skip) return (NULL);	/* Tried to open this shared library before and it was not available */
10730 | 	if (API->lib[lib_no].handle == NULL && (API->lib[lib_no].handle = dlopen (API->lib[lib_no].path, RTLD_LAZY)) == NULL) {	/* Not opened this shared library yet */
10731 | 		GMT_Report (API, GMT_MSG_ERROR, "Unable to open GMT shared %s library: %s\n", API->lib[lib_no].name, dlerror());
10732 | 		API->lib[lib_no].skip = true;	/* Not bother the next time... */
10747 | 	const char *group = NULL;       /* char pointer to module group */
10748 | 	const char * (*func)(void*, char*) = NULL;       /* function pointer */
10749 | 	if (API->lib[lib_no].skip) return (NULL);	/* Tried to open this shared library before and it was not available */
10750 | 	if (API->lib[lib_no].handle == NULL && (API->lib[lib_no].handle = dlopen (API->lib[lib_no].path, RTLD_LAZY)) == NULL) {	/* Not opened this shared library yet */
10751 | 		GMT_Report (API, GMT_MSG_ERROR, "Unable to open GMT shared %s library: %s\n", API->lib[lib_no].name, dlerror());
10752 | 		API->lib[lib_no].skip = true;	/* Not bother the next time... */
{% endraw %}

```
### src/gmt_sharedlibs.c

```c

{% raw %}
12 | #include "gmt_sharedlibs.h" 	/* Common shared libs structures */
13 | 
14 | #if defined(_WIN32)
15 | void *dlopen (const char *module_name, int mode) {	/* Opens a dll file*/
16 | 	UINT err_code;
17 | 	HINSTANCE dll_handle;
81 | 	VirtualQuery(GetMyModuleHandle, &mbi, sizeof(mbi));
82 | 	return (HINSTANCE) (mbi.AllocationBase);
83 | }
84 | void *dlopen_special(const char *name) {
85 | 	/* Opens the dll file of the current process.  This is how it is done
86 | 	 * under Windows, per http://en.wikipedia.org/wiki/Dynamic_loading */
95 | }
96 | #elif defined(__CYGWIN__)
97 | 	/* Cygwin behaves differently than most Unix and we must use regular dlopen with library name */
98 | void *dlopen_special(const char *name) {
99 | 	/* Opens the shared library file of the current process under *nix.
100 | 	 * Just call dlopen with NULL and RTLD_LAZY */
101 | 	return (dlopen (name, RTLD_LAZY));
102 | }
103 | #else
104 | 
105 | /* Extra convenience function for opening shared library of current process */
106 | 
107 | void *dlopen_special(const char *name) {
108 | 	/* Opens the shared library file of the current process under *nix.
109 | 	 * Just call dlopen with NULL and RTLD_LAZY */
110 | 	gmt_M_unused(name);
111 | 	return (dlopen (NULL, RTLD_LAZY));
112 | }
113 | #endif
{% endraw %}

```