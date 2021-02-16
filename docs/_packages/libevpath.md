---
name: "libevpath"
layout: package
next_package: libfabric
previous_package: libbsd
languages: ['pl', 'c']
---
## develop
10 / 228 files match, 7 filtered matches.

 - [cm.c](#cmc)
 - [gen_interface.pl](#gen_interfacepl)
 - [cm_transport.c](#cm_transportc)
 - [dlloader.c](#dlloaderc)
 - [dlloader.h](#dlloaderh)
 - [cm_util.c](#cm_utilc)
 - [response.c](#responsec)

### cm.c

```c

{% raw %}
3713 |     handle = CMdlopen(cm->CMTrace_file, libname, 0);
{% endraw %}

```
### gen_interface.pl

```pl

{% raw %}
754 | 	h = lt_dlopen(NULL);
759 | 	    dh = dlopen(NULL, 0);
761 | 	printf("Querying dlopen()\\n");
766 | 	    dh = dlopen(NULL, RTLD_GLOBAL|RTLD_LAZY);
774 | 	printf("Try linking the program with either \\"-rdynamic\\" (GCC) or \\"-dlopen self\\" (libtool)\\n");
{% endraw %}

```
### cm_transport.c

```c

{% raw %}
134 |     handle = CMdlopen(cm->CMTrace_file, libname, 0);
{% endraw %}

```
### dlloader.c

```c

{% raw %}
24 |     void *dlopen_handle;
28 | static int dlopen_verbose = -1;
31 | CMset_dlopen_verbose(int verbose)
33 |     dlopen_verbose = verbose;
37 | CMdlopen(void *CMTrace_filev, char *in_lib, int mode)
47 |     if (dlopen_verbose == -1) {
48 | 	dlopen_verbose = (getenv("CMTransportVerbose") != NULL);
51 |     if (dlopen_verbose) fprintf(CMTrace_file, "Trying to dlopen %s\n", in_lib);
57 | 	if (dlopen_verbose) fprintf(CMTrace_file, "Dlopen module name replaced, now %s\n", lib);
65 | 	handle = dlopen(tmp, RTLD_LAZY);
67 | 	if (dlopen_verbose) {
69 | 		fprintf(CMTrace_file, "Failed to dlopen %s, error is %s\n", tmp, err);
79 |         handle = dlopen(lib, RTLD_LAZY);
81 | 	if (dlopen_verbose) {
83 | 		fprintf(CMTrace_file, "Failed to dlopen %s, error is %s\n", tmp, err);
108 |     dlh->dlopen_handle = handle;
125 |     sym_val = dlsym(dlh->dlopen_handle, tmp);
128 | 	sym_val = dlsym(dlh->dlopen_handle, sym);
141 |     dlclose(dlh->dlopen_handle);
{% endraw %}

```
### dlloader.h

```c

{% raw %}
7 | extern void* CMdlopen(void *CMTrace_file, char *library, int mode);
11 | extern void CMset_dlopen_verbose(int verbose);
{% endraw %}

```
### cm_util.c

```c

{% raw %}
26 | extern void CMset_dlopen_verbose(int verbose);
110 | 	CMset_dlopen_verbose(1);
{% endraw %}

```
### response.c

```c

{% raw %}
2067 |     handle = CMdlopen(cm->CMTrace_file, path, 0);
{% endraw %}

```