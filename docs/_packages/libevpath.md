---
name: "libevpath"
layout: package
next_package: libfabric
previous_package: libepoxy
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
3710 |     strcpy(libname, "lib" CM_LIBRARY_PREFIX "cm");
3711 |     strcat(libname, select_module);
3712 |     strcat(libname, MODULE_EXT);
3713 |     handle = CMdlopen(cm->CMTrace_file, libname, 0);
3714 |     dlhandle = handle;
3715 |     free(libname);
{% endraw %}

```
### gen_interface.pl

```pl

{% raw %}
751 |     static void *dh = NULL;
752 |     if (h == NULL) {
753 | 	(void) lt_dlinit();
754 | 	h = lt_dlopen(NULL);
755 |     }
756 |     f = (EVSimpleHandlerFunc) lt_dlsym(h, name);
757 |     if (f == NULL) {
758 | 	if (dh == NULL) {
759 | 	    dh = dlopen(NULL, 0);
760 | 	}
761 | 	printf("Querying dlopen()\\n");
762 | 	f = (EVSimpleHandlerFunc)dlsym(dh, name);
763 |     }
764 |     if (f == NULL) {
765 | 	if (dh == NULL) {
766 | 	    dh = dlopen(NULL, RTLD_GLOBAL|RTLD_LAZY);
767 | 	}
768 | 	f = (EVSimpleHandlerFunc)dlsym(dh, name);
771 |     if (f == NULL) {
772 | 	printf("Dynamic symbol lookup for \\"%s\\" failed.\\n\\tEither the symbol is invalid, or symbol lookup is not enabled.\\n", name);
773 | 	printf("Make sure that the symbol is declared \\"extern\\" (not \\"static\\")\\n");
774 | 	printf("Try linking the program with either \\"-rdynamic\\" (GCC) or \\"-dlopen self\\" (libtool)\\n");
775 |     }
776 |     return f;
{% endraw %}

```
### cm_transport.c

```c

{% raw %}
131 | 
132 |     lt_dladdsearchdir(EVPATH_MODULE_BUILD_DIR);
133 |     lt_dladdsearchdir(EVPATH_MODULE_INSTALL_DIR);
134 |     handle = CMdlopen(cm->CMTrace_file, libname, 0);
135 |     if (!handle) {
136 | 	if (!quiet)
{% endraw %}

```
### dlloader.c

```c

{% raw %}
21 | }
22 | 
23 | typedef struct {
24 |     void *dlopen_handle;
25 |     char *lib_prefix;
26 | } *dlhandle;
27 | 
28 | static int dlopen_verbose = -1;
29 | 
30 | void
31 | CMset_dlopen_verbose(int verbose)
32 | {
33 |     dlopen_verbose = verbose;
34 | }
35 | 
36 | void *
37 | CMdlopen(void *CMTrace_filev, char *in_lib, int mode)
38 | {
39 | #if NO_DYNAMIC_LINKING
44 |     char *tmp;
45 |     char *lib;
46 |     FILE *CMTrace_file = (FILE*)CMTrace_filev;
47 |     if (dlopen_verbose == -1) {
48 | 	dlopen_verbose = (getenv("CMTransportVerbose") != NULL);
49 |     }
50 |     tmp = rindex(in_lib, '.');
51 |     if (dlopen_verbose) fprintf(CMTrace_file, "Trying to dlopen %s\n", in_lib);
52 |     if (tmp && (strcmp(tmp, ".la") == 0)) {
53 | 	/* can't open .la files */
54 | 	lib = malloc(strlen(in_lib) + strlen(MODULE_EXT) + 8);
55 | 	strcpy(lib, in_lib);
56 | 	strcpy(rindex(lib, '.'), MODULE_EXT);
57 | 	if (dlopen_verbose) fprintf(CMTrace_file, "Dlopen module name replaced, now %s\n", lib);
58 |     } else {
59 | 	lib = strdup(in_lib);
62 |     while(list && (list[0] != NULL)) {
63 |         char *tmp = malloc(strlen(list[0]) + strlen(lib) + 2);
64 | 	sprintf(tmp, "%s/%s", list[0], lib);
65 | 	handle = dlopen(tmp, RTLD_LAZY);
66 | 	char *err = dlerror();
67 | 	if (dlopen_verbose) {
68 | 	    if (err) {
69 | 		fprintf(CMTrace_file, "Failed to dlopen %s, error is %s\n", tmp, err);
70 | 	    } else {
71 | 		fprintf(CMTrace_file, "DLopen of %s succeeded\n", tmp);
76 | 	if (handle) list = NULL; // fall out
77 |     }
78 |     if (!handle) {
79 |         handle = dlopen(lib, RTLD_LAZY);
80 | 	char *err = dlerror();
81 | 	if (dlopen_verbose) {
82 | 	    if (err) {
83 | 		fprintf(CMTrace_file, "Failed to dlopen %s, error is %s\n", tmp, err);
84 | 	    } else {
85 | 		fprintf(CMTrace_file, "DLopen of %s succeeded\n", tmp);
105 |     }
106 |     tmp = rindex(dlh->lib_prefix, '.');
107 |     strcpy(tmp, "_LTX_");  /* kill postfix, add _LTX_ */
108 |     dlh->dlopen_handle = handle;
109 |     free(lib);
110 |     return (void*)dlh;
122 |     void *sym_val;
123 |     strcpy(tmp, dlh->lib_prefix);
124 |     strcat(tmp, sym);
125 |     sym_val = dlsym(dlh->dlopen_handle, tmp);
126 |     free(tmp);
127 |     if (!sym_val) 
128 | 	sym_val = dlsym(dlh->dlopen_handle, sym);
129 |     return sym_val;
130 | #endif
138 | #else
139 |     dlhandle dlh = (dlhandle)vdlh;
140 | #ifdef ACTUALL_DO_DLCLOSE
141 |     dlclose(dlh->dlopen_handle);
142 | #endif
143 |     free(dlh->lib_prefix);
{% endraw %}

```
### dlloader.h

```c

{% raw %}
4 | #define lt_dlhandle void*
5 | #define MODULE_EXT CMAKE_SHARED_MODULE_SUFFIX
6 | extern void CMdladdsearchdir(char *dir);
7 | extern void* CMdlopen(void *CMTrace_file, char *library, int mode);
8 | extern void CMdlclose(void *handle);
9 | extern void CMdlclearsearchlist();
10 | extern void* CMdlsym(void *handle, char *symbol);
11 | extern void CMset_dlopen_verbose(int verbose);
12 | 
{% endraw %}

```
### cm_util.c

```c

{% raw %}
23 | 
24 | 
25 | extern void EVfprint_version(FILE* out);
26 | extern void CMset_dlopen_verbose(int verbose);
27 | 
28 | int CMtrace_val[CMLastTraceType] = {-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1};
107 | 	if (i!=EVWarning) trace |= CMtrace_val[i];
108 |     }
109 |     if (CMtrace_val[CMTransportVerbose]) {
110 | 	CMset_dlopen_verbose(1);
111 |     }
112 | 
{% endraw %}

```
### response.c

```c

{% raw %}
2064 | {
2065 |     lt_dlhandle handle;
2066 | 
2067 |     handle = CMdlopen(cm->CMTrace_file, path, 0);
2068 |     if (!handle) {
2069 |     	fprintf(stderr, "failed opening %s\n", path);
{% endraw %}

```