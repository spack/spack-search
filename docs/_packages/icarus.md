---
name: "icarus"
layout: package
next_package: icedtea
previous_package: ibm-databroker
languages: ['cpp', 'c']
---
## v10_3
7 / 728 files match, 5 filtered matches.

 - [t-dll.cc](#t-dllcc)
 - [vvp/vpi_modules.cc](#vvpvpi_modulescc)
 - [vvp/ivl_dlfcn.h](#vvpivl_dlfcnh)
 - [cadpli/cadpli.c](#cadplicadplic)
 - [cadpli/ivl_dlfcn.h](#cadpliivl_dlfcnh)

### t-dll.cc

```cpp

{% raw %}
36 | 
37 | #if defined(__WIN32__)
38 | 
39 | inline ivl_dll_t ivl_dlopen(const char *name)
40 | {
41 |       ivl_dll_t res =  (ivl_dll_t) LoadLibrary(name);
69 |   return msg;
70 | }
71 | #elif defined(HAVE_DLFCN_H)
72 | inline ivl_dll_t ivl_dlopen(const char*name)
73 | { return dlopen(name,RTLD_LAZY); }
74 | 
75 | inline void* ivl_dlsym(ivl_dll_t dll, const char*nm)
85 | { dlclose(dll); }
86 | 
87 | #elif defined(HAVE_DL_H)
88 | inline ivl_dll_t ivl_dlopen(const char*name)
89 | { return shl_load(name, BIND_IMMEDIATE, 0); }
90 | 
686 | {
687 |       const char*dll_path_ = des->get_flag("DLL");
688 | 
689 |       dll_ = ivl_dlopen(dll_path_);
690 | 
691 |       if ((dll_ == 0) && (dll_path_[0] != '/')) {
692 | 	    size_t len = strlen(basedir) + 1 + strlen(dll_path_) + 1;
693 | 	    char*tmp = new char[len];
694 | 	    sprintf(tmp, "%s/%s", basedir, dll_path_);
695 | 	    dll_ = ivl_dlopen(tmp);
696 | 	    delete[]tmp;
697 |       }
2805 | 
2806 | void dll_target::test_version(const char*target_name)
2807 | {
2808 |       dll_ = ivl_dlopen(target_name);
2809 | 
2810 |       if ((dll_ == 0) && (target_name[0] != '/')) {
2811 | 	    size_t len = strlen(basedir) + 1 + strlen(target_name) + 1;
2812 | 	    char*tmp = new char[len];
2813 | 	    sprintf(tmp, "%s/%s", basedir, target_name);
2814 | 	    dll_ = ivl_dlopen(tmp);
2815 | 	    delete[]tmp;
2816 |       }
{% endraw %}

```
### vvp/vpi_modules.cc

```cpp

{% raw %}
134 |       /* must have found some file that could possibly be a vpi module
135 |        * try to open it as a shared object.
136 |        */
137 |       dll = ivl_dlopen(buf, export_flag);
138 |       if(dll==0) {
139 | 	/* hmm, this failed, let the user know what has really gone wrong */
140 | 	fprintf(stderr,"%s:`%s' failed to open using dlopen() because:\n"
141 | 		"    %s.\n",name,buf,dlerror());
142 | 
{% endraw %}

```
### vvp/ivl_dlfcn.h

```c

{% raw %}
31 | #endif
32 | 
33 | #if defined(__MINGW32__)
34 | inline ivl_dll_t ivl_dlopen(const char *name, bool)
35 | {
36 |       static char full_name[4096];
65 | }
66 | 
67 | #elif defined(HAVE_DLFCN_H)
68 | inline ivl_dll_t ivl_dlopen(const char*name, bool global_flag)
69 | { return dlopen(name,RTLD_LAZY|(global_flag?RTLD_GLOBAL:0)); }
70 | 
71 | inline void* ivl_dlsym(ivl_dll_t dll, const char*nm)
81 | { dlclose(dll); }
82 | 
83 | #elif defined(HAVE_DL_H)
84 | inline ivl_dll_t ivl_dlopen(const char*name)
85 | { return shl_load(name, BIND_IMMEDIATE, 0); }
86 | 
{% endraw %}

```
### cadpli/cadpli.c

```c

{% raw %}
52 | 	    strncpy(module, cp, bp-cp);
53 | 	    module[bp-cp] = 0;
54 | 
55 | 	    mod = ivl_dlopen(module);
56 | 	    if (mod == 0) {
57 | 		  vpi_printf("%s link: %s\n", vlog_info.argv[idx], dlerror());
{% endraw %}

```
### cadpli/ivl_dlfcn.h

```c

{% raw %}
31 | #endif
32 | 
33 | #if defined(__MINGW32__)
34 | static __inline__ ivl_dll_t ivl_dlopen(const char *name)
35 | { return (void *)LoadLibrary(name); }
36 | 
57 | }
58 | 
59 | #elif defined(HAVE_DLFCN_H)
60 | static __inline__ ivl_dll_t ivl_dlopen(const char*name)
61 | { return dlopen(name,RTLD_LAZY); }
62 | 
63 | static __inline__ void* ivl_dlsym(ivl_dll_t dll, const char*nm)
73 | { dlclose(dll); }
74 | 
75 | #elif defined(HAVE_DL_H)
76 | static __inline__ ivl_dll_t ivl_dlopen(const char*name)
77 | { return shl_load(name, BIND_IMMEDIATE, 0); }
78 | 
{% endraw %}

```