---
name: "gmt"
layout: package
next_package: cntk
previous_package: legion
languages: ['cmake', 'cpp']
---
## 6.1.0
4 / 3639 files match

 - [src/gmt_api.c](#srcgmt_apic)
 - [src/gmt_sharedlibs.h.in](#srcgmt_sharedlibshin)
 - [src/gmt_sharedlibs.c](#srcgmt_sharedlibsc)
 - [cmake/modules/ConfigureChecks.cmake](#cmakemodulesconfigurecheckscmake)

### src/gmt_api.c

```cpp

{% raw %}
988 | 	 * use the dlopen_special call which is defined in gmt_sharedlibs.c.  If the gmt core and supplemental
1005 | 		if ((API->lib[0].handle = dlopen_special (API->lib[0].path)) == NULL) {
10637 | 	if (API->lib[lib_no].handle == NULL && (API->lib[lib_no].handle = dlopen (API->lib[lib_no].path, RTLD_LAZY)) == NULL) {	/* Not opened this shared library yet */
10730 | 	if (API->lib[lib_no].handle == NULL && (API->lib[lib_no].handle = dlopen (API->lib[lib_no].path, RTLD_LAZY)) == NULL) {	/* Not opened this shared library yet */
10750 | 	if (API->lib[lib_no].handle == NULL && (API->lib[lib_no].handle = dlopen (API->lib[lib_no].path, RTLD_LAZY)) == NULL) {	/* Not opened this shared library yet */
{% endraw %}

```
### src/gmt_sharedlibs.h.in

```

{% raw %}
25 | EXTERN_MSC void *dlopen (const char *module_name, int mode);
33 | EXTERN_MSC void *dlopen_special (const char *name);
41 | 	void *handle;	/* Handle to the shared library, returned by dlopen or dlopen_special */
{% endraw %}

```
### src/gmt_sharedlibs.c

```cpp

{% raw %}
15 | void *dlopen (const char *module_name, int mode) {	/* Opens a dll file*/
84 | void *dlopen_special(const char *name) {
97 | 	/* Cygwin behaves differently than most Unix and we must use regular dlopen with library name */
98 | void *dlopen_special(const char *name) {
100 | 	 * Just call dlopen with NULL and RTLD_LAZY */
101 | 	return (dlopen (name, RTLD_LAZY));
107 | void *dlopen_special(const char *name) {
109 | 	 * Just call dlopen with NULL and RTLD_LAZY */
111 | 	return (dlopen (NULL, RTLD_LAZY));
{% endraw %}

```
### cmake/modules/ConfigureChecks.cmake

```cmake

{% raw %}
211 | 	check_function_exists (dlopen HAVE_BUILTIN_DYNAMIC_LINKING_LOADER)
213 | 		check_library_exists (dl dlopen "" HAVE_LIBDL)
{% endraw %}

```