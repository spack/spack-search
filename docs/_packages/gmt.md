---
name: "gmt"
layout: package
next_package: gnupg
previous_package: gmake
languages: ['c']
---
## 6.1.0
4 / 3639 files match, 2 filtered matches.

 - [src/gmt_api.c](#srcgmt_apic)
 - [src/gmt_sharedlibs.c](#srcgmt_sharedlibsc)

### src/gmt_api.c

```c

{% raw %}
1005 | 		if ((API->lib[0].handle = dlopen_special (API->lib[0].path)) == NULL) {
10637 | 	if (API->lib[lib_no].handle == NULL && (API->lib[lib_no].handle = dlopen (API->lib[lib_no].path, RTLD_LAZY)) == NULL) {	/* Not opened this shared library yet */
10730 | 	if (API->lib[lib_no].handle == NULL && (API->lib[lib_no].handle = dlopen (API->lib[lib_no].path, RTLD_LAZY)) == NULL) {	/* Not opened this shared library yet */
10750 | 	if (API->lib[lib_no].handle == NULL && (API->lib[lib_no].handle = dlopen (API->lib[lib_no].path, RTLD_LAZY)) == NULL) {	/* Not opened this shared library yet */
{% endraw %}

```
### src/gmt_sharedlibs.c

```c

{% raw %}
15 | void *dlopen (const char *module_name, int mode) {	/* Opens a dll file*/
84 | void *dlopen_special(const char *name) {
98 | void *dlopen_special(const char *name) {
101 | 	return (dlopen (name, RTLD_LAZY));
107 | void *dlopen_special(const char *name) {
111 | 	return (dlopen (NULL, RTLD_LAZY));
{% endraw %}

```